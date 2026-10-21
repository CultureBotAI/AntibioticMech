# Gatifloxacin: nonnumeric susceptibility-method metadata and Tequin name typing

- Review: 20261021T172035Z-gatifloxacin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T16:59:23Z
- Finished UTC: 2026-10-21T17:20:35Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native gatifloxacin molecular graph and inspected exact chemical references agree. Two corrections are warranted: the CRyPTIC writer renders a source WHO designation as a concentration with mg/L units, and Tequin is typed as an exact synonym rather than a brand. All293 source measurements and membership counts reproduce. Qualified CARD assertions and the existing Salmonella parE evidence limitation remain appropriately bounded.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position490; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:5280 | data/antibiotics/antibacterial/gatifloxacin.yaml | generated | gatifloxacin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:5280 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:5280 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:5280 | Actual focused execution exited 0. |
| Dedicated adopted CRyPTIC membership integrity | passed | True | CHEBI:5280 | Actual own049 audit exited0 across26 compounds,4012 groups and857940 memberships. No raw-release or rendered-page flags were used. |
| Authoritative full QC | failed | True | CHEBI:5280 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:5280 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:5280 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:5280 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:5280 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:5280 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:5280 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:5280 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:5280 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact molecule and structural classification

identity: supported. Targets: CHEBI:5280.

The native graph, source systematic names, parent terms and independently parsed exact public structures agree. Pharmaceutical hydration and unspecified molecular stereochemistry remain separate concepts.

### Nonnumeric source metadata rendered as concentration

consistency: concern. Targets: CHEBI:5280.

WHO is a categorical source token, not a numerical amount. Appending mg/L creates unsupported quantitative-looking assay information for69 measurements even though their source susceptibility category is faithfully preserved.

### Tequin product semantics

nomenclature: concern. Targets: CHEBI:5280.

The official historical product label supports retaining Tequin as a brand association, not exact chemical-name equivalence.

### Topoisomerase mechanism and qualified target

evidence: supported. Targets: CHEBI:5280.

Original enzyme studies support bacterial type-II-topoisomerase action with species/preparation scope. The native direct-GyrA assertion remains explicitly database-tier and PRIMARY_EVIDENCE_NEEDED; no isolated-subunit binding proof or equal host potency is inferred.

### All22 resistance assertions and parE qualification

evidence: unknown. Targets: CHEBI:5280.

All exact ARO edges persist, but current-linked primary abstracts do not uniformly establish exact-drug/allele causality. The inspected Salmonella original confirms why its native parE claim is qualified. Related-drug resistance, class-wide reviews and unvalidated mutations are not silently upgraded.

### Grouped source phenotypes and membership fidelity

evidence: supported. Targets: CHEBI:5280.

All293 source measurements and group-isolate counts reproduce; the existing membership artifact and adopted joins are internally valid. Source R/S values and reported critical-concentration metadata are not MIC measurements or species-wide susceptibility.

### All owners, citations and history

provenance: supported. Targets: CHEBI:5280.

The entire native record, original and appended25 hashes, eight history events, complete adopted compound citation list and actual source/writer lanes were assessed. Drug/document links preserve their broader contracts.

### Optional enrichment and limits

completeness: unknown. Targets: CHEBI:5280.

No missing optional clinical, producer, protein-example or causal object is itself a defect. Future primary target/resistance curation requires exact species, strain, allele, material and assay proof; current source qualifications remain valuable.

## Findings

### F1: Do not attach concentration units to the CRyPTIC WHO designation

major / open / confirmed; issue key: gatifloxacin-cryptic-who-token-as-mg-per-l-concentration.

The69-measurement WHO2019 source group dst_measurements:0600668ff179a303 carries literal method_cc=WHO and source phenotypeS. The writer turns this into critical concentration WHO mg/L. No numeric concentration or MIC is supplied for these rows, and neighboring2.0mg/L groups cannot supply the missing value. Source phenotype and membership content remain valid.

### F2: Retain Tequin as a brand name

minor / open / confirmed; issue key: gatifloxacin-tequin-exact-synonym-product-name.

Native synonym8 types Tequin as EXACT_SYNONYM. The official FDA product label identifies TEQUIN tablets/injection and describes gatifloxacin sesquihydrate. The searchable product name belongs under BRAND_NAME; this is not a reason to replace the parent molecular graph with the product hydrate.

## Recommended Actions And Acceptance Checks

### A1

Handle numeric and nonnumeric critical-concentration metadata separately in maintained emission.

- Preserve literal WHO and the sourceS phenotype. Render the token as a source designation without concentration units, or leave the numeric concentration unspecified. Never impute2.0mg/L from adjacent rows.
- Regenerate observations, digests and content-addressed membership/reference consistently through supported writers; retain all293 measurement and isolate joins and existing source provenance.
- Run focused native validation, corpus reproduction, dedicated membership audit and required QC. Add a meaningful regression covering a nonnumeric method_cc token if implementation is separately authorized.

### A2

Preserve Tequin with BRAND_NAME typing through maintained ARO name handling.

