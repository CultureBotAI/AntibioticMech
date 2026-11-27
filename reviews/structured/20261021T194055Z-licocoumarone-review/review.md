# Licocoumarone: coherent identity and compound-specific antibacterial support

- Review: 20261021T194055Z-licocoumarone-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T19:16:40Z
- Finished UTC: 2026-10-21T19:40:55Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The complete native record and actual ChEBI owner were reviewed. The neutral C20H20O5 structure agrees with current ChEBI, LIPID MAPS and an independent PubChem comparator, and with inspected original drawings and spectral descriptions. Exact licocoumarone inhibits tested MRSA and VRE strains. All seven adopted citation leads were dispositioned; host-enzyme and apoptosis findings are kept separate from antibacterial mechanism. No required native correction was established. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Assigned queue position 600; one exact native record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:69098 | data/antibiotics/antibacterial/licocoumarone.yaml | generated | licocoumarone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:69098 | Actual focused execution exited 0. Actual root-run execution against batch060; chemistry used existing batch019 RDKit, schema and strict used batch060. Results and exact commands were inspected without an unnecessary repeat. |
| Focused schema verification | passed | True | CHEBI:69098 | Actual focused execution exited 0. Actual root-run execution against batch060; chemistry used existing batch019 RDKit, schema and strict used batch060. Results and exact commands were inspected without an unnecessary repeat. |
| Focused strict verification | passed | True | CHEBI:69098 | Actual focused execution exited 0. Actual root-run execution against batch060; chemistry used existing batch019 RDKit, schema and strict used batch060. Results and exact commands were inspected without an unnecessary repeat. |
| Authoritative full QC | failed | True | CHEBI:69098 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:69098 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:69098 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:69098 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:69098 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:69098 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:69098 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:69098 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:69098 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact structure, names, formula and mass

identity: supported. Targets: CHEBI:69098.

The native constitution and both systematic synonyms agree with current authorities and the actual 2000/1991 drawings. The 1989 spectral description independently supports methoxy placement. Formula, neutral charge and masses are coherent, with no unresolved stereocentre or required prenyl E/Z specification.

### ChEBI identity, ontology parents and external accessions

grounding: supported. Targets: CHEBI:69098.

All three parent definitions fit the inspected graph, and antibacterial role is experimentally supported. LIPID MAPS exact chemistry is confirmed. HMDB and Reaxys resolve as source-linked accessions but their inaccessible contents remain unverified; no unsupported exact mismatch is asserted.

### Antibacterial and plant-origin assertions

evidence: supported. Targets: CHEBI:69098.

The compound-specific MRSA and VRE tables support antibacterial eligibility. The 2011 official supplement and additional 2014 original directly map licocoumarone to G. uralensis material. Host MAO/XO/apoptosis results and neighboring compounds are not used as antibacterial mechanism evidence. The producer statement is nonexclusive and survives the bounded G. glabra source conflict.

### Optional assay/producer enrichment and mechanism limits

completeness: unknown. Targets: CHEBI:69098.

No required missing representation was identified. Exact strain-specific activity and a voucher-backed producer observation could be added as optional primary enrichment. No direct antibacterial target is established by the inspected exact-compound evidence, and absent optional target fields are not treated as a defect.

### Generated ownership, adopted bibliography and history

provenance: supported. Targets: CHEBI:69098.

The entire source row and seven adopted citation dispositions are retained. ChEBI extraction and seeding own future changes. All original 13 and expanded 21 input hashes remain unchanged; the three seed/reseed history events are coherent and native status remains SEEDED.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optional primary enrichment can capture exact activity and producer observations without asserting a molecular target.

