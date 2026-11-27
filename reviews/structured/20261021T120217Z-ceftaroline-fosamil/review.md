# Ceftaroline fosamil: exact prodrug identity and four verified FDA assertions

- Review: 20261021T120217Z-ceftaroline-fosamil
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T11:48:59Z
- Finished UTC: 2026-10-21T12:02:17Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

No confirmed native defect. Native unsolvated fosamil structure and CAS/GSRS complete identities agree. All four FDA product assertions match official application/product facts and the exact GSRS prodrug identity. Clinical products use formulated monoacetate monohydrate with dose expressed as fosamil; active-ceftaroline antibacterial results remain distinct from prodrug administration and direct target claims. Every adopted lead is disposed at its inspected depth. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole-record review of exact ceftaroline fosamil, including four populated FDA clinical assertions.

Selection: Queue 252 in isolated batch 026; original inputs preserved and FDA source/extractor owner hashes appended before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:70718 | data/antibiotics/antibacterial/ceftaroline-fosamil.yaml | generated | ceftaroline fosamil |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | CHEBI:70718 | Actual focused command passed with zero errors. |
| Focused strict | passed | True | CHEBI:70718 | Actual focused command passed with zero errors. |
| Supplemental chemistry | passed | False | CHEBI:70718 | Actual command passed; complete native/CAS/GSRS identity and formula agree. |
| Supplemental xref-comparison | passed | False | CHEBI:70718 | Actual command passed; complete native/CAS/GSRS identity and formula agree. |
| Authoritative full QC | failed | True | CHEBI:70718 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:70718 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:70718 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:70718 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:70718 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:70718 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:70718 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:70718 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:70718 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact unsolvated fosamil graph and names

identity: supported. Targets: CHEBI:70718.

Complete key, formula, charge, masses, 6R,7R and Z oxime, exact systematic name and source mint agree.

### Six structural parents and antibacterial roles

grounding: supported. Targets: CHEBI:70718.

Parents fit the graph. Native definition explicitly places broad-spectrum/MRSA activity on the active ceftaroline context and calls fosamil its N-phospho prodrug. Prodrug-mediated antibacterial use is supported.

### Four FDA assertions and summary status

evidence: supported. Targets: CHEBI:70718.

Both NDA 200327 and ANDA 208075 products 001/002, original dates, sponsors, names, Prescription status and AP approval agree. Exact UNII/GSRS full key matches native; current version 36 does not invalidate captured version 33. Product material remains a formulated hydrate.

### Typed drug and documentary mappings

grounding: supported. Targets: CHEBI:70718.

CAS exact identity, DrugCentral drug context and native MX patent/family relevance verified. Reaxys proprietary content remains uninspected; no assay transfer from document existence.

### All ten adopted PMID dispositions

evidence: supported. Targets: CHEBI:70718.

Clinical trials, pooled safety, animal efficacy, pharmacodynamic discussion and review/commentary leads are separately bounded. Historical preapproval prose is not used for current status. No overlapping trial population is counted as an independent experiment.

### Active metabolite versus administered prodrug

evidence: supported. Targets: CHEBI:70718.

Active-ceftaroline in vitro observations support only the metabolite clause; fosamil in vivo/clinical regimens support prodrug treatment context. No direct native-prodrug numeric assay object is populated.

### Unpopulated direct protein claims

evidence: not_applicable. Targets: CHEBI:70718.

No native PBP or other protein target exists. Review/database PBP prose cannot establish direct fosamil binding; activation is retained as a separate pharmacological relationship.

### Structured source applicability

scope: not_applicable. Targets: CHEBI:70718.

Native record names no gene/protein/pathway or transcriptomics dataset. MRSA is an organism/phenotype context, not a named molecular target requiring an expression-module adapter query.

### Resistance, producer, datasets and graph

scope: not_applicable. Targets: CHEBI:70718.

No native populated assertions in these optional domains. FDA approval does not establish a natural producer or causal graph.

### Actual source ownership and history

provenance: supported. Targets: CHEBI:70718.

ChEBI and FDA/GSRS owners captured before judgment, full-key join inspected, six history events and original hashes preserved. Scientific curation status remains SEEDED.

### Focused and independent checks

schema: supported. Targets: CHEBI:70718.

Native schema/strict and supplemental chemistry pass; regulatory and scientific source review remains independently documented.

### Optional evidence enrichment

completeness: supported. Targets: CHEBI:70718.

No required-field defect established. Target/activity additions need active-metabolite versus prodrug and exact preparation qualification.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optionally enrich prodrug/clinical evidence without conflating formulations and active drug.