- Retain the source spelling and provenance while changing only its semantic name type; do not equate historical product hydration with the parent chemical graph.
- Regenerate and verify native schema/strict, source history and reproducibility.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/gatifloxacin.yaml; Entire native YAML, all22 resistance rows, molecular target, ten activity groups, membership reference and eight history events | supports | CHEBI:5280 is SEEDED and EXACT, neutral C19H22FN3O4, XUBOMFCQGDBHNK-UHFFFAOYSA-N. The methylpiperazine centre is unspecified. The native source-qualified mechanism is nucleic-acid synthesis inhibition from CHEBI:50750 with HOST_SHARED_TARGET scope. One CARD GyrA target is explicitly PRIMARY_EVIDENCE_NEEDED; resistance entries explicitly retain database tier. No primary target experiment, protein example, producer or causal graph is asserted. Ten CRyPTIC DST groups contain source R/S categories, not numerical MICs. |
| owners | 490-source-rows.json; 490-inspect.json; Complete adopted ChEBI/ARO, resistance, target, drug mapping and grouped CRyPTIC rows; actual writer and qualification ownership | supports | ChEBI supplies molecular identity and definition; ARO supplies class, merged names/exact links,22 resistance edges and one target. The maintained card_evidence_reviews overlay adds the explicit Salmonella parE limitation. GFX maps exactly to the parent gatifloxacin concept, with a documented racemic-drug mapping boundary. CRyPTIC grouping/membership writers supply ten observations and the content-addressed artifact. All25 captured inputs preserve the original13. |
| chemistry | 049-root-authority-chemistry.json; 490-chemistry.json; Eleven independent native/current-authority forward encodings | supports | Native SMILES/InChI, current ChEBI, PubChem name and exact CID5379, CHEMBL31 and KEGG C07661 molfile all reproduce the full native key and formula, neutral charge and unspecified tetrahedral centre. No water or counterion is encoded. The unspecified graph is not itself a proof of racemic bulk composition. |
| authority | CHEBI:5280; CHEBI:23765,26512,37143,46848,86324,33281,50750; ARO:3000659; Current compound, parent and role entries; drug/document identity lookups | supports | Quinolone, quinolinemonocarboxylic acid, organofluorine, N-arylpiperazine and quinolone-antibiotic classifications fit. CAS112811-59-3 is corroborated by chemical/drug entries. DrugBankDB01044, DrugCentral1280 and KEGG D08011 resolve to gatifloxacin under broader drug association semantics; related products/hydrates are not exact free-base assertions. Gmelin2281206, Reaxys7445861 and legacy LINCSLSM-5139 remain source-attributed without independent complete registry inspection. Wikipedia resolves the compound topic and is not primary scientific evidence. |
| adopted | PMID:10737746,12190308,12620077,12873512,12904069,15125930,15745831,15911273,16078842,16337791; PMID:8522459; All ten ChEBI-adopted and the ARO compound-adopted complete indexed abstracts | supports | 10737746 concerns MIC prediction;12190308,12873512,15745831 and15911273 concern host hERG models;12620077 and12904069 examine other synthesized quinolones;15125930 concerns anti-Toxoplasma analogues;16078842 concerns chiral nadifloxacin salts;16337791 concerns isothiazoloquinolones. These do not independently prove exact gatifloxacin bacterial binding. Original8522459 directly tests AM-1155 against clinical isolates and experimental mouse infections, supporting antibacterial context but not a unique purified-target mechanism. |
| aro | 490-current-aro-terms.json; https://purl.obolibrary.org/obo/aro.obo; Complete current compound/class/target and all22 determinant stanzas | supports | All22 exact gatifloxacin resistance relationships persist in current ARO: one qnr target-protection assertion and21 target-alteration assertions. The GyrA targeted_by_antibiotic relationship also persists. Current source agreement verifies database provenance, not uniform primary support for every species, allele or compound. The native source-tier language and existing parE qualification must not be upgraded or silently discarded. |
| aro-leads | 490-current-aro-leads-0.json through 490-current-aro-leads-3.json; All50 current ARO-linked discovery records;49 complete available abstracts and one metadata-only record | supports | PM15282231 has no abstract. Other supplied abstracts were read, including reviews and related-drug studies. Exact gatifloxacin appears in selected M.tuberculosis enzyme/clinical-isolate work, S.aureus comparative quinolone testing and C.difficile selection/surveillance experiments. Many E.coli, Bartonella, M.leprae, Ureaplasma, Morganella and Mycoplasma leads instead test ciprofloxacin, ofloxacin or other quinolones, and some describe unvalidated polymorphisms. PMID36010006 primarily studies sulbactam-durlobactam, while35944069 and30337678 are data/platform studies. Cross-drug, class-wide or review evidence is not promoted to exact gatifloxacin resistance proof. PMID27847014 specifically concerns ofloxacin-resistant M.tuberculosis. |
| primary1998 | PMID:9756776; DOI:10.1128/AAC.42.10.2678; https://journals.asm.org/doi/10.1128/aac.42.10.2678; Independent co-review of primary abstract, Table1 and selected compound/strain/enzyme/decatenation methods | supports | Gatifloxacin was synthesized by Kyorin. Reconstituted S.aureus MS5935 GrlA/GrlB topoisomeraseIV, affinity-purified E.coli NIHJ JC-2 gyrase and separately prepared HeLa topoisomeraseII gave IC50 values13.8,0.109 and265µg/mL respectively. These distinct preparations support antibacterial topoisomerase action and assay-specific bacterial selectivity while retaining measurable host-family inhibition. They do not prove isolated GyrA binding, identical target preference across species or clinical safety. |
| primary2001 | PMID:11709337; DOI:10.1128/AAC.45.12.3544-3547.2001; Independent co-review of complete abstract and primary material/strain/MIC/reconstitution/supercoiling/decatenation methods | supports | The S.aureus MS5935 comparison used GrlA Ser80Phe and GyrA Ser84Leu mutants, agar-dilution MICs and reconstituted holoenzymes. It classifies gatifloxacin as dual-targeting in that tested system. The original numerical gatifloxacin table row was not independently recovered and is not adopted. Holoenzyme inhibition and mutant susceptibility do not automatically prove a binding site on an isolated subunit. |
| pare | PMID:19104017; DOI:10.1128/AAC.01005-08; https://pureadmin.qub.ac.uk/ws/portalfiles/portal/5282229/Multiple_Regulatory_Pathways_Associated_with_High_Level_Cipro_oxacin.pdf; Independent co-review of original strain/selection/susceptibility/complementation methods, relevant Results/Discussion and visually inspected Tables1/3 | supports | Table1 concerns nalidixic acid/ciprofloxacin. Both5408-cip and its wild-type-parE complement retain ciprofloxacin MIC&gt;32µg/mL; gyrA/gyrB complements lower susceptibility endpoints in the tested backgrounds. The authors leave indirect parE contribution unresolved. Table3 concerns four nonquinolones and includes neither a parE-specific comparison nor gatifloxacin. An ignored-inclusive whole downloaded-text search found no gatifloxacin mention. This supports the existing native qualification, not universal parE inactivity or deletion of every inherited serovar/drug assertion. |
| adapter | 490-adapter-results.json; 475-imodulon-datasets.json; Covered-dataset catalog and thirteen actual gene searches across six covered organisms | supports | Searches in E.coli precise1k, M.tuberculosis modulome, S.aureus staph_precise108, S.enterica core, A.baumannii precise139 and S.pneumoniae precise718 returned relevant gyrA/gyrB/parC/parE annotations and no iModulons. Gene examples include E.coli b2231/b3019/b3030, M.tuberculosis Rv0006/Rv0005 and S.pneumoniae SP_0855. Broad gyrA search results also include other gyrase-associated genes and are not all exact gyrA hits. The other native taxa are outside this catalog; no missing result is treated as biological absence or binding/resistance evidence. |
| cryptic | DOI:10.5281/zenodo.15680920; https://zenodo.org/records/15680920/files/DST_MEASUREMENTS.parquet?download=1; All293 exact GFX rows in previously fetched pinned original DST parquet, compared with adopted activity/membership/isolate inventories | supports | The original parquet MD5 is45b4501ea7c3925af565dbbc6188dec0, SHA256a3159a5e4ce0f4d51d61a31be2b5b45fce1e1f5185e8988cb36a4d57826910b2. All ten group counts reproduce:1,3,1,3,44,9,126,3,34,69. There are16 source-resistant and277 source-susceptible measurements; every group has MEDIUM quality and no MIC value. The final WHO2019 group comprises69 distinct source isolates with METHOD_CC=WHO and phenotypeS. This does not provide a numeric concentration, a universal susceptibility judgment, exact reagent-form proof or an independently validated clinical breakpoint. |
| membership | 490-membership-independent.json; 490-membership-gate.json; Independent complete payload/hash/digest/raw-DST and adopted sequencing-registry join audit | supports | The native artifact has SHA2569c04e181212b9a3259e6973b7e175d2bb3836a1e5489f7ee4dcee1b68b2e976e,5114 compressed and55036 uncompressed bytes. All ten observation digests and293 subjects/memberships/measurements agree;142 subjects have adopted sequencing links and151 have null links. All293 group-isolate counts match original DST data, and adopted membership/isolate-registry joins match. Original WGS parquet was not redownloaded, so sequencing links are validated against adopted registries rather than independently against that original WGS file. |
| writer | scripts/seed_from_sources.py:2661; cryptic_activity_assay, especially lines2676–2677 | supports | The writer appends critical concentration and mg/L to every nonempty method_cc token without checking whether it is numeric. Thus the preserved raw designation WHO becomes critical concentration WHO mg/L at activity_spectrum[9].assay. Native evidence notes retain method_cc=WHO, exposing the source/representation distinction. Correcting the assay changes its observation digest and requires consistent regeneration of the membership artifact/reference. |
| brand | https://www.accessdata.fda.gov/drugsatfda_docs/nda/99/21061_Tequin_prntlbl.pdf; Actual original1999 FDA label scan, PDFpage2/printedpage1 viewed | supports | The label presents TEQUIN as the product name for gatifloxacin tablets/injection and describes racemic gatifloxacin sesquihydrate, formula C19H22FN3O4·1.5H2O and mass402.42. Native synonym8 types Tequin as EXACT_SYNONYM rather than BRAND_NAME. Product identity and hydration do not invalidate the anhydrous parent graph; this historical label does not establish current marketing status or a treatment recommendation. |
| patents | https://patents.google.com/patent/EP0230295A2/en; https://patents.google.com/patent/US4980470A/en; Independent co-review of exact Examples3/14, adjacent compound scope and analytical description | supports | Both patents explicitly synthesize the gatifloxacin connectivity with7-(3-methyl-1-piperazinyl) and8-methoxy groups. The analyzed examples are hemihydrate C19H22FN3O4·1/2H2O, so these are relevant document associations rather than proof of exact anhydrous experimental material or a resolved piperazine stereoisomer. No family-wide potency is transferred. |
| search | 490-local-hits.txt; 049-root-fetch1-manifest.json through 049-root-fetch7-manifest.json; 490-independent-audit-manifest.json; Ignored-inclusive local source search and actual bounded public authority/original-paper attempts | context_only | The initial local search and exact owner checks include hidden/ignored files. Current public authorities and all adopted abstracts were read; selected primary follow-up has the depths recorded above. Zenodo public page/API attempts returned403, while the previously fetched pinned original DST parquet was available locally. PMC challenge pages and metadata-only efetch responses are not full-text successes. |