- Preserve compound 40 versus licoricidin 33 in the 2000 paper and exact five S. aureus strains, 16 µg/mL values and &gt;128 µg/mL Gram-negative censoring.
- Preserve compound 27, both VRE strains, 32 µg/mL, Mueller-Hinton broth, 37 °C/24 h, triplicate visual endpoint and the source unspecified CFU denominator.
- Use the actual G. uralensis voucher/lot and original SI named isolation; retain the G. glabra report as a bounded source difference rather than implying exclusive plant occurrence.
- Do not transfer PBP2′ results from licoricidin 33 or PTP1B/oral-pathogen effects from other numbered compounds. Any adopted enrichment should use maintained curation inputs, generation and required native gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/licocoumarone.yaml; Entire native record, including both synonyms, three parents, role, xrefs, source and all three history events | supports | Native denotes an exact neutral C20H20O5 2-arylbenzofuran, SEEDED from CHEBI:69098. Its definition asserts substitution pattern and isolation from Glycyrrhiza uralensis. There are no separate structured molecular target, resistance, activity spectrum, producer, product or causal graph objects; definition and role assertions are assessed below. No evidence quotation or reviewed-status assertion is present. |
| owners | data/raw/chebi_antimicrobials.tsv; Complete exact source row 1755 and owner/readiness search | context_only | The ChEBI row reproduces the native definition, both systematic synonyms, graph, parents, antibacterial role, three chemical links and seven adopted PMIDs. Source extraction and seeding are the actual maintained owners. Original 13 input hashes were preserved, and guidance/readiness context expanded the captured set to 21 before detailed judgment. |
| search | /private/tmp/am-review-session/600-context-search.txt; Initial local search and ignored-inclusive exact follow-up | context_only | Exact identifier, label and slug searches covered hidden and ignored inventories, curation, configuration, scripts and local reference surfaces. No separate exact curator or decisions owner was found within that inspected scope. Optional missing structured annotations are not treated as schema defects. |
| adapter | kg-microbe-sources imodulondb; Native-claim applicability review before open research | context_only | Native contains no named gene, protein, pathway, regulator or transcriptomic assertion requiring a structured query. Literature host-enzyme assays were not converted into bacterial targets. The adapter was therefore not applicable to the native assertions, rather than a negative search result. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/69098/; Complete current compound response, structure, names, source citations and origin | supports | Current CHEBI:69098 retains the native substitution pattern, both exact synonyms, neutral graph, full key CNPMAFLUEHEXRE-UHFFFAOYSA-N, formula and source links. Its G. uralensis root origin cites PMID22074222. Additional current roles do not make their absence a required native flaw. |
| lipidmaps | https://www.lipidmaps.org/rest/compound/lm_id/LMPK12160045/all/json; Complete LMPK12160045 response | supports | The asserted LIPID MAPS accession supplies the same formula, full InChI/key and constitution, including 6-hydroxy, 4-methoxy, 5-prenyl and 2-(2,4-dihydroxyphenyl) substitution. Its linked ChEBI and HMDB accessions agree with native identifiers. This does not independently validate inaccessible HMDB structural content. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/licocoumarone/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass/JSON; Independent name lookup resolving CID503731 | supports | PubChem provides the same neutral graph and full key. This is an additional authority comparator, not an asserted native PubChem xref. |
| chemistry | /private/tmp/am-review-session/060-root-chemistry.json; Exact 600 section; eight encodings from native, ChEBI, PubChem and LIPID MAPS | supports | All eight SMILES/InChI reconstructions yield CNPMAFLUEHEXRE-UHFFFAOYSA-N, C20H20O5, charge zero, average mass 340.375 and monoisotopic mass 340.13107374. There are no tetrahedral stereocentres; the prenyl double bond has two identical methyl substituents on one carbon and requires no E/Z designation. This deterministic agreement is supplemented by original structure inspection. |
| term-33572 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/33572/; Complete term definition and identifier | supports | The definition requires meta benzenediol hydroxyl groups; the native pendant 2,4-dihydroxyphenyl ring meets it. |
| term-35618 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/35618/; Complete term definition and identifier | supports | The definition requires an ether oxygen attached to an aryl substituent; the native aryl methoxy group meets it. |
| term-38830 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/38830/; Complete term definition and identifier | supports | The class includes substituted 1-benzofuran skeletons, which the native graph contains. |
| term-33282 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/33282/; Complete term definition and identifier | supports | The role covers killing or slowing bacterial growth. Exact primary MIC observations support it without requiring a named molecular target. |
| registry-limits | https://hmdb.ca/metabolites/HMDB0038755; https://www.reaxys.com; Asserted registry links and recorded access attempts | unknown | HMDB HTML and XML routes returned 403 in the root retrieval manifest, and the Reaxys exact registry route returned 403. Current ChEBI and LIPID MAPS preserve these accession associations, but neither inaccessible registry was independently reconciled at the structural-content level. No mismatch is inferred from failed access. |
| adopted | PMID:10993226; PMID:12392103; PMID:1913999; PMID:1941536; PMID:20724155; PMID:22074222; PMID:2632045; Complete Europe PMC core metadata and all seven available abstracts | context_only | All seven adopted identifiers resolve to licorice phenolic studies. Exact licocoumarone is compound 40 in the 2000 antibacterial original, compound 14 in the 1991 MAO original, compound 8 in the 1989 XO original, and compound 3 in the 2010 PTP1B isolation abstract. The 2011 supplement independently supplies the exact named isolation. Nearby active compounds and extract assays are not transferred. |
| mrsa-identity | PMID:10993226; DOI:10.1248/cpb.48.1286; Original pp 1287–1291, Chart 2 compound 40, isolation and assay methods; actual pages1287–1289 viewed | supports | The actual compound 40 drawing agrees with native licocoumarone. Material was isolated from commercial licorice whose phenolic profile was consistent with G. uralensis; the reported licocoumarone isolation yield was 0.022%. The study tested isolated individual phenolics, rather than assigning the entire extract effect to each constituent. |
| mrsa-activity | PMID:10993226; DOI:10.1248/cpb.48.1286; Actual Table 1 p1288, row40; Experimental p1291 | supports | Licocoumarone MICs were 16 µg/mL against MRSA OM481, OM505, OM584 and OM623 and MSSA 209P; E. coli K12 and P. aeruginosa PAO1 were both &gt;128 µg/mL. The liquid dilution assay used 96-well plates and 10^4 CFU/well. General compound-panel medium/incubation details are partly deferred to a cited method. The separate licoricidin 33 growth-curve conditions are not silently assigned to40. |
| mrsa-mechanism-boundary | PMID:10993226; DOI:10.1248/cpb.48.1286; Results on oxacillin resistance and PBP2′; compound-number mapping | context_only | The PBP2′ and detailed oxacillin-resistance suppression experiments concern licoricidin 33. They do not establish a licocoumarone 40 protein target. Growth inhibition supports the native antibacterial role without requiring this transfer. |
| vre | PMID:24686577; DOI:10.3390/molecules19043883; Full original XML, exact isolation and Methods3.2/3.3/3.5; Table 2 row27 | supports | The additional original isolated licocoumarone 27 (7.9 mg) from G. uralensis root/stolon, lot 002009037, voucherGU-07112011(NEL). Table 2 gives MIC32 µg/mL against both E. faecium FN-1 and E. faecalis NCTC12201. Serial twofold broth dilutions in Mueller-Hinton broth were incubated37 °C for 24 h without shaking; visual MICs were determined in triplicate. The paper states final density about 10^5 CFU without an explicit per-volume denominator, which is preserved as an uncertainty. These are strain-specific inhibition observations, not a direct-binding mechanism. |
| apoptosis | PMID:12392103; DOI:10.1248/bpb.25.1388; Complete short original main text, Methods, NMR/MS description and figure captions | context_only | Pure licocoumarone from fraction 4 was spectrometrically identified, with 4-methoxy and three hydroxyl positions matching native. The paper names G. glabra as source and reports10 mg per100 g root. Human U937 leukemia-cell proliferation and DNA-fragmentation experiments are host-cell findings; the ethanol-stock pure-compound treatments are distinct from crude extract GL1. The caspase-inhibitor result is not evidence for a bacterial target. The 2002 G. glabra label differs from the limited 1991 species survey, but neither contradicts independently supported isolation from G. uralensis. |
| mao | PMID:1913999; DOI:10.1248/cpb.39.1238; Actual pp 1238,1241–1242; Chart 4 compound 14, TableIII, Fig3 and assay method | context_only | The actual compound 14 drawing agrees with native. TableIII gives licocoumarone MAO IC50 of 6.0×10^-5 M; the paper describes noncompetitive kinetics at that concentration. The enzyme was commercial bovine-plasma MAO, with benzylamine substrate,15 min preincubation and 30 min reaction at 37 °C, absorbance 250 nm, triplicate means. This host-enzyme experiment is not an antibacterial mechanism or a bacterial MAO binding assay. New-compound spectral elucidations elsewhere were not exhaustively reviewed. |
| licorice-survey | PMID:1941536; DOI:10.1248/yakushi1947.111.6_311; Actual English abstract on original p311 and complete indexed abstract; Japanese body not fully translated | partial | The limited HPLC survey associates licocoumarone 8 with tested G. uralensis/typeA samples and reports non-detection in the tested G. glabra/G. inflata samples. This is not universal species exclusivity, especially given the later G. glabra report. Its enzyme inhibition at 30 µg/mL concerns licorice extracts, not a pure licocoumarone potency. |
| ptp1b | PMID:20724155; DOI:10.1016/j.bmcl.2010.07.110; Complete abstract; publisher full-text attempt returned 403 | partial | The abstract explicitly identifies licocoumarone 3 among isolates from G. uralensis roots. Reported significant PTP1B values25.5 and 27.9 µM and kinetic conclusions concern glycybenzofuran 1 and glisoflavone 5, not3. A compound 3 table value or direct target cannot be inferred from this abstract; exact full-body assay mapping remains uninspected. |
| isolation2011 | PMID:22074222; DOI:10.1021/np2004775; Complete abstract and official SI PDF page 16, Isolation; SI contents reviewed | partial | The official supplement explicitly reports licocoumarone (1.0 mg) in fraction 5 from 615 mg extract after MPLC and semipreparative HPLC. Together with the original abstract identifying the G. uralensis supercritical-fluid extract, this supports the native producer statement. SI spectra focus on compounds 7–9 and do not provide a licocoumarone antibacterial table. Main text remained 403; abstract oral-pathogen potency belongs to licoricidin 1/licorisoflavan A 2 and is not transferred. |
| xo | PMID:2632045; DOI:10.1248/cpb.37.3005; Actual pp 3005,3007–3008; TableI row8 and exact spectral/isolation/assay sections | context_only | The original isolated licocoumarone 8 (15 mg) from Si-pei commercial Glycyrrhiza material. Its C4 methoxy placement was supported by an H3 NOE and comparison with authentic material by HPLC/TLC. TableI gives XO IC50 of 1.3×10^-5 M. The assay used cow-milk XO, xanthine, phosphate buffer pH 7.4,10 min preincubation and 30 min reaction at 37 °C, absorbance 295 nm, triplicate means. Discussion permits nonspecific protein binding; this is not bacterial target validation. The anti-HIV discussion concerns licopyranocoumarin 4, not8. |
| access | /private/tmp/am-review-session/600-fetch2.json; Bounded access and reading record | context_only | The 2010 DOI route supplied only a redirect shell and its direct publisher route returned 403. The 2011 ACS main returned 403, while official Figshare metadata and SI were successfully retrieved. Other additional search results were discovery leads only. Registry failures and selected-page reading limits are retained rather than converted into claims of complete access. |

