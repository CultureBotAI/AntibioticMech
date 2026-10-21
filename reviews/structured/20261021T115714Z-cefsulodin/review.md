# Cefsulodin: an under-specified PubChem mapping and overbroad spectrum wording

- Review: 20261021T115714Z-cefsulodin
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T11:39:25Z
- Finished UTC: 2026-10-21T11:57:14Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One major exact-grounding defect and one minor definition issue. Native cefsulodin specifies the R side chain, but PubChem CID 5284530 leaves that centre unassigned; CID 656575, ChEMBL and KEGG match the complete native structure. The unqualified broad-spectrum wording should be replaced by evidence-bounded activity wording. Primary sodium-preparation studies emphasize antipseudomonal activity with limited activity against many other Gram-negative organisms; the 2012 combination study does not establish broad monotherapy coverage.

## Scope And Provenance

Whole-record review of exact cefsulodin zwitterion.

Selection: Queue 249 in isolated batch 025; existing original captures preserved and actual ARO owner appended before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:3507 | data/antibiotics/antibacterial/cefsulodin.yaml | generated | cefsulodin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | CHEBI:3507 | Actual focused command passed with zero errors. |
| Focused strict | passed | True | CHEBI:3507 | Actual focused command passed with zero errors. |
| Supplemental chemistry | passed | False | CHEBI:3507 | Executed successfully against batch 025 cwd; chemical comparison preserves the detected external stereo mismatch. |
| Supplemental xref-comparison | passed | False | CHEBI:3507 | Executed successfully against batch 025 cwd; chemical comparison preserves the detected external stereo mismatch. |
| Authoritative full QC | failed | True | CHEBI:3507 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:3507 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:3507 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:3507 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:3507 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:3507 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:3507 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:3507 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:3507 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Native complete molecular graph

identity: supported. Targets: CHEBI:3507.

Definition chemical class, names, charge, masses, source mints and core/side-chain stereochemistry are internally coherent; ChEMBL and KEGG agree.

### Exact PubChem mapping

grounding: concern. Targets: CHEBI:3507.

CID 5284530 lacks the specified R side chain; CID 656575 agrees with the complete native structure. This affects exact equivalence, not the correct native molecule.

### Parents and antibacterial roles

grounding: supported. Targets: CHEBI:3507.

Structural parents fit. Primary literature supports antibacterial identity and activity with material/taxon qualifications.

### Spectrum wording

evidence: concern. Targets: CHEBI:3507.

Unqualified broad-spectrum wording obscures documented low activity against many other Gram-negative organisms. Combination sensitization does not establish broad single-agent coverage. A bounded activity description is justified.

### All four adopted PMID dispositions

evidence: supported. Targets: CHEBI:3507.

Original antipseudomonal activity and 2012 combination/mechanism studies are separated from antibody-conjugate and allergy context.

### Optional E. coli PBP enrichment

evidence: supported. Targets: CHEBI:3507.

The 2012 source supports bounded competition and deletion/complementation evidence. PBP1a has lower measured competition IC50; PBP1b partial inhibition explains combination sensitization. Reagent salt and kill-curve comparator identity remain unresolved.

### Structured adapter applicability

scope: not_applicable. Targets: CHEBI:3507.

Native record names no gene/protein/pathway or transcriptomics dataset. Newly inspected literature targets are evidence leads rather than native assertions; no module absence is used as negative evidence.

### Clinical, resistance, producer, dataset and graph fields

scope: not_applicable. Targets: CHEBI:3507.

No native claims populated in these optional domains; current drug mappings do not imply a present product authorization or natural producer.

### Maintained owners and history

provenance: supported. Targets: CHEBI:3507.

ChEBI and ARO ownership, source mints and four seed/reseed events traceable. Original hashes preserved.

### Focused validators

schema: supported. Targets: CHEBI:3507.

Native checks pass; findings require scientific source/xref review.

### Required repair versus optional enrichment

completeness: supported. Targets: CHEBI:3507.

Repair the populated exact xref and qualify spectrum wording. Unpopulated optional activity/target objects are not independent defects.

## Findings

### F1: The exact PubChem cross-reference omits the R side-chain stereocentre

major / open / confirmed; issue key: chebi-3507-pubchem-5284530-sidechain-stereo.

CID 5284530 is the partially specified SYLKGLMBLAAGSC-IKZMBGHXSA-N graph. Native cefsulodin is SYLKGLMBLAAGSC-QLVMHMETSA-N with R at the side-chain carbon. CAS-resolved CID 656575, ChEMBL and KEGG match the native complete molecule. Correct the source-owned equivalence without altering the correct native structure or describing the broader CID as a proven mixture.

### F2: The broad-spectrum definition needs evidence-bounded wording

minor / open / confirmed; issue key: chebi-3507-unqualified-broad-spectrum-definition.