- Keep exact GSRS substance identity and dated FDA assertions separate from complete monoacetate-monohydrate/L-arginine product composition.
- Inspect full original methods before adding quantitative strain/model claims from abstract-only leads; distinguish CANVAS trial cohorts from pooled safety.
- Assign active-ceftaroline PBP/MIC evidence to the active molecule and represent prodrug activation explicitly rather than asserting direct fosamil binding.
- Preserve source-owned identities/history and run applicable schema/strict, term/reference/history and corpus checks after any separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/ceftaroline-fosamil.yaml; Entire YAML | supports | Read seeded/exact identity, detailed chemical/prodrug/activity/clinical definition, four synonyms, six parents, two roles, full structure, CAS/Reaxys and DrugCentral mappings, patent/Wikipedia documents, ChEBI concept, approved summary and all four complete clinical assertions, plus six history events. No native activity, target, resistance, producer, dataset or graph objects. |
| owners | data/raw/chebi_antimicrobials.tsv;data/raw/fda_clinical_status.tsv; Entire ChEBI row 1811 and FDA rows 3684–3687 | supports | ChEBI owns chemical identity and ten adopted leads. FDA rows own NDA 200327 products 001/002 and ANDA 208075 products 001/002, all using UNII 7P6FQA5D21 and the native complete key. Original captures preserved; actual FDA owner/extractor added before assessment. |
| extractor | scripts/extract_fda_clinical_status.py; compact_substance and match_products | supports | Extractor derives full Standard InChIKey from GSRS chemical SMILES and joins exact complete corpus keys; it rejects ambiguous or connectivity-only matches. Thus the clinical join is substance-level and does not claim a vial lacks hydrate/counterion/excipients. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Identity, Equivalence, Evidence standard and clinical provenance | supports | Exact source identity, dated regulatory status and claim-level material scope are separate checks. No missing optional object alone establishes a defect. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:70718; Current full identity, exact systematic name, definition and six structural parents | supports | Current native graph and complete key agree. Cephalosporin, iminium betaine, oxime O-ether, organic phosphoramidate, thiadiazole and 1,3-thiazole parents fit. The definition explicitly identifies fosamil as the N-phospho prodrug of active ceftaroline; additional live roles are not required additions. |
| chemistry | RDKit 2026.03.5 molecular check; 252-chemistry.json | supports | Both native encodings reproduce ZCCUWMICIWSJIX-NQJJCJBVSA-N, C22H21N8O8PS4, net zero charge, one fragment, masses and core R,R; the Z oxime and source mint agree. |
| cas | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/229016-73-3/JSON; CAS-resolved CID 9852981 | supports | Exact unsolvated fosamil identity, complete key and formula match; acetate/water components are absent. |
| drugcentral | https://drugcentral.org/drugcard/4169; Identity, formula and drug aliases | supports | DrugCentral 4169 names ceftaroline fosamil with native formula and includes acetate/hydrate aliases. This is drug-level aggregation. Its active-ceftaroline PBP prose is not direct fosamil target evidence. |
| gsrs | https://gsrs.ncats.nih.gov/api/v1/substances/7P6FQA5D21; Current approved chemical substance, version 36, full structure | supports | UNII 7P6FQA5D21 has the native complete key, formula and 6R,7R/Z specification. Both current molfile and SMILES independently regenerate the complete native key despite alternate phosphate/carboxyl proton location. Native identity_record_version 33 is a dated retrieval snapshot, not a claim that current GSRS remains version 33. |
| fda-200327 | https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&amp;ApplNo=200327; Native referenced application page: product table and original approval | supports | Official page confirms ABBVIE Teflaro 400/600 mg per vial, prescription IV powder and original approval 2010-10-29. These correspond to the two native NDA assertions. Marketing status is a regulatory category, not proof of immediate inventory availability. |
| fda-208075 | https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&amp;ApplNo=208075; Native referenced application page: product table and original approval | supports | Official page confirms APOTEX ceftaroline fosamil 400/600 mg per vial, prescription IV powder and original approval 2021-09-21, corresponding to both native ANDA assertions. |
| fda-products | https://api.fda.gov/drug/drugsfda.json?search=application_number:NDA200327&amp;limit=1; Current openFDA NDA result, products 001/002 and original submission | supports | Product 001 is 400 mg/vial and 002 is 600 mg/vial; names, sponsor, prescription status and original AP submission/date match native. No discontinued product is substituted. |
| fda-generic-products | https://api.fda.gov/drug/drugsfda.json?search=application_number:ANDA208075&amp;limit=1; Current openFDA ANDA result, products 001/002 and original submission | supports | Both numbered APOTEX products and 2021-09-21 original AP approval agree. The asserted summary status APPROVED is consistent with these current product records and their captured source history. |
| label | https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=3ecde48b-75a2-4beb-9999-369f3f61bb8a; Official Teflaro sections 1.1, 11, 12.3 and 14.1 | supports | Confirms adult ABSSSI use, fosamil conversion to bioactive ceftaroline, and manufactured monoacetate monohydrate plus L-arginine. Dose is expressed as 600/400 mg anhydrous fosamil, corresponding to 668/446 mg hydrate. The exact-substance FDA join is compatible with this product formulation; it does not make the unsolvated structure a complete vial representation. |
| patent | https://patents.google.com/patent/MX2012003411A/en; Native document abstract and explicit family/priority link | partial | Native MX document resolves to ceftaroline/prodrug compositions for bacterial infection and links to PCT/US2010/049659 / WO2011035305A1. The Spanish abstract and displayed English translation are relevant; this is not an unrelated patent identifier. Full native claims were not available in this rendering. |
| patent-family | https://patents.google.com/patent/WO2011035305A1/en; Linked original family description, preparation/formulation paragraphs and claims 1–17 | partial | Family text explicitly distinguishes ceftaroline, phosphono prodrug, anhydrous forms and monohydrate acetic-acid solvate, plus L-arginine formulations and anhydrous/acetic-acid-free dose basis. Claims concern formulations/regimens and PK. This supports document relevance with material distinctions; no independent direct target or exact isolated-fosamil MIC is assigned from the patent. |
| wiki | https://en.wikipedia.org/wiki/Ceftaroline_fosamil; Native document identity | context_only | The named drug document resolves. It is contextual and does not substitute for original primary experiments or official approval data. |
| adopted-21076711 | PMID:21076711; DOI 10.1358/dot.2010.46.10.1519172; complete abstract | context_only | Review summarizes spectrum, animal and human studies. Its statement that the drug was still under FDA review is historical publication context, superseded for current status by original approval records; it is not a contradiction in native dated clinical assertions. |
| adopted-21115453 | PMID:21115453; DOI 10.1093/jac/dkq253; complete abstract | partial | Pharmacodynamic discussion combines prior MIC collections, free-time-above-MIC endpoints, Monte Carlo target attainment and clinical data. It uses fosamil terminology around active-drug effects; without full methods it is not treated as a new isolated-prodrug PBP2a-binding measurement or a direct compound-specific MIC source. |
| adopted-21115456 | PMID:21115456; DOI 10.1093/jac/dkq256; complete abstract | context_only | Integrated CANVAS 1/2 safety analysis of 1378 treated patients reuses the two skin-infection trial cohorts. It is not a third independent efficacy experiment; results pertain to those regimens and follow-up periods. |
| adopted-21393213 | PMID:21393213; DOI 10.1093/jac/dkr019; complete abstract | partial | Original rabbit endocarditis model compares administered fosamil, daptomycin and tigecycline for four days against MSSA/MRSA/GISA strains. Vegetation bacterial reduction is an in vivo treatment endpoint after prodrug administration; it is not direct binding or proof of clinical endocarditis approval. Exact solid reagent and full strain/protocol details remain unresolved from abstract. |
| adopted-21115454 | PMID:21115454; DOI 10.1093/jac/dkq254; CANVAS 1 complete abstract | partial | Randomized adult cSSSI trial compares 600 mg ceftaroline fosamil every 12 hours with vancomycin plus aztreonam for 5–14 days. Clinical cure in the evaluable population was 91.1% versus 93.3%; this supports clinical use under study conditions. The abstract does not itself identify exact solid-state form; label material and dose mapping are separate evidence. |
| adopted-21115455 | PMID:21115455; DOI 10.1093/jac/dkq255; CANVAS 2 complete abstract | partial | Second randomized adult cSSSI trial uses the same named prodrug regimen and comparator; evaluable clinical cure was 92.2% versus 92.1%. It is clinical efficacy, not a purified binding or direct monohydrate MIC experiment. Exact solid preparation is not resolved from the abstract alone. |
| adopted-21162631 | PMID:21162631; DOI 10.2217/fmb.10.132; complete abstract | context_only | Drug-profile synthesis distinguishes prodrug from active ceftaroline and summarizes clinical data. It is contextual secondary discussion, not an additional independent primary target experiment. |
| adopted-21252841 | PMID:21252841; Medical Letter 2011;53(1356):5–6; metadata and publisher introduction | context_only | Europe PMC/PubMed supply no abstract. Public publisher issue page and introduction describe adult skin-infection and pneumonia approval, but full issue requires subscription and was not inspected. This is contextual drug commentary, not primary mechanism evidence; no title-only scientific assertion is adopted. |
| adopted-21482565 | PMID:21482565; DOI 10.1093/jac/dkr095; complete abstract | context_only | Overview/review of ceftaroline fosamil summarizes pharmacology, active-ceftaroline activity and clinical use. Its PBP affinity prose is not an original isolated-hydrate binding measurement. |
| adopted-21482566 | PMID:21482566; DOI 10.1093/jac/dkr096; FOCUS 1 complete abstract | partial | Randomized CAP trial compares 600 mg fosamil every 12 hours with ceftriaxone in hospitalized non-ICU PORT III/IV adults; both groups also receive two clarithromycin doses on day 1. Keep that co-therapy and pneumonia setting distinct from skin-infection trials and direct active-moiety activity. |
| active-primary | PMID:18625769; DOI 10.1128/AAC.00149-08; original Methods and Results inspected as additional lead | context_only | Methods explicitly assay active ceftaroline PPI-0903M lot M599-R1001 rather than fosamil. Results support the definition’s active-ceftaroline MRSA and broader antibacterial clause, with susceptibility limits for E. faecium and resistant Enterobacteriaceae. These MICs are not assigned to the prodrug. |
| synthesis-lead | PMID:12735989; DOI 10.1016/S0968-0896(03)00126-3; original abstract | partial | Original N-phosphono-prodrug study distinguishes TAK-599 compound 1 from active T-91825 compound 2a and reports rapid conversion in rats/monkeys. Exact solid form of compound 1 is unresolved at this access depth; active 2a potency is not transferred to direct prodrug binding. |
| activation-lead | PMID:15290453; DOI 10.1007/s10156-004-0309-3; original abstract | partial | Separates T-91825 in vitro activity from TAK-599 in vivo mouse efficacy. Supports prodrug-mediated antibacterial use with organism/model boundaries rather than direct unsolvated-prodrug target activity. |
| xref-check | Independent exact compound and FDA-identity comparison; 251252-xref-check.json; 252 section | supports | Native, CAS-resolved CID 9852981, current GSRS SMILES and GSRS molfile all regenerate ZCCUWMICIWSJIX-NQJJCJBVSA-N with the same formula. |
| local-search | Ignored-inclusive native/owner and free primary review; 252-owner-hits.txt;252-local-hits.txt;252-adopted.json | context_only | Exact label, ID, key and source provenance searched with ignored/hidden coverage outside .git/.venv. All ten adopted leads were disposed, relevant patent resolved, and each of four FDA assertions checked individually against current official records. |
| gates | Actual focused commands; 252-focused-results.json | supports | Native schema, strict and supplemental molecular helper each exit 0; independent exact identity comparison also passes. |