## Limits And Additional Notes

- HMDB HTML/XML and Reaxys exact routes returned 403. Their association is independently propagated by current ChEBI/LIPID MAPS, but their registry structural contents were not inspected.
- The 2000 original was read for the complete exact compound/material/assay and relevant antibacterial mechanism sections; actual Table 1 and Chart 2 were viewed. The 2014 original was read through exact isolation, antibacterial results, Table 2 and assay methods, not every new-compound spectral derivation. Raw MIC data were not reanalyzed.
- The 2002 short main text and figure captions were read; apoptosis plot images were not independently digitized. The 1989 original was inspected at actual pp 3005,3007–3008 and the 1991 MAO original at pp 1238,1241–1242, covering exact identity, tables and methods; unrelated new-compound derivations were not exhaustively read.
- The 1991 Japanese survey was assessed through its actual English abstract and indexed abstract; its entire Japanese body was not translated. No universal plant-species absence is inferred.
- The 2010 main publisher text and 2011 ACS main remained 403. Both complete abstracts were read; the 2011 official SI contents and exact named isolation on PDF page 16 were inspected. That SI resolves producer mapping but does not establish an exact licocoumarone oral-pathogen assay.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All original 13 and expanded 21 captured input hashes were verified unchanged. This review created only scratch evidence and an unsaved draft; native records, source inventories, history, progress and Git were not changed.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T194055Z-licocoumarone-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Licocoumarone: coherent identity and compound-specific antibacterial support'
started_at: '2026-10-21T19:16:40Z'
finished_at: '2026-10-21T19:40:55Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the native record. The entire native
    and maintained source row were read, current authority encodings and actual chemistry
    calculations were inspected, and exact-compound primary text, structures and assay
    tables were independently assessed.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: The complete native record and actual ChEBI owner were reviewed. The neutral
  C20H20O5 structure agrees with current ChEBI, LIPID MAPS and an independent PubChem
  comparator, and with inspected original drawings and spectral descriptions. Exact
  licocoumarone inhibits tested MRSA and VRE strains. All seven adopted citation leads
  were dispositioned; host-enzyme and apoptosis findings are kept separate from antibacterial
  mechanism. No required native correction was established. Scientific assessment
  retains the stated evidence limits; full verification is blocked by the shared native-library
  failure.
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
  - path: data/antibiotics/antibacterial/licocoumarone.yaml
    sha256: 2e5e463abba53e0342e10e9f1a0bc8dae037b4740d9c6b8bd986e3630d5b8296
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
  - path: curation/record_review_queue.tsv
    sha256: 3828a5120b892ee0ee0b776affc6c3e4f1f1a3355ec4edd30e6005762de00e70
    role: context
  - path: CLAUDE.md
    sha256: 36fb92f8919481cfbf3f17ddde4a1e244c81f76c64396dbbac910c4815fb9f16
    role: context
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
    role: context
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
targets:
- target_id: CHEBI:69098
  path: data/antibiotics/antibacterial/licocoumarone.yaml
  label: licocoumarone
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Actual ChEBI identity, structure, roles, xrefs and citation owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated record field owner
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Assigned queue position 600; one exact native record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:69098
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0. Actual root-run execution against batch060;
    chemistry used existing batch019 RDKit, schema and strict used batch060. Results
    and exact commands were inspected without an unnecessary repeat.
  target_ids:
  - CHEBI:69098
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    600
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Actual root-run execution against batch060;
    chemistry used existing batch019 RDKit, schema and strict used batch060. Results
    and exact commands were inspected without an unnecessary repeat.
  target_ids:
  - CHEBI:69098
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/licocoumarone.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Actual root-run execution against batch060;
    chemistry used existing batch019 RDKit, schema and strict used batch060. Results
    and exact commands were inspected without an unnecessary repeat.
  target_ids:
  - CHEBI:69098
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/licocoumarone.yaml --out /private/tmp/am-review-session/600-strict.tsv
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
  - CHEBI:69098
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
  - CHEBI:69098
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
  - CHEBI:69098
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
  - CHEBI:69098
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
  - CHEBI:69098
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
  - CHEBI:69098
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
  - CHEBI:69098
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
  - CHEBI:69098
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
  - CHEBI:69098
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/licocoumarone.yaml
  locator: Entire native record, including both synonyms, three parents, role, xrefs,
    source and all three history events
  accessed_at: '2026-10-21T19:34:52Z'
  support: supports
  summary: Native denotes an exact neutral C20H20O5 2-arylbenzofuran, SEEDED from
    CHEBI:69098. Its definition asserts substitution pattern and isolation from Glycyrrhiza
    uralensis. There are no separate structured molecular target, resistance, activity
    spectrum, producer, product or causal graph objects; definition and role assertions
    are assessed below. No evidence quotation or reviewed-status assertion is present.
  snapshot_sha256: 2e5e463abba53e0342e10e9f1a0bc8dae037b4740d9c6b8bd986e3630d5b8296
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Complete exact source row 1755 and owner/readiness search
  accessed_at: '2026-10-21T19:34:52Z'
  support: context_only
  summary: The ChEBI row reproduces the native definition, both systematic synonyms,
    graph, parents, antibacterial role, three chemical links and seven adopted PMIDs.
    Source extraction and seeding are the actual maintained owners. Original 13 input
    hashes were preserved, and guidance/readiness context expanded the captured set
    to 21 before detailed judgment.
  snapshot_sha256: 2c7f5a118cebbd2d730d6e13b24692cbeebe26c2734bf2aacf2ce4b5aabcb898
