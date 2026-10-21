# Loganetin: supported native structure with an internally inconsistent exact reference

- Review: 20261021T195157Z-loganetin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T19:32:14Z
- Finished UTC: 2026-10-21T19:51:57Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The entire native record and exact source row were assessed. Native chemistry, the systematic synonym and primary synthetic structure agree. KNApSAcK supplies mutually inconsistent stereochemical descriptors under the asserted accession, requiring exact-link adjudication; the definition also contains a spelling error. Primary activity evidence is retained at its demonstrated weak standalone and combination scope.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position607; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:195298 | data/antibiotics/antibacterial/loganetin.yaml | generated | loganetin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:195298 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:195298 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:195298 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:195298 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:195298 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:195298 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:195298 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:195298 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:195298 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:195298 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:195298 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:195298 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact native structure and relational stereochemical naming

identity: supported. Targets: CHEBI:195298.

The native graph and full systematic synonym agree with independent chemical encodings and the primary synthetic drawing. Parent-name CIP changes are explicitly explained. No wrong-native-identity finding is established.

### Exact external links and ontology classes

grounding: concern. Targets: CHEBI:195298.

KEGG matches; KNApSAcK has inconsistent stereo descriptors requiring adjudication. CAS and MetaCyc remain access-limited. All six structural parents fit the verified graph.

### Antibacterial eligibility and mechanism boundaries

evidence: supported. Targets: CHEBI:195298.

The original weak standalone and combination results support bounded antibacterial context. No direct molecular mechanism is established. Host, extract, biosynthetic and related-compound evidence is kept separate.

### Complete adopted lead disposition and source ownership

provenance: supported. Targets: CHEBI:195298.

All ten adopted abstracts were read and individually dispositioned; two additional current leads were scoped. All thirteen original captures remain unchanged. Exact generated owners and three chronological history events are retained.

### Optional target, activity and producer enrichment

completeness: unknown. Targets: CHEBI:195298.

No required optional field is missing. Any enrichment must preserve exact material, standalone versus combination endpoints, uncertain strain identity and source-reading limits.

## Findings

### F1: Adjudicate the internally inconsistent KNApSAcK exact link

major / open / confirmed; issue key: loganetin-knapsack-internally-conflicting-stereo.

Native xrefs[2] treats C00036132 as exact. Its matching SMILES and conflicting InChI do not jointly establish unqualified exact stereochemical equivalence. The latter inverts canonical C9 and yields a different stereochemical key. Preserve supported native chemistry while resolving the source association.

### F2: Correct the definition spelling

minor / open / confirmed; issue key: loganetin-definition-postion-typo.

The maintained ChEBI-derived definition spells position as postion. This is a bounded text correction and does not justify changing the relational parent stereochemistry.

## Recommended Actions And Acceptance Checks

### A1

Resolve the KNApSAcK descriptor conflict through maintained source handling before retaining an unqualified exact chemical association.

- Independently compare both registry encodings and displayed key to the native five-centre structure.
- Retain the supported native structure; qualify or remove the exact association until the source discrepancy is resolved, preserving useful provenance.
- Regenerate and rerun schema, strict, chemical, term/reference/history and required corpus checks.

### A2

Correct postion to position through the maintained definition owner.

- Regenerated definition has the corrected spelling.
- Preserve justified parent/full-product CIP distinction and all exact native chemistry.

### A3

Optional activity enrichment requires exact material and endpoint mapping.

