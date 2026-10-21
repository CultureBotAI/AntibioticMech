# Review of linezolid

- Review: 20261021T195014Z-linezolid-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T19:32:12Z
- Finished UTC: 2026-10-21T19:50:14Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact neutral S-linezolid identity, curated A-site ribosomal mechanism, nine separately curated MIC observations and dated FDA assertions are supported. Nine CRyPTIC assay strings misrender the categorical WHO designation as a concentration; three verified product names need BRAND_NAME typing. Historical initiation/P-site interpretations, later context-specific elongation, qualified resistance assertions and access limits are explicitly distinguished.

## Scope And Provenance

Entire 5,736-line native record: all identity fields, ten resistance assertions, two targets, 273 activity observations, one compact membership collection, 37 FDA product assertions and fourteen history events. The 264 CRyPTIC rows and 37 FDA assertions were read through verified lossless representations, with all differing fields retained.

Selection: Initially uncovered queue position 605; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:63607 | data/antibiotics/antibacterial/linezolid.yaml | generated | linezolid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:63607 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:63607 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:63607 | Actual focused execution exited 0. |
| Independent authority verification | passed | False | CHEBI:63607 | Actual final execution returned exit 0; earlier scratch diagnostics are disclosed separately. |
| Independent cdc-source verification | passed | False | CHEBI:63607 | Actual final execution returned exit 0; earlier scratch diagnostics are disclosed separately. |
| Independent fda-source verification | passed | False | CHEBI:63607 | Actual final execution returned exit 0; earlier scratch diagnostics are disclosed separately. |
| Independent source-ledger verification | passed | False | CHEBI:63607 | Actual final execution returned exit 0; earlier scratch diagnostics are disclosed separately. |
| Authoritative full QC | failed | True | CHEBI:63607 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:63607 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:63607 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:63607 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:63607 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:63607 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:63607 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:63607 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:63607 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral S-linezolid

identity: supported. Targets: CHEBI:63607.

Independent structural authorities agree after a documented stereo-preserving amide-tautomer normalization. Source chemical names, formula, charge and exact stereochemistry are supported. No unspecified-stereo mixture inference or product-form substitution is made.

### Chemical and product aliases

nomenclature: concern. Targets: CHEBI:63607.

Chemical aliases fit the exact graph. Three verified product names are incorrectly typed EXACT_SYNONYM; the unverified Zyvoxa alias retains a separate limit.

### Chemical, drug and document identifiers

grounding: unknown. Targets: CHEBI:63607.

Inspected exact structures and document links agree, while DrugBank/Reaxys/CAS Registry/LINCS remain independently unresolved. Drug-context links do not assert chemical equivalence.

### A-site mechanism and historical functional interpretations

evidence: supported. Targets: CHEBI:63607.

Native primary D. radiodurans A-site/PTC evidence and HOST_SHARED_TARGET scope are supported. Historical initiation/P-site assays, official label phrasing and later context-dependent elongation are distinguished; the CARD P-site assertion remains explicitly database-qualified.

### Ten qualified resistance associations

evidence: unknown. Targets: CHEBI:63607.

All current database relations are present, with individual citation dispositions and selected original follow-up. Heterologous effects, mixed clinical backgrounds and unresolved exact alleles are not generalized or mistaken for unsupported native primary claims.

### 273 activity observations and memberships

scope: concern. Targets: CHEBI:63607.

Nine separately curated observations match their checked sources, and all compact memberships match the independent audit. Nine categorical WHO source designations are misrendered as concentrations. Original UKMYC/WGS limitations remain explicit.

### Dated FDA approval and product context

scope: supported. Targets: CHEBI:63607.

All 37 assertions match adopted original approvals, product data and exact ingredient mapping. Current sponsor/marketing differences remain dated refresh context, separate from proof of historical accuracy or clinical recommendations.

### Structural classes, role and exact source scope

scope: supported. Targets: CHEBI:63607.

The acetamide, morpholine, organofluorine and oxazolidinone parents and antibacterial-drug role fit the verified structure and primary mechanism. Family, derivative and clinical evidence is kept within its demonstrated scope.

### Owners, hashes, source mints and history

provenance: supported. Targets: CHEBI:63607.

Original captures and appended maintained-owner hashes are unchanged, source mints agree and history is chronological. Focused checks do not replace required shared corpus gates.

## Findings

### F1: Nine categorical WHO designations are rendered as concentrations

major / open / confirmed; issue key: linezolid-cryptic-who-token-as-mg-l.

At activity indices 68,69,70,71,74,75,76,77,86 the generator turns METHOD_CC=WHO into critical concentration WHO mg/L. WHO is a categorical designation, not a numeric concentration. Source phenotypes, memberships and the three U groups correctly lacking an activity category remain intact.

### F2: Three verified product names need brand typing

minor / open / confirmed; issue key: linezolid-zyvox-zyvoxam-zyvoxid-brand-typing.

Native synonyms 3,5,6 label Zyvox, Zyvoxam and Zyvoxid EXACT_SYNONYM. Official product documents establish BRAND_NAME scope. The separate Zyvoxa alias is not included in this confirmed finding because exact original product documentation was not independently inspected.

## Recommended Actions And Acceptance Checks

### A1

Change cryptic_activity_assay to distinguish numeric concentrations from categorical source designations. Preserve WHO as a designation without mg/L, retain genuine numeric values and source phenotypes, and do not infer thresholds from adjacent rows. Regenerate through the maintained source pipeline.

- All nine affected strings retain WHO without presenting it as a concentration.
- A meaningful generator check distinguishes numeric, categorical and empty METHOD_CC values.
- All 264 observation identities, 55,094 memberships and 30,401 subject contexts remain correct; U groups remain unclassified.
- MIC inequalities, units and source R/S/U calls remain unchanged.
- Required schema, strict, term/reference/history and corpus gates pass after curation.

### A2

Type the source-owned Zyvox, Zyvoxam and Zyvoxid names as product brands using reproducible ARO extraction typing or equivalent maintained policy that emits BRAND_NAME. Preserve names and source provenance. Resolve Zyvoxa separately with exact product evidence before extending this confirmed correction.