- evidence_id: search
  kind: search
  reference: /private/tmp/am-review-session/600-context-search.txt
  locator: Initial local search and ignored-inclusive exact follow-up
  accessed_at: '2026-10-21T19:34:52Z'
  support: context_only
  summary: Exact identifier, label and slug searches covered hidden and ignored inventories,
    curation, configuration, scripts and local reference surfaces. No separate exact
    curator or decisions owner was found within that inspected scope. Optional missing
    structured annotations are not treated as schema defects.
  snapshot_sha256: e4d7cc7cf8318c552b25f494277e6f549722f63aea487066772bac3c1753ed46
  search_scope: Preserved initial600-local-hits plus rg --no-ignore --hidden for CHEBI:69098,
    licocoumarone and its exact slug across curation, conf, scripts and data/raw.
- evidence_id: adapter
  kind: search
  reference: kg-microbe-sources imodulondb
  locator: Native-claim applicability review before open research
  accessed_at: '2026-10-21T19:34:52Z'
  support: context_only
  summary: Native contains no named gene, protein, pathway, regulator or transcriptomic
    assertion requiring a structured query. Literature host-enzyme assays were not
    converted into bacterial targets. The adapter was therefore not applicable to
    the native assertions, rather than a negative search result.
  snapshot_sha256: 466090bec56b7740afe6e747423396f732221fd032df0a3a42c6be2054f0ac08
  search_scope: Entire native definition and all structured field names examined for
    the skill applicability trigger.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/69098/
  locator: Complete current compound response, structure, names, source citations
    and origin
  accessed_at: '2026-10-21T19:24:41Z'
  support: supports
  summary: Current CHEBI:69098 retains the native substitution pattern, both exact
    synonyms, neutral graph, full key CNPMAFLUEHEXRE-UHFFFAOYSA-N, formula and source
    links. Its G. uralensis root origin cites PMID22074222. Additional current roles
    do not make their absence a required native flaw.
  snapshot_sha256: 2b26bc30d320a1d803edbd47794c5a763700d928b784b63a71f4bfaa483bfdaa