- Resolve original strain-label discrepancy before attaching a canonical strain accession.
- Keep weak standalone inhibition and antibiotic-combination effects separate; do not infer direct efflux binding from enhancement.
- Do not transfer extract, host, biosynthesis or related-iridoid results into exact antibacterial claims.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/loganetin.yaml; Entire native YAML, single exact synonym, six parents, role, four xrefs, source concept and all three history events | supports | The SEEDED EXACT record denotes neutral C11H16O5 with five assigned centres and full key XWOHZIIPBYAMJX-KHBMLBSESA-N. The sole systematic synonym specifies 1R,4aS,6S,7R,7aS. No molecular target, resistance, numeric activity, clinical, producer-object or causal-graph assertion is present. |
| owners | data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Complete exact inventory row, source extraction and generation ownership | supports | The adopted ChEBI row supplies native chemistry, naming, classes, role and all ten citation leads. Source owners are captured in the unchanged original thirteen inputs. Exact curator/decisions overrides were not found in the ignored-inclusive local scope. Preserve maintained-source correction paths and native SEEDED history. |
| search | /private/tmp/am-review-session/607-local-hits.txt; Initial ignored-inclusive local search plus bounded public discovery | supports | All returned local paths and all sixteen exact-title/abstract discovery titles plus twenty antibacterial-query titles were inspected. Related loganin, derivatives, extracts, host biology and biosynthetic enzymes were kept separate. This is a bounded literature search, not an exhaustive assertion of absence. |
| adapter | Native structured-source applicability assessment; Entire native field set and definition | supports | No bacterial protein, pathway, regulatory or transcriptomic claim is asserted natively, so an iModulonDB lookup is not applicable. Biosynthesis and host-target leads were not promoted to antibacterial targets. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/195298/; Complete current response and molfile | supports | Current ChEBI repeats the native graph, five assigned centres, formula, masses, definition, systematic name, parents, role and four associations. Its repetition of a source spelling or external descriptor conflict does not independently resolve that conflict. |
| chemistry | /private/tmp/am-review-session/607-authority-chemistry.json; Independent RDKit parsing of ten native/current serializations using the019 interpreter against061 | supports | Nine serializations agree, including native SMILES/InChI, three ChEBI forms, two PubChem CID10466307 forms, KEGG molfile and KNApSAcK SMILES. They have five centres, zero charge and native formula/key. KNApSAcK InChI alone has canonical C9 inverted. Formula and masses agree at native precision. |
| kegg | https://rest.kegg.jp/get/C22676; Complete entry and independently parsed molfile | supports | KEGG identifies loganetin and its CAS association. The molfile encodes all five stereocentres and yields the native full key; apparent wedge-count differences are not missing-centre evidence. |
| knapsack | https://www.knapsackfamily.com/knapsack_core/information.php?word=C00036132; Actual asserted accession, displayed SMILES, InChI and InChIKey | refutes | The displayed SMILES matches native, but its InChI gives XWOHZIIPBYAMJX-NRBMLLDGSA-N after standardization, with canonical InChI C9 R rather than native S. The displayed nonstandard-era key XWOHZIIPBYAMJX-IAMKKNOZNA-N is also not the recomputed native key. This is internal descriptor inconsistency under a matching name/accession, not evidence that every representation of the entry is wrong. |
| definition-cip | /private/tmp/am-review-session/607-bare-parent-cip.json; Scratch-only removal of specified hydroxy/methyl substituents, retaining fused-ring geometry | supports | The unsubstituted parent in the relational definition has 4aS,7aR: independent CIP recalculation gives original InChI C6 S/C9 R. Adding the stated substituents changes the latter priority label to S without inverting geometry. Therefore the parent-name 7aR versus full-synonym 7aS is not a confirmed stereo defect. The spelling postion is a separate minor error. |
| term25248 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/25248/; Complete current term definition | supports | The methyl ester term fits the native graph or bounded activity evidence. The antibacterial role does not impose a low-MIC threshold or require an identified protein target. |
| term35681 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/35681/; Complete current term definition | supports | The secondary alcohol term fits the native graph or bounded activity evidence. The antibacterial role does not impose a low-MIC threshold or require an identified protein target. |
| term38131 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/38131/; Complete current term definition | supports | The lactol term fits the native graph or bounded activity evidence. The antibacterial role does not impose a low-MIC threshold or require an identified protein target. |
| term38606 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/38606/; Complete current term definition | supports | The cyclopentapyran term fits the native graph or bounded activity evidence. The antibacterial role does not impose a low-MIC threshold or require an identified protein target. |
| term50563 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/50563/; Complete current term definition | supports | The iridoid monoterpenoid term fits the native graph or bounded activity evidence. The antibacterial role does not impose a low-MIC threshold or require an identified protein target. |
| term51702 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/51702/; Complete current term definition | supports | The enoate ester term fits the native graph or bounded activity evidence. The antibacterial role does not impose a low-MIC threshold or require an identified protein target. |
| term33282 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/33282/; Complete current term definition | supports | The antibacterial role term fits the native graph or bounded activity evidence. The antibacterial role does not impose a low-MIC threshold or require an identified protein target. |
| registries | CAS:29748-10-5; MetaCyc:CPD-16441; Current associations and actual direct retrieval outcomes | unknown | CAS detail returned a client error shell, not registry chemistry. Both MetaCyc HTML and XML routes returned account/login pages, not the compound record. ChEBI/KEGG associations are retained as context; these inaccessible exact registry graphs remain unverified and are not declared wrong. |
| synthesis | PMID:37026980; DOI:10.1021/acs.joc.3c00253; Complete original abstract and official SI actual pages27/29; HPLC conditions text page32 | supports | The 2023 synthesis explicitly distinguishes loganetin from its enantiomer and C1-methoxy derivative. Actual SI page27 shows the native-compatible loganetin constitution and five same-face stereobonds alongside proton/carbon spectra; page29 depicts the opposite enantiomer. The SI crystal table concerns intermediate10, not a parent-loganetin crystal. HPLC uses an Eclipse XDB-C18 column, so its area purity is not adopted as proof of enantiomeric purity. The full main text was unavailable. |
| bioenhancer | DOI:10.1080/01496395.2013.862548; Author-uploaded full main text through browser; original Table1 text, Methods, Results and references read | supports | A. scholaris bark voucher9479 yielded 48mg of 94.4%-HPLC-pure loganetin; NMR/MS identity was compared with prior literature. Mueller-Hinton microdilution used 5e5CFU/mL,37C,24h. Table1 reports standalone MIC500µg/mL in both E. coli strains despite the abstract calling it inactive. At10µg/mL, loganetin reduced nalidixic-acid MIC6.25→1.56 in CA8000 and100→12.5 in the resistant strain. The strain section names MTCC1652 while methods/table name DH5α; this conflict is unresolved. Enhancement does not prove direct efflux inhibition. Actual figure images and full PDF were not retrieved. |
| bioenhancer-context | DOI:10.1080/01496395.2013.862548; Remaining original discussion/conclusion and references, browser text | supports | The paper treats the isolated compound as a bioenhancer and compares reserpine, but supplies no direct target-binding experiment. The weak standalone endpoint is retained rather than converted into universal inactivity or high potency. |
| adopted12943773 | PMID:12943773; Complete original indexed abstract; deeper reading stated separately | context_only | C. spruceanum bark isolation includes loganetin, but the abstract Trypanosoma activities belong to four other named seco-iridoids; they are not transferred. |
| adopted19967996 | PMID:19967996; Complete original indexed abstract; deeper reading stated separately | context_only | L. fragrantissima volatile profiling reports loganetin in time-dependent flower extracts; mixture composition is not a purified-compound antibacterial experiment. |
| adopted21799001 | PMID:21799001; Complete original indexed abstract; deeper reading stated separately | context_only | UGT85A24 glucosyltransferase substrate specificity includes weak loganetin use. This is biosynthesis, not an antibacterial target. |
| adopted22466563 | PMID:22466563; Complete original indexed abstract; deeper reading stated separately | context_only | B. longum BglX hydrolyzes loganin to loganetin. Substrate conversion is not antibacterial protein inhibition. |
| adopted26749820 | PMID:26749820; Complete original indexed abstract; deeper reading stated separately | context_only | N. orientalis yields loganetin as compound2. Antioxidant results singled out for other compounds are not transferred. |
| adopted27534097 | PMID:27534097; Complete original indexed abstract; deeper reading stated separately | context_only | S. nux-blanda isolation includes loganetin3; the study concerns human cancer-cell assays, not bacterial activity. |
| adopted29276981 | PMID:29276981; Complete original indexed abstract; deeper reading stated separately | context_only | Gut-flora transformation of loganin supplies metabolism context. Metabolite formation is distinct from microbial inhibition. |
| adopted30205569 | PMID:30205569; Complete original indexed abstract; deeper reading stated separately | context_only | N. reticulata stems yield loganetin6. Exact follow-up Table2 reports Hep3B EC50&gt;100µg/mL; this is host cytotoxicity, not antibacterial activity. |
| adopted30706443 | PMID:30706443; Complete original indexed abstract; deeper reading stated separately | context_only | Loganetin attenuates LPS-associated acute kidney injury with TLR4-related host responses. This does not establish direct bacterial killing or bacterial TLR4 binding. |
| adopted33098378 | PMID:33098378; Complete original indexed abstract; deeper reading stated separately | context_only | Loganetin plus fluorouracil is investigated in gastric-cancer systems. Host synergy is not antibacterial activity or a bacterial target. |
| isolation2018 | PMID:30205569; DOI:10.3390/molecules23092297; Selected exact-compound isolation/results paragraphs and complete Table2 in full XML | context_only | Loganetin is known compound6, distinct from new neoretininA3 and active host-cytotoxic compounds10,11,13. The table retains a censored &gt;100µg/mL host-cell endpoint. Proposed biosynthetic transformations are hypotheses, not exact antibacterial mechanism experiments. |
| current-extra | PMID:34692636; Complete indexed abstract in exact-compound discovery | context_only | This is computational docking/dynamics of GSK3β in an Alzheimer context. Loganetin is an aglycone despite broad glycoside wording; the source is not experimental antibacterial target evidence. The additional current2023 synthesis lead was assessed separately. |
| secondary-chain | PMC10205999 Table2; DOI:10.4236/ajps.2015.616264 section3.4; Selected2023 table and2015 review passage, not whole articles | context_only | The host-neuroprotection article attaches an antimicrobial/antifungal label to a mass-spectral loganetin assignment and cites Moreira2015. That review separates loganetin isolation from extract assays and other iridoid activities. This chain is discovery/context, not an independent pure-loganetin antibacterial experiment. The adopted original PMID12943773 likewise scopes activity to other compounds. |