- The three verified product aliases regenerate as BRAND_NAME.
- The exact native structure and valid drug/product relationships remain intact.
- The unverified fourth alias is neither silently corrected nor removed.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/linezolid.yaml; Entire native; 605-initial-inspect.json,605-inspect.json; lossless 605-native-lossless.json and 605-native-fda.json | supports | REVIEWED/EXACT antibacterial CHEBI:63607 contains the neutral S graph, seven aliases, five parents, one activity role, eight chemical xrefs, three qualified drug links, three document links, two source concepts, ten qualified resistance assertions, two targets,273 activity observations and 37 dated FDA assertions. All source rows and history were inspected. No separate producer, causal-graph or protein-example objects are present; definition and curator-note claims were assessed. |
| chemistry | Independent authority structure comparison; 605-authority-check.py ; 605-authority-chemistry.json; actual 019 interpreter against 061 cwd | supports | Seventeen encodings agree on complete InChIKey TYZROVQLWOKYKF-ZDUSSCGKSA-N, C16H20FN3O4, charge 0 and the S center: native, current ChEBI, PubChem 441401, ChEMBL 126, KEGG C08146/D00947, CCD ZLD and GSRS. Five InChI imports produce the amide imidic-acid tautomer and fail a raw graph comparison; canonical tautomer comparison with tetrahedral and bond stereo removal disabled gives reciprocal chirality-aware matches. This is an explicitly diagnosed normalization boundary, not a distinct-isomer finding. |
| groundings | Official ChEBI, ARO, KEGG, PubChem, ChEMBL, CCD and drug registries; 605-source-audit.json authority_dispositions; timestamped 605-fetch.json through 605-fetch6.json | supports | Current structural parent definitions fit the scaffold and the antibacterial-drug role is supported. Qualified drug_xrefs retain their drug-context meaning. DrugCentral resolves the expected compound; DrugBank/Reaxys independent content remains unavailable. CAS page is a shell. The limited HMS archive contains no LSM-5750, which does not establish a wrong identifier. Wikipedia was inspected only as a secondary document. GSRS identity validation is separate from FDA approval. |
| patents | patent:US5688792; patent:WO957271; Public patent-family texts 605-patent-US5688792.html/.txt and 605-patent-WO957271.html/.txt; Example 5 and family metadata | supports | US5688792A explicitly identifies PCT publication WO95/07271, resolved as WO1995007271A1. Both Example 5 passages describe the S monofluoro morpholinyl acetamide matching linezolid. The exact example, preferred-compound context and synthesis were inspected; general Markush or class antibacterial claims are not transferred to every example. These remain relevant document links, not asserted patent-status or freedom-to-operate opinions. |
| primary2008 | PMID:18757750; DOI:10.1073/pnas.0804276105; PMC2533191 complete main/captions; actual Figures 1 and 4 ; 605-PMC2533191.html and 605-2008-fig*.jpg | supports | Original D. radiodurans 50S crystals soaked with 5 micromolar linezolid support the native A-site/PTC target and a U2585-dependent tRNA-positioning model. Final refinement is 3.5 angstrom; 3.3 angstrom diffraction collection is not substituted for that resolution. Figure 1C supports the exact S compound; Figure 4F and text distinguish A-site overlap from indirect P-site functional effects. A derivative cross-link or a proposed downstream model is not relabeled as a direct parent-drug binding measurement. |
| historical | PMID:9835522; PMID:11897593; Original 1998 PMC106030 selected Methods/Results; 2002 PMC127084 selected Methods, linezolid-specific results and Discussion ; 605-PMC106030.html,605-PMC127084.html | supports | The 1998 linezolid experiments support inhibition of measured initiation-complex formation in E. coli and S. aureus systems. The 2002 PNU-100766 assays show functional effects on fMet-tRNA binding/translocation and propose P-site involvement; several EF-P assays instead use PNU-176798. These functional interpretations are distinguished from the later direct A-site structure. Native CARD P-site annotation is explicitly DATABASE_ASSERTION/PRIMARY_EVIDENCE_NEEDED, and the curated A-site target has its own primary support. |
| elongation | PMID:27791002; DOI:10.1073/pnas.1613055113; PMC5086994 selected profiling/toeprinting Methods, Results, Discussion and captions ; 605-PMC5086994.html | supports | In tolC-deficient E. coli BWDK cells exposed to 100-fold MIC for 2.5 minutes and in defined translation systems, linezolid produces context-dependent elongation arrest, influenced by nascent-peptide residues. Its poor first-peptide-bond inhibition under these conditions does not erase all earlier initiation assays. Native definition wording is historical and also appears in official labeling; it should not be read as an exclusive universal step of action. |
| host | PMID:16723564; PMID:17499045; Original 2006 PMC1479116 selected mitochondrial incorporation Methods and linezolid-specific Results/Figure 4 captions;2007 complete indexed abstract in 605-followup-core.json | supports | Exact linezolid inhibits protein synthesis in isolated mammalian mitochondria from rat/rabbit preparations, supporting HOST_SHARED_TARGET scope. The 2007 bacterial/human mitochondrial photolabeling study uses oxazolidinone derivatives; those experiments are not claimed as an exact parent-linezolid-only human structural study. Neither observation implies binding to human cytoplasmic ribosomes or a new clinical risk estimate. |
| adapter | kg-microbe-sources iModulonDB adapter; 605-adapter-results.json; four executed searches, all exit 0; dataset inventory 575-adapter-datasets.json | supports | Adapter searches preceded open-ended protein follow-up. S. aureus staph_precise108 resolves LmrS USA300HOU_RS11735. The 23S substring hits are methyltransferases rlmB/rlmN/rlmH, not the rRNA target itself. E. coli rrlA and Mtb rrl returned no gene hits. No component hits required summarize; no D. radiodurans dataset was available. Resource membership or absence is not direct binding, resistance or negative experimental evidence. |
| aro | https://purl.obolibrary.org/obo/aro.obo; Reused official 426-current-aro.obo with 426-fetch2-results.json; exact 13 blocks 605-aro-blocks.json; maintained rows 605-raw-rows.json | supports | All ten native resistance relations, antibiotic/class terms and CARD target resolve in the current ontology. All thirteen current PMID leads were resolved, with twelve indexed abstracts read and one metadata-only review. Database qualification remains meaningful: individual variant, strain, material and effect are not inferred merely from class membership. The Mtb rrl WHO-catalogue link resolves at publication level, but variant tables were not independently revalidated. |
| resistance | PMID:26248384; PMID:32277823; PMID:29635422; PMID:25977397; 2015 PMC4576063 selected Methods, Table 1, Results/Discussion; remaining complete indexed abstracts; individual 605-source-audit.json dispositions | supports | Original cfr(B) work raises linezolid MIC in heterologous S. aureus RN4220 while explicitly leaving the contribution in its enterococcal isolates unresolved. The cfr(D) abstract reports effects in E. coli AG100A but not the tested enterococcal hosts; optrA and poxtA expression contexts are also bounded. Native generic qualified associations are not rewritten as universal host effects or rejected for lacking an asserted primary claim. LmrS/23S/clcD leads retain their explicit abstract-only limits. |
| adopted | All12 adopted ChEBI/ARO PMID leads; 605-adopted-core.json; exact individual dispositions 605-source-audit.json | supports | Every adopted PMID resolves: eleven available indexed abstracts and one metadata-only review were inspected. Clinical toxicity, pharmacokinetics, combination treatment, animal implants, toxin expression, biofilm MBEC and sub-MIC adhesion studies retain their own endpoints and taxa. The structural original was read more deeply as stated separately. Reviews and broad clinical contexts are not promoted to direct molecular or exact MIC experiments. |
| freitas | DOI:10.1093/jac/dkaa227; Original publisher PDF pp 2417–2418 Methods, WGS/accession and Results passages ; 605-web-pdf-evidence.json; PMID32607549; direct downloads 403 | supports | The original supports all three native clonal representatives: C59, 149T and 2Fez each have linezolid MIC 8 mg/L measured by broth microdilution and interpreted with EUCAST. Their origin/year and respective WLYR00000000,WLYQ00000000,WLYP00000000 mappings under PRJNA580369 agree. Browser-accessible primary PDF passages were inspected; the inaccessible direct download, uninspected SI and lack of a separate genome-registry rejoin are explicit limits. |
| cdc | CDC/FDA Antimicrobial Resistance Isolate Bank; All six native URLs fetched and individually checked ; 605-cdc-audit.py/.json ; 605-cdc-*.html | supports | All six MIC values, greater-than signs, R source interpretations, taxon/strain labels, broth method, modal-MIC wording and CLSI 2025 M100 S35 edition match official pages. Five named BioSamples match; 0780 explicitly lacks an available accession. Micrograms/mL equals native mg/L. These are preserved source interpretations rather than newly calculated clinical breakpoints. |
| cryptic | Independent coordinating-reviewer CRyPTIC audit; 605-root-cryptic-audit.py/.json/.log; original pinned 134-DST_MEASUREMENTS.parquet; adopted activity/membership/isolate registries | supports | Independent audit verifies 264 observation digests, 55,094 memberships/measurements and 30,401 subjects: 22,294 linked and 8,107 explicit nulls. All adopted joins agree; 88 DST groups independently join 33,413 original LZD source rows. The 176 UKMYC groups match adopted rows but original UKMYC is unavailable; original WGS assignments were not rejoined. Nine assay strings append mg/L to categorical METHOD_CC=WHO. Source R/S/U calls and membership integrity remain supported. |
| fda | FDA Drugs@FDA downloadable archive; FDA GSRS; 605-fda-current.zip,605-fda-audit.py/.json,605-gsrs-full.json; official download https://www.fda.gov/media/89850/download?attachment= | supports | All 37 native product assertions across 29 applications exactly match their adopted fields, dated source metadata and GSRS identity mapping. Current official archive comparison confirms original approval dates and products; it changes sponsor 205154 and marketing status 210378 relative to the dated native snapshot. These are refresh observations, not proof the historical assertions were false. Current GSRS version 162 agrees on exact identity; native version 90 provenance remains intact. |
| brands | Official Zyvox, Zyvoxam and Zyvoxid product labeling; 605-zyvox-exact-spl.html sections 11/12.4 ; 605-zyvoxam-official.pdf title/composition plus Health Canada DIN 02243685 ; 605-zyvoxid-bfarm.pdf sections 1/2 and 605-zyvoxid-austria.html | supports | The three named authorities identify Zyvox, Zyvoxam and Zyvoxid as products containing linezolid. Native synonyms 3,5,6 therefore need BRAND_NAME typing while their valid relationship to the compound remains. Zyvoxa was found as a historical lead but no exact original product document was independently inspected; its spelling and classification are left bounded rather than forced. |
| provenance | Preserved inputs and maintained-owner audit; 605-ledger.py ; 605-source-audit.json ; 605-scratch-check-attempts.json | supports | All 29 captured inputs match, including the unchanged thirteen originals. Both source-concept mints recompute and fourteen history events are chronological. Focused schema, strict and native chemistry pass. Supplementary helper development exposed an amide-tautomer comparison assumption and FDA parser assumptions; those diagnostics are recorded separately and final corrected helper executions pass. No native/source data were changed. |

