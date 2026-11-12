# Review of A47934

- Review: 20261021T083153Z-a47934-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T08:25:11Z
- Finished UTC: 2026-10-21T08:31:53Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

A47934 is the sulfated, nonglycosylated glycopeptide-family antibiotic from S. toyocaensis. Native ChEBI chemistry is internally consistent, but linked PubChem, KEGG and KNApSAcK representations conflict stereochemically. One major finding requires reconciliation; two minor findings cover a flattened systematic name and available primary target/activity evidence. No replacement structure is endorsed.

## Scope And Provenance

Whole exact record; ChEBI/ARO owners; chemical encodings, all synonyms, seven parents, role, six compound xrefs and five document xrefs; all seven adopted compound PMID leads plus the target-definition reference; primary producer and exact target-binding evidence.

Selection: Path-ordered unreviewed queue index 074; exactly one record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:29505 | data/antibiotics/antibacterial/a47934.yaml | generated | A47934 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented per-record LinkML validation | passed | True | CHEBI:29505 | Exit 0; No issues found. |
| Documented closed-schema validation | passed | True | CHEBI:29505 | Exit 0; one record and zero ERROR rows. |
| Native consistency and exact xref stereochemistry | failed | False | CHEBI:29505 | Exit 1: native encodings, formula, charge, masses and mints agree, but external stereo keys conflict. |
| Current ChEBI and ARO source assertions | failed | False | CHEBI:29505 | Exit 1 for lost bridge-locant delimiters in the systematic synonym. Exact term, native structure, six ChEBI parents, role link, common synonyms, source xref strings and ARO target/class checks pass. |
| Structured-source applicability before web research | not_applicable | False | CHEBI:29505 | Current native target is a chemical D-Ala-D-Ala cell-wall component, not a gene or protein. No native regulator, locus, pathway or expression dataset supplies an adapter candidate. |
| Authoritative full QC | failed | True | CHEBI:29505 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:29505 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:29505 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:29505 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:29505 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:29505 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:29505 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:29505 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:29505 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Intended sulfated A47934 and stereochemistry

identity: concern. Targets: CHEBI:29505.

Intended compound, formula, scaffold and producer are clear. Exact stereochemistry is internally consistent but conflicts with multiple linked authorities.

### Parent classes and activity role

grounding: supported. Targets: CHEBI:29505.

All chemical parents and broad glycopeptide-family classification fit the sulfated aglycone. The family term does not claim attached sugar.

### Systematic-name bridge locants

representation: concern. Targets: CHEBI:29505.

Common synonyms are correct; source-to-native flattening concatenates bridge sizes and attachment locants in the systematic name.

### Qualified cell-wall-component assertion

evidence: supported. Targets: CHEBI:29505.

The native target is properly typed and qualified as database-only; independent exact-compound ITC supports this chemical target. No protein target or primary evidence status is falsely asserted.

### Claim-level primary annotation

completeness: concern. Targets: CHEBI:29505.

Verified exact-compound binding/activity and producer self-resistance can enrich evidence without transferring analogue measurements.

### Source ownership and seed history

ownership: supported. Targets: CHEBI:29505.

Actual ChEBI plus ARO owners captured before judgment; all 16 input hashes remain unchanged and five seed/reseed events are coherent.

### Patent and external identifier scope

scope: supported. Targets: CHEBI:29505.

All five patents resolve as documents. CAS is corroborated by multiple chemical databases; MetaCyc target access remains unresolved and stereochemical xrefs require correction.

### Clinical, causal graphs and datasets

representation: not_applicable. Targets: CHEBI:29505.

No such native assertions need correction. Clinical use of other glycopeptides does not establish clinical efficacy of A47934.

### Focused native validators

schema: supported. Targets: CHEBI:29505.

Both documented native checks pass; supplemental comparisons expose semantic issues.

## Findings

### F1: Linked A47934 structures disagree in tetrahedral stereochemistry

major / open / confirmed; issue key: chebi-29505-a47934-cross-reference-stereochemistry-conflict.

ChEBI/native, PubChem/KEGG and KNApSAcK cannot all be treated as one exact structural encoding. The conflict is confirmed, but which assignment is chemically correct requires primary stereochemical reconciliation; native internal consistency alone does not settle it.

### F2: Exact primary target-binding and activity evidence is available

minor / open / confirmed; issue key: chebi-29505-a47934-primary-target-activity-evidence.

The record correctly limits its target to a database assertion, while inspected exact-compound primary data can support a bounded primary annotation and producer self-resistance context.

### F3: Systematic synonym loses delimiters around bridge locants

minor / open / confirmed; issue key: chebi-29505-a47934-systematic-name-bridge-locants-flattened.

Native undecacyclo[38.14.2.23,6.214,17...] concatenates bridge sizes and attachment locants. Current source text uses [38.14.2.2(3,6).2(14,17)...], retaining the intended numerical grouping.

## Recommended Actions And Acceptance Checks

### A1

Resolve the exact A47934 stereo assignment against primary structural evidence and qualify or repair the conflicting source mappings before regeneration.