## Limits And Additional Notes

- CAS returned an error shell and both MetaCyc routes returned account pages; exact registry chemistry was not inspected.
- The2014 original was read through browser-accessible author-uploaded text, including table text, full scientific main and references. Direct publisher/author-page downloads returned403; the PDF and actual figure images were not inspected. Strain naming is internally inconsistent and material enantiopurity is not independently established.
- The2023 synthetic main text returned403. Official SI was retrieved; actual loganetin/enantiomer drawings and spectra pages27/29 and HPLC conditions page32 were inspected. Raw spectra and intermediate crystal data were not reprocessed, and HPLC area purity is not an independent ee determination.
- All ten adopted complete abstracts were read. The2018 original was inspected in selected exact-compound sections/Table2, not every unrelated structural derivation. Host and biosynthetic studies retain abstract-level boundaries unless separately identified.
- The2023 neuroprotection table and2015 review were followed only for the source chain. Their secondary or extract-level statements were not used as decisive purified-compound evidence. No exhaustive antibacterial literature or clinical efficacy claim is made.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Original thirteen captured inputs are unchanged; no native record, source inventory, curation status or history was edited.
- Scratch CIP derivation removes stated substituents only to test relational nomenclature, and is not a proposed native chemical edit.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T195157Z-loganetin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Loganetin: supported native structure with an internally inconsistent exact
  reference'