## Limits And Additional Notes

- Nine adopted leads had inspectable abstracts; PMID 21252841 was limited to metadata and previously inspected public publisher introduction. Full original clinical/animal methods were not inspected, and no paywalled source was purchased.
- Additional 2008 active-ceftaroline Methods/Results were inspected, but exact TAK-599 solid form remains unresolved in the additional synthesis/activation abstracts. No direct prodrug target assay is inferred.
- Native MX patent rendering exposes abstract and family links; relevant original family description/selected claims were inspected, not every native drawing, example or legal-status event.
- Independent proprietary Reaxys content was not inspected. Current official marketing status confirms regulatory category, not real-time commercial stock.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 22 expanded hashes unchanged, including FDA inventory/extractor; no native/source/status/history changes.
- Native validation used batch 026 environment; supplemental RDKit 2026.03.5 used existing batch 019 interpreter against batch 026 cwd.
- Official label, active-ceftaroline full text and public Medical Letter preview were inspected during immediately adjacent reviews; original source snapshots/access timestamps are retained where applicable. Free public sources only.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T120217Z-ceftaroline-fosamil
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Ceftaroline fosamil: exact prodrug identity and four verified FDA assertions'
started_at: '2026-10-21T11:48:59Z'
finished_at: '2026-10-21T12:02:17Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Independent complete native, ChEBI and FDA raw-owner review;
    all ten adopted PMID dispositions; current official FDA pages/API and GSRS complete
    structure; exact CAS comparison; native patent abstract and relevant family original
    description/claims; active-metabolite primary and original prodrug abstracts.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: No confirmed native defect. Native unsolvated fosamil structure and CAS/GSRS
  complete identities agree. All four FDA product assertions match official application/product
  facts and the exact GSRS prodrug identity. Clinical products use formulated monoacetate
  monohydrate with dose expressed as fosamil; active-ceftaroline antibacterial results
  remain distinct from prodrug administration and direct target claims. Every adopted
  lead is disposed at its inspected depth. Scientific assessment retains the stated
  evidence limits; full verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/ceftaroline-fosamil.yaml
    sha256: dcf3221d46d355e8d7408a6976a9a6a65b667f958ea4eeb40901dc6cf99a8a8c
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
  - path: data/raw/fda_clinical_status.tsv
    sha256: a6952f85426afa53c5704c588681a078e599ce245bf18f7c9dd390d70e7bb16c
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
  - path: scripts/extract_fda_clinical_status.py
    sha256: f30f385ea6d530dc1749e3d805dbcdbc8715fbc476abc510bf144ea13964e171
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
- target_id: CHEBI:70718
  path: data/antibiotics/antibacterial/ceftaroline-fosamil.yaml
  label: ceftaroline fosamil
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI identity, structure, definition, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/fda_clinical_status.tsv
    role: Adopted four FDA clinical assertions and exact GSRS identity
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: FDA/GSRS source extraction
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
  description: Whole-record review of exact ceftaroline fosamil, including four populated
    FDA clinical assertions.
  selection: Queue 252 in isolated batch 026; original inputs preserved and FDA source/extractor
    owner hashes appended before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:70718
  exclusions:
  - target: Acetate/hydrate material, active ceftaroline and complete formulated products
      as exact chemical equivalents
    reason: Related material and pharmacological states are qualified rather than
      conflated with the unsolvated prodrug.