## Limits And Additional Notes

- All twelve adopted and thirteen current PMID leads were resolved; eleven and twelve indexed abstracts respectively were read, with one overlapping metadata-only review. Original full versus selected reading is itemized, not implied for every lead.
- The primary structural experiment is a D. radiodurans isolated 50S complex. Historical initiation assays, indirect P-site interpretations, derivative photolabeling and later context-dependent E. coli elongation retain their distinct systems and material scope.
- Current label and source definition preserve initiation wording. The reviewed originals support a more nuanced mechanism; no universal exclusive-step claim or blanket historical-refutation finding is imposed.
- Freitas exact MIC/method/accession passages were inspected in the browser-accessible publisher PDF. Direct PDF/HTML retrieval failed 403, SI was not read and the three genomes were not independently rejoined to NCBI registry records.
- The 176 UKMYC groups agree with adopted data but their original public source remains unavailable; original WGS assignments were not independently rejoined. WHO variant sheets underlying Mtb rrl were not independently inspected.
- CAS Registry, Reaxys, DrugBank and exact LINCS content remain unavailable independently. Absence from the limited official HMS archive is not an invalid-ID conclusion. Zyvoxa remains a bounded unresolved product alias.
- Current FDA sponsor and marketing updates do not invalidate the explicitly dated native snapshot. GSRS exact ingredient matching is not itself approval evidence.
- Some PMC HTML retrievals returned challenge pages and XML calls failed 500; those responses are not counted as primary reading. Initial guessed FDA archive/label routes failed or resolved to non-evidence pages; the final successful official sources are identified separately.
- The required shared full-QC gate has the established platform SciPy import failure. Focused native checks, source helpers and review-contract success do not substitute for separately recorded shared gates.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All thirteen original inputs are preserved within 29 verified hashes. Native records, maintained inputs and prior saved reviews remain unchanged by this review.
- Standalone chemistry used the 019 interpreter against 061; schema, strict, source ledger and draft contract used 061. Earlier scratch helper diagnostics and the final successful executions are preserved separately.
- The coordinating reviewer independently audited original DST joins and all compact memberships; its exact report hash is recorded in 605-source-audit.json. No native curation status or history was changed.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T195014Z-linezolid-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of linezolid
started_at: '2026-10-21T19:32:12Z'
finished_at: '2026-10-21T19:50:14Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the native record. Entire native content,
    exact maintained owners, current authorities and original sources were assessed.
    A separate coordinating reviewer independently checked CRyPTIC memberships and
    original DST joins; that contribution and its limits are attributed explicitly.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The exact neutral S-linezolid identity, curated A-site ribosomal mechanism,
  nine separately curated MIC observations and dated FDA assertions are supported.
  Nine CRyPTIC assay strings misrender the categorical WHO designation as a concentration;
  three verified product names need BRAND_NAME typing. Historical initiation/P-site
  interpretations, later context-specific elongation, qualified resistance assertions
  and access limits are explicitly distinguished.
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
  - path: data/antibiotics/antibacterial/linezolid.yaml
    sha256: a8c7f2e532c2069e2e11770d6bb73fe28220a47d92f518b46cb16721796f8601
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
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: context
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: context
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
  - path: scripts/card_evidence_reviews.py
    sha256: f9ec8aff30066bf04b9c2757af7d6f5d179d045e57b9f3b352bbed0b851f50a8
    role: context
  - path: data/raw/cryptic_activity.tsv
    sha256: fa2fe5e5258328f10f9fe5724e4b74f354a98f5355bac68108ab28ffb17c7987
    role: context
  - path: data/raw/cryptic_memberships.tsv.gz
    sha256: f121fc3ac48a44a89931366d908877d833bd846d9690257583c5dbbdb8bd2601
    role: context
  - path: data/raw/cryptic_isolates.tsv.gz
    sha256: 7d51bf3032e295a56e2543f52f12e59d6a8589ad6f2208e2314a154e6e8cf2c5
    role: context
  - path: curation/cryptic_drug_map.tsv
    sha256: 69643f9b5e6dfc91761a4541317de63c5dca565131f6a07a3193878d7f863a54
    role: context
  - path: scripts/extract_cryptic_memberships.py
    sha256: d944260859c29ff3af55137c311e14be45b6c3219b5283c4cbd1b794d49fe952
    role: context
  - path: scripts/cryptic_membership_inventory.py
    sha256: b0d8ae24cac64dfb2813bfa5a5ef590e3330e3c5ace82e25f3528b025147d6cc
    role: context
  - path: src/antibioticmech/activity_memberships.py
    sha256: 22849043b741d7a48a708dfade09524a11ac46afa7efb08d350ec7422ec2e146
    role: context
  - path: data/raw/fda_clinical_status.tsv
    sha256: a6952f85426afa53c5704c588681a078e599ce245bf18f7c9dd390d70e7bb16c
    role: context
  - path: scripts/extract_fda_clinical_status.py
    sha256: f30f385ea6d530dc1749e3d805dbcdbc8715fbc476abc510bf144ea13964e171
    role: context
  - path: data/antibiotics/antibacterial/membership-9de54716d11cc3c8d3113c5bd1bf3c33fc3479e2e994b1d118d05c9cbd9d7895.json.gz
    sha256: 9de54716d11cc3c8d3113c5bd1bf3c33fc3479e2e994b1d118d05c9cbd9d7895
    role: context