- Atom-map all eight centres across native ChEBI, PubChem 16131155 and KEGG C12016; primary connectivity Figure 1 alone is insufficient to arbitrate them. Verify the experimentally supported absolute configuration before changing any structure.
- Reconcile KNApSAcK displayed key, InChI and partially specified SMILES; preserve an explicit source conflict if no exact corrected accession exists. Do not replace native chemistry simply by majority vote.
- Keep sulfate ester, desulfo analogue, neutral molecule and physiological ionic forms distinct; MetaCyc mapping must retain charge/form scope.
- Repair maintained rows/import or cross-source selection, regenerate through scripts/seed_from_sources.py, and recheck exact encodings/xrefs, native schema/strict, term/reference/history and corpus gates.

### A2

Add exact primary evidence with binding, assay, analogue and producer scope preserved.

- Attach the direct peptide-binding study to the chemical cell-wall target, preserving ligand and experimental conditions. Do not invent a protein example for a chemical group.
- Retain organism/strain, assay endpoint, units and exposure context for activity and resistance observations. Keep desulfo/dechloro analogues separate.
- Treat resistance-induction and dimerization observations as bounded phenotypes, not direct binding of A47934 to VanS.
- Support structured producer/self-resistance from the exact biosynthetic studies, then use validated writer/history and all required native gates before scientific sign-off.

### A3

Preserve systematic-name bridge-locant grouping during source text normalization and regeneration.