checks:
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  summary: Actual focused command passed with zero errors.
  target_ids:
  - CHEBI:70718
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/ceftaroline-fosamil.yaml
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
  - CHEBI:70718
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/ceftaroline-fosamil.yaml --out /private/tmp/am-review-session/252-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Supplemental chemistry
  status: passed
  required: false
  summary: Actual command passed; complete native/CAS/GSRS identity and formula agree.
  target_ids:
  - CHEBI:70718
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/check199200.py
    252 (cwd /private/tmp/antibioticmech-record-reviews-026)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: xref-comparison
  name: Supplemental xref-comparison
  status: passed
  required: false
  summary: Actual command passed; complete native/CAS/GSRS identity and formula agree.
  target_ids:
  - CHEBI:70718
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/compare-251252.py
    (cwd /private/tmp/antibioticmech-record-reviews-026)
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
  - CHEBI:70718
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
  - CHEBI:70718
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
  - CHEBI:70718
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
  - CHEBI:70718
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
  - CHEBI:70718
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
  - CHEBI:70718
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
  - CHEBI:70718
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
  - CHEBI:70718
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
  - CHEBI:70718
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/ceftaroline-fosamil.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T11:57:20Z'
  support: supports
  summary: Read seeded/exact identity, detailed chemical/prodrug/activity/clinical
    definition, four synonyms, six parents, two roles, full structure, CAS/Reaxys
    and DrugCentral mappings, patent/Wikipedia documents, ChEBI concept, approved
    summary and all four complete clinical assertions, plus six history events. No
    native activity, target, resistance, producer, dataset or graph objects.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv;data/raw/fda_clinical_status.tsv
  locator: Entire ChEBI row 1811 and FDA rows 3684–3687
  accessed_at: '2026-10-21T11:57:20Z'
  support: supports
  summary: ChEBI owns chemical identity and ten adopted leads. FDA rows own NDA 200327
    products 001/002 and ANDA 208075 products 001/002, all using UNII 7P6FQA5D21 and
    the native complete key. Original captures preserved; actual FDA owner/extractor
    added before assessment.
- evidence_id: extractor
  kind: record_content
  reference: scripts/extract_fda_clinical_status.py
  locator: compact_substance and match_products
  accessed_at: '2026-10-21T11:57:20Z'
  support: supports
  summary: Extractor derives full Standard InChIKey from GSRS chemical SMILES and
    joins exact complete corpus keys; it rejects ambiguous or connectivity-only matches.
    Thus the clinical join is substance-level and does not claim a vial lacks hydrate/counterion/excipients.
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Identity, Equivalence, Evidence standard and clinical provenance
  accessed_at: '2026-10-21T11:57:20Z'
  support: supports
  summary: Exact source identity, dated regulatory status and claim-level material
    scope are separate checks. No missing optional object alone establishes a defect.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:70718
  locator: Current full identity, exact systematic name, definition and six structural
    parents
  accessed_at: '2026-10-21T11:53:37Z'
  support: supports
  summary: Current native graph and complete key agree. Cephalosporin, iminium betaine,
    oxime O-ether, organic phosphoramidate, thiadiazole and 1,3-thiazole parents fit.
    The definition explicitly identifies fosamil as the N-phospho prodrug of active
    ceftaroline; additional live roles are not required additions.
  snapshot_sha256: 1fecef284a670758d921a750e3cf296401b5324ea709ea72b08b2a15d9757abd
- evidence_id: chemistry
  kind: validation
  reference: RDKit 2026.03.5 molecular check
  locator: 252-chemistry.json
  accessed_at: '2026-10-21T11:53:19Z'
  support: supports
  summary: Both native encodings reproduce ZCCUWMICIWSJIX-NQJJCJBVSA-N, C22H21N8O8PS4,
    net zero charge, one fragment, masses and core R,R; the Z oxime and source mint
    agree.
  snapshot_sha256: 4c43d68f3b6c381b189a58ad778b14b7a47cbe358546b7f1cdb48ffaab5cec31