targets:
- target_id: CHEBI:63607
  path: data/antibiotics/antibacterial/linezolid.yaml
  label: linezolid
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Exact chemical identity, structure, roles and adopted leads
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_role_names.tsv
    role: ChEBI role labels
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: ARO concept, aliases and source leads
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Ten source resistance assertions
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Source target assertion
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Target relation policy
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Evidence scope overlay
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Evidence scope application
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/cryptic_activity.tsv
    role: Grouped CRyPTIC activities
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/cryptic_memberships.tsv.gz
    role: Adopted group-isolate membership
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/cryptic_isolates.tsv.gz
    role: Adopted isolate context
  - repository: CultureBotAI/AntibioticMech
    path: curation/cryptic_drug_map.tsv
    role: Exact drug mapping
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_cryptic_memberships.py
    role: Membership extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/cryptic_membership_inventory.py
    role: Membership generation
  - repository: CultureBotAI/AntibioticMech
    path: src/antibioticmech/activity_memberships.py
    role: Membership contract
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/fda_clinical_status.tsv
    role: FDA exact structure product status inventory
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: FDA product and GSRS structure joining
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI and CARD extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated source claims and curated-field preservation
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Source and synonym/role policy
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Exact identity decisions
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/linezolid.yaml
    role: Curator-owned target, mechanism, MIC evidence and history preserved by seeder
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/membership-9de54716d11cc3c8d3113c5bd1bf3c33fc3479e2e994b1d118d05c9cbd9d7895.json.gz
    role: Immutable membership payload
scope:
  description: 'Entire 5,736-line native record: all identity fields, ten resistance
    assertions, two targets, 273 activity observations, one compact membership collection,
    37 FDA product assertions and fourteen history events. The 264 CRyPTIC rows and
    37 FDA assertions were read through verified lossless representations, with all
    differing fields retained.'
  selection: Initially uncovered queue position 605; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:63607
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:63607
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    605
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:63607
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/linezolid.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:63607
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/linezolid.yaml --out /private/tmp/am-review-session/605-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: authority
  name: Independent authority verification
  status: passed
  required: false
  summary: Actual final execution returned exit 0; earlier scratch diagnostics are
    disclosed separately.
  target_ids:
  - CHEBI:63607
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/605-authority-check.py
  exit_code: 0
  expected_exit_code: 0
- check_id: cdc-source
  name: Independent cdc-source verification
  status: passed
  required: false
  summary: Actual final execution returned exit 0; earlier scratch diagnostics are
    disclosed separately.
  target_ids:
  - CHEBI:63607
  command: /private/tmp/antibioticmech-record-reviews-061/.venv/bin/python /private/tmp/am-review-session/605-cdc-audit.py
  exit_code: 0
  expected_exit_code: 0
- check_id: fda-source
  name: Independent fda-source verification
  status: passed
  required: false
  summary: Actual final execution returned exit 0; earlier scratch diagnostics are
    disclosed separately.
  target_ids:
  - CHEBI:63607
  command: /private/tmp/antibioticmech-record-reviews-061/.venv/bin/python /private/tmp/am-review-session/605-fda-audit.py
  exit_code: 0
  expected_exit_code: 0