- Preserve parentheses or equivalent unambiguous superscript/plain-text notation for each bridge descriptor. Compare the full corrected synonym against the authoritative source and chosen stereo identity.
- Ensure the adopted inventory and generated synonym reproduce the correction; inspect other affected source serialization only as separately authorized follow-up.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/a47934.yaml; Entire generated record | supports | Read exact ChEBI identity, producer definition, three synonyms, seven parents, activity role, full chemistry, six compound and five patent xrefs, two source mints, qualified D-Ala-D-Ala target and all five seed/reseed events. No quantified activity, direct primary target evidence or native resistance assertion is present. |
| inventory | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv; Exact CHEBI:29505 and ARO:3000117 rows; 074-owner-hits.txt | supports | ChEBI owns chemistry, producer definition, six chemical parents, synonyms and document xrefs; ARO adds the valid family class and explicitly database-only chemical target. Both deterministic source mints reproduce. Ignored-inclusive owner search found the exact adopted rows. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:29505; 074-chebi.html; 074-ols.json | partial | Current non-obsolete 3_STAR A47934 reproduces native SMILES/InChI/key HRGFAEUWEMDRRZ-RIZHWKQXSA-N, neutral C58H44Cl3N7O21S, definition and common synonyms. Current systematic name preserves bridge locants as 2(3,6), 2(14,17), etc.; the native name concatenates these digits. |
| ontology | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_29505/parents; 074-parents.json; current ChEBI role link | supports | Six chemical parents resolve to heterodetic cyclic peptide, peptide antibiotic, polyphenol, organochlorine compound, cyclic ether and aryl sulfate. CHEBI:33281 is linked as antimicrobial agent on the current ChEBI page. The glyc(o)peptide family wording does not assert glycosylation of this aglycone. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/16131155; 074-pubchem.json | refutes | The exact native CID resolves, but both current PubChem encodings yield HRGFAEUWEMDRRZ-QLRHZSCISA-N rather than the native key. Formula/connectivity agree; two tetrahedral assignments differ after canonical orientation normalization. |
| kegg | https://rest.kegg.jp/get/C12016; 074-kegg.txt and 074-kegg.mol | partial | KEGG resolves to A47934 and the same CAS/formula. Its MOL structure yields the same stereo key as PubChem, differing from native ChEBI. Its generic PubChem cross-link is not automatically a compound CID. |
| knapsack | https://www.knapsackfamily.com/knapsack_core/information.php?word=C00017818; 074-knapsack.html | refutes | Entry names A47934 and S. toyocaensis NRRL 15009 but displays inconsistent representations: listed key HRGFAEUWEMDRRZ-XJCGJUTINA-N; key regenerated from its InChI HRGFAEUWEMDRRZ-ZYFHSOSJSA-N; SMILES key HRGFAEUWEMDRRZ-WFIQNICMSA-N with one unassigned centre. None equals the native key. |
| metacyc | https://biocyc.org/compound?orgid=META&amp;id=CPD-15750; 074-metacyc.html; ChEBI cross-reference scope | unknown | HTTP200 returned a Create Account page rather than the compound, so the external structure remains unresolved. ChEBI repeats CPD-15750 on both neutral A47934 and its major physiological dianion CHEBI:76892; protonation scope needs care and is not evidence that native charge zero is wrong. |
| patents | patent:EP0100605; patent:US4462942; patent:US4537879; patent:US4659660; patent:US4880735; 074-EP0100605A1.html; 074-US4462942A.html; 074-US4537879A.html; 074-US4659660A.html; 074-US4880735A.html | supports | All five document identifiers resolve to A47934 production documents. The first four concern the exact sulfate antibiotic and NRRL 15009; US4880735 concerns improved producer NRRL 18112. Patent text describes salts as well as free antibiotic; document links are not asserted as exact salt identities or independent clinical proof. |
| producer-primary | PMID:3793622; DOI:10.7164/antibiotics.39.1533; 074-primary1986.pdf taxonomy/fermentation sections and Fig1 | supports | Primary work supports production by S. toyocaensis NRRL 15009 and the nonglycosylated sulfate-ester scaffold. Original Fig1 is a connectivity depiction and does not resolve the current stereochemical conflict. B. subtilis ATCC6633 agar-well/bioautography is a fermentation bioassay, not a reported pure-compound MIC. Introductory mouse/feeding claims are cited background, not clinical efficacy. |
| binding-primary | PMID:23104813; DOI:10.1128/JB.01617-12; publisher/PMC full-text Methods, Results and Table1 exposed by web reader | supports | Exact A47934 binds Nα,Nε-diacetyl-L-Lys-D-Ala-D-Ala by ITC: KD 4.76±1.6 µM, using citrate pH 5.1. Table 1 reports MIC 512 µg/mL for S. coelicolor and 8 for each Streptomyces isolate WAC1380/WAC1386; solid-phase assays use 2×10^4 spores/well, 30°C, 72 h. Desulfo-A47934 is separate. Weaker resistance induction and reduced dimerization do not directly demonstrate A47934–VanS binding. |
| biosynthesis-primary | PMID:12060705; DOI:10.1073/pnas.102285099; public PMC Results on antibiotic resistance and Figure5 | supports | The biosynthetic cluster belongs to S. toyocaensis NRRL 15009. Insertional vanAst disruption causes A47934 sensitivity and delayed production; in-trans vanHAX rescue supports producer self-resistance. The locus is a resistance/biosynthesis context, not the antibiotic molecular target. |
| chlorination-lead | PMID:30275088; DOI:10.1128/AAC.01540-18; inspected indexed abstract and primary Results paragraph | context_only | The 2018 study is relevant to biosynthetic chlorination and resistance induction. Its displayed ITC comparison measures desulfo-A47934 and the desulfo/dechloro derivative; those affinities are not transferred to sulfated native A47934. |
| adopted-leads | Europe PMC indexed records; 074-core.json; 074-target-core.json; 074-lead-dispositions.json | supports | All seven distinct compound-source PMIDs were resolved and their abstracts read: 12060705 cluster/self-resistance; 17329243 StaL structure and substrate modeling; 17884639 oxygenase crosslinking; 3124730 radiolabeled biosynthesis; 3793622 taxonomy/fermentation; 16492565 sulfation enzymology and comparative activity; 9435111 producer D-Ala ligases. Target-term PMID 18258256 concerns oritavancin/vancomycin, not direct A47934 evidence. Each scope is recorded in the disposition file. |
| chemistry | RDKit exact structure and source-mint calculations; 074-chemistry.py and 074-chemistry.json | supports | Native SMILES and InChI agree and assign all eight tetrahedral centres; formula, charge and masses agree. Both mints reproduce. All compared structures have the same stereo-stripped standard identity, but stereo keys differ as detailed above; this establishes conflict rather than selecting the true natural-product encoding. |
| source-check | Current ChEBI and ARO checks; 074-source-check.py and 074-source-check.json | supports | Source labels, exact native structure, chemical parents, role link, common synonyms and xref strings reproduce; ARO class and D-Ala-D-Ala edge agree with read-only OBO cache SHA256 d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4. Systematic synonym bridge-locant formatting differs and causes exit 1. |
| validation | just validate; just validate-strict; Actual batch008 focused native executions; 074-strict.tsv | supports | Both native focused validators exited 0; strict scanned one file and found zero ERROR rows. Chemical cross-source conflicts are outside those checks. |
| search | Ignored-inclusive local and exact-compound public search; 074-local-hits.txt and 074-owner-hits.txt | context_only | Confirmed exact source rows and researched exact A47934 identity, original production, peptide binding and resistance. No claim of exhaustive literature absence is made. |

## Limits And Additional Notes

- The natural-product absolute stereochemistry remains unresolved across inspected authorities. The 1986 primary structure figure confirms connectivity but does not supply explicit stereobonds. No replacement encoding or native identity rejection is asserted.
- All seven adopted compound-source PMID abstracts and the target-definition PMID were read and dispositioned. Primary2013 Methods/Results/Table 1 and primary 2002 resistance Results were inspected through the web reader. Their local PMC HTML downloads returned browser challenges, not article bodies; no snapshot hash is falsely attached to those primary passages.
- Europe PMC XML retrievals for primary 2002/2013/2018 failed with HTTP500, publisher direct fetch403 and the attempted primary 2013 CiteSeer PDF404. Primary1986 PDF was successfully read; failed retrievals do not negate successfully inspected web primary text.
- MetaCyc CPD-15750 returned an account page. CAS 90039-80-8 is corroborated by KEGG/KNApSAcK/ChEBI but was not independently resolved against the CAS registry.
- Required shared gates are coordinated separately; native scientific status remains SEEDED and no sign-off is claimed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Only scratch artifacts were written; all 16 captured input hashes rechecked unchanged.
- The first supplemental source-check attempts failed at the OLS has_role response and exact synonym comparison. The final check uses the actual ChEBI page role link, records the systematic-name defect and exits 1 for that defect; the has_role response is not used as a valid role assertion.
- Primary2018 ITC values concern desulfo and desulfo/dechloro analogues and are deliberately excluded from proposed native quantitative binding evidence.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T083153Z-a47934-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of A47934
started_at: '2026-10-21T08:25:11Z'
finished_at: '2026-10-21T08:31:53Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Major cross-authority stereochemistry inconsistency; native encodings
  internally agree, broad identity and qualified target are supported