- evidence_id: cas
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/229016-73-3/JSON
  locator: CAS-resolved CID 9852981
  accessed_at: '2026-10-21T11:53:37Z'
  support: supports
  summary: Exact unsolvated fosamil identity, complete key and formula match; acetate/water
    components are absent.
  snapshot_sha256: 5a57084b0d1b0610aaef873bdf67788e1948f04a6998d1f8f4d1d3e82ad2bbe9
- evidence_id: drugcentral
  kind: database
  reference: https://drugcentral.org/drugcard/4169
  locator: Identity, formula and drug aliases
  accessed_at: '2026-10-21T11:53:38Z'
  support: supports
  summary: DrugCentral 4169 names ceftaroline fosamil with native formula and includes
    acetate/hydrate aliases. This is drug-level aggregation. Its active-ceftaroline
    PBP prose is not direct fosamil target evidence.
  snapshot_sha256: 8f2b00374e421e68470b3d29d6e5ac79b7c1bf17feeca8efcd5616919f24edf4
- evidence_id: gsrs
  kind: authority
  reference: https://gsrs.ncats.nih.gov/api/v1/substances/7P6FQA5D21
  locator: Current approved chemical substance, version 36, full structure
  accessed_at: '2026-10-21T11:53:38Z'
  support: supports
  summary: UNII 7P6FQA5D21 has the native complete key, formula and 6R,7R/Z specification.
    Both current molfile and SMILES independently regenerate the complete native key
    despite alternate phosphate/carboxyl proton location. Native identity_record_version
    33 is a dated retrieval snapshot, not a claim that current GSRS remains version
    33.
  snapshot_sha256: 7fd15fcf0a62854d2392ae2e25262f06a4ae9758562650f3f15e440b7075647e
- evidence_id: fda-200327
  kind: authority
  reference: https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=200327
  locator: 'Native referenced application page: product table and original approval'
  accessed_at: '2026-10-21T11:54:52Z'
  support: supports
  summary: Official page confirms ABBVIE Teflaro 400/600 mg per vial, prescription
    IV powder and original approval 2010-10-29. These correspond to the two native
    NDA assertions. Marketing status is a regulatory category, not proof of immediate
    inventory availability.
  snapshot_sha256: 4eee619c7d23ec2a51e28b90bcbbaffa75b7708ee5ea04649e6b9861e78a0ccf
- evidence_id: fda-208075
  kind: authority
  reference: https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=208075
  locator: 'Native referenced application page: product table and original approval'
  accessed_at: '2026-10-21T11:54:52Z'
  support: supports
  summary: Official page confirms APOTEX ceftaroline fosamil 400/600 mg per vial,
    prescription IV powder and original approval 2021-09-21, corresponding to both
    native ANDA assertions.
  snapshot_sha256: 6a5eadc13f9edd6cc0bebb71f65f5054b9f174007c21a5b8a2caf3747821e444
- evidence_id: fda-products
  kind: authority
  reference: https://api.fda.gov/drug/drugsfda.json?search=application_number:NDA200327&limit=1
  locator: Current openFDA NDA result, products 001/002 and original submission
  accessed_at: '2026-10-21T11:53:39Z'
  support: supports
  summary: Product 001 is 400 mg/vial and 002 is 600 mg/vial; names, sponsor, prescription
    status and original AP submission/date match native. No discontinued product is
    substituted.
  snapshot_sha256: 3328dca2c034954cee285fc0c5ee4f74e87f44554b8dcdf2badadd8f20b30f86
- evidence_id: fda-generic-products
  kind: authority
  reference: https://api.fda.gov/drug/drugsfda.json?search=application_number:ANDA208075&limit=1
  locator: Current openFDA ANDA result, products 001/002 and original submission
  accessed_at: '2026-10-21T11:53:39Z'
  support: supports
  summary: Both numbered APOTEX products and 2021-09-21 original AP approval agree.
    The asserted summary status APPROVED is consistent with these current product
    records and their captured source history.
  snapshot_sha256: 214bed007e1aa2e1835a539020dcd9ac2d85b6eed9353d8a881fc66bd4118374
- evidence_id: label
  kind: authority
  reference: https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=3ecde48b-75a2-4beb-9999-369f3f61bb8a
  locator: Official Teflaro sections 1.1, 11, 12.3 and 14.1
  accessed_at: '2026-10-21T11:49:37Z'
  support: supports
  summary: Confirms adult ABSSSI use, fosamil conversion to bioactive ceftaroline,
    and manufactured monoacetate monohydrate plus L-arginine. Dose is expressed as
    600/400 mg anhydrous fosamil, corresponding to 668/446 mg hydrate. The exact-substance
    FDA join is compatible with this product formulation; it does not make the unsolvated
    structure a complete vial representation.
  snapshot_sha256: 36415b712a00b0cc1a15255298d51092b00d1ad9e88c67842c3e6cd2ede6361c
- evidence_id: patent
  kind: primary_source
  reference: https://patents.google.com/patent/MX2012003411A/en
  locator: Native document abstract and explicit family/priority link
  accessed_at: '2026-10-21T11:53:38Z'
  support: partial
  summary: Native MX document resolves to ceftaroline/prodrug compositions for bacterial
    infection and links to PCT/US2010/049659 / WO2011035305A1. The Spanish abstract
    and displayed English translation are relevant; this is not an unrelated patent
    identifier. Full native claims were not available in this rendering.
  snapshot_sha256: 12718e56b6958734548b018970f4b958b74d28af25fe3e620e0b7f27bec791aa
- evidence_id: patent-family
  kind: primary_source
  reference: https://patents.google.com/patent/WO2011035305A1/en
  locator: Linked original family description, preparation/formulation paragraphs
    and claims 1–17
  accessed_at: '2026-10-21T11:54:11Z'
  support: partial
  summary: Family text explicitly distinguishes ceftaroline, phosphono prodrug, anhydrous
    forms and monohydrate acetic-acid solvate, plus L-arginine formulations and anhydrous/acetic-acid-free
    dose basis. Claims concern formulations/regimens and PK. This supports document
    relevance with material distinctions; no independent direct target or exact isolated-fosamil
    MIC is assigned from the patent.
  snapshot_sha256: 49c8682d202453b4725a38bf54a5d39018a5fced1995d0a22005a67ed7ff7b39