- check_id: source-ledger
  name: Independent source-ledger verification
  status: passed
  required: false
  summary: Actual final execution returned exit 0; earlier scratch diagnostics are
    disclosed separately.
  target_ids:
  - CHEBI:63607
  command: /private/tmp/antibioticmech-record-reviews-061/.venv/bin/python /private/tmp/am-review-session/605-ledger.py
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
  - CHEBI:63607
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
  - CHEBI:63607
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
  - CHEBI:63607
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
  - CHEBI:63607
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
  - CHEBI:63607
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
  - CHEBI:63607
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
  - CHEBI:63607
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
  - CHEBI:63607
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
  - CHEBI:63607
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/linezolid.yaml
  locator: Entire native; 605-initial-inspect.json,605-inspect.json; lossless 605-native-lossless.json
    and 605-native-fda.json
  accessed_at: '2026-10-21T19:44:38Z'
  support: supports
  summary: REVIEWED/EXACT antibacterial CHEBI:63607 contains the neutral S graph,
    seven aliases, five parents, one activity role, eight chemical xrefs, three qualified
    drug links, three document links, two source concepts, ten qualified resistance
    assertions, two targets,273 activity observations and 37 dated FDA assertions.
    All source rows and history were inspected. No separate producer, causal-graph
    or protein-example objects are present; definition and curator-note claims were
    assessed.
  snapshot_sha256: 495db27e6729da01e3b6193ccdc63fcd7fca0d03f0b4483d999565809b7b4201
- evidence_id: chemistry
  kind: validation
  reference: Independent authority structure comparison
  locator: 605-authority-check.py ; 605-authority-chemistry.json; actual 019 interpreter
    against 061 cwd
  accessed_at: '2026-10-21T19:44:38Z'
  support: supports
  summary: 'Seventeen encodings agree on complete InChIKey TYZROVQLWOKYKF-ZDUSSCGKSA-N,
    C16H20FN3O4, charge 0 and the S center: native, current ChEBI, PubChem 441401,
    ChEMBL 126, KEGG C08146/D00947, CCD ZLD and GSRS. Five InChI imports produce the
    amide imidic-acid tautomer and fail a raw graph comparison; canonical tautomer
    comparison with tetrahedral and bond stereo removal disabled gives reciprocal
    chirality-aware matches. This is an explicitly diagnosed normalization boundary,
    not a distinct-isomer finding.'
  snapshot_sha256: 6906c66602cbb0ce75f2de588350592c90ae99c069b43aa3bad10da1e565718d
- evidence_id: groundings
  kind: authority
  reference: Official ChEBI, ARO, KEGG, PubChem, ChEMBL, CCD and drug registries
  locator: 605-source-audit.json authority_dispositions; timestamped 605-fetch.json
    through 605-fetch6.json
  accessed_at: '2026-10-21T19:44:38Z'
  support: supports
  summary: Current structural parent definitions fit the scaffold and the antibacterial-drug
    role is supported. Qualified drug_xrefs retain their drug-context meaning. DrugCentral
    resolves the expected compound; DrugBank/Reaxys independent content remains unavailable.
    CAS page is a shell. The limited HMS archive contains no LSM-5750, which does
    not establish a wrong identifier. Wikipedia was inspected only as a secondary
    document. GSRS identity validation is separate from FDA approval.
  snapshot_sha256: 495db27e6729da01e3b6193ccdc63fcd7fca0d03f0b4483d999565809b7b4201
- evidence_id: patents
  kind: primary_source
  reference: patent:US5688792; patent:WO957271
  locator: Public patent-family texts 605-patent-US5688792.html/.txt and 605-patent-WO957271.html/.txt;
    Example 5 and family metadata
  accessed_at: '2026-10-21T19:44:38Z'
  support: supports
  summary: US5688792A explicitly identifies PCT publication WO95/07271, resolved as
    WO1995007271A1. Both Example 5 passages describe the S monofluoro morpholinyl
    acetamide matching linezolid. The exact example, preferred-compound context and
    synthesis were inspected; general Markush or class antibacterial claims are not
    transferred to every example. These remain relevant document links, not asserted
    patent-status or freedom-to-operate opinions.
  snapshot_sha256: eaf1c575e7d38e4f5a55794012206ac9e361504694e8fecc855179ebd0beea49
- evidence_id: primary2008
  kind: primary_source
  reference: PMID:18757750
  locator: DOI:10.1073/pnas.0804276105; PMC2533191 complete main/captions; actual
    Figures 1 and 4 ; 605-PMC2533191.html and 605-2008-fig*.jpg
  accessed_at: '2026-10-21T19:44:38Z'
  support: supports
  summary: Original D. radiodurans 50S crystals soaked with 5 micromolar linezolid
    support the native A-site/PTC target and a U2585-dependent tRNA-positioning model.
    Final refinement is 3.5 angstrom; 3.3 angstrom diffraction collection is not substituted
    for that resolution. Figure 1C supports the exact S compound; Figure 4F and text
    distinguish A-site overlap from indirect P-site functional effects. A derivative
    cross-link or a proposed downstream model is not relabeled as a direct parent-drug
    binding measurement.
  snapshot_sha256: 511346f3fb3b1bbf855aff00e9dedd160dc592b340a6add51f91209b0e79e951
- evidence_id: historical
  kind: primary_source
  reference: PMID:9835522; PMID:11897593
  locator: Original 1998 PMC106030 selected Methods/Results; 2002 PMC127084 selected
    Methods, linezolid-specific results and Discussion ; 605-PMC106030.html,605-PMC127084.html
  accessed_at: '2026-10-21T19:44:38Z'
  support: supports
  summary: The 1998 linezolid experiments support inhibition of measured initiation-complex
    formation in E. coli and S. aureus systems. The 2002 PNU-100766 assays show functional
    effects on fMet-tRNA binding/translocation and propose P-site involvement; several
    EF-P assays instead use PNU-176798. These functional interpretations are distinguished
    from the later direct A-site structure. Native CARD P-site annotation is explicitly
    DATABASE_ASSERTION/PRIMARY_EVIDENCE_NEEDED, and the curated A-site target has
    its own primary support.
  snapshot_sha256: 7aaf8d79d6e8a23d049d1df3e47f86540ad208e0077f608ab9d3053061acd417
- evidence_id: elongation
  kind: primary_source
  reference: PMID:27791002
  locator: DOI:10.1073/pnas.1613055113; PMC5086994 selected profiling/toeprinting
    Methods, Results, Discussion and captions ; 605-PMC5086994.html
  accessed_at: '2026-10-21T19:44:38Z'
  support: supports
  summary: In tolC-deficient E. coli BWDK cells exposed to 100-fold MIC for 2.5 minutes
    and in defined translation systems, linezolid produces context-dependent elongation
    arrest, influenced by nascent-peptide residues. Its poor first-peptide-bond inhibition
    under these conditions does not erase all earlier initiation assays. Native definition
    wording is historical and also appears in official labeling; it should not be
    read as an exclusive universal step of action.
  snapshot_sha256: e06499f7b0959977ee513dfe70f87021bedcb2b3cbd2df1ce0c0a569f54ec21e