scientific_review: true
summary: A47934 is the sulfated, nonglycosylated glycopeptide-family antibiotic from
  S. toyocaensis. Native ChEBI chemistry is internally consistent, but linked PubChem,
  KEGG and KNApSAcK representations conflict stereochemically. One major finding requires
  reconciliation; two minor findings cover a flattened systematic name and available
  primary target/activity evidence. No replacement structure is endorsed.
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
  - path: data/antibiotics/antibacterial/a47934.yaml
    sha256: da60ffacfff0b233bf5e565315a48185cf2761e5b14697d35247a88845699a3b
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
    role: context
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
scope:
  description: Whole exact record; ChEBI/ARO owners; chemical encodings, all synonyms,
    seven parents, role, six compound xrefs and five document xrefs; all seven adopted
    compound PMID leads plus the target-definition reference; primary producer and
    exact target-binding evidence.
  selection: Path-ordered unreviewed queue index 074; exactly one record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:29505
targets:
- target_id: CHEBI:29505
  path: data/antibiotics/antibacterial/a47934.yaml
  label: A47934
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
    role: Adopted ARO class and identity
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Adopted exact D-Ala-D-Ala target assertion
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Reviewed target-evidence qualifications
checks:
- check_id: schema
  name: Documented per-record LinkML validation
  status: passed
  required: true
  summary: Exit 0; No issues found.
  target_ids:
  - CHEBI:29505
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/a47934.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented closed-schema validation
  status: passed
  required: true
  summary: Exit 0; one record and zero ERROR rows.
  target_ids:
  - CHEBI:29505
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/a47934.yaml --out /private/tmp/am-review-session/074-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Native consistency and exact xref stereochemistry
  status: failed
  required: false
  summary: 'Exit 1: native encodings, formula, charge, masses and mints agree, but
    external stereo keys conflict.'
  target_ids:
  - CHEBI:29505
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/074-chemistry.py
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: source-check
  name: Current ChEBI and ARO source assertions
  status: failed
  required: false
  summary: Exit 1 for lost bridge-locant delimiters in the systematic synonym. Exact
    term, native structure, six ChEBI parents, role link, common synonyms, source
    xref strings and ARO target/class checks pass.
  target_ids:
  - CHEBI:29505
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/074-source-check.py
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - source-check
- check_id: imodulondb
  name: Structured-source applicability before web research
  status: not_applicable
  required: false
  summary: Current native target is a chemical D-Ala-D-Ala cell-wall component, not
    a gene or protein. No native regulator, locus, pathway or expression dataset supplies
    an adapter candidate.
  target_ids:
  - CHEBI:29505
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:29505
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
  - CHEBI:29505
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
  - CHEBI:29505
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
  - CHEBI:29505
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
  - CHEBI:29505
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
  - CHEBI:29505
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
  - CHEBI:29505
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
  - CHEBI:29505
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
  - CHEBI:29505
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/a47934.yaml
  locator: Entire generated record
  accessed_at: '2026-10-21T08:31:08Z'
  support: supports
  summary: Read exact ChEBI identity, producer definition, three synonyms, seven parents,
    activity role, full chemistry, six compound and five patent xrefs, two source
    mints, qualified D-Ala-D-Ala target and all five seed/reseed events. No quantified
    activity, direct primary target evidence or native resistance assertion is present.
- evidence_id: inventory
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv
  locator: Exact CHEBI:29505 and ARO:3000117 rows; 074-owner-hits.txt
  accessed_at: '2026-10-21T08:31:08Z'
  support: supports
  summary: ChEBI owns chemistry, producer definition, six chemical parents, synonyms
    and document xrefs; ARO adds the valid family class and explicitly database-only
    chemical target. Both deterministic source mints reproduce. Ignored-inclusive
    owner search found the exact adopted rows.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:29505
  locator: 074-chebi.html; 074-ols.json
  accessed_at: '2026-10-21T08:31:08Z'
  support: partial
  summary: Current non-obsolete 3_STAR A47934 reproduces native SMILES/InChI/key HRGFAEUWEMDRRZ-RIZHWKQXSA-N,
    neutral C58H44Cl3N7O21S, definition and common synonyms. Current systematic name
    preserves bridge locants as 2(3,6), 2(14,17), etc.; the native name concatenates
    these digits.
  snapshot_sha256: 08cc20ea9648839cf59812d30e1a8d79ba419fcd2c420a7cec33503e718a4d29