The definition labels cefsulodin broadly without qualification. The adopted 1979 source, additional original sodium-material reports and ARO describe focused antipseudomonal activity with low activity against many other Gram-negative organisms; some Gram-positive and other bacterial activity is retained. The 2012 broad isolate sensitization is a combination result. Replace broad-spectrum shorthand with a bounded description rather than claiming universal inactivity outside Pseudomonas.

## Recommended Actions And Acceptance Checks

### A1

Repair the exact PubChem mapping through maintained source ownership.

- Replace or adjudicate CID 5284530 using the verified complete R,R,R identity; CID 656575 is a directly verified candidate.
- Preserve native structure and complete InChIKey; ensure reseeding does not reintroduce the broader ARO mapping.
- Run exact xref structure comparison plus native schema/strict and applicable term/reference/history/corpus gates after separate curation authorization.

### A2

Qualify the spectrum definition without erasing supported activity.

- Describe antipseudomonal activity and limited activity against many other Gram-negative organisms, retaining some Gram-positive activity and sodium-source scope.
- Do not transfer combination sensitization to monotherapy or interpret a finite negative panel as universal species resistance.

### A3

Optionally curate 2012 activity and PBP evidence with assay-specific scope.

- Resolve cefsulodin reagent salt/material before quantitative transfer.
- Separate strain MIC, Bocillin competition IC50, deletion/complementation and inferred partial inhibition; do not use competition IC50 as Kd.
- Resolve Figure 3 cefadroxil versus prose cefotaxime before extracting the time-kill comparator.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/cefsulodin.yaml; Entire YAML | supports | Read seeded/exact identity, definition, six synonyms, four parents, two roles, cephalosporin class, structure, five exact xrefs, two drug xrefs, document, both source concepts and four history events. No populated activity, target, resistance, clinical, producer, dataset or graph objects. |
| owners | data/raw/chebi_antimicrobials.tsv;data/raw/aro_antibiotics.tsv; Entire ChEBI row 92 and ARO row 357 | supports | ChEBI owns broad-spectrum definition and three PMID leads; ARO owns under-specified PubChem mapping and PMID 119787. ARO describes Pseudomonas activity with little activity against other Gram-negative bacteria. All four adopted lead dispositions are retained. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Identity, Equivalence and Evidence standard | supports | Exact structural xrefs must agree at specified stereocentres; definition activity scope should match primary evidence. Optional missing slots alone are not defects. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:3507; Current complete identity, definition, names and parents | partial | Current ChEBI retains the native R,R,R structure and broad-spectrum wording. Primary carboxamide, cephalosporin and organosulfonic-acid parents fit the graph. Current source agreement does not independently validate the disputed wording. |
| chemistry | RDKit 2026.03.5 native molecular check; 249-chemistry.json | supports | Both native encodings reproduce SYLKGLMBLAAGSC-QLVMHMETSA-N, C22H20N4O8S2, net zero charge, one fragment, masses and three R centres; both source mints agree. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/5284530/JSON; Complete current molecule, InChI and stereochemical SMILES | refutes | Native xref CID 5284530 has SYLKGLMBLAAGSC-IKZMBGHXSA-N and unassigned side-chain stereochemistry, while core 6R,7R remains specified. It is a partially specified molecular graph, not a demonstrated opposite epimer or a proven mixture. |
| cas-exact | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/62587-73-9/JSON; CAS lookup and complete molecular graph | supports | CAS 62587-73-9 resolves CID 656575, whose full key and R side chain match native exact cefsulodin. This is a supported replacement candidate, subject to maintained source adjudication. |
| chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL3351077.json; Full InChI, SMILES and molfile | supports | All three ChEMBL molecular encodings reproduce the native full key and three R stereocentres. |
| kegg | https://rest.kegg.jp/get/C11253; C11253 and D07653 entries; C11253 molfile | supports | Compound and drug entries name cefsulodin with matching formula. The compound molfile reproduces native full key and three R centres; generic drug-target prose is not a primary target experiment. |
| aro | https://card.mcmaster.ca/aro/3004727; Current definition, graph and xrefs | partial | ARO canonical stereochemical SMILES matches the exact native graph, but it propagates the under-specified PubChem CID. Its activity description is focused on Pseudomonas with little other Gram-negative activity. |
| drugcentral | https://drugcentral.org/drugcard/558; Drug identity, formula and aliases | supports | DrugCentral 558 has cefsulodin, matching CAS and formula. Sodium aliases are drug-level aggregation and are not exact neutral-form equivalences. |
| wiki | https://en.wikipedia.org/wiki/Cefsulodin; Document identity only | context_only | The named document resolves; it is context, not primary scientific evidence. |
| adopted-119787 | https://academic.oup.com/jac/article-abstract/5/6/687/782360; PMID 119787; DOI 10.1093/jac/5.6.687; publisher abstract inspected through web tool | partial | Original study identifies CGP 7174/E and SCE 129 as cefsulodin. It reports high P. aeruginosa activity but relative inactivity against coliforms, and distinguishes additive/synergistic combination responses. Europe PMC has no abstract; publisher abstract was readable through the web tool while direct downloads returned 403. Full reagent methods remain unresolved. |
| adopted-1384868 | PMID:1384868; DOI 10.1159/000236216; complete inspected abstract | context_only | Original aztreonam monoclonal-antibody epitope/cross-reaction experiments concern beta-lactam–albumin conjugates and degraded determinants. This abstract does not identify a cef­sulodin-specific antibacterial result and is not used as mechanism support. |
| adopted-29017833 | PMID:29017833; DOI 10.1016/j.jaip.2017.08.027; inspected abstract | context_only | Allergy and side-chain cross-reactivity review; contextual lead, not primary cefsulodin antibacterial evidence. |
| adopted-23139798 | PMID:23139798; DOI 10.1371/journal.pone.0048598; full body, Methods, Results, Tables 1–4 | supports | Primary study uses E. coli CS109/2443 and mrcA/mrcB deletion/complementation plus clinical isolates. Table 3 reports cefsulodin MIC 32 mg/L for both parental strains and 1 mg/L after mrcB deletion, restored to 32 mg/L by complementation. Tables 2/4 distinguish single-agent measurements from 4 mg/L cefsulodin combinations; these cannot establish broad monotherapy efficacy. Exact supplier/salt is not specified in the inspected Methods. |
| pbp-binding | PMID:23139798; Results: Cefsulodin Binding Efficacy of PBP1a is Ten Times Higher than that of PBP1b; concluding interpretation | supports | Bocillin FL competition in deletion backgrounds reports approximately 10 µM IC50 for PBP1a and 100 µM for PBP1b. These are competition endpoints, not purified equilibrium Kd. The authors infer partial PBP1b inhibition to explain combination sensitization; deletion/complementation is physiological evidence, not proof that PBP1b is the higher-affinity target. Figure 3 names cefadroxil whereas adjacent prose names cefotaxime, so that comparator identity requires adjudication before extracting kill curves. |
| original-spectrum | DOI:10.11250/chemotherapy1953.27.Supplement2_12; Original 1979 English summary p41; visually inspected Figure 1 p12 | supports | The primary report explicitly studies cefsulodin monosodium salt. Figure 1 visibly contains SO3Na. Its English summary reports potent P. aeruginosa and some Gram-positive activity with low activity against many Gram-negative rods. Preserve sodium material and taxon/strain dependence; no exact-neutral MIC transfer or claim that only Pseudomonas can be affected. |
| spectrum-6770753 | PMID:6770753; DOI 10.1128/AAC.17.2.165; complete inspected abstract | partial | Original sodium-cefsulodin study reports activity against P. aeruginosa and selected other named Pseudomonas species but not the other tested Gram-negative organisms. Inoculum effects and beta-lactamase susceptibility are enzyme/isolate dependent. This corroborates focused spectrum, not universal resistance or a neutral-form quantitative assay. |
| xref-check | Independent complete structure comparison; 249250-xref-check.json; 249 section | supports | Native, all three ChEMBL encodings, KEGG molfile and CAS-resolved CID 656575 agree at R,R,R. Native CID 5284530 retains R at core centres but leaves the side-chain carbon unassigned. |
| local-search | Ignored-inclusive record/owner and free primary searches; 249-owner-hits.txt;249-local-hits.txt;249-primary-search.json | context_only | Exact ID, label, source IDs and full key searched across isolated batch 025 outside .git/.venv with ignored/hidden coverage. Every adopted lead inspected at stated depth; additional original spectrum source followed. No global exhaustive literature claim. |
| gates | Actual focused native commands; 249-focused-results.json | supports | Schema, strict and supplemental native chemistry/mints each exit 0; these do not detect external stereo incompleteness or overbroad wording. |