## Limits And Additional Notes

- All11 compound-adopted abstracts and all50 current ARO discovery records were assessed;49 of the latter supplied abstracts and PMID15282231 was metadata only. The source-supplied PMID3311572 abstract is itself truncated. Not all50 original papers were read in full.
- The1998 and2001 mechanism originals were inspected at the specific selected-table/method depths stated by an independent co-reviewer. Browser excerpts are not full-paper snapshots; unsuccessful PMC/EPMC routes remain explicit.
- The Salmonella publisher PDF was inspected in relevant methods/results/discussion and actual Tables1/3; not every figure or supplement was reviewed. No exact gatifloxacin result is inferred from its ciprofloxacin and other-drug experiments.
- All293 original DST joins were checked. The142 sequencing mappings were compared with adopted isolate/membership registries, not independently with an original WGS parquet. No UKMYC row belongs to this target.
- The WHO source token does not establish an amount; original source R/S categories are retained without independent breakpoint adjudication. No source observation is a numeric MIC and source-material stereochemical/hydrate purity was not established.
- Gmelin, Reaxys and LINCS accessions remain source-attributed. Historical FDA label and patent preparations are document/product evidence, not proof of current approval or exact anhydrous assay material.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Root assessed the entire native/source record, all stated indexed abstracts and independent chemistry; delegated reviewers independently audited original mechanism/patent material and complete CRyPTIC membership reconstruction. Their exact reading depths, retrieval receipts and hashes are retained.
- No native, source, qualification overlay or membership artifact was edited. All25 input hashes remain unchanged, preserving the original13.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T172035Z-gatifloxacin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Gatifloxacin: nonnumeric susceptibility-method metadata and Tequin name typing'
started_at: '2026-10-21T16:59:23Z'
finished_at: '2026-10-21T17:20:35Z'
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
summary: 'The native gatifloxacin molecular graph and inspected exact chemical references
  agree. Two corrections are warranted: the CRyPTIC writer renders a source WHO designation
  as a concentration with mg/L units, and Tequin is typed as an exact synonym rather
  than a brand. All293 source measurements and membership counts reproduce. Qualified
  CARD assertions and the existing Salmonella parE evidence limitation remain appropriately
  bounded.'
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
  - path: data/antibiotics/antibacterial/gatifloxacin.yaml
    sha256: 1a31fc90aa55a35dd92173028d86b098c668f97699b6b58e7f1f36e9077af851
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
  - path: data/raw/aro_resistance_edges.tsv
    role: context
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
  - path: data/raw/aro_target_edges.tsv
    role: context
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
  - path: curation/card_evidence_reviews.json
    role: context
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
  - path: scripts/card_evidence_reviews.py
    role: context
    sha256: f9ec8aff30066bf04b9c2757af7d6f5d179d045e57b9f3b352bbed0b851f50a8
  - path: data/raw/cryptic_activity.tsv
    role: context
    sha256: fa2fe5e5258328f10f9fe5724e4b74f354a98f5355bac68108ab28ffb17c7987
  - path: curation/cryptic_drug_map.tsv
    role: context
    sha256: 69643f9b5e6dfc91761a4541317de63c5dca565131f6a07a3193878d7f863a54
  - path: data/raw/cryptic_memberships.tsv.gz
    role: context
    sha256: f121fc3ac48a44a89931366d908877d833bd846d9690257583c5dbbdb8bd2601
  - path: data/raw/cryptic_isolates.tsv.gz
    role: context
    sha256: 7d51bf3032e295a56e2543f52f12e59d6a8589ad6f2208e2314a154e6e8cf2c5
  - path: scripts/cryptic_membership_inventory.py
    role: context
    sha256: b0d8ae24cac64dfb2813bfa5a5ef590e3330e3c5ace82e25f3528b025147d6cc
  - path: src/antibioticmech/activity_memberships.py
    role: context
    sha256: 22849043b741d7a48a708dfade09524a11ac46afa7efb08d350ec7422ec2e146
  - path: data/antibiotics/antibacterial/membership-9c04e181212b9a3259e6973b7e175d2bb3836a1e5489f7ee4dcee1b68b2e976e.json.gz
    role: context
    sha256: 9c04e181212b9a3259e6973b7e175d2bb3836a1e5489f7ee4dcee1b68b2e976e