- evidence_id: ontology
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_29505/parents
  locator: 074-parents.json; current ChEBI role link
  accessed_at: '2026-10-21T08:31:08Z'
  support: supports
  summary: Six chemical parents resolve to heterodetic cyclic peptide, peptide antibiotic,
    polyphenol, organochlorine compound, cyclic ether and aryl sulfate. CHEBI:33281
    is linked as antimicrobial agent on the current ChEBI page. The glyc(o)peptide
    family wording does not assert glycosylation of this aglycone.
  snapshot_sha256: 9bd20daedd7d7285170e0f65c1c64c0607452c637367f2f8af8e5860122e4131
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/16131155
  locator: 074-pubchem.json
  accessed_at: '2026-10-21T08:31:08Z'
  support: refutes
  summary: The exact native CID resolves, but both current PubChem encodings yield
    HRGFAEUWEMDRRZ-QLRHZSCISA-N rather than the native key. Formula/connectivity agree;
    two tetrahedral assignments differ after canonical orientation normalization.
  snapshot_sha256: 2fc4dd2f7f9c108c80048a82937c30e72d758e1126420de7b5d26be067806f77
- evidence_id: kegg
  kind: database
  reference: https://rest.kegg.jp/get/C12016
  locator: 074-kegg.txt and 074-kegg.mol
  accessed_at: '2026-10-21T08:31:08Z'
  support: partial
  summary: KEGG resolves to A47934 and the same CAS/formula. Its MOL structure yields
    the same stereo key as PubChem, differing from native ChEBI. Its generic PubChem
    cross-link is not automatically a compound CID.
  snapshot_sha256: 85fd67158dcca306b5c7e81a908c0abde96858ce70cdf9a557cc8a017a52d542
- evidence_id: knapsack
  kind: database
  reference: https://www.knapsackfamily.com/knapsack_core/information.php?word=C00017818
  locator: 074-knapsack.html
  accessed_at: '2026-10-21T08:31:08Z'
  support: refutes
  summary: 'Entry names A47934 and S. toyocaensis NRRL 15009 but displays inconsistent
    representations: listed key HRGFAEUWEMDRRZ-XJCGJUTINA-N; key regenerated from
    its InChI HRGFAEUWEMDRRZ-ZYFHSOSJSA-N; SMILES key HRGFAEUWEMDRRZ-WFIQNICMSA-N
    with one unassigned centre. None equals the native key.'
  snapshot_sha256: d620cbcf957133e36fc979a04e4f4c111a7ba1c5cfc553f124290fbca689f557
- evidence_id: metacyc
  kind: database
  reference: https://biocyc.org/compound?orgid=META&id=CPD-15750
  locator: 074-metacyc.html; ChEBI cross-reference scope
  accessed_at: '2026-10-21T08:31:08Z'
  support: unknown
  summary: HTTP200 returned a Create Account page rather than the compound, so the
    external structure remains unresolved. ChEBI repeats CPD-15750 on both neutral
    A47934 and its major physiological dianion CHEBI:76892; protonation scope needs
    care and is not evidence that native charge zero is wrong.
  snapshot_sha256: 24b2a5abdd8d3058fe1e7712b8b3184785d0d2e8b86ff8784e1e511f2bda41da
- evidence_id: patents
  kind: primary_source
  reference: patent:EP0100605; patent:US4462942; patent:US4537879; patent:US4659660;
    patent:US4880735
  locator: 074-EP0100605A1.html; 074-US4462942A.html; 074-US4537879A.html; 074-US4659660A.html;
    074-US4880735A.html
  accessed_at: '2026-10-21T08:31:08Z'
  support: supports
  summary: All five document identifiers resolve to A47934 production documents. The
    first four concern the exact sulfate antibiotic and NRRL 15009; US4880735 concerns
    improved producer NRRL 18112. Patent text describes salts as well as free antibiotic;
    document links are not asserted as exact salt identities or independent clinical
    proof.
  snapshot_sha256: d511f3ee9af3e39096828033eb09aa59ede787f56401dd327054f5969ff34e74
- evidence_id: producer-primary
  kind: primary_source
  reference: PMID:3793622
  locator: DOI:10.7164/antibiotics.39.1533; 074-primary1986.pdf taxonomy/fermentation
    sections and Fig1
  accessed_at: '2026-10-21T08:31:08Z'
  support: supports
  summary: Primary work supports production by S. toyocaensis NRRL 15009 and the nonglycosylated
    sulfate-ester scaffold. Original Fig1 is a connectivity depiction and does not
    resolve the current stereochemical conflict. B. subtilis ATCC6633 agar-well/bioautography
    is a fermentation bioassay, not a reported pure-compound MIC. Introductory mouse/feeding
    claims are cited background, not clinical efficacy.
  snapshot_sha256: 3300a299ab1ed052826909a2b2b0daaf9afdff016c19500930f00f184d11e649
- evidence_id: binding-primary
  kind: primary_source
  reference: PMID:23104813
  locator: DOI:10.1128/JB.01617-12; publisher/PMC full-text Methods, Results and Table1
    exposed by web reader
  accessed_at: '2026-10-21T08:31:08Z'
  support: supports
  summary: 'Exact A47934 binds Nα,Nε-diacetyl-L-Lys-D-Ala-D-Ala by ITC: KD 4.76±1.6
    µM, using citrate pH 5.1. Table 1 reports MIC 512 µg/mL for S. coelicolor and
    8 for each Streptomyces isolate WAC1380/WAC1386; solid-phase assays use 2×10^4
    spores/well, 30°C, 72 h. Desulfo-A47934 is separate. Weaker resistance induction
    and reduced dimerization do not directly demonstrate A47934–VanS binding.'