## Limits And Additional Notes

- 1979 adopted paper was inspected through publisher abstract; full methods inaccessible via direct 403. The 1979 J-STAGE English summary and structure figure were inspected; complete Japanese experimental narrative was not translated.
- Original spectrum studies explicitly use sodium material; exact native-zwitterion quantitative transfer remains unresolved.
- The 2012 full text does not specify exact cefsulodin supplier/salt in its inspected Methods. Its Figure 3 and adjacent prose disagree on one companion beta-lactam.
- Antibody and allergy leads were inspected at abstract level and are not used for exact antibacterial or binding claims.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 21 expanded input hashes unchanged; no native/source/status/history changes.
- Native gates used batch 025 environment; standalone RDKit 2026.03.5 checks used existing batch 019 interpreter against batch 025 cwd.
- Free public sources only; no exact-compound or universal-spectrum claim inferred from document titles alone.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T115714Z-cefsulodin
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cefsulodin: an under-specified PubChem mapping and overbroad spectrum wording'
started_at: '2026-10-21T11:39:25Z'
finished_at: '2026-10-21T11:57:14Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Independent whole native/owner review, complete current xref
    structure comparison, every adopted lead disposition, full 2012 PLOS body and
    tables, original 1979 English summary and structure figure, and 1980 primary abstract.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: One major exact-grounding defect and one minor definition issue. Native cefsulodin
  specifies the R side chain, but PubChem CID 5284530 leaves that centre unassigned;
  CID 656575, ChEMBL and KEGG match the complete native structure. The unqualified
  broad-spectrum wording should be replaced by evidence-bounded activity wording.
  Primary sodium-preparation studies emphasize antipseudomonal activity with limited
  activity against many other Gram-negative organisms; the 2012 combination study
  does not establish broad monotherapy coverage.
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
  - path: data/antibiotics/antibacterial/cefsulodin.yaml
    sha256: 4d82e52ba22b1107bd6628b12793af9dcd59a42177a16772bb201e7b8314e1cb
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
- target_id: CHEBI:3507
  path: data/antibiotics/antibacterial/cefsulodin.yaml
  label: cefsulodin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI identity, structure, definition, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, class, xrefs and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding and exclusion overrides