targets:
- target_id: CHEBI:5280
  path: data/antibiotics/antibacterial/gatifloxacin.yaml
  label: gatifloxacin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI identity, structure, ontology, xrefs and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ChEBI and ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated native field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding and exclusion decisions
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO antibiotic/class source
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Qualified CARD resistance assertions
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Qualified CARD molecular target assertion
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Maintained CARD evidence qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: CARD qualification application
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/cryptic_activity.tsv
    role: Grouped CRyPTIC DST source
  - repository: CultureBotAI/AntibioticMech
    path: curation/cryptic_drug_map.tsv
    role: Exact CRyPTIC compound mapping
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/cryptic_memberships.tsv.gz
    role: Adopted CRyPTIC membership inventory
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/cryptic_isolates.tsv.gz
    role: Adopted CRyPTIC isolate inventory
  - repository: CultureBotAI/AntibioticMech
    path: scripts/cryptic_membership_inventory.py
    role: Membership generation and source integrity
  - repository: CultureBotAI/AntibioticMech
    path: src/antibioticmech/activity_memberships.py
    role: Membership collection semantics and validation
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/membership-9c04e181212b9a3259e6973b7e175d2bb3836a1e5489f7ee4dcee1b68b2e976e.json.gz
    role: Native generated membership payload
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position490; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:5280
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:5280
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    490
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:5280
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/gatifloxacin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:5280
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/gatifloxacin.yaml --out /private/tmp/am-review-session/490-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: cryptic-memberships
  name: Dedicated adopted CRyPTIC membership integrity
  status: passed
  required: true
  summary: Actual own049 audit exited0 across26 compounds,4012 groups and857940 memberships.
    No raw-release or rendered-page flags were used.
  target_ids:
  - CHEBI:5280
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just audit-cryptic-memberships
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
  - CHEBI:5280
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
  - CHEBI:5280
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
  - CHEBI:5280
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
  - CHEBI:5280
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
  - CHEBI:5280
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
  - CHEBI:5280
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
  - CHEBI:5280
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
  - CHEBI:5280
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
  - CHEBI:5280
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/gatifloxacin.yaml
  locator: Entire native YAML, all22 resistance rows, molecular target, ten activity
    groups, membership reference and eight history events
  accessed_at: '2026-10-21T17:19:34Z'
  support: supports
  summary: CHEBI:5280 is SEEDED and EXACT, neutral C19H22FN3O4, XUBOMFCQGDBHNK-UHFFFAOYSA-N.
    The methylpiperazine centre is unspecified. The native source-qualified mechanism
    is nucleic-acid synthesis inhibition from CHEBI:50750 with HOST_SHARED_TARGET
    scope. One CARD GyrA target is explicitly PRIMARY_EVIDENCE_NEEDED; resistance
    entries explicitly retain database tier. No primary target experiment, protein
    example, producer or causal graph is asserted. Ten CRyPTIC DST groups contain
    source R/S categories, not numerical MICs.