- evidence_id: biosynthesis-primary
  kind: primary_source
  reference: PMID:12060705
  locator: DOI:10.1073/pnas.102285099; public PMC Results on antibiotic resistance
    and Figure5
  accessed_at: '2026-10-21T08:31:08Z'
  support: supports
  summary: The biosynthetic cluster belongs to S. toyocaensis NRRL 15009. Insertional
    vanAst disruption causes A47934 sensitivity and delayed production; in-trans vanHAX
    rescue supports producer self-resistance. The locus is a resistance/biosynthesis
    context, not the antibiotic molecular target.
- evidence_id: chlorination-lead
  kind: primary_source
  reference: PMID:30275088
  locator: DOI:10.1128/AAC.01540-18; inspected indexed abstract and primary Results
    paragraph
  accessed_at: '2026-10-21T08:31:08Z'
  support: context_only
  summary: The 2018 study is relevant to biosynthetic chlorination and resistance
    induction. Its displayed ITC comparison measures desulfo-A47934 and the desulfo/dechloro
    derivative; those affinities are not transferred to sulfated native A47934.
- evidence_id: adopted-leads
  kind: database
  reference: Europe PMC indexed records
  locator: 074-core.json; 074-target-core.json; 074-lead-dispositions.json
  accessed_at: '2026-10-21T08:31:08Z'
  support: supports
  summary: 'All seven distinct compound-source PMIDs were resolved and their abstracts
    read: 12060705 cluster/self-resistance; 17329243 StaL structure and substrate
    modeling; 17884639 oxygenase crosslinking; 3124730 radiolabeled biosynthesis;
    3793622 taxonomy/fermentation; 16492565 sulfation enzymology and comparative activity;
    9435111 producer D-Ala ligases. Target-term PMID 18258256 concerns oritavancin/vancomycin,
    not direct A47934 evidence. Each scope is recorded in the disposition file.'
  snapshot_sha256: 46628df2e7867331aa406e0b5e0d113526b705c9afd5d81359cbb1b6cdeca4ec
- evidence_id: chemistry
  kind: validation
  reference: RDKit exact structure and source-mint calculations
  locator: 074-chemistry.py and 074-chemistry.json
  accessed_at: '2026-10-21T08:31:08Z'
  support: supports
  summary: Native SMILES and InChI agree and assign all eight tetrahedral centres;
    formula, charge and masses agree. Both mints reproduce. All compared structures
    have the same stereo-stripped standard identity, but stereo keys differ as detailed
    above; this establishes conflict rather than selecting the true natural-product
    encoding.
  snapshot_sha256: e0d17d3443504158020bd796b528b79768452096bc3b3a53557d259874fe4b0c
- evidence_id: source-check
  kind: validation
  reference: Current ChEBI and ARO checks
  locator: 074-source-check.py and 074-source-check.json
  accessed_at: '2026-10-21T08:31:08Z'
  support: supports
  summary: Source labels, exact native structure, chemical parents, role link, common
    synonyms and xref strings reproduce; ARO class and D-Ala-D-Ala edge agree with
    read-only OBO cache SHA256 d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4.
    Systematic synonym bridge-locant formatting differs and causes exit 1.
  snapshot_sha256: cadef2c587eda233e82a9768b1b0f234a48c43a2f2e6d3dcda536d40c5755c83
- evidence_id: validation
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual batch008 focused native executions; 074-strict.tsv
  accessed_at: '2026-10-21T08:31:08Z'
  support: supports
  summary: Both native focused validators exited 0; strict scanned one file and found
    zero ERROR rows. Chemical cross-source conflicts are outside those checks.
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local and exact-compound public search
  locator: 074-local-hits.txt and 074-owner-hits.txt
  accessed_at: '2026-10-21T08:31:08Z'
  support: context_only
  summary: Confirmed exact source rows and researched exact A47934 identity, original
    production, peptide binding and resistance. No claim of exhaustive literature
    absence is made.
  search_scope: prepare.py 74 ran rg --no-ignore --hidden excluding only .git/.venv
    before judgment; follow-up searched raw inventories,curation,conf by CHEBI,ARO
    and key. Public work included all adopted compound PMID leads, target reference
    and five patent documents.
assessments:
- assessment_id: identity
  area: identity
  topic: Intended sulfated A47934 and stereochemistry
  outcome: concern
  summary: Intended compound, formula, scaffold and producer are clear. Exact stereochemistry
    is internally consistent but conflicts with multiple linked authorities.
  target_ids:
  - CHEBI:29505
  evidence_ids:
  - record
  - chebi
  - pubchem
  - kegg
  - knapsack
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: Parent classes and activity role
  outcome: supported
  summary: All chemical parents and broad glycopeptide-family classification fit the
    sulfated aglycone. The family term does not claim attached sugar.
  target_ids:
  - CHEBI:29505
  evidence_ids:
  - ontology
  - source-check
  - producer-primary