- evidence_id: lipidmaps
  kind: authority
  reference: https://www.lipidmaps.org/rest/compound/lm_id/LMPK12160045/all/json
  locator: Complete LMPK12160045 response
  accessed_at: '2026-10-21T19:24:44Z'
  support: supports
  summary: The asserted LIPID MAPS accession supplies the same formula, full InChI/key
    and constitution, including 6-hydroxy, 4-methoxy, 5-prenyl and 2-(2,4-dihydroxyphenyl)
    substitution. Its linked ChEBI and HMDB accessions agree with native identifiers.
    This does not independently validate inaccessible HMDB structural content.
  snapshot_sha256: f9fa395db4c278cccf129530a64eccf3c62153c374076d3dc970fe588ac93ddb
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/licocoumarone/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass/JSON
  locator: Independent name lookup resolving CID503731
  accessed_at: '2026-10-21T19:24:41Z'
  support: supports
  summary: PubChem provides the same neutral graph and full key. This is an additional
    authority comparator, not an asserted native PubChem xref.
  snapshot_sha256: 047813e5202135aea8a93face25ba38396099aca38a0bf4b6d2fcaae13d358cf
- evidence_id: chemistry
  kind: validation
  reference: /private/tmp/am-review-session/060-root-chemistry.json
  locator: Exact 600 section; eight encodings from native, ChEBI, PubChem and LIPID
    MAPS
  accessed_at: '2026-10-21T19:34:52Z'
  support: supports
  summary: All eight SMILES/InChI reconstructions yield CNPMAFLUEHEXRE-UHFFFAOYSA-N,
    C20H20O5, charge zero, average mass 340.375 and monoisotopic mass 340.13107374.
    There are no tetrahedral stereocentres; the prenyl double bond has two identical
    methyl substituents on one carbon and requires no E/Z designation. This deterministic
    agreement is supplemented by original structure inspection.
  snapshot_sha256: 6f9b4e94c432a0bd143e5b917f2a813453d7d1b99f3fe8566184323158a72479
- evidence_id: term-33572
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/33572/
  locator: Complete term definition and identifier
  accessed_at: '2026-10-21T19:24:41Z'
  support: supports
  summary: The definition requires meta benzenediol hydroxyl groups; the native pendant
    2,4-dihydroxyphenyl ring meets it.
  snapshot_sha256: 3773760f57ea2d844685e1b715dbfddf1c334b246027c8a748baeef6efe72b16
- evidence_id: term-35618
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/35618/
  locator: Complete term definition and identifier
  accessed_at: '2026-10-21T19:24:41Z'
  support: supports
  summary: The definition requires an ether oxygen attached to an aryl substituent;
    the native aryl methoxy group meets it.
  snapshot_sha256: 313f535b9f2b86e55b4da02cdd6f05e29bea628f236abdb72d96bee2d1900891
- evidence_id: term-38830
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/38830/
  locator: Complete term definition and identifier
  accessed_at: '2026-10-21T19:24:41Z'
  support: supports
  summary: The class includes substituted 1-benzofuran skeletons, which the native
    graph contains.
  snapshot_sha256: 66ee47805cc2ce568f301413c9d33c2d0459ccfd98ecbcb2db98a314d2758f37
- evidence_id: term-33282
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/33282/
  locator: Complete term definition and identifier
  accessed_at: '2026-10-21T19:24:36Z'
  support: supports
  summary: The role covers killing or slowing bacterial growth. Exact primary MIC
    observations support it without requiring a named molecular target.
  snapshot_sha256: 20d92ce7e00c204b1753184671c043160821d692438278344335446aadcd5082
- evidence_id: registry-limits
  kind: authority
  reference: https://hmdb.ca/metabolites/HMDB0038755; https://www.reaxys.com
  locator: Asserted registry links and recorded access attempts
  accessed_at: '2026-10-21T19:34:52Z'
  support: unknown
  summary: HMDB HTML and XML routes returned 403 in the root retrieval manifest, and
    the Reaxys exact registry route returned 403. Current ChEBI and LIPID MAPS preserve
    these accession associations, but neither inaccessible registry was independently
    reconciled at the structural-content level. No mismatch is inferred from failed
    access.
  snapshot_sha256: 6295abc6e4fa76c61801cb7dc67792c7be7b43fc1daaf3917cae109f6ad80cd2