- evidence_id: owners
  kind: record_content
  reference: 490-source-rows.json; 490-inspect.json
  locator: Complete adopted ChEBI/ARO, resistance, target, drug mapping and grouped
    CRyPTIC rows; actual writer and qualification ownership
  accessed_at: '2026-10-21T17:19:34Z'
  support: supports
  summary: ChEBI supplies molecular identity and definition; ARO supplies class, merged
    names/exact links,22 resistance edges and one target. The maintained card_evidence_reviews
    overlay adds the explicit Salmonella parE limitation. GFX maps exactly to the
    parent gatifloxacin concept, with a documented racemic-drug mapping boundary.
    CRyPTIC grouping/membership writers supply ten observations and the content-addressed
    artifact. All25 captured inputs preserve the original13.
  snapshot_sha256: df1d0cedeea0972e6901f4a33ecf8bd9bb8bffc44ecaf035a1a2c8d73f3b6497
- evidence_id: chemistry
  kind: validation
  reference: 049-root-authority-chemistry.json; 490-chemistry.json
  locator: Eleven independent native/current-authority forward encodings
  accessed_at: '2026-10-21T17:19:34Z'
  support: supports
  summary: Native SMILES/InChI, current ChEBI, PubChem name and exact CID5379, CHEMBL31
    and KEGG C07661 molfile all reproduce the full native key and formula, neutral
    charge and unspecified tetrahedral centre. No water or counterion is encoded.
    The unspecified graph is not itself a proof of racemic bulk composition.
  snapshot_sha256: 708b390e6a3a9b13adf021f4f7291c2bf9623e2db88a5b188c1c6d9533361d36
- evidence_id: authority
  kind: authority
  reference: CHEBI:5280; CHEBI:23765,26512,37143,46848,86324,33281,50750; ARO:3000659
  locator: Current compound, parent and role entries; drug/document identity lookups
  accessed_at: '2026-10-21T17:19:34Z'
  support: supports
  summary: Quinolone, quinolinemonocarboxylic acid, organofluorine, N-arylpiperazine
    and quinolone-antibiotic classifications fit. CAS112811-59-3 is corroborated by
    chemical/drug entries. DrugBankDB01044, DrugCentral1280 and KEGG D08011 resolve
    to gatifloxacin under broader drug association semantics; related products/hydrates
    are not exact free-base assertions. Gmelin2281206, Reaxys7445861 and legacy LINCSLSM-5139
    remain source-attributed without independent complete registry inspection. Wikipedia
    resolves the compound topic and is not primary scientific evidence.
  snapshot_sha256: 9aa857510ac2e0ef233336096246fae2f28acb6de813e772b3ec6573db2efab0
- evidence_id: adopted
  kind: primary_source
  reference: PMID:10737746,12190308,12620077,12873512,12904069,15125930,15745831,15911273,16078842,16337791;
    PMID:8522459
  locator: All ten ChEBI-adopted and the ARO compound-adopted complete indexed abstracts
  accessed_at: '2026-10-21T17:19:34Z'
  support: supports
  summary: 10737746 concerns MIC prediction;12190308,12873512,15745831 and15911273
    concern host hERG models;12620077 and12904069 examine other synthesized quinolones;15125930
    concerns anti-Toxoplasma analogues;16078842 concerns chiral nadifloxacin salts;16337791
    concerns isothiazoloquinolones. These do not independently prove exact gatifloxacin
    bacterial binding. Original8522459 directly tests AM-1155 against clinical isolates
    and experimental mouse infections, supporting antibacterial context but not a
    unique purified-target mechanism.
  snapshot_sha256: 0d488483ef99784569dadd47f909b6e870a0d4a1c849c8a99c9e74b24e42b486
- evidence_id: aro
  kind: authority
  reference: 490-current-aro-terms.json; https://purl.obolibrary.org/obo/aro.obo
  locator: Complete current compound/class/target and all22 determinant stanzas
  accessed_at: '2026-10-21T17:19:34Z'
  support: supports
  summary: 'All22 exact gatifloxacin resistance relationships persist in current ARO:
    one qnr target-protection assertion and21 target-alteration assertions. The GyrA
    targeted_by_antibiotic relationship also persists. Current source agreement verifies
    database provenance, not uniform primary support for every species, allele or
    compound. The native source-tier language and existing parE qualification must
    not be upgraded or silently discarded.'
  snapshot_sha256: fbe063e6d32db763071e0adfe8ccac2e8638fad215b725093693b86d0f0bf919
- evidence_id: aro-leads
  kind: primary_source
  reference: 490-current-aro-leads-0.json through 490-current-aro-leads-3.json
  locator: All50 current ARO-linked discovery records;49 complete available abstracts
    and one metadata-only record
  accessed_at: '2026-10-21T17:19:34Z'
  support: supports
  summary: PM15282231 has no abstract. Other supplied abstracts were read, including
    reviews and related-drug studies. Exact gatifloxacin appears in selected M.tuberculosis
    enzyme/clinical-isolate work, S.aureus comparative quinolone testing and C.difficile
    selection/surveillance experiments. Many E.coli, Bartonella, M.leprae, Ureaplasma,
    Morganella and Mycoplasma leads instead test ciprofloxacin, ofloxacin or other
    quinolones, and some describe unvalidated polymorphisms. PMID36010006 primarily
    studies sulbactam-durlobactam, while35944069 and30337678 are data/platform studies.
    Cross-drug, class-wide or review evidence is not promoted to exact gatifloxacin
    resistance proof. PMID27847014 specifically concerns ofloxacin-resistant M.tuberculosis.
  snapshot_sha256: fbdcbee0f716f8af2b69ac45fdf0497c729f17ecb86524a441063d99a17602c5