- evidence_id: host
  kind: primary_source
  reference: PMID:16723564; PMID:17499045
  locator: Original 2006 PMC1479116 selected mitochondrial incorporation Methods and
    linezolid-specific Results/Figure 4 captions;2007 complete indexed abstract in
    605-followup-core.json
  accessed_at: '2026-10-21T19:44:38Z'
  support: supports
  summary: Exact linezolid inhibits protein synthesis in isolated mammalian mitochondria
    from rat/rabbit preparations, supporting HOST_SHARED_TARGET scope. The 2007 bacterial/human
    mitochondrial photolabeling study uses oxazolidinone derivatives; those experiments
    are not claimed as an exact parent-linezolid-only human structural study. Neither
    observation implies binding to human cytoplasmic ribosomes or a new clinical risk
    estimate.
  snapshot_sha256: f97682c96da4de27de46112f4fd873e13fd2cdfc3e246cc9a010d02ddb208631
- evidence_id: adapter
  kind: database
  reference: kg-microbe-sources iModulonDB adapter
  locator: 605-adapter-results.json; four executed searches, all exit 0; dataset inventory
    575-adapter-datasets.json
  accessed_at: '2026-10-21T19:44:38Z'
  support: supports
  summary: Adapter searches preceded open-ended protein follow-up. S. aureus staph_precise108
    resolves LmrS USA300HOU_RS11735. The 23S substring hits are methyltransferases
    rlmB/rlmN/rlmH, not the rRNA target itself. E. coli rrlA and Mtb rrl returned
    no gene hits. No component hits required summarize; no D. radiodurans dataset
    was available. Resource membership or absence is not direct binding, resistance
    or negative experimental evidence.
  snapshot_sha256: b78148983a160ee4089cfa198a6f47086da82c5c2a04b6fe1ffdd32178921b62
- evidence_id: aro
  kind: database
  reference: https://purl.obolibrary.org/obo/aro.obo
  locator: Reused official 426-current-aro.obo with 426-fetch2-results.json; exact
    13 blocks 605-aro-blocks.json; maintained rows 605-raw-rows.json
  accessed_at: '2026-10-21T19:44:38Z'
  support: supports
  summary: 'All ten native resistance relations, antibiotic/class terms and CARD target
    resolve in the current ontology. All thirteen current PMID leads were resolved,
    with twelve indexed abstracts read and one metadata-only review. Database qualification
    remains meaningful: individual variant, strain, material and effect are not inferred
    merely from class membership. The Mtb rrl WHO-catalogue link resolves at publication
    level, but variant tables were not independently revalidated.'
  snapshot_sha256: 0d0915ea34e20ca67f59b2400fb8b663b565c81972d0e0bcbadd8000bdad9b39
- evidence_id: resistance
  kind: primary_source
  reference: PMID:26248384; PMID:32277823; PMID:29635422; PMID:25977397
  locator: 2015 PMC4576063 selected Methods, Table 1, Results/Discussion; remaining
    complete indexed abstracts; individual 605-source-audit.json dispositions
  accessed_at: '2026-10-21T19:44:38Z'
  support: supports
  summary: Original cfr(B) work raises linezolid MIC in heterologous S. aureus RN4220
    while explicitly leaving the contribution in its enterococcal isolates unresolved.
    The cfr(D) abstract reports effects in E. coli AG100A but not the tested enterococcal
    hosts; optrA and poxtA expression contexts are also bounded. Native generic qualified
    associations are not rewritten as universal host effects or rejected for lacking
    an asserted primary claim. LmrS/23S/clcD leads retain their explicit abstract-only
    limits.
  snapshot_sha256: 495db27e6729da01e3b6193ccdc63fcd7fca0d03f0b4483d999565809b7b4201
- evidence_id: adopted
  kind: primary_source
  reference: All12 adopted ChEBI/ARO PMID leads
  locator: 605-adopted-core.json; exact individual dispositions 605-source-audit.json
  accessed_at: '2026-10-21T19:44:38Z'
  support: supports
  summary: 'Every adopted PMID resolves: eleven available indexed abstracts and one
    metadata-only review were inspected. Clinical toxicity, pharmacokinetics, combination
    treatment, animal implants, toxin expression, biofilm MBEC and sub-MIC adhesion
    studies retain their own endpoints and taxa. The structural original was read
    more deeply as stated separately. Reviews and broad clinical contexts are not
    promoted to direct molecular or exact MIC experiments.'
  snapshot_sha256: 495db27e6729da01e3b6193ccdc63fcd7fca0d03f0b4483d999565809b7b4201
- evidence_id: freitas
  kind: primary_source
  reference: DOI:10.1093/jac/dkaa227
  locator: Original publisher PDF pp 2417–2418 Methods, WGS/accession and Results
    passages ; 605-web-pdf-evidence.json; PMID32607549; direct downloads 403
  accessed_at: '2026-10-21T19:44:38Z'
  support: supports
  summary: 'The original supports all three native clonal representatives: C59, 149T
    and 2Fez each have linezolid MIC 8 mg/L measured by broth microdilution and interpreted
    with EUCAST. Their origin/year and respective WLYR00000000,WLYQ00000000,WLYP00000000
    mappings under PRJNA580369 agree. Browser-accessible primary PDF passages were
    inspected; the inaccessible direct download, uninspected SI and lack of a separate
    genome-registry rejoin are explicit limits.'
  snapshot_sha256: 4cb3034aabb97bc105ea99b43c4af276bdbb4f8af5a38ab97b9bc0ea553248fe
- evidence_id: cdc
  kind: authority
  reference: CDC/FDA Antimicrobial Resistance Isolate Bank
  locator: All six native URLs fetched and individually checked ; 605-cdc-audit.py/.json
    ; 605-cdc-*.html
  accessed_at: '2026-10-21T19:44:38Z'
  support: supports
  summary: All six MIC values, greater-than signs, R source interpretations, taxon/strain
    labels, broth method, modal-MIC wording and CLSI 2025 M100 S35 edition match official
    pages. Five named BioSamples match; 0780 explicitly lacks an available accession.
    Micrograms/mL equals native mg/L. These are preserved source interpretations rather
    than newly calculated clinical breakpoints.
  snapshot_sha256: 025fca9522733df56d6398d664e5583680a47d73cecc92d10ab7264df5eb4fb0