- evidence_id: wiki
  kind: database
  reference: https://en.wikipedia.org/wiki/Ceftaroline_fosamil
  locator: Native document identity
  accessed_at: '2026-10-21T11:53:38Z'
  support: context_only
  summary: The named drug document resolves. It is contextual and does not substitute
    for original primary experiments or official approval data.
  snapshot_sha256: 6e664c260effca49b293bb10092bad9b48eb448eb16cf4608256c3e90766a0ae
- evidence_id: adopted-21076711
  kind: primary_source
  reference: PMID:21076711
  locator: DOI 10.1358/dot.2010.46.10.1519172; complete abstract
  accessed_at: '2026-10-21T11:53:38Z'
  support: context_only
  summary: Review summarizes spectrum, animal and human studies. Its statement that
    the drug was still under FDA review is historical publication context, superseded
    for current status by original approval records; it is not a contradiction in
    native dated clinical assertions.
  snapshot_sha256: ce870df14bac1a717c2afdadd77ef27f524ea3283019582b8ba00c0a2d101532
- evidence_id: adopted-21115453
  kind: primary_source
  reference: PMID:21115453
  locator: DOI 10.1093/jac/dkq253; complete abstract
  accessed_at: '2026-10-21T11:53:38Z'
  support: partial
  summary: Pharmacodynamic discussion combines prior MIC collections, free-time-above-MIC
    endpoints, Monte Carlo target attainment and clinical data. It uses fosamil terminology
    around active-drug effects; without full methods it is not treated as a new isolated-prodrug
    PBP2a-binding measurement or a direct compound-specific MIC source.
  snapshot_sha256: ce870df14bac1a717c2afdadd77ef27f524ea3283019582b8ba00c0a2d101532
- evidence_id: adopted-21115456
  kind: primary_source
  reference: PMID:21115456
  locator: DOI 10.1093/jac/dkq256; complete abstract
  accessed_at: '2026-10-21T11:53:38Z'
  support: context_only
  summary: Integrated CANVAS 1/2 safety analysis of 1378 treated patients reuses the
    two skin-infection trial cohorts. It is not a third independent efficacy experiment;
    results pertain to those regimens and follow-up periods.
  snapshot_sha256: ce870df14bac1a717c2afdadd77ef27f524ea3283019582b8ba00c0a2d101532
- evidence_id: adopted-21393213
  kind: primary_source
  reference: PMID:21393213
  locator: DOI 10.1093/jac/dkr019; complete abstract
  accessed_at: '2026-10-21T11:53:38Z'
  support: partial
  summary: Original rabbit endocarditis model compares administered fosamil, daptomycin
    and tigecycline for four days against MSSA/MRSA/GISA strains. Vegetation bacterial
    reduction is an in vivo treatment endpoint after prodrug administration; it is
    not direct binding or proof of clinical endocarditis approval. Exact solid reagent
    and full strain/protocol details remain unresolved from abstract.
  snapshot_sha256: ce870df14bac1a717c2afdadd77ef27f524ea3283019582b8ba00c0a2d101532
- evidence_id: adopted-21115454
  kind: primary_source
  reference: PMID:21115454
  locator: DOI 10.1093/jac/dkq254; CANVAS 1 complete abstract
  accessed_at: '2026-10-21T11:53:38Z'
  support: partial
  summary: Randomized adult cSSSI trial compares 600 mg ceftaroline fosamil every
    12 hours with vancomycin plus aztreonam for 5–14 days. Clinical cure in the evaluable
    population was 91.1% versus 93.3%; this supports clinical use under study conditions.
    The abstract does not itself identify exact solid-state form; label material and
    dose mapping are separate evidence.
  snapshot_sha256: ce870df14bac1a717c2afdadd77ef27f524ea3283019582b8ba00c0a2d101532
- evidence_id: adopted-21115455
  kind: primary_source
  reference: PMID:21115455
  locator: DOI 10.1093/jac/dkq255; CANVAS 2 complete abstract
  accessed_at: '2026-10-21T11:53:38Z'
  support: partial
  summary: Second randomized adult cSSSI trial uses the same named prodrug regimen
    and comparator; evaluable clinical cure was 92.2% versus 92.1%. It is clinical
    efficacy, not a purified binding or direct monohydrate MIC experiment. Exact solid
    preparation is not resolved from the abstract alone.
  snapshot_sha256: ce870df14bac1a717c2afdadd77ef27f524ea3283019582b8ba00c0a2d101532
- evidence_id: adopted-21162631
  kind: primary_source
  reference: PMID:21162631
  locator: DOI 10.2217/fmb.10.132; complete abstract
  accessed_at: '2026-10-21T11:53:38Z'
  support: context_only
  summary: Drug-profile synthesis distinguishes prodrug from active ceftaroline and
    summarizes clinical data. It is contextual secondary discussion, not an additional
    independent primary target experiment.
  snapshot_sha256: ce870df14bac1a717c2afdadd77ef27f524ea3283019582b8ba00c0a2d101532
- evidence_id: adopted-21252841
  kind: primary_source
  reference: PMID:21252841
  locator: Medical Letter 2011;53(1356):5–6; metadata and publisher introduction
  accessed_at: '2026-10-21T11:53:38Z'
  support: context_only
  summary: Europe PMC/PubMed supply no abstract. Public publisher issue page and introduction
    describe adult skin-infection and pneumonia approval, but full issue requires
    subscription and was not inspected. This is contextual drug commentary, not primary
    mechanism evidence; no title-only scientific assertion is adopted.
  snapshot_sha256: ce870df14bac1a717c2afdadd77ef27f524ea3283019582b8ba00c0a2d101532