scope:
  description: Whole-record review of exact cefsulodin zwitterion.
  selection: Queue 249 in isolated batch 025; existing original captures preserved
    and actual ARO owner appended before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:3507
  exclusions:
  - target: Sodium preparations, under-specified PubChem structure and combination-level
      results
    reason: Keep exact material, stereochemistry and monotherapy versus combination
      scope separate.
checks:
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  summary: Actual focused command passed with zero errors.
  target_ids:
  - CHEBI:3507
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefsulodin.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: strict
  name: Focused strict
  status: passed
  required: true
  summary: Actual focused command passed with zero errors.
  target_ids:
  - CHEBI:3507
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefsulodin.yaml --out /private/tmp/am-review-session/249-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Supplemental chemistry
  status: passed
  required: false
  summary: Executed successfully against batch 025 cwd; chemical comparison preserves
    the detected external stereo mismatch.
  target_ids:
  - CHEBI:3507
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/check199200.py
    249 (cwd /private/tmp/antibioticmech-record-reviews-025)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: xref-comparison
  name: Supplemental xref-comparison
  status: passed
  required: false
  summary: Executed successfully against batch 025 cwd; chemical comparison preserves
    the detected external stereo mismatch.
  target_ids:
  - CHEBI:3507
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/compare-249250.py
    (cwd /private/tmp/antibioticmech-record-reviews-025)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - xref-check
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:3507
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
  - CHEBI:3507
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
  - CHEBI:3507
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
  - CHEBI:3507
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
  - CHEBI:3507
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
  - CHEBI:3507
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
  - CHEBI:3507
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
  - CHEBI:3507
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
  - CHEBI:3507
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/cefsulodin.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T11:51:34Z'
  support: supports
  summary: Read seeded/exact identity, definition, six synonyms, four parents, two
    roles, cephalosporin class, structure, five exact xrefs, two drug xrefs, document,
    both source concepts and four history events. No populated activity, target, resistance,
    clinical, producer, dataset or graph objects.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv;data/raw/aro_antibiotics.tsv
  locator: Entire ChEBI row 92 and ARO row 357
  accessed_at: '2026-10-21T11:51:34Z'
  support: supports
  summary: ChEBI owns broad-spectrum definition and three PMID leads; ARO owns under-specified
    PubChem mapping and PMID 119787. ARO describes Pseudomonas activity with little
    activity against other Gram-negative bacteria. All four adopted lead dispositions
    are retained.
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Identity, Equivalence and Evidence standard
  accessed_at: '2026-10-21T11:51:34Z'
  support: supports
  summary: Exact structural xrefs must agree at specified stereocentres; definition
    activity scope should match primary evidence. Optional missing slots alone are
    not defects.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:3507
  locator: Current complete identity, definition, names and parents
  accessed_at: '2026-10-21T11:48:49Z'
  support: partial
  summary: Current ChEBI retains the native R,R,R structure and broad-spectrum wording.
    Primary carboxamide, cephalosporin and organosulfonic-acid parents fit the graph.
    Current source agreement does not independently validate the disputed wording.
  snapshot_sha256: 47b00cf56e762a4c833949a390f1571892d6cd74c0228bc84be2da12fffa60c9
- evidence_id: chemistry
  kind: validation
  reference: RDKit 2026.03.5 native molecular check
  locator: 249-chemistry.json
  accessed_at: '2026-10-21T11:48:36Z'
  support: supports
  summary: Both native encodings reproduce SYLKGLMBLAAGSC-QLVMHMETSA-N, C22H20N4O8S2,
    net zero charge, one fragment, masses and three R centres; both source mints agree.
  snapshot_sha256: d3e05d1d094602487f4fc1c7cd1464d88f3c9473531818c66c7cf8eb8cae1b3d
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/5284530/JSON
  locator: Complete current molecule, InChI and stereochemical SMILES
  accessed_at: '2026-10-21T11:48:49Z'
  support: refutes
  summary: Native xref CID 5284530 has SYLKGLMBLAAGSC-IKZMBGHXSA-N and unassigned
    side-chain stereochemistry, while core 6R,7R remains specified. It is a partially
    specified molecular graph, not a demonstrated opposite epimer or a proven mixture.
  snapshot_sha256: 2c38122ed0ded07d234ff8dc1b48508ad54521dfeb892cb68f858780d03fc08b