started_at: '2026-10-21T19:32:14Z'
finished_at: '2026-10-21T19:51:57Z'
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
summary: The entire native record and exact source row were assessed. Native chemistry,
  the systematic synonym and primary synthetic structure agree. KNApSAcK supplies
  mutually inconsistent stereochemical descriptors under the asserted accession, requiring
  exact-link adjudication; the definition also contains a spelling error. Primary
  activity evidence is retained at its demonstrated weak standalone and combination
  scope.
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
  - path: data/antibiotics/antibacterial/loganetin.yaml
    sha256: b76a23c084f218cfef72be7d3b35a1035f4f01a2138c03324fde9993a9972891
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
- target_id: CHEBI:195298
  path: data/antibiotics/antibacterial/loganetin.yaml
  label: loganetin
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
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position607; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:195298
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:195298
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    607
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:195298
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/loganetin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:195298
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/loganetin.yaml --out /private/tmp/am-review-session/607-strict.tsv
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
  - CHEBI:195298
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
  - CHEBI:195298
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
  - CHEBI:195298
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
  - CHEBI:195298
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
  - CHEBI:195298
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
  - CHEBI:195298
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
  - CHEBI:195298
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
  - CHEBI:195298
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
  - CHEBI:195298
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/loganetin.yaml
  locator: Entire native YAML, single exact synonym, six parents, role, four xrefs,
    source concept and all three history events
  accessed_at: '2026-10-21T19:51:29Z'
  support: supports
  summary: The SEEDED EXACT record denotes neutral C11H16O5 with five assigned centres
    and full key XWOHZIIPBYAMJX-KHBMLBSESA-N. The sole systematic synonym specifies
    1R,4aS,6S,7R,7aS. No molecular target, resistance, numeric activity, clinical,
    producer-object or causal-graph assertion is present.
  snapshot_sha256: b76a23c084f218cfef72be7d3b35a1035f4f01a2138c03324fde9993a9972891
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: Complete exact inventory row, source extraction and generation ownership
  accessed_at: '2026-10-21T19:51:29Z'
  support: supports
  summary: The adopted ChEBI row supplies native chemistry, naming, classes, role
    and all ten citation leads. Source owners are captured in the unchanged original
    thirteen inputs. Exact curator/decisions overrides were not found in the ignored-inclusive
    local scope. Preserve maintained-source correction paths and native SEEDED history.
  snapshot_sha256: 877dd9d66ee97766d95605184fedd7336c9077496051ee20db51c0ed66e27d58
- evidence_id: search
  kind: search
  reference: /private/tmp/am-review-session/607-local-hits.txt
  locator: Initial ignored-inclusive local search plus bounded public discovery
  accessed_at: '2026-10-21T19:51:29Z'
  support: supports
  summary: All returned local paths and all sixteen exact-title/abstract discovery
    titles plus twenty antibacterial-query titles were inspected. Related loganin,
    derivatives, extracts, host biology and biosynthetic enzymes were kept separate.
    This is a bounded literature search, not an exhaustive assertion of absence.
  search_scope: Local exact label/identifier search included ignored and hidden files.
    Europe PMC TITLE_ABS:loganetin and loganetin AND (antibacterial OR antimicrobial
    OR bioenhancer), plus official authority and primary-paper follow-up, 2026-10-21.
  snapshot_sha256: 4faf865065f12664bd27843c594c0034f368005d32d48694e44420325f7effed
- evidence_id: adapter
  kind: search
  reference: Native structured-source applicability assessment
  locator: Entire native field set and definition
  accessed_at: '2026-10-21T19:51:29Z'
  support: supports
  summary: No bacterial protein, pathway, regulatory or transcriptomic claim is asserted
    natively, so an iModulonDB lookup is not applicable. Biosynthesis and host-target
    leads were not promoted to antibacterial targets.
  snapshot_sha256: b76a23c084f218cfef72be7d3b35a1035f4f01a2138c03324fde9993a9972891
  search_scope: Full native claims assessed for structured-source triggers; none applicable.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/195298/
  locator: Complete current response and molfile
  accessed_at: '2026-10-21T19:41:47Z'
  support: supports
  summary: Current ChEBI repeats the native graph, five assigned centres, formula,
    masses, definition, systematic name, parents, role and four associations. Its
    repetition of a source spelling or external descriptor conflict does not independently
    resolve that conflict.
  snapshot_sha256: d5a8ae61ed9ca02d209809b3d3a6a92555ad75d26ee5a8e1cf1a78561102840e
- evidence_id: chemistry
  kind: validation
  reference: /private/tmp/am-review-session/607-authority-chemistry.json
  locator: Independent RDKit parsing of ten native/current serializations using the019
    interpreter against061
  accessed_at: '2026-10-21T19:51:29Z'
  support: supports
  summary: Nine serializations agree, including native SMILES/InChI, three ChEBI forms,
    two PubChem CID10466307 forms, KEGG molfile and KNApSAcK SMILES. They have five
    centres, zero charge and native formula/key. KNApSAcK InChI alone has canonical
    C9 inverted. Formula and masses agree at native precision.
  snapshot_sha256: 049afffb6e05f84af9271df55fa0a98c6516ba782788cbc83b6225a4a8aeed45
- evidence_id: kegg
  kind: authority
  reference: https://rest.kegg.jp/get/C22676
  locator: Complete entry and independently parsed molfile
  accessed_at: '2026-10-21T19:41:55Z'
  support: supports
  summary: KEGG identifies loganetin and its CAS association. The molfile encodes
    all five stereocentres and yields the native full key; apparent wedge-count differences
    are not missing-centre evidence.
  snapshot_sha256: 94437554b110e8fa5095edc382e2989a23fe4357130dd539b05ab59e11870085