- evidence_id: cryptic
  kind: validation
  reference: Independent coordinating-reviewer CRyPTIC audit
  locator: 605-root-cryptic-audit.py/.json/.log; original pinned 134-DST_MEASUREMENTS.parquet;
    adopted activity/membership/isolate registries
  accessed_at: '2026-10-21T19:44:38Z'
  support: supports
  summary: 'Independent audit verifies 264 observation digests, 55,094 memberships/measurements
    and 30,401 subjects: 22,294 linked and 8,107 explicit nulls. All adopted joins
    agree; 88 DST groups independently join 33,413 original LZD source rows. The 176
    UKMYC groups match adopted rows but original UKMYC is unavailable; original WGS
    assignments were not rejoined. Nine assay strings append mg/L to categorical METHOD_CC=WHO.
    Source R/S/U calls and membership integrity remain supported.'
  snapshot_sha256: d1b89bdf0ff54034eb09864920d4458f5048d55db473b56a07454a66828a9afb
- evidence_id: fda
  kind: authority
  reference: FDA Drugs@FDA downloadable archive; FDA GSRS
  locator: 605-fda-current.zip,605-fda-audit.py/.json,605-gsrs-full.json; official
    download https://www.fda.gov/media/89850/download?attachment=
  accessed_at: '2026-10-21T19:44:38Z'
  support: supports
  summary: All 37 native product assertions across 29 applications exactly match their
    adopted fields, dated source metadata and GSRS identity mapping. Current official
    archive comparison confirms original approval dates and products; it changes sponsor
    205154 and marketing status 210378 relative to the dated native snapshot. These
    are refresh observations, not proof the historical assertions were false. Current
    GSRS version 162 agrees on exact identity; native version 90 provenance remains
    intact.
  snapshot_sha256: 89ac5d9e15d10bfb865e7fc351e5a912f06030dafb8ed2ed501ea0f077a26bfc
- evidence_id: brands
  kind: authority
  reference: Official Zyvox, Zyvoxam and Zyvoxid product labeling
  locator: 605-zyvox-exact-spl.html sections 11/12.4 ; 605-zyvoxam-official.pdf title/composition
    plus Health Canada DIN 02243685 ; 605-zyvoxid-bfarm.pdf sections 1/2 and 605-zyvoxid-austria.html
  accessed_at: '2026-10-21T19:44:38Z'
  support: supports
  summary: The three named authorities identify Zyvox, Zyvoxam and Zyvoxid as products
    containing linezolid. Native synonyms 3,5,6 therefore need BRAND_NAME typing while
    their valid relationship to the compound remains. Zyvoxa was found as a historical
    lead but no exact original product document was independently inspected; its spelling
    and classification are left bounded rather than forced.
  snapshot_sha256: 7fcbc221286b25ce6fb6bc6cd0d8a3151f8f9cc905657ee6d37633556909bb92
- evidence_id: provenance
  kind: validation
  reference: Preserved inputs and maintained-owner audit
  locator: 605-ledger.py ; 605-source-audit.json ; 605-scratch-check-attempts.json
  accessed_at: '2026-10-21T19:44:38Z'
  support: supports
  summary: All 29 captured inputs match, including the unchanged thirteen originals.
    Both source-concept mints recompute and fourteen history events are chronological.
    Focused schema, strict and native chemistry pass. Supplementary helper development
    exposed an amide-tautomer comparison assumption and FDA parser assumptions; those
    diagnostics are recorded separately and final corrected helper executions pass.
    No native/source data were changed.
  snapshot_sha256: 495db27e6729da01e3b6193ccdc63fcd7fca0d03f0b4483d999565809b7b4201
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral S-linezolid
  outcome: supported
  summary: Independent structural authorities agree after a documented stereo-preserving
    amide-tautomer normalization. Source chemical names, formula, charge and exact
    stereochemistry are supported. No unspecified-stereo mixture inference or product-form
    substitution is made.
  target_ids:
  - CHEBI:63607
  evidence_ids:
  - native
  - chemistry
  - patents
  - groundings
- assessment_id: nomenclature
  area: nomenclature
  topic: Chemical and product aliases
  outcome: concern
  summary: Chemical aliases fit the exact graph. Three verified product names are
    incorrectly typed EXACT_SYNONYM; the unverified Zyvoxa alias retains a separate
    limit.
  target_ids:
  - CHEBI:63607
  evidence_ids:
  - native
  - brands
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: Chemical, drug and document identifiers
  outcome: unknown
  summary: Inspected exact structures and document links agree, while DrugBank/Reaxys/CAS
    Registry/LINCS remain independently unresolved. Drug-context links do not assert
    chemical equivalence.
  target_ids:
  - CHEBI:63607
  evidence_ids:
  - groundings
  - patents
  - chemistry
  - fda
- assessment_id: mechanism
  area: evidence
  topic: A-site mechanism and historical functional interpretations
  outcome: supported
  summary: Native primary D. radiodurans A-site/PTC evidence and HOST_SHARED_TARGET
    scope are supported. Historical initiation/P-site assays, official label phrasing
    and later context-dependent elongation are distinguished; the CARD P-site assertion
    remains explicitly database-qualified.
  target_ids:
  - CHEBI:63607
  evidence_ids:
  - primary2008
  - historical
  - elongation
  - host
  - aro
  - adapter
- assessment_id: resistance
  area: evidence
  topic: Ten qualified resistance associations
  outcome: unknown
  summary: All current database relations are present, with individual citation dispositions
    and selected original follow-up. Heterologous effects, mixed clinical backgrounds
    and unresolved exact alleles are not generalized or mistaken for unsupported native
    primary claims.
  target_ids:
  - CHEBI:63607
  evidence_ids:
  - aro
  - resistance
  - adopted
  - adapter
- assessment_id: activity
  area: scope
  topic: 273 activity observations and memberships
  outcome: concern
  summary: Nine separately curated observations match their checked sources, and all
    compact memberships match the independent audit. Nine categorical WHO source designations
    are misrendered as concentrations. Original UKMYC/WGS limitations remain explicit.
  target_ids:
  - CHEBI:63607
  evidence_ids:
  - freitas
  - cdc
  - cryptic
- assessment_id: clinical
  area: scope
  topic: Dated FDA approval and product context
  outcome: supported
  summary: All 37 assertions match adopted original approvals, product data and exact
    ingredient mapping. Current sponsor/marketing differences remain dated refresh
    context, separate from proof of historical accuracy or clinical recommendations.
  target_ids:
  - CHEBI:63607
  evidence_ids:
  - fda
  - brands
- assessment_id: classification
  area: scope
  topic: Structural classes, role and exact source scope
  outcome: supported
  summary: The acetamide, morpholine, organofluorine and oxazolidinone parents and
    antibacterial-drug role fit the verified structure and primary mechanism. Family,
    derivative and clinical evidence is kept within its demonstrated scope.
  target_ids:
  - CHEBI:63607
  evidence_ids:
  - groundings
  - primary2008
  - host
  - adopted
  - patents