- evidence_id: primary1998
  kind: primary_source
  reference: PMID:9756776; DOI:10.1128/AAC.42.10.2678; https://journals.asm.org/doi/10.1128/aac.42.10.2678
  locator: Independent co-review of primary abstract, Table1 and selected compound/strain/enzyme/decatenation
    methods
  accessed_at: '2026-10-21T17:19:34Z'
  support: supports
  summary: Gatifloxacin was synthesized by Kyorin. Reconstituted S.aureus MS5935 GrlA/GrlB
    topoisomeraseIV, affinity-purified E.coli NIHJ JC-2 gyrase and separately prepared
    HeLa topoisomeraseII gave IC50 values13.8,0.109 and265µg/mL respectively. These
    distinct preparations support antibacterial topoisomerase action and assay-specific
    bacterial selectivity while retaining measurable host-family inhibition. They
    do not prove isolated GyrA binding, identical target preference across species
    or clinical safety.
  snapshot_sha256: 5132e0c05046ef1fee7b938402cb82aa2e007a2364bcf6ef5e8b5c5e08703417
- evidence_id: primary2001
  kind: primary_source
  reference: PMID:11709337; DOI:10.1128/AAC.45.12.3544-3547.2001
  locator: Independent co-review of complete abstract and primary material/strain/MIC/reconstitution/supercoiling/decatenation
    methods
  accessed_at: '2026-10-21T17:19:34Z'
  support: supports
  summary: The S.aureus MS5935 comparison used GrlA Ser80Phe and GyrA Ser84Leu mutants,
    agar-dilution MICs and reconstituted holoenzymes. It classifies gatifloxacin as
    dual-targeting in that tested system. The original numerical gatifloxacin table
    row was not independently recovered and is not adopted. Holoenzyme inhibition
    and mutant susceptibility do not automatically prove a binding site on an isolated
    subunit.
  snapshot_sha256: 9ca85242f4f2ea7a50a3b852f2cb41cafdcc7f01fdff9ac7980e10b1783d7138
- evidence_id: pare
  kind: primary_source
  reference: PMID:19104017; DOI:10.1128/AAC.01005-08; https://pureadmin.qub.ac.uk/ws/portalfiles/portal/5282229/Multiple_Regulatory_Pathways_Associated_with_High_Level_Cipro_oxacin.pdf
  locator: Independent co-review of original strain/selection/susceptibility/complementation
    methods, relevant Results/Discussion and visually inspected Tables1/3
  accessed_at: '2026-10-21T17:19:34Z'
  support: supports
  summary: Table1 concerns nalidixic acid/ciprofloxacin. Both5408-cip and its wild-type-parE
    complement retain ciprofloxacin MIC>32µg/mL; gyrA/gyrB complements lower susceptibility
    endpoints in the tested backgrounds. The authors leave indirect parE contribution
    unresolved. Table3 concerns four nonquinolones and includes neither a parE-specific
    comparison nor gatifloxacin. An ignored-inclusive whole downloaded-text search
    found no gatifloxacin mention. This supports the existing native qualification,
    not universal parE inactivity or deletion of every inherited serovar/drug assertion.
  snapshot_sha256: 3281d8f94f69709393c506e6739a9a78bab73487634ff2aa264fcfe257a9ebf2
- evidence_id: adapter
  kind: database
  reference: 490-adapter-results.json; 475-imodulon-datasets.json
  locator: Covered-dataset catalog and thirteen actual gene searches across six covered
    organisms
  accessed_at: '2026-10-21T17:19:34Z'
  support: supports
  summary: Searches in E.coli precise1k, M.tuberculosis modulome, S.aureus staph_precise108,
    S.enterica core, A.baumannii precise139 and S.pneumoniae precise718 returned relevant
    gyrA/gyrB/parC/parE annotations and no iModulons. Gene examples include E.coli
    b2231/b3019/b3030, M.tuberculosis Rv0006/Rv0005 and S.pneumoniae SP_0855. Broad
    gyrA search results also include other gyrase-associated genes and are not all
    exact gyrA hits. The other native taxa are outside this catalog; no missing result
    is treated as biological absence or binding/resistance evidence.
  snapshot_sha256: 331561195145eee1a3e98c674d1001afefe0358f5a09558ce3a2d9a4df69a085
- evidence_id: cryptic
  kind: primary_source
  reference: DOI:10.5281/zenodo.15680920; https://zenodo.org/records/15680920/files/DST_MEASUREMENTS.parquet?download=1
  locator: All293 exact GFX rows in previously fetched pinned original DST parquet,
    compared with adopted activity/membership/isolate inventories
  accessed_at: '2026-10-21T17:19:34Z'
  support: supports
  summary: The original parquet MD5 is45b4501ea7c3925af565dbbc6188dec0, SHA256a3159a5e4ce0f4d51d61a31be2b5b45fce1e1f5185e8988cb36a4d57826910b2.
    All ten group counts reproduce:1,3,1,3,44,9,126,3,34,69. There are16 source-resistant
    and277 source-susceptible measurements; every group has MEDIUM quality and no
    MIC value. The final WHO2019 group comprises69 distinct source isolates with METHOD_CC=WHO
    and phenotypeS. This does not provide a numeric concentration, a universal susceptibility
    judgment, exact reagent-form proof or an independently validated clinical breakpoint.
  snapshot_sha256: 5d648ee84fe29ce41f8f0b9e5a57a52b3e847d4c3f8b772545cb9b0f5a54ffdc
- evidence_id: membership
  kind: validation
  reference: 490-membership-independent.json; 490-membership-gate.json
  locator: Independent complete payload/hash/digest/raw-DST and adopted sequencing-registry
    join audit
  accessed_at: '2026-10-21T17:19:34Z'
  support: supports
  summary: The native artifact has SHA2569c04e181212b9a3259e6973b7e175d2bb3836a1e5489f7ee4dcee1b68b2e976e,5114
    compressed and55036 uncompressed bytes. All ten observation digests and293 subjects/memberships/measurements
    agree;142 subjects have adopted sequencing links and151 have null links. All293
    group-isolate counts match original DST data, and adopted membership/isolate-registry
    joins match. Original WGS parquet was not redownloaded, so sequencing links are
    validated against adopted registries rather than independently against that original
    WGS file.
  snapshot_sha256: 4533a2d63710a7a96a17ab76cd52783e7e8e13f02e96ff4e2c13003d398b4395