- evidence_id: knapsack
  kind: authority
  reference: https://www.knapsackfamily.com/knapsack_core/information.php?word=C00036132
  locator: Actual asserted accession, displayed SMILES, InChI and InChIKey
  accessed_at: '2026-10-21T19:41:55Z'
  support: refutes
  summary: The displayed SMILES matches native, but its InChI gives XWOHZIIPBYAMJX-NRBMLLDGSA-N
    after standardization, with canonical InChI C9 R rather than native S. The displayed
    nonstandard-era key XWOHZIIPBYAMJX-IAMKKNOZNA-N is also not the recomputed native
    key. This is internal descriptor inconsistency under a matching name/accession,
    not evidence that every representation of the entry is wrong.
  snapshot_sha256: 0ef1cb1b741d04c8617040ddb39f5d94e343943e22edac80ef14e8ed071ac216
- evidence_id: definition-cip
  kind: validation
  reference: /private/tmp/am-review-session/607-bare-parent-cip.json
  locator: Scratch-only removal of specified hydroxy/methyl substituents, retaining
    fused-ring geometry
  accessed_at: '2026-10-21T19:51:29Z'
  support: supports
  summary: 'The unsubstituted parent in the relational definition has 4aS,7aR: independent
    CIP recalculation gives original InChI C6 S/C9 R. Adding the stated substituents
    changes the latter priority label to S without inverting geometry. Therefore the
    parent-name 7aR versus full-synonym 7aS is not a confirmed stereo defect. The
    spelling postion is a separate minor error.'
  snapshot_sha256: 07226700ef7cbb5a3d84aae6f607101aecbb2a2a4309ef682a7d2c58e859fcff
- evidence_id: term25248
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/25248/
  locator: Complete current term definition
  accessed_at: '2026-10-21T19:41:48Z'
  support: supports
  summary: The methyl ester term fits the native graph or bounded activity evidence.
    The antibacterial role does not impose a low-MIC threshold or require an identified
    protein target.
  snapshot_sha256: c14bd82431a77fb8195daeb8cc70ed6d618c0f727f8faccf9db58e70c39b73bc
- evidence_id: term35681
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/35681/
  locator: Complete current term definition
  accessed_at: '2026-10-21T19:41:48Z'
  support: supports
  summary: The secondary alcohol term fits the native graph or bounded activity evidence.
    The antibacterial role does not impose a low-MIC threshold or require an identified
    protein target.
  snapshot_sha256: 6c7bb094d5cee846fd3474aa3cd1e0060b4505ea5c6c91bce5934f9568866694
- evidence_id: term38131
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/38131/
  locator: Complete current term definition
  accessed_at: '2026-10-21T19:41:48Z'
  support: supports
  summary: The lactol term fits the native graph or bounded activity evidence. The
    antibacterial role does not impose a low-MIC threshold or require an identified
    protein target.
  snapshot_sha256: cc7528c5a7a56673300f14bf4953d141faecec0318dd5e7c57839123d4d258c4
- evidence_id: term38606
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/38606/
  locator: Complete current term definition
  accessed_at: '2026-10-21T19:41:48Z'
  support: supports
  summary: The cyclopentapyran term fits the native graph or bounded activity evidence.
    The antibacterial role does not impose a low-MIC threshold or require an identified
    protein target.
  snapshot_sha256: 107c175576c591a4a6c623ad28a944a3cd79cc8a3e8513659cff4b3c3475e4dc
- evidence_id: term50563
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/50563/
  locator: Complete current term definition
  accessed_at: '2026-10-21T19:41:49Z'
  support: supports
  summary: The iridoid monoterpenoid term fits the native graph or bounded activity
    evidence. The antibacterial role does not impose a low-MIC threshold or require
    an identified protein target.
  snapshot_sha256: c5ab22c35d12d7e7bdf0f27a2ce3dc1d10e6a7ab232982262ca38a10eb1a921c
- evidence_id: term51702
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/51702/
  locator: Complete current term definition
  accessed_at: '2026-10-21T19:41:49Z'
  support: supports
  summary: The enoate ester term fits the native graph or bounded activity evidence.
    The antibacterial role does not impose a low-MIC threshold or require an identified
    protein target.
  snapshot_sha256: 7357174a0788d0f601d59047e679f74c49bcf6d3501f8f686f833ca5fbd1c63c
- evidence_id: term33282
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/33282/
  locator: Complete current term definition
  accessed_at: '2026-10-21T19:41:49Z'
  support: supports
  summary: The antibacterial role term fits the native graph or bounded activity evidence.
    The antibacterial role does not impose a low-MIC threshold or require an identified
    protein target.
  snapshot_sha256: 20d92ce7e00c204b1753184671c043160821d692438278344335446aadcd5082
- evidence_id: registries
  kind: authority
  reference: CAS:29748-10-5; MetaCyc:CPD-16441
  locator: Current associations and actual direct retrieval outcomes
  accessed_at: '2026-10-21T19:51:29Z'
  support: unknown
  summary: CAS detail returned a client error shell, not registry chemistry. Both
    MetaCyc HTML and XML routes returned account/login pages, not the compound record.
    ChEBI/KEGG associations are retained as context; these inaccessible exact registry
    graphs remain unverified and are not declared wrong.
  snapshot_sha256: 1de435e3df3dcf0409cce79738775ae9f3cb820e69d64727ae1f387f71528a08