- evidence_id: cas-exact
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/62587-73-9/JSON
  locator: CAS lookup and complete molecular graph
  accessed_at: '2026-10-21T11:48:49Z'
  support: supports
  summary: CAS 62587-73-9 resolves CID 656575, whose full key and R side chain match
    native exact cefsulodin. This is a supported replacement candidate, subject to
    maintained source adjudication.
  snapshot_sha256: e3afd026dd076d31cb7c8b7354408f883f885d339fe18351316aee0eff57fa91
- evidence_id: chembl
  kind: database
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL3351077.json
  locator: Full InChI, SMILES and molfile
  accessed_at: '2026-10-21T11:48:49Z'
  support: supports
  summary: All three ChEMBL molecular encodings reproduce the native full key and
    three R stereocentres.
  snapshot_sha256: 9a775fc6df009fefe9dead2273a3e5bc80101b5bb67124c1dfd556f4c89aa565
- evidence_id: kegg
  kind: database
  reference: https://rest.kegg.jp/get/C11253
  locator: C11253 and D07653 entries; C11253 molfile
  accessed_at: '2026-10-21T11:49:37Z'
  support: supports
  summary: Compound and drug entries name cefsulodin with matching formula. The compound
    molfile reproduces native full key and three R centres; generic drug-target prose
    is not a primary target experiment.
  snapshot_sha256: 3bf01aa57c4cd0f9b2f496b2235d891ad30f052ee58a43acfaf6668eed7ebe48
- evidence_id: aro
  kind: authority
  reference: https://card.mcmaster.ca/aro/3004727
  locator: Current definition, graph and xrefs
  accessed_at: '2026-10-21T11:48:49Z'
  support: partial
  summary: ARO canonical stereochemical SMILES matches the exact native graph, but
    it propagates the under-specified PubChem CID. Its activity description is focused
    on Pseudomonas with little other Gram-negative activity.
  snapshot_sha256: 77a7588c1399b0d84928354ae59af339ebfcd53d82618eaa2bb1ad0ae571eb04
- evidence_id: drugcentral
  kind: database
  reference: https://drugcentral.org/drugcard/558
  locator: Drug identity, formula and aliases
  accessed_at: '2026-10-21T11:48:50Z'
  support: supports
  summary: DrugCentral 558 has cefsulodin, matching CAS and formula. Sodium aliases
    are drug-level aggregation and are not exact neutral-form equivalences.
  snapshot_sha256: 5cbd4a3cb6e9752450a1c7c0a50a207ea8045b6fd3a8afb4c33fd27adf053cd9
- evidence_id: wiki
  kind: database
  reference: https://en.wikipedia.org/wiki/Cefsulodin
  locator: Document identity only
  accessed_at: '2026-10-21T11:48:51Z'
  support: context_only
  summary: The named document resolves; it is context, not primary scientific evidence.
  snapshot_sha256: 7a8e83fecfb77f29e351f0d5195eac3d1dc0ffabe1e46a4bf7a660591c8673a0
- evidence_id: adopted-119787
  kind: primary_source
  reference: https://academic.oup.com/jac/article-abstract/5/6/687/782360
  locator: PMID 119787; DOI 10.1093/jac/5.6.687; publisher abstract inspected through
    web tool
  accessed_at: '2026-10-21T11:51:34Z'
  support: partial
  summary: Original study identifies CGP 7174/E and SCE 129 as cefsulodin. It reports
    high P. aeruginosa activity but relative inactivity against coliforms, and distinguishes
    additive/synergistic combination responses. Europe PMC has no abstract; publisher
    abstract was readable through the web tool while direct downloads returned 403.
    Full reagent methods remain unresolved.
- evidence_id: adopted-1384868
  kind: primary_source
  reference: PMID:1384868
  locator: DOI 10.1159/000236216; complete inspected abstract
  accessed_at: '2026-10-21T11:48:51Z'
  support: context_only
  summary: Original aztreonam monoclonal-antibody epitope/cross-reaction experiments
    concern beta-lactam–albumin conjugates and degraded determinants. This abstract
    does not identify a cef­sulodin-specific antibacterial result and is not used
    as mechanism support.
  snapshot_sha256: 6ab4a4e95d597c9d115da2fd8e7184448df43d9fe4a8beebd16d1e165df43c5a