- evidence_id: writer
  kind: record_content
  reference: scripts/seed_from_sources.py:2661
  locator: cryptic_activity_assay, especially lines2676–2677
  accessed_at: '2026-10-21T17:19:34Z'
  support: supports
  summary: The writer appends critical concentration and mg/L to every nonempty method_cc
    token without checking whether it is numeric. Thus the preserved raw designation
    WHO becomes critical concentration WHO mg/L at activity_spectrum[9].assay. Native
    evidence notes retain method_cc=WHO, exposing the source/representation distinction.
    Correcting the assay changes its observation digest and requires consistent regeneration
    of the membership artifact/reference.
- evidence_id: brand
  kind: authority
  reference: https://www.accessdata.fda.gov/drugsatfda_docs/nda/99/21061_Tequin_prntlbl.pdf
  locator: Actual original1999 FDA label scan, PDFpage2/printedpage1 viewed
  accessed_at: '2026-10-21T17:19:34Z'
  support: supports
  summary: The label presents TEQUIN as the product name for gatifloxacin tablets/injection
    and describes racemic gatifloxacin sesquihydrate, formula C19H22FN3O4·1.5H2O and
    mass402.42. Native synonym8 types Tequin as EXACT_SYNONYM rather than BRAND_NAME.
    Product identity and hydration do not invalidate the anhydrous parent graph; this
    historical label does not establish current marketing status or a treatment recommendation.
  snapshot_sha256: ed4cf8bf897d91a463e128fb0994c6520e8489e1788695cbd1d1f3d4c2742458
- evidence_id: patents
  kind: primary_source
  reference: https://patents.google.com/patent/EP0230295A2/en; https://patents.google.com/patent/US4980470A/en
  locator: Independent co-review of exact Examples3/14, adjacent compound scope and
    analytical description
  accessed_at: '2026-10-21T17:19:34Z'
  support: supports
  summary: Both patents explicitly synthesize the gatifloxacin connectivity with7-(3-methyl-1-piperazinyl)
    and8-methoxy groups. The analyzed examples are hemihydrate C19H22FN3O4·1/2H2O,
    so these are relevant document associations rather than proof of exact anhydrous
    experimental material or a resolved piperazine stereoisomer. No family-wide potency
    is transferred.
  snapshot_sha256: 12dccdac3981eb1d3399ba4d6e91f012c179355cc7f1aed50fc763b8d11f4de5
- evidence_id: search
  kind: search
  reference: 490-local-hits.txt; 049-root-fetch1-manifest.json through 049-root-fetch7-manifest.json;
    490-independent-audit-manifest.json
  locator: Ignored-inclusive local source search and actual bounded public authority/original-paper
    attempts
  accessed_at: '2026-10-21T17:19:34Z'
  support: context_only
  summary: The initial local search and exact owner checks include hidden/ignored
    files. Current public authorities and all adopted abstracts were read; selected
    primary follow-up has the depths recorded above. Zenodo public page/API attempts
    returned403, while the previously fetched pinned original DST parquet was available
    locally. PMC challenge pages and metadata-only efetch responses are not full-text
    successes.
  search_scope: 2026-10-21; rg --no-ignore --hidden in own049 tree; ChEBI/PubChem/ChEMBL/KEGG,
    exact ARO stanzas and50 PMID records, official FDA label, public publisher/QUB
    originals, source parquet and adopted membership registries.
  snapshot_sha256: bd1165b5709067013d49fe568701fc7fe57f6c8a6293371bc010081ceaf82a5d
assessments:
- assessment_id: identity
  area: identity
  topic: Exact molecule and structural classification
  outcome: supported
  summary: The native graph, source systematic names, parent terms and independently
    parsed exact public structures agree. Pharmaceutical hydration and unspecified
    molecular stereochemistry remain separate concepts.
  target_ids:
  - CHEBI:5280
  evidence_ids:
  - native
  - chemistry
  - authority
  - brand
- assessment_id: assay
  area: consistency
  topic: Nonnumeric source metadata rendered as concentration
  outcome: concern
  summary: WHO is a categorical source token, not a numerical amount. Appending mg/L
    creates unsupported quantitative-looking assay information for69 measurements
    even though their source susceptibility category is faithfully preserved.
  target_ids:
  - CHEBI:5280
  evidence_ids:
  - cryptic
  - writer
  - membership
- assessment_id: names
  area: nomenclature
  topic: Tequin product semantics
  outcome: concern
  summary: The official historical product label supports retaining Tequin as a brand
    association, not exact chemical-name equivalence.
  target_ids:
  - CHEBI:5280
  evidence_ids:
  - native
  - brand
- assessment_id: targets
  area: evidence
  topic: Topoisomerase mechanism and qualified target
  outcome: supported
  summary: Original enzyme studies support bacterial type-II-topoisomerase action
    with species/preparation scope. The native direct-GyrA assertion remains explicitly
    database-tier and PRIMARY_EVIDENCE_NEEDED; no isolated-subunit binding proof or
    equal host potency is inferred.
  target_ids:
  - CHEBI:5280
  evidence_ids:
  - native
  - aro
  - primary1998
  - primary2001
  - adapter
- assessment_id: resistance
  area: evidence
  topic: All22 resistance assertions and parE qualification
  outcome: unknown
  summary: All exact ARO edges persist, but current-linked primary abstracts do not
    uniformly establish exact-drug/allele causality. The inspected Salmonella original
    confirms why its native parE claim is qualified. Related-drug resistance, class-wide
    reviews and unvalidated mutations are not silently upgraded.
  target_ids:
  - CHEBI:5280
  evidence_ids:
  - aro
  - aro-leads
  - pare
  - adapter
  - owners
- assessment_id: activity
  area: evidence
  topic: Grouped source phenotypes and membership fidelity
  outcome: supported
  summary: All293 source measurements and group-isolate counts reproduce; the existing
    membership artifact and adopted joins are internally valid. Source R/S values
    and reported critical-concentration metadata are not MIC measurements or species-wide
    susceptibility.
  target_ids:
  - CHEBI:5280
  evidence_ids:
  - cryptic
  - membership
  - native