- evidence_id: synthesis
  kind: primary_source
  reference: PMID:37026980; DOI:10.1021/acs.joc.3c00253
  locator: Complete original abstract and official SI actual pages27/29; HPLC conditions
    text page32
  accessed_at: '2026-10-21T19:45:28Z'
  support: supports
  summary: The 2023 synthesis explicitly distinguishes loganetin from its enantiomer
    and C1-methoxy derivative. Actual SI page27 shows the native-compatible loganetin
    constitution and five same-face stereobonds alongside proton/carbon spectra; page29
    depicts the opposite enantiomer. The SI crystal table concerns intermediate10,
    not a parent-loganetin crystal. HPLC uses an Eclipse XDB-C18 column, so its area
    purity is not adopted as proof of enantiomeric purity. The full main text was
    unavailable.
  snapshot_sha256: 15e43a61dda33b59dea8f5a2179a5424299ed993b7e674052fa1c005a46ce9a6
- evidence_id: bioenhancer
  kind: primary_source
  reference: DOI:10.1080/01496395.2013.862548
  locator: Author-uploaded full main text through browser; original Table1 text, Methods,
    Results and references read
  accessed_at: '2026-10-21T19:51:29Z'
  support: supports
  summary: A. scholaris bark voucher9479 yielded 48mg of 94.4%-HPLC-pure loganetin;
    NMR/MS identity was compared with prior literature. Mueller-Hinton microdilution
    used 5e5CFU/mL,37C,24h. Table1 reports standalone MIC500µg/mL in both E. coli
    strains despite the abstract calling it inactive. At10µg/mL, loganetin reduced
    nalidixic-acid MIC6.25→1.56 in CA8000 and100→12.5 in the resistant strain. The
    strain section names MTCC1652 while methods/table name DH5α; this conflict is
    unresolved. Enhancement does not prove direct efflux inhibition. Actual figure
    images and full PDF were not retrieved.
  snapshot_sha256: 6f7b33fcb52e2af534f30b2f17e6cbc282c0a0fc8375cf53479252839138706a
- evidence_id: bioenhancer-context
  kind: primary_source
  reference: DOI:10.1080/01496395.2013.862548
  locator: Remaining original discussion/conclusion and references, browser text
  accessed_at: '2026-10-21T19:51:29Z'
  support: supports
  summary: The paper treats the isolated compound as a bioenhancer and compares reserpine,
    but supplies no direct target-binding experiment. The weak standalone endpoint
    is retained rather than converted into universal inactivity or high potency.
  snapshot_sha256: a5ce7d6c58625dba867a84cb899f754ea32fafb7ff13951db405501b71e756d9
- evidence_id: adopted12943773
  kind: primary_source
  reference: PMID:12943773
  locator: Complete original indexed abstract; deeper reading stated separately
  accessed_at: '2026-10-21T19:41:49Z'
  support: context_only
  summary: C. spruceanum bark isolation includes loganetin, but the abstract Trypanosoma
    activities belong to four other named seco-iridoids; they are not transferred.
  snapshot_sha256: 94baebbca57b97c4d29c6b2fd3b4fed9ac69653c23a3339cdd1c6582cf8c553d
- evidence_id: adopted19967996
  kind: primary_source
  reference: PMID:19967996
  locator: Complete original indexed abstract; deeper reading stated separately
  accessed_at: '2026-10-21T19:41:49Z'
  support: context_only
  summary: L. fragrantissima volatile profiling reports loganetin in time-dependent
    flower extracts; mixture composition is not a purified-compound antibacterial
    experiment.
  snapshot_sha256: 94baebbca57b97c4d29c6b2fd3b4fed9ac69653c23a3339cdd1c6582cf8c553d
- evidence_id: adopted21799001
  kind: primary_source
  reference: PMID:21799001
  locator: Complete original indexed abstract; deeper reading stated separately
  accessed_at: '2026-10-21T19:41:49Z'
  support: context_only
  summary: UGT85A24 glucosyltransferase substrate specificity includes weak loganetin
    use. This is biosynthesis, not an antibacterial target.
  snapshot_sha256: 94baebbca57b97c4d29c6b2fd3b4fed9ac69653c23a3339cdd1c6582cf8c553d
- evidence_id: adopted22466563
  kind: primary_source
  reference: PMID:22466563
  locator: Complete original indexed abstract; deeper reading stated separately
  accessed_at: '2026-10-21T19:41:49Z'
  support: context_only
  summary: B. longum BglX hydrolyzes loganin to loganetin. Substrate conversion is
    not antibacterial protein inhibition.
  snapshot_sha256: 94baebbca57b97c4d29c6b2fd3b4fed9ac69653c23a3339cdd1c6582cf8c553d
- evidence_id: adopted26749820
  kind: primary_source
  reference: PMID:26749820
  locator: Complete original indexed abstract; deeper reading stated separately
  accessed_at: '2026-10-21T19:41:49Z'
  support: context_only
  summary: N. orientalis yields loganetin as compound2. Antioxidant results singled
    out for other compounds are not transferred.
  snapshot_sha256: 94baebbca57b97c4d29c6b2fd3b4fed9ac69653c23a3339cdd1c6582cf8c553d