- assessment_id: provenance
  area: provenance
  topic: Owners, hashes, source mints and history
  outcome: supported
  summary: Original captures and appended maintained-owner hashes are unchanged, source
    mints agree and history is chronological. Focused checks do not replace required
    shared corpus gates.
  target_ids:
  - CHEBI:63607
  evidence_ids:
  - provenance
  - cryptic
  - fda
  - native
findings:
- finding_id: F1
  issue_key: linezolid-cryptic-who-token-as-mg-l
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Nine categorical WHO designations are rendered as concentrations
  description: At activity indices 68,69,70,71,74,75,76,77,86 the generator turns
    METHOD_CC=WHO into critical concentration WHO mg/L. WHO is a categorical designation,
    not a numeric concentration. Source phenotypes, memberships and the three U groups
    correctly lacking an activity category remain intact.
  target_ids:
  - CHEBI:63607
  field_paths:
  - activity_spectrum[68].assay
  - activity_spectrum[69].assay
  - activity_spectrum[70].assay
  - activity_spectrum[71].assay
  - activity_spectrum[74].assay
  - activity_spectrum[75].assay
  - activity_spectrum[76].assay
  - activity_spectrum[77].assay
  - activity_spectrum[86].assay
  evidence_ids:
  - cryptic
  - native
  rule_id: Quantitative assay provenance and source scope
  normalization_reason: Systematic source formatting invents concentration units for
    categorical metadata. This is major provenance/representation, with no demonstrated
    membership corruption.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: cryptic_activity_assay formatting of METHOD_CC
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/cryptic_activity.tsv
    role: Adopted categorical critical-concentration source token
- finding_id: F2
  issue_key: linezolid-zyvox-zyvoxam-zyvoxid-brand-typing
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: Three verified product names need brand typing
  description: Native synonyms 3,5,6 label Zyvox, Zyvoxam and Zyvoxid EXACT_SYNONYM.
    Official product documents establish BRAND_NAME scope. The separate Zyvoxa alias
    is not included in this confirmed finding because exact original product documentation
    was not independently inspected.
  target_ids:
  - CHEBI:63607
  field_paths:
  - synonyms[3].synonym_type
  - synonyms[5].synonym_type
  - synonyms[6].synonym_type
  evidence_ids:
  - brands
  - native
  rule_id: Chemical equivalence versus product-brand alias
  normalization_reason: Bounded alias-type defect; preserve the legitimate product
    association and exact native chemical identity.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Source-owned product aliases
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO synonym extraction and typing
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: BRAND NAME to BRAND_NAME generation
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - CHEBI:63607
  description: Change cryptic_activity_assay to distinguish numeric concentrations
    from categorical source designations. Preserve WHO as a designation without mg/L,
    retain genuine numeric values and source phenotypes, and do not infer thresholds
    from adjacent rows. Regenerate through the maintained source pipeline.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: cryptic_activity_assay formatting of METHOD_CC
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/cryptic_activity.tsv
    role: Adopted categorical critical-concentration source token
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - All nine affected strings retain WHO without presenting it as a concentration.
  - A meaningful generator check distinguishes numeric, categorical and empty METHOD_CC
    values.
  - All 264 observation identities, 55,094 memberships and 30,401 subject contexts
    remain correct; U groups remain unclassified.
  - MIC inequalities, units and source R/S/U calls remain unchanged.
  - Required schema, strict, term/reference/history and corpus gates pass after curation.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - CHEBI:63607
  description: Type the source-owned Zyvox, Zyvoxam and Zyvoxid names as product brands
    using reproducible ARO extraction typing or equivalent maintained policy that
    emits BRAND_NAME. Preserve names and source provenance. Resolve Zyvoxa separately
    with exact product evidence before extending this confirmed correction.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Source-owned product aliases
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO synonym extraction and typing
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: BRAND NAME to BRAND_NAME generation
  generator: scripts/extract_source_inventory.py and scripts/seed_from_sources.py
  acceptance_checks:
  - The three verified product aliases regenerate as BRAND_NAME.
  - The exact native structure and valid drug/product relationships remain intact.
  - The unverified fourth alias is neither silently corrected nor removed.
limitations:
- All twelve adopted and thirteen current PMID leads were resolved; eleven and twelve
  indexed abstracts respectively were read, with one overlapping metadata-only review.
  Original full versus selected reading is itemized, not implied for every lead.
- The primary structural experiment is a D. radiodurans isolated 50S complex. Historical
  initiation assays, indirect P-site interpretations, derivative photolabeling and
  later context-dependent E. coli elongation retain their distinct systems and material
  scope.
- Current label and source definition preserve initiation wording. The reviewed originals
  support a more nuanced mechanism; no universal exclusive-step claim or blanket historical-refutation
  finding is imposed.
- Freitas exact MIC/method/accession passages were inspected in the browser-accessible
  publisher PDF. Direct PDF/HTML retrieval failed 403, SI was not read and the three
  genomes were not independently rejoined to NCBI registry records.
- The 176 UKMYC groups agree with adopted data but their original public source remains
  unavailable; original WGS assignments were not independently rejoined. WHO variant
  sheets underlying Mtb rrl were not independently inspected.
- CAS Registry, Reaxys, DrugBank and exact LINCS content remain unavailable independently.
  Absence from the limited official HMS archive is not an invalid-ID conclusion. Zyvoxa
  remains a bounded unresolved product alias.
- Current FDA sponsor and marketing updates do not invalidate the explicitly dated
  native snapshot. GSRS exact ingredient matching is not itself approval evidence.
- Some PMC HTML retrievals returned challenge pages and XML calls failed 500; those
  responses are not counted as primary reading. Initial guessed FDA archive/label
  routes failed or resolved to non-evidence pages; the final successful official sources
  are identified separately.
- The required shared full-QC gate has the established platform SciPy import failure.
  Focused native checks, source helpers and review-contract success do not substitute
  for separately recorded shared gates.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All thirteen original inputs are preserved within 29 verified hashes. Native records,
  maintained inputs and prior saved reviews remain unchanged by this review.
- Standalone chemistry used the 019 interpreter against 061; schema, strict, source
  ledger and draft contract used 061. Earlier scratch helper diagnostics and the final
  successful executions are preserved separately.
- The coordinating reviewer independently audited original DST joins and all compact
  memberships; its exact report hash is recorded in 605-source-audit.json. No native
  curation status or history was changed.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