- evidence_id: adopted-29017833
  kind: primary_source
  reference: PMID:29017833
  locator: DOI 10.1016/j.jaip.2017.08.027; inspected abstract
  accessed_at: '2026-10-21T11:48:51Z'
  support: context_only
  summary: Allergy and side-chain cross-reactivity review; contextual lead, not primary
    cefsulodin antibacterial evidence.
  snapshot_sha256: 6ab4a4e95d597c9d115da2fd8e7184448df43d9fe4a8beebd16d1e165df43c5a
- evidence_id: adopted-23139798
  kind: primary_source
  reference: PMID:23139798
  locator: DOI 10.1371/journal.pone.0048598; full body, Methods, Results, Tables 1–4
  accessed_at: '2026-10-21T11:49:18Z'
  support: supports
  summary: Primary study uses E. coli CS109/2443 and mrcA/mrcB deletion/complementation
    plus clinical isolates. Table 3 reports cefsulodin MIC 32 mg/L for both parental
    strains and 1 mg/L after mrcB deletion, restored to 32 mg/L by complementation.
    Tables 2/4 distinguish single-agent measurements from 4 mg/L cefsulodin combinations;
    these cannot establish broad monotherapy efficacy. Exact supplier/salt is not
    specified in the inspected Methods.
  snapshot_sha256: 15f74b9dd1d988239a3db97b07b5db676700b575919423ea775fb95f38048690
- evidence_id: pbp-binding
  kind: primary_source
  reference: PMID:23139798
  locator: 'Results: Cefsulodin Binding Efficacy of PBP1a is Ten Times Higher than
    that of PBP1b; concluding interpretation'
  accessed_at: '2026-10-21T11:49:18Z'
  support: supports
  summary: Bocillin FL competition in deletion backgrounds reports approximately 10
    µM IC50 for PBP1a and 100 µM for PBP1b. These are competition endpoints, not purified
    equilibrium Kd. The authors infer partial PBP1b inhibition to explain combination
    sensitization; deletion/complementation is physiological evidence, not proof that
    PBP1b is the higher-affinity target. Figure 3 names cefadroxil whereas adjacent
    prose names cefotaxime, so that comparator identity requires adjudication before
    extracting kill curves.
  snapshot_sha256: 15f74b9dd1d988239a3db97b07b5db676700b575919423ea775fb95f38048690
- evidence_id: original-spectrum
  kind: primary_source
  reference: DOI:10.11250/chemotherapy1953.27.Supplement2_12
  locator: Original 1979 English summary p41; visually inspected Figure 1 p12
  accessed_at: '2026-10-21T11:49:37Z'
  support: supports
  summary: The primary report explicitly studies cefsulodin monosodium salt. Figure
    1 visibly contains SO3Na. Its English summary reports potent P. aeruginosa and
    some Gram-positive activity with low activity against many Gram-negative rods.
    Preserve sodium material and taxon/strain dependence; no exact-neutral MIC transfer
    or claim that only Pseudomonas can be affected.
  snapshot_sha256: 9b423177ebc3e886c51ee6d71dd5be737948485689ef933554f701b27b6c7788
- evidence_id: spectrum-6770753
  kind: primary_source
  reference: PMID:6770753
  locator: DOI 10.1128/AAC.17.2.165; complete inspected abstract
  accessed_at: '2026-10-21T11:49:37Z'
  support: partial
  summary: Original sodium-cefsulodin study reports activity against P. aeruginosa
    and selected other named Pseudomonas species but not the other tested Gram-negative
    organisms. Inoculum effects and beta-lactamase susceptibility are enzyme/isolate
    dependent. This corroborates focused spectrum, not universal resistance or a neutral-form
    quantitative assay.
  snapshot_sha256: 58bec38b75ede16cfb075f102b618ed7d8b7c9e72c9d41c503001b646fd70f9b
- evidence_id: xref-check
  kind: validation
  reference: Independent complete structure comparison
  locator: 249250-xref-check.json; 249 section
  accessed_at: '2026-10-21T11:50:04Z'
  support: supports
  summary: Native, all three ChEMBL encodings, KEGG molfile and CAS-resolved CID 656575
    agree at R,R,R. Native CID 5284530 retains R at core centres but leaves the side-chain
    carbon unassigned.
  snapshot_sha256: 91282c04a364f5df05aca695b9b16a433251a986c24317b832af660035368804
- evidence_id: local-search
  kind: search
  reference: Ignored-inclusive record/owner and free primary searches
  locator: 249-owner-hits.txt;249-local-hits.txt;249-primary-search.json
  accessed_at: '2026-10-21T11:48:20Z'
  support: context_only
  summary: Exact ID, label, source IDs and full key searched across isolated batch
    025 outside .git/.venv with ignored/hidden coverage. Every adopted lead inspected
    at stated depth; additional original spectrum source followed. No global exhaustive
    literature claim.
  snapshot_sha256: e4d5fa4b83044008fe358e3855d470131bcc96083f59e0c224d7f9b7a666c7b3
  search_scope: 2026-10-21; rg --no-ignore --hidden across batch 025 outside .git/.venv;
    current official identities, every adopted PMID, original PLOS full text and J-STAGE
    spectrum report.