- evidence_id: adopted27534097
  kind: primary_source
  reference: PMID:27534097
  locator: Complete original indexed abstract; deeper reading stated separately
  accessed_at: '2026-10-21T19:41:49Z'
  support: context_only
  summary: S. nux-blanda isolation includes loganetin3; the study concerns human cancer-cell
    assays, not bacterial activity.
  snapshot_sha256: 94baebbca57b97c4d29c6b2fd3b4fed9ac69653c23a3339cdd1c6582cf8c553d
- evidence_id: adopted29276981
  kind: primary_source
  reference: PMID:29276981
  locator: Complete original indexed abstract; deeper reading stated separately
  accessed_at: '2026-10-21T19:41:49Z'
  support: context_only
  summary: Gut-flora transformation of loganin supplies metabolism context. Metabolite
    formation is distinct from microbial inhibition.
  snapshot_sha256: 94baebbca57b97c4d29c6b2fd3b4fed9ac69653c23a3339cdd1c6582cf8c553d
- evidence_id: adopted30205569
  kind: primary_source
  reference: PMID:30205569
  locator: Complete original indexed abstract; deeper reading stated separately
  accessed_at: '2026-10-21T19:41:49Z'
  support: context_only
  summary: N. reticulata stems yield loganetin6. Exact follow-up Table2 reports Hep3B
    EC50>100µg/mL; this is host cytotoxicity, not antibacterial activity.
  snapshot_sha256: 94baebbca57b97c4d29c6b2fd3b4fed9ac69653c23a3339cdd1c6582cf8c553d
- evidence_id: adopted30706443
  kind: primary_source
  reference: PMID:30706443
  locator: Complete original indexed abstract; deeper reading stated separately
  accessed_at: '2026-10-21T19:41:49Z'
  support: context_only
  summary: Loganetin attenuates LPS-associated acute kidney injury with TLR4-related
    host responses. This does not establish direct bacterial killing or bacterial
    TLR4 binding.
  snapshot_sha256: 94baebbca57b97c4d29c6b2fd3b4fed9ac69653c23a3339cdd1c6582cf8c553d
- evidence_id: adopted33098378
  kind: primary_source
  reference: PMID:33098378
  locator: Complete original indexed abstract; deeper reading stated separately
  accessed_at: '2026-10-21T19:41:49Z'
  support: context_only
  summary: Loganetin plus fluorouracil is investigated in gastric-cancer systems.
    Host synergy is not antibacterial activity or a bacterial target.
  snapshot_sha256: 94baebbca57b97c4d29c6b2fd3b4fed9ac69653c23a3339cdd1c6582cf8c553d
- evidence_id: isolation2018
  kind: primary_source
  reference: PMID:30205569; DOI:10.3390/molecules23092297
  locator: Selected exact-compound isolation/results paragraphs and complete Table2
    in full XML
  accessed_at: '2026-10-21T19:43:48Z'
  support: context_only
  summary: Loganetin is known compound6, distinct from new neoretininA3 and active
    host-cytotoxic compounds10,11,13. The table retains a censored >100µg/mL host-cell
    endpoint. Proposed biosynthetic transformations are hypotheses, not exact antibacterial
    mechanism experiments.
  snapshot_sha256: 970555dec79bb9bf0d8e60e592320c3e9810b4055e65b11a0231259567c926b2
- evidence_id: current-extra
  kind: primary_source
  reference: PMID:34692636
  locator: Complete indexed abstract in exact-compound discovery
  accessed_at: '2026-10-21T19:41:49Z'
  support: context_only
  summary: This is computational docking/dynamics of GSK3β in an Alzheimer context.
    Loganetin is an aglycone despite broad glycoside wording; the source is not experimental
    antibacterial target evidence. The additional current2023 synthesis lead was assessed
    separately.
  snapshot_sha256: d8ed26935b31704951399aac82ed3a17b5ba58f40011fab1476ef2d80ed5fe65
- evidence_id: secondary-chain
  kind: database
  reference: PMC10205999 Table2; DOI:10.4236/ajps.2015.616264 section3.4
  locator: Selected2023 table and2015 review passage, not whole articles
  accessed_at: '2026-10-21T19:51:29Z'
  support: context_only
  summary: The host-neuroprotection article attaches an antimicrobial/antifungal label
    to a mass-spectral loganetin assignment and cites Moreira2015. That review separates
    loganetin isolation from extract assays and other iridoid activities. This chain
    is discovery/context, not an independent pure-loganetin antibacterial experiment.
    The adopted original PMID12943773 likewise scopes activity to other compounds.
  snapshot_sha256: 54a46c81c96087888e6e3e17325353ed901241fc39f3aedd8c407a8bdd2be331
assessments:
- assessment_id: identity
  area: identity
  topic: Exact native structure and relational stereochemical naming
  outcome: supported
  summary: The native graph and full systematic synonym agree with independent chemical
    encodings and the primary synthetic drawing. Parent-name CIP changes are explicitly
    explained. No wrong-native-identity finding is established.
  target_ids:
  - CHEBI:195298
  evidence_ids:
  - native
  - chebi
  - chemistry
  - definition-cip
  - synthesis
- assessment_id: grounding
  area: grounding
  topic: Exact external links and ontology classes
  outcome: concern
  summary: KEGG matches; KNApSAcK has inconsistent stereo descriptors requiring adjudication.
    CAS and MetaCyc remain access-limited. All six structural parents fit the verified
    graph.
  target_ids:
  - CHEBI:195298
  evidence_ids:
  - kegg
  - knapsack
  - chemistry
  - registries
  - term25248
  - term35681
  - term38131
  - term38606
  - term50563
  - term51702