- assessment_id: synonyms
  area: representation
  topic: Systematic-name bridge locants
  outcome: concern
  summary: Common synonyms are correct; source-to-native flattening concatenates bridge
    sizes and attachment locants in the systematic name.
  target_ids:
  - CHEBI:29505
  evidence_ids:
  - chebi
  - source-check
- assessment_id: target
  area: evidence
  topic: Qualified cell-wall-component assertion
  outcome: supported
  summary: The native target is properly typed and qualified as database-only; independent
    exact-compound ITC supports this chemical target. No protein target or primary
    evidence status is falsely asserted.
  target_ids:
  - CHEBI:29505
  evidence_ids:
  - record
  - source-check
  - binding-primary
- assessment_id: completeness
  area: completeness
  topic: Claim-level primary annotation
  outcome: concern
  summary: Verified exact-compound binding/activity and producer self-resistance can
    enrich evidence without transferring analogue measurements.
  target_ids:
  - CHEBI:29505
  evidence_ids:
  - binding-primary
  - biosynthesis-primary
  - chlorination-lead
- assessment_id: provenance
  area: ownership
  topic: Source ownership and seed history
  outcome: supported
  summary: Actual ChEBI plus ARO owners captured before judgment; all 16 input hashes
    remain unchanged and five seed/reseed events are coherent.
  target_ids:
  - CHEBI:29505
  evidence_ids:
  - inventory
  - record
- assessment_id: document-xrefs
  area: scope
  topic: Patent and external identifier scope
  outcome: supported
  summary: All five patents resolve as documents. CAS is corroborated by multiple
    chemical databases; MetaCyc target access remains unresolved and stereochemical
    xrefs require correction.
  target_ids:
  - CHEBI:29505
  evidence_ids:
  - patents
  - kegg
  - knapsack
  - metacyc
- assessment_id: optional
  area: representation
  topic: Clinical, causal graphs and datasets
  outcome: not_applicable
  summary: No such native assertions need correction. Clinical use of other glycopeptides
    does not establish clinical efficacy of A47934.
  target_ids:
  - CHEBI:29505
  evidence_ids:
  - record
- assessment_id: schema
  area: schema
  topic: Focused native validators
  outcome: supported
  summary: Both documented native checks pass; supplemental comparisons expose semantic
    issues.
  target_ids:
  - CHEBI:29505
  evidence_ids:
  - validation
  - chemistry
  - source-check
findings:
- finding_id: F1
  issue_key: chebi-29505-a47934-cross-reference-stereochemistry-conflict
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Linked A47934 structures disagree in tetrahedral stereochemistry
  description: ChEBI/native, PubChem/KEGG and KNApSAcK cannot all be treated as one
    exact structural encoding. The conflict is confirmed, but which assignment is
    chemically correct requires primary stereochemical reconciliation; native internal
    consistency alone does not settle it.
  target_ids:
  - CHEBI:29505
  field_paths:
  - chemical_structure
  - xrefs
  evidence_ids:
  - chebi
  - pubchem
  - kegg
  - knapsack
  - chemistry
  - producer-primary
  rule_id: 'review-checklist: Identity and source cross-references'
  native_severity: major unresolved exact-structure consistency conflict
  normalization_reason: The intended compound is unambiguous; a major consistency
    finding preserves conflicting evidence without declaring a wrong-target blocker
    or unproven replacement.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Maintained ChEBI structure and xref row
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: ARO PubChem xref owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Exact source import and text normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated representation and cross-source merge
- finding_id: F2
  issue_key: chebi-29505-a47934-primary-target-activity-evidence
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Exact primary target-binding and activity evidence is available
  description: The record correctly limits its target to a database assertion, while
    inspected exact-compound primary data can support a bounded primary annotation
    and producer self-resistance context.
  target_ids:
  - CHEBI:29505
  field_paths:
  - evidence
  - molecular_targets
  - activity_spectrum
  - resistance_mechanisms
  - producer_organisms
  evidence_ids:
  - record
  - binding-primary
  - biosynthesis-primary
  - producer-primary
  rule_id: 'review-checklist: Evidence standard, Activity, Mechanism and Resistance'
  native_severity: minor actionable primary-evidence enrichment
  normalization_reason: Existing scoped claims are sound; the finding concerns specific
    available evidence, not optional field emptiness.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/a47934.yaml
    role: Curator-owned evidence, activity_spectrum, molecular_targets, resistance_mechanisms
      and producer_organisms via validated writer/history
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Maintained reviewed CARD target-evidence qualification
- finding_id: F3
  issue_key: chebi-29505-a47934-systematic-name-bridge-locants-flattened
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Systematic synonym loses delimiters around bridge locants
  description: Native undecacyclo[38.14.2.23,6.214,17...] concatenates bridge sizes
    and attachment locants. Current source text uses [38.14.2.2(3,6).2(14,17)...],
    retaining the intended numerical grouping.
  target_ids:
  - CHEBI:29505
  field_paths:
  - synonyms[0].synonym_text
  evidence_ids:
  - record
  - chebi
  - source-check
  rule_id: 'review-checklist: Synonym accuracy'
  native_severity: minor systematic-name serialization defect
  normalization_reason: Common names and identifiers still resolve the intended compound,
    but the flattened systematic name is ambiguous.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Maintained ChEBI structure and xref row
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: ARO PubChem xref owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Exact source import and text normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated representation and cross-source merge
actions:
- action_id: A1
  description: Resolve the exact A47934 stereo assignment against primary structural
    evidence and qualify or repair the conflicting source mappings before regeneration.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:29505
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Maintained ChEBI structure and xref row
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: ARO PubChem xref owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Exact source import and text normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated representation and cross-source merge
  acceptance_checks:
  - Atom-map all eight centres across native ChEBI, PubChem 16131155 and KEGG C12016;
    primary connectivity Figure 1 alone is insufficient to arbitrate them. Verify
    the experimentally supported absolute configuration before changing any structure.
  - Reconcile KNApSAcK displayed key, InChI and partially specified SMILES; preserve
    an explicit source conflict if no exact corrected accession exists. Do not replace
    native chemistry simply by majority vote.
  - Keep sulfate ester, desulfo analogue, neutral molecule and physiological ionic
    forms distinct; MetaCyc mapping must retain charge/form scope.
  - Repair maintained rows/import or cross-source selection, regenerate through scripts/seed_from_sources.py,
    and recheck exact encodings/xrefs, native schema/strict, term/reference/history
    and corpus gates.