- evidence_id: gates
  kind: validation
  reference: Actual focused native commands
  locator: 249-focused-results.json
  accessed_at: '2026-10-21T11:48:36Z'
  support: supports
  summary: Schema, strict and supplemental native chemistry/mints each exit 0; these
    do not detect external stereo incompleteness or overbroad wording.
  snapshot_sha256: db3dd15cf50db3dd09cdbbfe0206a7055823a45e2d1275a504a6b47552da279f
assessments:
- assessment_id: identity
  area: identity
  topic: Native complete molecular graph
  outcome: supported
  summary: Definition chemical class, names, charge, masses, source mints and core/side-chain
    stereochemistry are internally coherent; ChEMBL and KEGG agree.
  target_ids:
  - CHEBI:3507
  evidence_ids:
  - native
  - chebi
  - chemistry
  - chembl
  - kegg
- assessment_id: grounding
  area: grounding
  topic: Exact PubChem mapping
  outcome: concern
  summary: CID 5284530 lacks the specified R side chain; CID 656575 agrees with the
    complete native structure. This affects exact equivalence, not the correct native
    molecule.
  target_ids:
  - CHEBI:3507
  evidence_ids:
  - pubchem
  - cas-exact
  - xref-check
  - rubric
- assessment_id: roles
  area: grounding
  topic: Parents and antibacterial roles
  outcome: supported
  summary: Structural parents fit. Primary literature supports antibacterial identity
    and activity with material/taxon qualifications.
  target_ids:
  - CHEBI:3507
  evidence_ids:
  - chebi
  - original-spectrum
  - adopted-23139798
- assessment_id: definition
  area: evidence
  topic: Spectrum wording
  outcome: concern
  summary: Unqualified broad-spectrum wording obscures documented low activity against
    many other Gram-negative organisms. Combination sensitization does not establish
    broad single-agent coverage. A bounded activity description is justified.
  target_ids:
  - CHEBI:3507
  evidence_ids:
  - owners
  - aro
  - adopted-119787
  - original-spectrum
  - spectrum-6770753
  - adopted-23139798
- assessment_id: leads
  area: evidence
  topic: All four adopted PMID dispositions
  outcome: supported
  summary: Original antipseudomonal activity and 2012 combination/mechanism studies
    are separated from antibody-conjugate and allergy context.
  target_ids:
  - CHEBI:3507
  evidence_ids:
  - adopted-119787
  - adopted-1384868
  - adopted-23139798
  - adopted-29017833
- assessment_id: mechanism
  area: evidence
  topic: Optional E. coli PBP enrichment
  outcome: supported
  summary: The 2012 source supports bounded competition and deletion/complementation
    evidence. PBP1a has lower measured competition IC50; PBP1b partial inhibition
    explains combination sensitization. Reagent salt and kill-curve comparator identity
    remain unresolved.
  target_ids:
  - CHEBI:3507
  evidence_ids:
  - pbp-binding
  - adopted-23139798
- assessment_id: adapter
  area: scope
  topic: Structured adapter applicability
  outcome: not_applicable
  summary: Native record names no gene/protein/pathway or transcriptomics dataset.
    Newly inspected literature targets are evidence leads rather than native assertions;
    no module absence is used as negative evidence.
  target_ids:
  - CHEBI:3507
  evidence_ids:
  - native
- assessment_id: other-fields
  area: scope
  topic: Clinical, resistance, producer, dataset and graph fields
  outcome: not_applicable
  summary: No native claims populated in these optional domains; current drug mappings
    do not imply a present product authorization or natural producer.
  target_ids:
  - CHEBI:3507
  evidence_ids:
  - native
  - drugcentral
- assessment_id: provenance
  area: provenance
  topic: Maintained owners and history
  outcome: supported
  summary: ChEBI and ARO ownership, source mints and four seed/reseed events traceable.
    Original hashes preserved.
  target_ids:
  - CHEBI:3507
  evidence_ids:
  - native
  - owners
  - chemistry
- assessment_id: schema
  area: schema
  topic: Focused validators
  outcome: supported
  summary: Native checks pass; findings require scientific source/xref review.
  target_ids:
  - CHEBI:3507
  evidence_ids:
  - gates
  - xref-check
- assessment_id: completeness
  area: completeness
  topic: Required repair versus optional enrichment
  outcome: supported
  summary: Repair the populated exact xref and qualify spectrum wording. Unpopulated
    optional activity/target objects are not independent defects.
  target_ids:
  - CHEBI:3507
  evidence_ids:
  - rubric
  - pbp-binding