- evidence_id: adopted
  kind: primary_source
  reference: PMID:10993226; PMID:12392103; PMID:1913999; PMID:1941536; PMID:20724155;
    PMID:22074222; PMID:2632045
  locator: Complete Europe PMC core metadata and all seven available abstracts
  accessed_at: '2026-10-21T19:24:41Z'
  support: context_only
  summary: All seven adopted identifiers resolve to licorice phenolic studies. Exact
    licocoumarone is compound 40 in the 2000 antibacterial original, compound 14 in
    the 1991 MAO original, compound 8 in the 1989 XO original, and compound 3 in the
    2010 PTP1B isolation abstract. The 2011 supplement independently supplies the
    exact named isolation. Nearby active compounds and extract assays are not transferred.
  snapshot_sha256: 4252ec4a22be1deb6bb6b23ba09910900934d631cf9e5404afbae6f1d60eb004
- evidence_id: mrsa-identity
  kind: primary_source
  reference: PMID:10993226; DOI:10.1248/cpb.48.1286
  locator: Original pp 1287–1291, Chart 2 compound 40, isolation and assay methods;
    actual pages1287–1289 viewed
  accessed_at: '2026-10-21T19:25:36Z'
  support: supports
  summary: The actual compound 40 drawing agrees with native licocoumarone. Material
    was isolated from commercial licorice whose phenolic profile was consistent with
    G. uralensis; the reported licocoumarone isolation yield was 0.022%. The study
    tested isolated individual phenolics, rather than assigning the entire extract
    effect to each constituent.
  snapshot_sha256: de3c10db9636ec3839014bd0994bf5f72af7509eec44e400418b5b5096d73563
- evidence_id: mrsa-activity
  kind: primary_source
  reference: PMID:10993226; DOI:10.1248/cpb.48.1286
  locator: Actual Table 1 p1288, row40; Experimental p1291
  accessed_at: '2026-10-21T19:25:36Z'
  support: supports
  summary: Licocoumarone MICs were 16 µg/mL against MRSA OM481, OM505, OM584 and OM623
    and MSSA 209P; E. coli K12 and P. aeruginosa PAO1 were both >128 µg/mL. The liquid
    dilution assay used 96-well plates and 10^4 CFU/well. General compound-panel medium/incubation
    details are partly deferred to a cited method. The separate licoricidin 33 growth-curve
    conditions are not silently assigned to40.
  snapshot_sha256: de3c10db9636ec3839014bd0994bf5f72af7509eec44e400418b5b5096d73563
- evidence_id: mrsa-mechanism-boundary
  kind: primary_source
  reference: PMID:10993226; DOI:10.1248/cpb.48.1286
  locator: Results on oxacillin resistance and PBP2′; compound-number mapping
  accessed_at: '2026-10-21T19:25:36Z'
  support: context_only
  summary: The PBP2′ and detailed oxacillin-resistance suppression experiments concern
    licoricidin 33. They do not establish a licocoumarone 40 protein target. Growth
    inhibition supports the native antibacterial role without requiring this transfer.
  snapshot_sha256: de3c10db9636ec3839014bd0994bf5f72af7509eec44e400418b5b5096d73563
- evidence_id: vre
  kind: primary_source
  reference: PMID:24686577; DOI:10.3390/molecules19043883
  locator: Full original XML, exact isolation and Methods3.2/3.3/3.5; Table 2 row27
  accessed_at: '2026-10-21T19:25:37Z'
  support: supports
  summary: The additional original isolated licocoumarone 27 (7.9 mg) from G. uralensis
    root/stolon, lot 002009037, voucherGU-07112011(NEL). Table 2 gives MIC32 µg/mL
    against both E. faecium FN-1 and E. faecalis NCTC12201. Serial twofold broth dilutions
    in Mueller-Hinton broth were incubated37 °C for 24 h without shaking; visual MICs
    were determined in triplicate. The paper states final density about 10^5 CFU without
    an explicit per-volume denominator, which is preserved as an uncertainty. These
    are strain-specific inhibition observations, not a direct-binding mechanism.
  snapshot_sha256: 59ba8b45ef1592b0e2c4bf5e534d254f8565abc027520c06432f5bf49a0e2bb0
- evidence_id: apoptosis
  kind: primary_source
  reference: PMID:12392103; DOI:10.1248/bpb.25.1388
  locator: Complete short original main text, Methods, NMR/MS description and figure
    captions
  accessed_at: '2026-10-21T19:25:36Z'
  support: context_only
  summary: Pure licocoumarone from fraction 4 was spectrometrically identified, with
    4-methoxy and three hydroxyl positions matching native. The paper names G. glabra
    as source and reports10 mg per100 g root. Human U937 leukemia-cell proliferation
    and DNA-fragmentation experiments are host-cell findings; the ethanol-stock pure-compound
    treatments are distinct from crude extract GL1. The caspase-inhibitor result is
    not evidence for a bacterial target. The 2002 G. glabra label differs from the
    limited 1991 species survey, but neither contradicts independently supported isolation
    from G. uralensis.
  snapshot_sha256: 6d0bb5749e239f8d08ac9c0bf1a29bc4af1174c49b423c90e57a5b5dd25bd4a6