- evidence_id: adopted-21482565
  kind: primary_source
  reference: PMID:21482565
  locator: DOI 10.1093/jac/dkr095; complete abstract
  accessed_at: '2026-10-21T11:53:38Z'
  support: context_only
  summary: Overview/review of ceftaroline fosamil summarizes pharmacology, active-ceftaroline
    activity and clinical use. Its PBP affinity prose is not an original isolated-hydrate
    binding measurement.
  snapshot_sha256: ce870df14bac1a717c2afdadd77ef27f524ea3283019582b8ba00c0a2d101532
- evidence_id: adopted-21482566
  kind: primary_source
  reference: PMID:21482566
  locator: DOI 10.1093/jac/dkr096; FOCUS 1 complete abstract
  accessed_at: '2026-10-21T11:53:38Z'
  support: partial
  summary: Randomized CAP trial compares 600 mg fosamil every 12 hours with ceftriaxone
    in hospitalized non-ICU PORT III/IV adults; both groups also receive two clarithromycin
    doses on day 1. Keep that co-therapy and pneumonia setting distinct from skin-infection
    trials and direct active-moiety activity.
  snapshot_sha256: ce870df14bac1a717c2afdadd77ef27f524ea3283019582b8ba00c0a2d101532
- evidence_id: active-primary
  kind: primary_source
  reference: PMID:18625769
  locator: DOI 10.1128/AAC.00149-08; original Methods and Results inspected as additional
    lead
  accessed_at: '2026-10-21T11:54:11Z'
  support: context_only
  summary: Methods explicitly assay active ceftaroline PPI-0903M lot M599-R1001 rather
    than fosamil. Results support the definition’s active-ceftaroline MRSA and broader
    antibacterial clause, with susceptibility limits for E. faecium and resistant
    Enterobacteriaceae. These MICs are not assigned to the prodrug.
  snapshot_sha256: 04358c674d9db7f15811e9da85af7725be152c90a95f717b5d549dbd5cd6c825
- evidence_id: synthesis-lead
  kind: primary_source
  reference: PMID:12735989
  locator: DOI 10.1016/S0968-0896(03)00126-3; original abstract
  accessed_at: '2026-10-21T11:54:52Z'
  support: partial
  summary: Original N-phosphono-prodrug study distinguishes TAK-599 compound 1 from
    active T-91825 compound 2a and reports rapid conversion in rats/monkeys. Exact
    solid form of compound 1 is unresolved at this access depth; active 2a potency
    is not transferred to direct prodrug binding.
  snapshot_sha256: bee558aec3b96f9641f20dce8ca68e438a9dbd96ff537a04db07dcf4d4d16183
- evidence_id: activation-lead
  kind: primary_source
  reference: PMID:15290453
  locator: DOI 10.1007/s10156-004-0309-3; original abstract
  accessed_at: '2026-10-21T11:54:52Z'
  support: partial
  summary: Separates T-91825 in vitro activity from TAK-599 in vivo mouse efficacy.
    Supports prodrug-mediated antibacterial use with organism/model boundaries rather
    than direct unsolvated-prodrug target activity.
  snapshot_sha256: 739a459165fc718ae9d5d6cecf02d31d6163dce86be2e0e935a26a7c798faf9a
- evidence_id: xref-check
  kind: validation
  reference: Independent exact compound and FDA-identity comparison
  locator: 251252-xref-check.json; 252 section
  accessed_at: '2026-10-21T11:54:34Z'
  support: supports
  summary: Native, CAS-resolved CID 9852981, current GSRS SMILES and GSRS molfile
    all regenerate ZCCUWMICIWSJIX-NQJJCJBVSA-N with the same formula.
  snapshot_sha256: 15d9561940c68f0e5ee55e97be647f734f9743e078921bc81ece86550e100387
- evidence_id: local-search
  kind: search
  reference: Ignored-inclusive native/owner and free primary review
  locator: 252-owner-hits.txt;252-local-hits.txt;252-adopted.json
  accessed_at: '2026-10-21T11:53:15Z'
  support: context_only
  summary: Exact label, ID, key and source provenance searched with ignored/hidden
    coverage outside .git/.venv. All ten adopted leads were disposed, relevant patent
    resolved, and each of four FDA assertions checked individually against current
    official records.
  snapshot_sha256: fd19f4a619e9b249a30198c64020eda5fae64c05e8f6b682d82d43c1fb4e5964
  search_scope: 2026-10-21; rg --no-ignore --hidden in isolated batch 026 outside
    .git/.venv; current official ChEBI/CAS/GSRS/FDA, all ten adopted PMID leads, free
    primary comparator text, native patent and linked original family.
- evidence_id: gates
  kind: validation
  reference: Actual focused commands
  locator: 252-focused-results.json
  accessed_at: '2026-10-21T11:53:19Z'
  support: supports
  summary: Native schema, strict and supplemental molecular helper each exit 0; independent
    exact identity comparison also passes.
  snapshot_sha256: fa227cce189b29ecb8c814b15eccef70d690761881e8cc6c571c65d281650f20
assessments:
- assessment_id: identity
  area: identity
  topic: Exact unsolvated fosamil graph and names
  outcome: supported
  summary: Complete key, formula, charge, masses, 6R,7R and Z oxime, exact systematic
    name and source mint agree.
  target_ids:
  - CHEBI:70718
  evidence_ids:
  - native
  - chebi
  - chemistry
  - cas
  - xref-check
- assessment_id: grounding
  area: grounding
  topic: Six structural parents and antibacterial roles
  outcome: supported
  summary: Parents fit the graph. Native definition explicitly places broad-spectrum/MRSA
    activity on the active ceftaroline context and calls fosamil its N-phospho prodrug.
    Prodrug-mediated antibacterial use is supported.
  target_ids:
  - CHEBI:70718
  evidence_ids:
  - chebi
  - label
  - active-primary
  - synthesis-lead
  - activation-lead