- assessment_id: evidence
  area: evidence
  topic: Antibacterial eligibility and mechanism boundaries
  outcome: supported
  summary: The original weak standalone and combination results support bounded antibacterial
    context. No direct molecular mechanism is established. Host, extract, biosynthetic
    and related-compound evidence is kept separate.
  target_ids:
  - CHEBI:195298
  evidence_ids:
  - bioenhancer
  - bioenhancer-context
  - term33282
  - secondary-chain
  - current-extra
  - isolation2018
- assessment_id: provenance
  area: provenance
  topic: Complete adopted lead disposition and source ownership
  outcome: supported
  summary: All ten adopted abstracts were read and individually dispositioned; two
    additional current leads were scoped. All thirteen original captures remain unchanged.
    Exact generated owners and three chronological history events are retained.
  target_ids:
  - CHEBI:195298
  evidence_ids:
  - owners
  - native
  - adopted12943773
  - adopted19967996
  - adopted21799001
  - adopted22466563
  - adopted26749820
  - adopted27534097
  - adopted29276981
  - adopted30205569
  - adopted30706443
  - adopted33098378
- assessment_id: completeness
  area: completeness
  topic: Optional target, activity and producer enrichment
  outcome: unknown
  summary: No required optional field is missing. Any enrichment must preserve exact
    material, standalone versus combination endpoints, uncertain strain identity and
    source-reading limits.
  target_ids:
  - CHEBI:195298
  evidence_ids:
  - search
  - adapter
  - bioenhancer
  - registries
findings:
- finding_id: F1
  issue_key: loganetin-knapsack-internally-conflicting-stereo
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Adjudicate the internally inconsistent KNApSAcK exact link
  description: Native xrefs[2] treats C00036132 as exact. Its matching SMILES and
    conflicting InChI do not jointly establish unqualified exact stereochemical equivalence.
    The latter inverts canonical C9 and yields a different stereochemical key. Preserve
    supported native chemistry while resolving the source association.
  target_ids:
  - CHEBI:195298
  field_paths:
  - xrefs[2]
  evidence_ids:
  - knapsack
  - chemistry
  - chebi
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
  rule_id: Exact chemical-reference consistency
  normalization_reason: Confirmed external descriptor conflict; native identity is
    supported, so not a wrong-identity blocker.
- finding_id: F2
  issue_key: loganetin-definition-postion-typo
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the definition spelling
  description: The maintained ChEBI-derived definition spells position as postion.
    This is a bounded text correction and does not justify changing the relational
    parent stereochemistry.
  target_ids:
  - CHEBI:195298
  field_paths:
  - definition
  evidence_ids:
  - native
  - owners
  - definition-cip
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
  rule_id: Accurate readable definition
  normalization_reason: Minor source text typo with no demonstrated identity change.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - CHEBI:195298
  description: Resolve the KNApSAcK descriptor conflict through maintained source
    handling before retaining an unqualified exact chemical association.
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
  acceptance_checks:
  - Independently compare both registry encodings and displayed key to the native
    five-centre structure.
  - Retain the supported native structure; qualify or remove the exact association
    until the source discrepancy is resolved, preserving useful provenance.
  - Regenerate and rerun schema, strict, chemical, term/reference/history and required
    corpus checks.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - CHEBI:195298
  description: Correct postion to position through the maintained definition owner.
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
  acceptance_checks:
  - Regenerated definition has the corrected spelling.
  - Preserve justified parent/full-product CIP distinction and all exact native chemistry.
- action_id: A3
  finding_ids: []
  target_ids:
  - CHEBI:195298
  description: Optional activity enrichment requires exact material and endpoint mapping.
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
  acceptance_checks:
  - Resolve original strain-label discrepancy before attaching a canonical strain
    accession.
  - Keep weak standalone inhibition and antibiotic-combination effects separate; do
    not infer direct efflux binding from enhancement.
  - Do not transfer extract, host, biosynthesis or related-iridoid results into exact
    antibacterial claims.
limitations:
- CAS returned an error shell and both MetaCyc routes returned account pages; exact
  registry chemistry was not inspected.
- The2014 original was read through browser-accessible author-uploaded text, including
  table text, full scientific main and references. Direct publisher/author-page downloads
  returned403; the PDF and actual figure images were not inspected. Strain naming
  is internally inconsistent and material enantiopurity is not independently established.
- The2023 synthetic main text returned403. Official SI was retrieved; actual loganetin/enantiomer
  drawings and spectra pages27/29 and HPLC conditions page32 were inspected. Raw spectra
  and intermediate crystal data were not reprocessed, and HPLC area purity is not
  an independent ee determination.
- All ten adopted complete abstracts were read. The2018 original was inspected in
  selected exact-compound sections/Table2, not every unrelated structural derivation.
  Host and biosynthetic studies retain abstract-level boundaries unless separately
  identified.
- The2023 neuroprotection table and2015 review were followed only for the source chain.
  Their secondary or extract-level statements were not used as decisive purified-compound
  evidence. No exhaustive antibacterial literature or clinical efficacy claim is made.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Original thirteen captured inputs are unchanged; no native record, source inventory,
  curation status or history was edited.
- Scratch CIP derivation removes stated substituents only to test relational nomenclature,
  and is not a proposed native chemical edit.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