- evidence_id: mao
  kind: primary_source
  reference: PMID:1913999; DOI:10.1248/cpb.39.1238
  locator: Actual pp 1238,1241–1242; Chart 4 compound 14, TableIII, Fig3 and assay
    method
  accessed_at: '2026-10-21T19:25:37Z'
  support: context_only
  summary: The actual compound 14 drawing agrees with native. TableIII gives licocoumarone
    MAO IC50 of 6.0×10^-5 M; the paper describes noncompetitive kinetics at that concentration.
    The enzyme was commercial bovine-plasma MAO, with benzylamine substrate,15 min
    preincubation and 30 min reaction at 37 °C, absorbance 250 nm, triplicate means.
    This host-enzyme experiment is not an antibacterial mechanism or a bacterial MAO
    binding assay. New-compound spectral elucidations elsewhere were not exhaustively
    reviewed.
  snapshot_sha256: fd767c6346b8b8959964017d052110b1c4577bdb8748cc6ce7f1447e6ba7949d
- evidence_id: licorice-survey
  kind: primary_source
  reference: PMID:1941536; DOI:10.1248/yakushi1947.111.6_311
  locator: Actual English abstract on original p311 and complete indexed abstract;
    Japanese body not fully translated
  accessed_at: '2026-10-21T19:25:37Z'
  support: partial
  summary: The limited HPLC survey associates licocoumarone 8 with tested G. uralensis/typeA
    samples and reports non-detection in the tested G. glabra/G. inflata samples.
    This is not universal species exclusivity, especially given the later G. glabra
    report. Its enzyme inhibition at 30 µg/mL concerns licorice extracts, not a pure
    licocoumarone potency.
  snapshot_sha256: b5d63bf334430b30c2ecf56c6b7d85ee4eb576fc975330060120e180867bea55
- evidence_id: ptp1b
  kind: primary_source
  reference: PMID:20724155; DOI:10.1016/j.bmcl.2010.07.110
  locator: Complete abstract; publisher full-text attempt returned 403
  accessed_at: '2026-10-21T19:24:41Z'
  support: partial
  summary: The abstract explicitly identifies licocoumarone 3 among isolates from
    G. uralensis roots. Reported significant PTP1B values25.5 and 27.9 µM and kinetic
    conclusions concern glycybenzofuran 1 and glisoflavone 5, not3. A compound 3 table
    value or direct target cannot be inferred from this abstract; exact full-body
    assay mapping remains uninspected.
  snapshot_sha256: 4252ec4a22be1deb6bb6b23ba09910900934d631cf9e5404afbae6f1d60eb004
- evidence_id: isolation2011
  kind: primary_source
  reference: PMID:22074222; DOI:10.1021/np2004775
  locator: Complete abstract and official SI PDF page 16, Isolation; SI contents reviewed
  accessed_at: '2026-10-21T19:32:56.874396Z'
  support: partial
  summary: The official supplement explicitly reports licocoumarone (1.0 mg) in fraction
    5 from 615 mg extract after MPLC and semipreparative HPLC. Together with the original
    abstract identifying the G. uralensis supercritical-fluid extract, this supports
    the native producer statement. SI spectra focus on compounds 7–9 and do not provide
    a licocoumarone antibacterial table. Main text remained 403; abstract oral-pathogen
    potency belongs to licoricidin 1/licorisoflavan A 2 and is not transferred.
  snapshot_sha256: bb2e36884535f43f6ec19e1dcb47c7b4fb9c512fdbae1332eb78eb6a044f967b
- evidence_id: xo
  kind: primary_source
  reference: PMID:2632045; DOI:10.1248/cpb.37.3005
  locator: Actual pp 3005,3007–3008; TableI row8 and exact spectral/isolation/assay
    sections
  accessed_at: '2026-10-21T19:25:37Z'
  support: context_only
  summary: The original isolated licocoumarone 8 (15 mg) from Si-pei commercial Glycyrrhiza
    material. Its C4 methoxy placement was supported by an H3 NOE and comparison with
    authentic material by HPLC/TLC. TableI gives XO IC50 of 1.3×10^-5 M. The assay
    used cow-milk XO, xanthine, phosphate buffer pH 7.4,10 min preincubation and 30
    min reaction at 37 °C, absorbance 295 nm, triplicate means. Discussion permits
    nonspecific protein binding; this is not bacterial target validation. The anti-HIV
    discussion concerns licopyranocoumarin 4, not8.
  snapshot_sha256: 1a3e10df3e5022b21bf1b9fe0629439db5a5c12da63fa19e44e781c9d638a525
- evidence_id: access
  kind: validation
  reference: /private/tmp/am-review-session/600-fetch2.json
  locator: Bounded access and reading record
  accessed_at: '2026-10-21T19:34:52Z'
  support: context_only
  summary: The 2010 DOI route supplied only a redirect shell and its direct publisher
    route returned 403. The 2011 ACS main returned 403, while official Figshare metadata
    and SI were successfully retrieved. Other additional search results were discovery
    leads only. Registry failures and selected-page reading limits are retained rather
    than converted into claims of complete access.
  snapshot_sha256: efedb514218564bbf96fec5cf435668dc8ee5942745232bea8394700ad9dc628