- assessment_id: clinical
  area: evidence
  topic: Four FDA assertions and summary status
  outcome: supported
  summary: Both NDA 200327 and ANDA 208075 products 001/002, original dates, sponsors,
    names, Prescription status and AP approval agree. Exact UNII/GSRS full key matches
    native; current version 36 does not invalidate captured version 33. Product material
    remains a formulated hydrate.
  target_ids:
  - CHEBI:70718
  evidence_ids:
  - owners
  - extractor
  - gsrs
  - fda-200327
  - fda-208075
  - fda-products
  - fda-generic-products
  - label
- assessment_id: xrefs
  area: grounding
  topic: Typed drug and documentary mappings
  outcome: supported
  summary: CAS exact identity, DrugCentral drug context and native MX patent/family
    relevance verified. Reaxys proprietary content remains uninspected; no assay transfer
    from document existence.
  target_ids:
  - CHEBI:70718
  evidence_ids:
  - cas
  - drugcentral
  - patent
  - patent-family
  - wiki
- assessment_id: leads
  area: evidence
  topic: All ten adopted PMID dispositions
  outcome: supported
  summary: Clinical trials, pooled safety, animal efficacy, pharmacodynamic discussion
    and review/commentary leads are separately bounded. Historical preapproval prose
    is not used for current status. No overlapping trial population is counted as
    an independent experiment.
  target_ids:
  - CHEBI:70718
  evidence_ids:
  - adopted-21076711
  - adopted-21115453
  - adopted-21115454
  - adopted-21115455
  - adopted-21115456
  - adopted-21162631
  - adopted-21252841
  - adopted-21393213
  - adopted-21482565
  - adopted-21482566
- assessment_id: activity
  area: evidence
  topic: Active metabolite versus administered prodrug
  outcome: supported
  summary: Active-ceftaroline in vitro observations support only the metabolite clause;
    fosamil in vivo/clinical regimens support prodrug treatment context. No direct
    native-prodrug numeric assay object is populated.
  target_ids:
  - CHEBI:70718
  evidence_ids:
  - active-primary
  - activation-lead
  - adopted-21393213
  - label
- assessment_id: mechanism
  area: evidence
  topic: Unpopulated direct protein claims
  outcome: not_applicable
  summary: No native PBP or other protein target exists. Review/database PBP prose
    cannot establish direct fosamil binding; activation is retained as a separate
    pharmacological relationship.
  target_ids:
  - CHEBI:70718
  evidence_ids:
  - native
  - drugcentral
  - adopted-21115453
- assessment_id: adapter
  area: scope
  topic: Structured source applicability
  outcome: not_applicable
  summary: Native record names no gene/protein/pathway or transcriptomics dataset.
    MRSA is an organism/phenotype context, not a named molecular target requiring
    an expression-module adapter query.
  target_ids:
  - CHEBI:70718
  evidence_ids:
  - native
- assessment_id: other-fields
  area: scope
  topic: Resistance, producer, datasets and graph
  outcome: not_applicable
  summary: No native populated assertions in these optional domains. FDA approval
    does not establish a natural producer or causal graph.
  target_ids:
  - CHEBI:70718
  evidence_ids:
  - native
- assessment_id: provenance
  area: provenance
  topic: Actual source ownership and history
  outcome: supported
  summary: ChEBI and FDA/GSRS owners captured before judgment, full-key join inspected,
    six history events and original hashes preserved. Scientific curation status remains
    SEEDED.
  target_ids:
  - CHEBI:70718
  evidence_ids:
  - native
  - owners
  - extractor
  - chemistry
- assessment_id: schema
  area: schema
  topic: Focused and independent checks
  outcome: supported
  summary: Native schema/strict and supplemental chemistry pass; regulatory and scientific
    source review remains independently documented.
  target_ids:
  - CHEBI:70718
  evidence_ids:
  - gates
  - xref-check
- assessment_id: completeness
  area: completeness
  topic: Optional evidence enrichment
  outcome: supported
  summary: No required-field defect established. Target/activity additions need active-metabolite
    versus prodrug and exact preparation qualification.
  target_ids:
  - CHEBI:70718
  evidence_ids:
  - rubric
  - label
  - active-primary
findings: []
actions:
- action_id: A1
  description: Optionally enrich prodrug/clinical evidence without conflating formulations
    and active drug.
  finding_ids: []
  target_ids:
  - CHEBI:70718
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/ceftaroline-fosamil.yaml
    role: Curator-owned primary evidence and optional activity/target annotations
      via validated writer
  acceptance_checks:
  - Keep exact GSRS substance identity and dated FDA assertions separate from complete
    monoacetate-monohydrate/L-arginine product composition.
  - Inspect full original methods before adding quantitative strain/model claims from
    abstract-only leads; distinguish CANVAS trial cohorts from pooled safety.
  - Assign active-ceftaroline PBP/MIC evidence to the active molecule and represent
    prodrug activation explicitly rather than asserting direct fosamil binding.
  - Preserve source-owned identities/history and run applicable schema/strict, term/reference/history
    and corpus checks after any separately authorized curation.
limitations:
- Nine adopted leads had inspectable abstracts; PMID 21252841 was limited to metadata
  and previously inspected public publisher introduction. Full original clinical/animal
  methods were not inspected, and no paywalled source was purchased.
- Additional 2008 active-ceftaroline Methods/Results were inspected, but exact TAK-599
  solid form remains unresolved in the additional synthesis/activation abstracts.
  No direct prodrug target assay is inferred.
- Native MX patent rendering exposes abstract and family links; relevant original
  family description/selected claims were inspected, not every native drawing, example
  or legal-status event.
- Independent proprietary Reaxys content was not inspected. Current official marketing
  status confirms regulatory category, not real-time commercial stock.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 22 expanded hashes unchanged, including FDA inventory/extractor; no native/source/status/history
  changes.
- Native validation used batch 026 environment; supplemental RDKit 2026.03.5 used
  existing batch 019 interpreter against batch 026 cwd.
- Official label, active-ceftaroline full text and public Medical Letter preview were
  inspected during immediately adjacent reviews; original source snapshots/access
  timestamps are retained where applicable. Free public sources only.
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