- assessment_id: provenance
  area: provenance
  topic: All owners, citations and history
  outcome: supported
  summary: The entire native record, original and appended25 hashes, eight history
    events, complete adopted compound citation list and actual source/writer lanes
    were assessed. Drug/document links preserve their broader contracts.
  target_ids:
  - CHEBI:5280
  evidence_ids:
  - owners
  - adopted
  - patents
  - search
  - membership
- assessment_id: completeness
  area: completeness
  topic: Optional enrichment and limits
  outcome: unknown
  summary: No missing optional clinical, producer, protein-example or causal object
    is itself a defect. Future primary target/resistance curation requires exact species,
    strain, allele, material and assay proof; current source qualifications remain
    valuable.
  target_ids:
  - CHEBI:5280
  evidence_ids:
  - native
  - aro-leads
  - primary1998
  - pare
findings:
- finding_id: F1
  issue_key: gatifloxacin-cryptic-who-token-as-mg-per-l-concentration
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Do not attach concentration units to the CRyPTIC WHO designation
  description: The69-measurement WHO2019 source group dst_measurements:0600668ff179a303
    carries literal method_cc=WHO and source phenotypeS. The writer turns this into
    critical concentration WHO mg/L. No numeric concentration or MIC is supplied for
    these rows, and neighboring2.0mg/L groups cannot supply the missing value. Source
    phenotype and membership content remain valid.
  target_ids:
  - CHEBI:5280
  field_paths:
  - activity_spectrum[9].assay
  evidence_ids:
  - native
  - cryptic
  - writer
  - membership
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Critical-concentration prose and observation emission
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/cryptic_activity.tsv
    role: Preserved source method token
  - repository: CultureBotAI/AntibioticMech
    path: scripts/cryptic_membership_inventory.py
    role: Membership generation and observation identity
  - repository: CultureBotAI/AntibioticMech
    path: src/antibioticmech/activity_memberships.py
    role: Artifact/digest semantics
  rule_id: Preserve assay units and source measurement semantics
  native_severity: major
  normalization_reason: The generated assay misrepresents nonnumeric metadata as a
    concentration for a defined observation cohort.
- finding_id: F2
  issue_key: gatifloxacin-tequin-exact-synonym-product-name
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: Retain Tequin as a brand name
  description: Native synonym8 types Tequin as EXACT_SYNONYM. The official FDA product
    label identifies TEQUIN tablets/injection and describes gatifloxacin sesquihydrate.
    The searchable product name belongs under BRAND_NAME; this is not a reason to
    replace the parent molecular graph with the product hydrate.
  target_ids:
  - CHEBI:5280
  field_paths:
  - synonyms[8].synonym_type
  evidence_ids:
  - native
  - brand
  - owners
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Imported Tequin synonym
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Synonym typing and emission
  rule_id: Product versus exact chemical name semantics
  native_severity: minor
  normalization_reason: Localized alias-type correction with intact compound identity.
actions:
- action_id: A1
  description: Handle numeric and nonnumeric critical-concentration metadata separately
    in maintained emission.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:5280
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Critical-concentration prose and observation emission
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/cryptic_activity.tsv
    role: Preserved source method token
  - repository: CultureBotAI/AntibioticMech
    path: scripts/cryptic_membership_inventory.py
    role: Membership generation and observation identity
  - repository: CultureBotAI/AntibioticMech
    path: src/antibioticmech/activity_memberships.py
    role: Artifact/digest semantics
  acceptance_checks:
  - Preserve literal WHO and the sourceS phenotype. Render the token as a source designation
    without concentration units, or leave the numeric concentration unspecified. Never
    impute2.0mg/L from adjacent rows.
  - Regenerate observations, digests and content-addressed membership/reference consistently
    through supported writers; retain all293 measurement and isolate joins and existing
    source provenance.
  - Run focused native validation, corpus reproduction, dedicated membership audit
    and required QC. Add a meaningful regression covering a nonnumeric method_cc token
    if implementation is separately authorized.
- action_id: A2
  description: Preserve Tequin with BRAND_NAME typing through maintained ARO name
    handling.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:5280
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Imported Tequin synonym
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Synonym typing and emission
  acceptance_checks:
  - Retain the source spelling and provenance while changing only its semantic name
    type; do not equate historical product hydration with the parent chemical graph.
  - Regenerate and verify native schema/strict, source history and reproducibility.
limitations:
- All11 compound-adopted abstracts and all50 current ARO discovery records were assessed;49
  of the latter supplied abstracts and PMID15282231 was metadata only. The source-supplied
  PMID3311572 abstract is itself truncated. Not all50 original papers were read in
  full.
- The1998 and2001 mechanism originals were inspected at the specific selected-table/method
  depths stated by an independent co-reviewer. Browser excerpts are not full-paper
  snapshots; unsuccessful PMC/EPMC routes remain explicit.
- The Salmonella publisher PDF was inspected in relevant methods/results/discussion
  and actual Tables1/3; not every figure or supplement was reviewed. No exact gatifloxacin
  result is inferred from its ciprofloxacin and other-drug experiments.
- All293 original DST joins were checked. The142 sequencing mappings were compared
  with adopted isolate/membership registries, not independently with an original WGS
  parquet. No UKMYC row belongs to this target.
- The WHO source token does not establish an amount; original source R/S categories
  are retained without independent breakpoint adjudication. No source observation
  is a numeric MIC and source-material stereochemical/hydrate purity was not established.
- Gmelin, Reaxys and LINCS accessions remain source-attributed. Historical FDA label
  and patent preparations are document/product evidence, not proof of current approval
  or exact anhydrous assay material.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Root assessed the entire native/source record, all stated indexed abstracts and
  independent chemistry; delegated reviewers independently audited original mechanism/patent
  material and complete CRyPTIC membership reconstruction. Their exact reading depths,
  retrieval receipts and hashes are retained.
- No native, source, qualification overlay or membership artifact was edited. All25
  input hashes remain unchanged, preserving the original13.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