assessments:
- assessment_id: identity
  area: identity
  topic: Exact structure, names, formula and mass
  outcome: supported
  summary: The native constitution and both systematic synonyms agree with current
    authorities and the actual 2000/1991 drawings. The 1989 spectral description independently
    supports methoxy placement. Formula, neutral charge and masses are coherent, with
    no unresolved stereocentre or required prenyl E/Z specification.
  target_ids:
  - CHEBI:69098
  evidence_ids:
  - native
  - chebi
  - lipidmaps
  - pubchem
  - chemistry
  - mrsa-identity
  - mao
  - xo
- assessment_id: grounding
  area: grounding
  topic: ChEBI identity, ontology parents and external accessions
  outcome: supported
  summary: All three parent definitions fit the inspected graph, and antibacterial
    role is experimentally supported. LIPID MAPS exact chemistry is confirmed. HMDB
    and Reaxys resolve as source-linked accessions but their inaccessible contents
    remain unverified; no unsupported exact mismatch is asserted.
  target_ids:
  - CHEBI:69098
  evidence_ids:
  - chebi
  - lipidmaps
  - term-33572
  - term-35618
  - term-38830
  - term-33282
  - registry-limits
  - mrsa-activity
  - vre
- assessment_id: evidence
  area: evidence
  topic: Antibacterial and plant-origin assertions
  outcome: supported
  summary: The compound-specific MRSA and VRE tables support antibacterial eligibility.
    The 2011 official supplement and additional 2014 original directly map licocoumarone
    to G. uralensis material. Host MAO/XO/apoptosis results and neighboring compounds
    are not used as antibacterial mechanism evidence. The producer statement is nonexclusive
    and survives the bounded G. glabra source conflict.
  target_ids:
  - CHEBI:69098
  evidence_ids:
  - mrsa-identity
  - mrsa-activity
  - mrsa-mechanism-boundary
  - vre
  - isolation2011
  - ptp1b
  - apoptosis
  - licorice-survey
  - mao
  - xo
- assessment_id: completeness
  area: completeness
  topic: Optional assay/producer enrichment and mechanism limits
  outcome: unknown
  summary: No required missing representation was identified. Exact strain-specific
    activity and a voucher-backed producer observation could be added as optional
    primary enrichment. No direct antibacterial target is established by the inspected
    exact-compound evidence, and absent optional target fields are not treated as
    a defect.
  target_ids:
  - CHEBI:69098
  evidence_ids:
  - search
  - adapter
  - mrsa-activity
  - vre
  - isolation2011
  - mrsa-mechanism-boundary
  - access
- assessment_id: provenance
  area: provenance
  topic: Generated ownership, adopted bibliography and history
  outcome: supported
  summary: The entire source row and seven adopted citation dispositions are retained.
    ChEBI extraction and seeding own future changes. All original 13 and expanded
    21 input hashes remain unchanged; the three seed/reseed history events are coherent
    and native status remains SEEDED.
  target_ids:
  - CHEBI:69098
  evidence_ids:
  - owners
  - native
  - adopted
  - chebi
  - search
findings: []
actions:
- action_id: A1
  finding_ids: []
  target_ids:
  - CHEBI:69098
  description: Optional primary enrichment can capture exact activity and producer
    observations without asserting a molecular target.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Actual ChEBI identity, structure, roles, xrefs and citation owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated record field owner
  acceptance_checks:
  - Preserve compound 40 versus licoricidin 33 in the 2000 paper and exact five S.
    aureus strains, 16 µg/mL values and >128 µg/mL Gram-negative censoring.
  - Preserve compound 27, both VRE strains, 32 µg/mL, Mueller-Hinton broth, 37 °C/24
    h, triplicate visual endpoint and the source unspecified CFU denominator.
  - Use the actual G. uralensis voucher/lot and original SI named isolation; retain
    the G. glabra report as a bounded source difference rather than implying exclusive
    plant occurrence.
  - Do not transfer PBP2′ results from licoricidin 33 or PTP1B/oral-pathogen effects
    from other numbered compounds. Any adopted enrichment should use maintained curation
    inputs, generation and required native gates.
limitations:
- HMDB HTML/XML and Reaxys exact routes returned 403. Their association is independently
  propagated by current ChEBI/LIPID MAPS, but their registry structural contents were
  not inspected.
- The 2000 original was read for the complete exact compound/material/assay and relevant
  antibacterial mechanism sections; actual Table 1 and Chart 2 were viewed. The 2014
  original was read through exact isolation, antibacterial results, Table 2 and assay
  methods, not every new-compound spectral derivation. Raw MIC data were not reanalyzed.
- The 2002 short main text and figure captions were read; apoptosis plot images were
  not independently digitized. The 1989 original was inspected at actual pp 3005,3007–3008
  and the 1991 MAO original at pp 1238,1241–1242, covering exact identity, tables
  and methods; unrelated new-compound derivations were not exhaustively read.
- The 1991 Japanese survey was assessed through its actual English abstract and indexed
  abstract; its entire Japanese body was not translated. No universal plant-species
  absence is inferred.
- The 2010 main publisher text and 2011 ACS main remained 403. Both complete abstracts
  were read; the 2011 official SI contents and exact named isolation on PDF page 16
  were inspected. That SI resolves producer mapping but does not establish an exact
  licocoumarone oral-pathogen assay.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All original 13 and expanded 21 captured input hashes were verified unchanged. This
  review created only scratch evidence and an unsaved draft; native records, source
  inventories, history, progress and Git were not changed.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