- action_id: A2
  description: Add exact primary evidence with binding, assay, analogue and producer
    scope preserved.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:29505
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/a47934.yaml
    role: Curator-owned evidence, activity_spectrum, molecular_targets, resistance_mechanisms
      and producer_organisms via validated writer/history
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Maintained reviewed CARD target-evidence qualification
  acceptance_checks:
  - Attach the direct peptide-binding study to the chemical cell-wall target, preserving
    ligand and experimental conditions. Do not invent a protein example for a chemical
    group.
  - Retain organism/strain, assay endpoint, units and exposure context for activity
    and resistance observations. Keep desulfo/dechloro analogues separate.
  - Treat resistance-induction and dimerization observations as bounded phenotypes,
    not direct binding of A47934 to VanS.
  - Support structured producer/self-resistance from the exact biosynthetic studies,
    then use validated writer/history and all required native gates before scientific
    sign-off.
- action_id: A3
  description: Preserve systematic-name bridge-locant grouping during source text
    normalization and regeneration.
  finding_ids:
  - F3
  target_ids:
  - CHEBI:29505
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Maintained ChEBI structure and xref row
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: ARO PubChem xref owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Exact source import and text normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated representation and cross-source merge
  acceptance_checks:
  - Preserve parentheses or equivalent unambiguous superscript/plain-text notation
    for each bridge descriptor. Compare the full corrected synonym against the authoritative
    source and chosen stereo identity.
  - Ensure the adopted inventory and generated synonym reproduce the correction; inspect
    other affected source serialization only as separately authorized follow-up.
limitations:
- The natural-product absolute stereochemistry remains unresolved across inspected
  authorities. The 1986 primary structure figure confirms connectivity but does not
  supply explicit stereobonds. No replacement encoding or native identity rejection
  is asserted.
- All seven adopted compound-source PMID abstracts and the target-definition PMID
  were read and dispositioned. Primary2013 Methods/Results/Table 1 and primary 2002
  resistance Results were inspected through the web reader. Their local PMC HTML downloads
  returned browser challenges, not article bodies; no snapshot hash is falsely attached
  to those primary passages.
- Europe PMC XML retrievals for primary 2002/2013/2018 failed with HTTP500, publisher
  direct fetch403 and the attempted primary 2013 CiteSeer PDF404. Primary1986 PDF
  was successfully read; failed retrievals do not negate successfully inspected web
  primary text.
- MetaCyc CPD-15750 returned an account page. CAS 90039-80-8 is corroborated by KEGG/KNApSAcK/ChEBI
  but was not independently resolved against the CAS registry.
- Required shared gates are coordinated separately; native scientific status remains
  SEEDED and no sign-off is claimed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Only scratch artifacts were written; all 16 captured input hashes rechecked unchanged.
- The first supplemental source-check attempts failed at the OLS has_role response
  and exact synonym comparison. The final check uses the actual ChEBI page role link,
  records the systematic-name defect and exits 1 for that defect; the has_role response
  is not used as a valid role assertion.
- Primary2018 ITC values concern desulfo and desulfo/dechloro analogues and are deliberately
  excluded from proposed native quantitative binding evidence.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:29505
- https://pubchem.ncbi.nlm.nih.gov/compound/16131155
- https://rest.kegg.jp/get/C12016
- https://doi.org/10.7164/antibiotics.39.1533
- https://doi.org/10.1128/JB.01617-12
- https://doi.org/10.1073/pnas.102285099
tags:
- record-review
- a47934
- glycopeptide-aglycone
- stereochemical-source-conflict
- primary-binding
```