findings:
- finding_id: F1
  issue_key: chebi-3507-pubchem-5284530-sidechain-stereo
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: The exact PubChem cross-reference omits the R side-chain stereocentre
  description: CID 5284530 is the partially specified SYLKGLMBLAAGSC-IKZMBGHXSA-N
    graph. Native cefsulodin is SYLKGLMBLAAGSC-QLVMHMETSA-N with R at the side-chain
    carbon. CAS-resolved CID 656575, ChEMBL and KEGG match the native complete molecule.
    Correct the source-owned equivalence without altering the correct native structure
    or describing the broader CID as a proven mixture.
  target_ids:
  - CHEBI:3507
  field_paths:
  - xrefs[4]
  evidence_ids:
  - native
  - owners
  - pubchem
  - cas-exact
  - chembl
  - kegg
  - xref-check
  - rubric
  rule_id: native-review-checklist:Identity and Equivalence
  native_severity: major incorrect exact structural grounding
  normalization_reason: A populated exact xref loses specified stereochemistry, while
    the native primary identifier and structure remain correct; major rather than
    wrong-record-identity blocker.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI identity, structure, definition, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, class, xrefs and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding and exclusion overrides
- finding_id: F2
  issue_key: chebi-3507-unqualified-broad-spectrum-definition
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: The broad-spectrum definition needs evidence-bounded wording
  description: The definition labels cefsulodin broadly without qualification. The
    adopted 1979 source, additional original sodium-material reports and ARO describe
    focused antipseudomonal activity with low activity against many other Gram-negative
    organisms; some Gram-positive and other bacterial activity is retained. The 2012
    broad isolate sensitization is a combination result. Replace broad-spectrum shorthand
    with a bounded description rather than claiming universal inactivity outside Pseudomonas.
  target_ids:
  - CHEBI:3507
  field_paths:
  - definition
  evidence_ids:
  - native
  - owners
  - aro
  - adopted-119787
  - original-spectrum
  - spectrum-6770753
  - adopted-23139798
  rule_id: native-review-checklist:Evidence standard and Completeness
  native_severity: minor overbroad descriptive wording
  normalization_reason: The antibiotic identity and antibacterial eligibility are
    supported; this is imprecise spectrum shorthand in prose, not an invented quantitative
    susceptibility observation.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI identity, structure, definition, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, class, xrefs and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding and exclusion overrides
actions:
- action_id: A1
  description: Repair the exact PubChem mapping through maintained source ownership.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:3507
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI identity, structure, definition, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, class, xrefs and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding and exclusion overrides
  acceptance_checks:
  - Replace or adjudicate CID 5284530 using the verified complete R,R,R identity;
    CID 656575 is a directly verified candidate.
  - Preserve native structure and complete InChIKey; ensure reseeding does not reintroduce
    the broader ARO mapping.
  - Run exact xref structure comparison plus native schema/strict and applicable term/reference/history/corpus
    gates after separate curation authorization.
- action_id: A2
  description: Qualify the spectrum definition without erasing supported activity.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:3507
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI identity, structure, definition, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, class, xrefs and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding and exclusion overrides
  acceptance_checks:
  - Describe antipseudomonal activity and limited activity against many other Gram-negative
    organisms, retaining some Gram-positive activity and sodium-source scope.
  - Do not transfer combination sensitization to monotherapy or interpret a finite
    negative panel as universal species resistance.
- action_id: A3
  description: Optionally curate 2012 activity and PBP evidence with assay-specific
    scope.
  finding_ids: []
  target_ids:
  - CHEBI:3507
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefsulodin.yaml
    role: Curator-owned activity_spectrum and PRIMARY_LITERATURE targets via validated
      writer
  acceptance_checks:
  - Resolve cefsulodin reagent salt/material before quantitative transfer.
  - Separate strain MIC, Bocillin competition IC50, deletion/complementation and inferred
    partial inhibition; do not use competition IC50 as Kd.
  - Resolve Figure 3 cefadroxil versus prose cefotaxime before extracting the time-kill
    comparator.
limitations:
- 1979 adopted paper was inspected through publisher abstract; full methods inaccessible
  via direct 403. The 1979 J-STAGE English summary and structure figure were inspected;
  complete Japanese experimental narrative was not translated.
- Original spectrum studies explicitly use sodium material; exact native-zwitterion
  quantitative transfer remains unresolved.
- The 2012 full text does not specify exact cefsulodin supplier/salt in its inspected
  Methods. Its Figure 3 and adjacent prose disagree on one companion beta-lactam.
- Antibody and allergy leads were inspected at abstract level and are not used for
  exact antibacterial or binding claims.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 21 expanded input hashes unchanged; no native/source/status/history changes.
- Native gates used batch 025 environment; standalone RDKit 2026.03.5 checks used
  existing batch 019 interpreter against batch 025 cwd.
- Free public sources only; no exact-compound or universal-spectrum claim inferred
  from document titles alone.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:3502
- https://doi.org/10.7164/antibiotics.45.709
- https://www.jstage.jst.go.jp/article/antibiotics1968/45/5/45_5_709/_pdf
tags:
- cefozopran
- chemical-description
- thiadiazole
- primary-activity
```
