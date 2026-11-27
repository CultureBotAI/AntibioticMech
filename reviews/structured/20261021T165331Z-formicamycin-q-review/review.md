# Formicamycin Q: coherent original structure with bounded primary and database activity evidence

- Review: 20261021T165331Z-formicamycin-q-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T16:45:50Z
- Finished UTC: 2026-10-21T16:53:31Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native neutral formicamycin Q graph agrees with the original 2020 supplementary drawing and current ChEBI, PubChem and ChEMBL. The original abstract identifies the isolated congener and producer; exact MIC extracts are available at ChEMBL database tier, while the original full assay table remains inaccessible. No confirmed native correction is identified. Family resistance claims and structural revisions of other congeners are not transferred to this molecule. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 472; thirteen original input hashes preserved within twenty-three expanded inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-63b276648e | data/antibiotics/antibacterial/formicamycin-q.yaml | generated | formicamycin Q |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-63b276648e | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-63b276648e | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-63b276648e | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | antibioticmech:aro-63b276648e | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-63b276648e | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-63b276648e | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-63b276648e | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-63b276648e | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-63b276648e | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-63b276648e | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-63b276648e | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-63b276648e | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact molecular form and original assignment

identity: supported. Targets: antibioticmech:aro-63b276648e.

The neutral Q graph, formula and R,R point stereochemistry agree across three current chemical authorities and with the original compound 9 drawing. Absolute-configuration reasoning beyond the abstract and the raw spectra has not been independently reconstructed; the axial configuration is not explicitly represented.

### Minted concept, exact chemical xrefs and broader parent

grounding: supported. Targets: antibioticmech:aro-63b276648e.

The ARO mint reproduces; all four native identifiers resolve to the named compound and the broader polyketide parent resolves correctly. No drug-level or document accession is present as an exact molecular link.

### Antibacterial eligibility and quantitative limits

evidence: supported. Targets: antibioticmech:aro-63b276648e.

The original isolation/antibacterial abstract and exact database activity extracts support the named congener as an antibacterial. Quantitative values remain explicitly database-tier; they are not promoted to independently inspected original-table observations. The Q MRSA result is specific to shhs-A1 and the database-described method.

### Collective definition and congener scope

scope: supported. Targets: antibioticmech:aro-63b276648e.

The native definition explicitly describes congeners collectively and its adopted primary repeats that context. It should not be read as evidence that this individual compound was tested against VRE or in resistance selection. The exact antibacterial classification has support beyond family membership.

### Individual resistance-barrier claim

evidence: unknown. Targets: antibioticmech:aro-63b276648e.

No Q-specific passage or resistance mechanism is established by the inspected sources. The record has no resistance items, and a future individual assertion would need exact evidence.

### Target, mode and causal assertions

evidence: unknown. Targets: antibioticmech:aro-63b276648e.

No native named protein, pathway, mode, target or causal graph is asserted, so a structured adapter is not applicable to a native protein claim. Biosynthetic regulator results and fasamycin target assignments do not establish a P/Q antibacterial target.

### Original producer versus family producer

evidence: supported. Targets: antibioticmech:aro-63b276648e.

The original 2020 abstract identifies the exact new P/Q compounds from Streptomyces sp. KIB-1414. Do not substitute S. formicae KY5 from the different adopted 2021 study. Native has no producer annotation; detailed production conditions remain limited by main-text access.

### Optional evidence and unresolved structural depth

completeness: unknown. Targets: antibioticmech:aro-63b276648e.

Activity and producer annotations could be added after appropriate source adjudication; their absence is not a required-field defect. No Q-specific structure correction follows from the 2026 congener revisions. No clinical, dataset, discussion or regulatory claim is present.

### Status, history and maintained owners

provenance: supported. Targets: antibioticmech:aro-63b276648e.

The entire native record and all three seed/reseed events were read. Thirteen initial captures remain preserved in twenty-three expanded inputs; actual ARO and PubChem owners were traced. SEEDED status is retained, and no native field or history event was changed.

### Deterministic native checks

schema: supported. Targets: antibioticmech:aro-63b276648e.

Schema, strict, molecular consistency and source mint checks pass. Scientific access limits remain separate from deterministic validation.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optional future curation: recover the original 2020 main text and adjudicate exact formicamycin Q activity, production and structural reasoning before adding primary observations.

- Verify the original compound-number mapping, table entries and full method, preserving exact units, relation, strain and Not Determined states. Keep ChEMBL evidence labeled as database evidence until independently verified.
- Retain Streptomyces sp. KIB-1414 as the source organism at the documented resolution; do not import KY5 production or C/J/L passage results.
- Reconcile any future exact P/Q structure evidence directly, rather than applying B/D/I corrections by analogy. Preserve the current source agreement and the original assignment history.
- Use the validated curation writer and accurate curation history only in a separately authorized task; optional fields do not require completion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/formicamycin-q.yaml; Entire exact native record and all three history events | supports | Formicamycin Q is ARO-minted, SEEDED and filed as antibacterial. It contains the collective congener definition citing PMID:33440167, broader polyketide parent ARO:3005171, neutral PubChem structure, four chemical xrefs and one source concept. No synonym, activity observation, molecular target, resistance item, producer, clinical product, causal graph or curator mechanism claim is asserted. |
| owners | 472-inputs-expanded.json; 471472-raw-rows.json; Full ARO row 482, PubChem enrichment row 193, exact decisions/curator/ChEBI matching | supports | The ARO raw row supplies identity, definition, class and chemical links; the PubChem structure row supplies molecular properties. Exact ChEBI inventory, decision and curator override matches were absent from the inspected rows. The original thirteen captures were verified before judgment, and actual ARO/PubChem owners plus the enrichment transform were appended with unchanged hashes. |
| search | 471472-local-paths.txt; Ignored-inclusive name and source identifier search | context_only | Search included hidden and ignored files in data, curation, conf, scripts, src, reports and reviews. Exact source rows were inspected; missing optional collections are not native schema defects. |
| aro | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3007595; Current ARO concept, definition citation and xrefs | supports | The ARO concept resolves to formicamycin Q, the native collective definition and PMID:33440167. Its ChEBI, ChEMBL and PubChem links match the native identifiers. Source family wording is not an exact-congener mechanism experiment. |
| parent | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3005171; ARO:3005171 current label and definition | supports | The asserted parent resolves to polyketide with antibiotic activity, a broader chemical/activity class. No class is misused as an exact chemical xref. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/226647/; CHEBI:226647 default structure | supports | The current authority graph exactly reproduces native key CZOSIVQZBIQJDQ-IIMAJNMQSA-N, neutral formula and two assigned R stereocentres. The ordinary structure strings do not explicitly encode the biaryl axis; absence of that encoding is not evidence of a racemate. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/156018422/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON; PubChem CID 156018422 properties | supports | The current authority graph exactly reproduces native key CZOSIVQZBIQJDQ-IIMAJNMQSA-N, neutral formula and two assigned R stereocentres. The ordinary structure strings do not explicitly encode the biaryl axis; absence of that encoding is not evidence of a racemate. |
| chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL4643580.json; CHEMBL4643580 molecular structure | supports | The current authority graph exactly reproduces native key CZOSIVQZBIQJDQ-IIMAJNMQSA-N, neutral formula and two assigned R stereocentres. The ordinary structure strings do not explicitly encode the biaryl axis; absence of that encoding is not evidence of a racemate. |
| chemistry | 472-chemistry.json; RDKit 2026.03.5; existing 019 interpreter against 048 cwd | supports | Native SMILES and InChI mutually reproduce the stored key, formula, charge, reported mass precision and R,R centres. The ARO source mint reproduces. These checks establish internal consistency rather than independent natural-product structure determination. |
| xref-comparison | 471472-xref-check.json; Independent four-way molecular comparison for Q | supports | Native, current ChEBI, PubChem and ChEMBL structures were parsed independently and yield the same key and assigned point stereochemistry. |
| primary2020 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28EXT_ID%3A33440167%20OR%20EXT_ID%3A32519857%29%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=100; PMID:32519857; DOI:10.1021/acs.jnatprod.0c00161; complete original abstract | supports | The original abstract identifies formicamycins N–Q as compounds 6–9, mapping Q to 9, isolated from rhizospheric soil-derived Streptomyces sp. KIB-1414. It reports NMR/HRMS and comparative CD structure elucidation and antibacterial activity across the collected compounds. Its collective 0.20–50 µg/mL range does not assign an exact MIC or every tested organism to Q. |
| primary2020-si | https://ndownloader.figshare.com/files/23064317; Original SI contents and exact compound 9 structure/NMR/HRMS pages S40–S43, Figures S58–S64 | supports | The compound 9 drawing actually viewed on S40 shows two chlorines, both E-ring methoxy groups and a third methoxy on the other substituted aromatic ring, with the two wedged bridgehead groups. S43 HRESIMS actually viewed gives neutral formula C30H28Cl2O8 and [M−H]− measured/calculated 585.1088. S40 displays 1H/13C NMR in CDCl3; the SI indexes HSQC, HMBC, COSY and ROESY on S41–42. These drawings and mass assignments agree with native. The supplied SI contains spectra and selected analogue NMR tables; it does not provide the missing original MIC table or complete extraction/assay methods. |
| publisher-access | https://pubs.acs.org/doi/10.1021/acs.jnatprod.0c00161; Actual direct publisher retrieval attempt | context_only | The DOI resolves to the 2020 paper, but this direct publisher request returned HTTP403. The original main-text assay table and detailed methods were not inspected; ChEMBL extracts below remain database evidence. |
| chembl-document | https://www.ebi.ac.uk/chembl/api/data/document/CHEMBL4622887.json; CHEMBL4622887 publication metadata | supports | ChEMBL document CHEMBL4622887 resolves to Yuan et al., J Nat Prod 83:1919–1924 (2020), DOI 10.1021/acs.jnatprod.0c00161, PMID 32519857. This links the activity extracts to the correct original paper but is not access to its full table. |
| chembl-activity | https://www.ebi.ac.uk/chembl/api/data/activity.json?molecule_chembl_id=CHEMBL4643580&amp;limit=1000; All four activity entries for CHEMBL4643580; document CHEMBL4622887 | supports | The exact Q extract reports MRSA shhs-A1 MIC 25, S. aureus ATCC 6538 MIC 6.25, B. subtilis ATCC 6633 MIC 25 and E. coli ATCC 8099 MIC 25 µg/mL. Each numeric relation is equality; descriptions specify 16 h broth microdilution. ChEMBL standardizes the ATCC 6633 target to B. spizizenii while the assay description says B. subtilis; retain that source-label distinction. Medium, inoculum, solvent and original table footnotes were not verified from primary methods. |
| adopted2021 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8062789/fullTextXML; Sole adopted PMID:33440167; original introduction, Table 2, discussion and relevant STAR Methods | supports | The adopted paper concerns engineering production in S. formicae KY5. Its introduction/discussion cites family MRSA/VRE and resistance-barrier context from 2017. Table 2 measures formicamycins J, R and S, not P or Q. The BGC regulator ForJ is distinct from compound J, and regulation of biosynthesis is not evidence of a formicamycin drug target. This source does not establish KIB-1414 P/Q production conditions or exact P/Q MICs. |
| passage-boundary | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5414599/fullTextXML; Original 2017 resistance-selection paragraph and compound numbering | context_only | The primary 2017 discovery tested formicamycins C, J and L (compounds 6, 13 and 15) in MRSA serial passage, not the later-discovered P/Q. That experiment supports the collective context of the ARO definition but cannot establish a P/Q-specific resistance barrier. |
| revision-boundary | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13532170/fullTextXML; Original2026 structural-revision results, tables and named congener scope | context_only | The 2026 paper establishes methoxy corrections for formicamycins B, D and I and directly crystallizes G, H, I, J, R and S. It does not directly examine P or Q. Q has both E-ring methoxy groups; the single-methoxy revision of other congeners does not change its constitution by analogy. No wrong-identity finding is inferred from the other compounds. |
| gates | 472-focused-results.json; Actual focused chemistry, schema and strict checks | supports | All focused executions exited 0. Native schema/strict used 048; chemistry used the existing 019 RDKit interpreter against 048 cwd. All captured input hashes were rechecked. |

## Limits And Additional Notes

- The 2020 primary main text returned 403. Complete original abstract and exact-congener SI structure/NMR and mass pages were inspected, but original assay table, detailed extraction/production methods, yields, full assay conditions and absolute-configuration argument remain unavailable. The raw 2D correlations and CD calculations were not independently reanalyzed.
- The exact ChEMBL activity extract is database-tier evidence. The assay description uses B. subtilis ATCC 6633 while its normalized organism is B. spizizenii; no taxonomic or clinical-breakpoint inference is made.
- The 2021 adopted original was read for its relevant introduction, production context, Table 2 and methods/discussion. It measures other congeners and does not fill the exact P/Q primary assay gap.
- The 2026 structures of other congeners are not direct P/Q structure determinations. The ordinary stored strings omit explicit axial stereo; this does not imply a racemate.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native or maintained file was edited. All 23 inputs and preserved 13 original hashes were rechecked. Optional links, tags and notes were checked specifically for formicamycin Q.
- The supplementary PDF was downloaded earlier in this session and independently inspected for this exact target; its original public URL, timestamp and hash are retained.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T165331Z-formicamycin-q-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Formicamycin Q: coherent original structure with bounded primary and database
  activity evidence'
started_at: '2026-10-21T16:45:50Z'
finished_at: '2026-10-21T16:53:31Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the native record. The entire record
    and maintained source were read, independent chemistry calculated, asserted chemical
    groundings checked and exact-compound primary literature assessed with explicit
    access boundaries.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: The native neutral formicamycin Q graph agrees with the original 2020 supplementary
  drawing and current ChEBI, PubChem and ChEMBL. The original abstract identifies
  the isolated congener and producer; exact MIC extracts are available at ChEMBL database
  tier, while the original full assay table remains inaccessible. No confirmed native
  correction is identified. Family resistance claims and structural revisions of other
  congeners are not transferred to this molecule. Scientific assessment retains the
  stated evidence limits; full verification is blocked by the shared native-library
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
  - path: data/antibiotics/antibacterial/formicamycin-q.yaml
    sha256: 267d6fe15a69a97ffce7ccde068f495c73b71c4a21564da4f0cc4d6808c41da5
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
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
targets:
- target_id: antibioticmech:aro-63b276648e
  path: data/antibiotics/antibacterial/formicamycin-q.yaml
  label: formicamycin Q
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual ARO identity, definition, class and citation owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Actual PubChem structure enrichment owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem exact structure enrichment transform
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 472; thirteen original input hashes preserved within twenty-three
    expanded inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-63b276648e
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-63b276648e
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/471472-focused.py
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-63b276648e
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/formicamycin-q.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-63b276648e
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/formicamycin-q.yaml --out /private/tmp/am-review-session/472-strict.tsv
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
  - antibioticmech:aro-63b276648e
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
  - antibioticmech:aro-63b276648e
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
  - antibioticmech:aro-63b276648e
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
  - antibioticmech:aro-63b276648e
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
  - antibioticmech:aro-63b276648e
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
  - antibioticmech:aro-63b276648e
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
  - antibioticmech:aro-63b276648e
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
  - antibioticmech:aro-63b276648e
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
  - antibioticmech:aro-63b276648e
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/formicamycin-q.yaml
  locator: Entire exact native record and all three history events
  accessed_at: '2026-10-21T16:48:38Z'
  support: supports
  summary: Formicamycin Q is ARO-minted, SEEDED and filed as antibacterial. It contains
    the collective congener definition citing PMID:33440167, broader polyketide parent
    ARO:3005171, neutral PubChem structure, four chemical xrefs and one source concept.
    No synonym, activity observation, molecular target, resistance item, producer,
    clinical product, causal graph or curator mechanism claim is asserted.
- evidence_id: owners
  kind: record_content
  reference: 472-inputs-expanded.json; 471472-raw-rows.json
  locator: Full ARO row 482, PubChem enrichment row 193, exact decisions/curator/ChEBI
    matching
  accessed_at: '2026-10-21T16:48:38Z'
  support: supports
  summary: The ARO raw row supplies identity, definition, class and chemical links;
    the PubChem structure row supplies molecular properties. Exact ChEBI inventory,
    decision and curator override matches were absent from the inspected rows. The
    original thirteen captures were verified before judgment, and actual ARO/PubChem
    owners plus the enrichment transform were appended with unchanged hashes.
  snapshot_sha256: 9798bc12850ab8efb0cdff018f84163098f33b736feb219e72df8844183162e9
- evidence_id: search
  kind: search
  reference: 471472-local-paths.txt
  locator: Ignored-inclusive name and source identifier search
  accessed_at: '2026-10-21T16:48:38Z'
  support: context_only
  summary: Search included hidden and ignored files in data, curation, conf, scripts,
    src, reports and reviews. Exact source rows were inspected; missing optional collections
    are not native schema defects.
  search_scope: rg --no-ignore --hidden -il 'formicamycin[ -][pq]|300759[05]|22664[27]'
    data curation conf scripts src reports reviews
  snapshot_sha256: 574d84215e1a0241aa75bdc1680701141628445c1ab896f4463a0b79d9f669e8
- evidence_id: aro
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3007595
  locator: Current ARO concept, definition citation and xrefs
  accessed_at: '2026-10-21T16:46:46.817837Z'
  support: supports
  summary: The ARO concept resolves to formicamycin Q, the native collective definition
    and PMID:33440167. Its ChEBI, ChEMBL and PubChem links match the native identifiers.
    Source family wording is not an exact-congener mechanism experiment.
  snapshot_sha256: 2631a17368f5a443a2383e2dcda5582b5209c900b44760958c18e845d7787dcf
- evidence_id: parent
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3005171
  locator: ARO:3005171 current label and definition
  accessed_at: '2026-10-21T16:38:20.266771Z'
  support: supports
  summary: The asserted parent resolves to polyketide with antibiotic activity, a
    broader chemical/activity class. No class is misused as an exact chemical xref.
  snapshot_sha256: b1b803e251ea13f0277e11cce1fdf5a7343d52360231e7ad438fcd597778caff
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/226647/
  locator: CHEBI:226647 default structure
  accessed_at: '2026-10-21T16:46:46.463748Z'
  support: supports
  summary: The current authority graph exactly reproduces native key CZOSIVQZBIQJDQ-IIMAJNMQSA-N,
    neutral formula and two assigned R stereocentres. The ordinary structure strings
    do not explicitly encode the biaryl axis; absence of that encoding is not evidence
    of a racemate.
  snapshot_sha256: 3b82067eb0a17f455ccf8b6426d4880d429646c2f26448b241dc4f53f36955c3
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/156018422/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON
  locator: PubChem CID 156018422 properties
  accessed_at: '2026-10-21T16:46:46.796176Z'
  support: supports
  summary: The current authority graph exactly reproduces native key CZOSIVQZBIQJDQ-IIMAJNMQSA-N,
    neutral formula and two assigned R stereocentres. The ordinary structure strings
    do not explicitly encode the biaryl axis; absence of that encoding is not evidence
    of a racemate.
  snapshot_sha256: 4aac2967de40cc82c586cb57d951f0e3eb07f96e630397203656a6fa9b2c57d9
- evidence_id: chembl
  kind: authority
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL4643580.json
  locator: CHEMBL4643580 molecular structure
  accessed_at: '2026-10-21T16:46:47.143137Z'
  support: supports
  summary: The current authority graph exactly reproduces native key CZOSIVQZBIQJDQ-IIMAJNMQSA-N,
    neutral formula and two assigned R stereocentres. The ordinary structure strings
    do not explicitly encode the biaryl axis; absence of that encoding is not evidence
    of a racemate.
  snapshot_sha256: fc17f7bd1ad415d24a014a7f680f3b5c2abdfa03e6bd6566e265709ad323a327
- evidence_id: chemistry
  kind: validation
  reference: 472-chemistry.json
  locator: RDKit 2026.03.5; existing 019 interpreter against 048 cwd
  accessed_at: '2026-10-21T16:48:38Z'
  support: supports
  summary: Native SMILES and InChI mutually reproduce the stored key, formula, charge,
    reported mass precision and R,R centres. The ARO source mint reproduces. These
    checks establish internal consistency rather than independent natural-product
    structure determination.
  snapshot_sha256: 4469f266c9ef862c64d4e707fa7e350073920b5ce40f4c6300e8da4cfb73db33
- evidence_id: xref-comparison
  kind: validation
  reference: 471472-xref-check.json
  locator: Independent four-way molecular comparison for Q
  accessed_at: '2026-10-21T16:48:38Z'
  support: supports
  summary: Native, current ChEBI, PubChem and ChEMBL structures were parsed independently
    and yield the same key and assigned point stereochemistry.
  snapshot_sha256: d5fd1be5fb9ce45834b92d42dceb29b0e3a8446f74dce32c1cf5f7093aa7c32e
- evidence_id: primary2020
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28EXT_ID%3A33440167%20OR%20EXT_ID%3A32519857%29%20AND%20SRC%3AMED&format=json&resultType=core&pageSize=100
  locator: PMID:32519857; DOI:10.1021/acs.jnatprod.0c00161; complete original abstract
  accessed_at: '2026-10-21T16:46:47.440891Z'
  support: supports
  summary: The original abstract identifies formicamycins N–Q as compounds 6–9, mapping
    Q to 9, isolated from rhizospheric soil-derived Streptomyces sp. KIB-1414. It
    reports NMR/HRMS and comparative CD structure elucidation and antibacterial activity
    across the collected compounds. Its collective 0.20–50 µg/mL range does not assign
    an exact MIC or every tested organism to Q.
  snapshot_sha256: 93d9b8cef14e7bfaa9b6f4205e7cf968063a829fb2ee1a6febd040bff3d539c2
- evidence_id: primary2020-si
  kind: primary_source
  reference: https://ndownloader.figshare.com/files/23064317
  locator: Original SI contents and exact compound 9 structure/NMR/HRMS pages S40–S43,
    Figures S58–S64
  accessed_at: '2026-10-21T15:50:36.814181Z'
  support: supports
  summary: The compound 9 drawing actually viewed on S40 shows two chlorines, both
    E-ring methoxy groups and a third methoxy on the other substituted aromatic ring,
    with the two wedged bridgehead groups. S43 HRESIMS actually viewed gives neutral
    formula C30H28Cl2O8 and [M−H]− measured/calculated 585.1088. S40 displays 1H/13C
    NMR in CDCl3; the SI indexes HSQC, HMBC, COSY and ROESY on S41–42. These drawings
    and mass assignments agree with native. The supplied SI contains spectra and selected
    analogue NMR tables; it does not provide the missing original MIC table or complete
    extraction/assay methods.
  snapshot_sha256: 541af1eb06e40a6048ad327ca0c61a7eae45200a93c2541e98ee7a6a444c6d9b
- evidence_id: publisher-access
  kind: search
  reference: https://pubs.acs.org/doi/10.1021/acs.jnatprod.0c00161
  locator: Actual direct publisher retrieval attempt
  accessed_at: '2026-10-21T16:46:48.134614Z'
  support: context_only
  summary: The DOI resolves to the 2020 paper, but this direct publisher request returned
    HTTP403. The original main-text assay table and detailed methods were not inspected;
    ChEMBL extracts below remain database evidence.
  snapshot_sha256: d9585d74443111beefc73b076dcc5fee15d90bb4ddc5e612e2b44a842020d034
  search_scope: Direct free public retrieval of https://pubs.acs.org/doi/10.1021/acs.jnatprod.0c00161
    on 2026-10-21; no paid access attempted.
- evidence_id: chembl-document
  kind: database
  reference: https://www.ebi.ac.uk/chembl/api/data/document/CHEMBL4622887.json
  locator: CHEMBL4622887 publication metadata
  accessed_at: '2026-10-21T16:43:25Z'
  support: supports
  summary: ChEMBL document CHEMBL4622887 resolves to Yuan et al., J Nat Prod 83:1919–1924
    (2020), DOI 10.1021/acs.jnatprod.0c00161, PMID 32519857. This links the activity
    extracts to the correct original paper but is not access to its full table.
  snapshot_sha256: 971e7ee9656ee285fbf53ec2c8f09957ada4bbba6211958c90c3af329295c324
- evidence_id: chembl-activity
  kind: database
  reference: https://www.ebi.ac.uk/chembl/api/data/activity.json?molecule_chembl_id=CHEMBL4643580&limit=1000
  locator: All four activity entries for CHEMBL4643580; document CHEMBL4622887
  accessed_at: '2026-10-21T16:46:47.236631Z'
  support: supports
  summary: The exact Q extract reports MRSA shhs-A1 MIC 25, S. aureus ATCC 6538 MIC
    6.25, B. subtilis ATCC 6633 MIC 25 and E. coli ATCC 8099 MIC 25 µg/mL. Each numeric
    relation is equality; descriptions specify 16 h broth microdilution. ChEMBL standardizes
    the ATCC 6633 target to B. spizizenii while the assay description says B. subtilis;
    retain that source-label distinction. Medium, inoculum, solvent and original table
    footnotes were not verified from primary methods.
  snapshot_sha256: 553e1149539be599da7f9cf38d312e39d5825d20ae93f6d6282a2f715173d407
- evidence_id: adopted2021
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8062789/fullTextXML
  locator: Sole adopted PMID:33440167; original introduction, Table 2, discussion
    and relevant STAR Methods
  accessed_at: '2026-10-21T16:29:46Z'
  support: supports
  summary: The adopted paper concerns engineering production in S. formicae KY5. Its
    introduction/discussion cites family MRSA/VRE and resistance-barrier context from
    2017. Table 2 measures formicamycins J, R and S, not P or Q. The BGC regulator
    ForJ is distinct from compound J, and regulation of biosynthesis is not evidence
    of a formicamycin drug target. This source does not establish KIB-1414 P/Q production
    conditions or exact P/Q MICs.
  snapshot_sha256: e55b2fd0ccc375fd9d04e77b0102d8588ed7bab670427d6124477a3d2c38cdae
- evidence_id: passage-boundary
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5414599/fullTextXML
  locator: Original 2017 resistance-selection paragraph and compound numbering
  accessed_at: '2026-10-21T16:30:15Z'
  support: context_only
  summary: The primary 2017 discovery tested formicamycins C, J and L (compounds 6,
    13 and 15) in MRSA serial passage, not the later-discovered P/Q. That experiment
    supports the collective context of the ARO definition but cannot establish a P/Q-specific
    resistance barrier.
  snapshot_sha256: 741a682eefa78fdbcfb69b76eddd1d23df3e5bffbb60b2c7df34b51d923083d5
- evidence_id: revision-boundary
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13532170/fullTextXML
  locator: Original2026 structural-revision results, tables and named congener scope
  accessed_at: '2026-10-21T16:29:46Z'
  support: context_only
  summary: The 2026 paper establishes methoxy corrections for formicamycins B, D and
    I and directly crystallizes G, H, I, J, R and S. It does not directly examine
    P or Q. Q has both E-ring methoxy groups; the single-methoxy revision of other
    congeners does not change its constitution by analogy. No wrong-identity finding
    is inferred from the other compounds.
  snapshot_sha256: 55796020973e571658d3a02c0080a44cff02e2bd6113dbfe0c942357eb04354d
- evidence_id: gates
  kind: validation
  reference: 472-focused-results.json
  locator: Actual focused chemistry, schema and strict checks
  accessed_at: '2026-10-21T16:48:38Z'
  support: supports
  summary: All focused executions exited 0. Native schema/strict used 048; chemistry
    used the existing 019 RDKit interpreter against 048 cwd. All captured input hashes
    were rechecked.
  snapshot_sha256: 76164fe4454799e71d6ae251cbe056f81b30ade28d291281789cb9fdc24f85be
assessments:
- assessment_id: identity
  area: identity
  topic: Exact molecular form and original assignment
  outcome: supported
  summary: The neutral Q graph, formula and R,R point stereochemistry agree across
    three current chemical authorities and with the original compound 9 drawing. Absolute-configuration
    reasoning beyond the abstract and the raw spectra has not been independently reconstructed;
    the axial configuration is not explicitly represented.
  target_ids:
  - antibioticmech:aro-63b276648e
  evidence_ids:
  - native
  - chemistry
  - xref-comparison
  - primary2020
  - primary2020-si
- assessment_id: grounding
  area: grounding
  topic: Minted concept, exact chemical xrefs and broader parent
  outcome: supported
  summary: The ARO mint reproduces; all four native identifiers resolve to the named
    compound and the broader polyketide parent resolves correctly. No drug-level or
    document accession is present as an exact molecular link.
  target_ids:
  - antibioticmech:aro-63b276648e
  evidence_ids:
  - owners
  - aro
  - parent
  - chebi
  - pubchem
  - chembl
  - xref-comparison
- assessment_id: activity
  area: evidence
  topic: Antibacterial eligibility and quantitative limits
  outcome: supported
  summary: The original isolation/antibacterial abstract and exact database activity
    extracts support the named congener as an antibacterial. Quantitative values remain
    explicitly database-tier; they are not promoted to independently inspected original-table
    observations. The Q MRSA result is specific to shhs-A1 and the database-described
    method.
  target_ids:
  - antibioticmech:aro-63b276648e
  evidence_ids:
  - primary2020
  - primary2020-si
  - chembl-document
  - chembl-activity
  - publisher-access
- assessment_id: definition
  area: scope
  topic: Collective definition and congener scope
  outcome: supported
  summary: The native definition explicitly describes congeners collectively and its
    adopted primary repeats that context. It should not be read as evidence that this
    individual compound was tested against VRE or in resistance selection. The exact
    antibacterial classification has support beyond family membership.
  target_ids:
  - antibioticmech:aro-63b276648e
  evidence_ids:
  - native
  - aro
  - adopted2021
  - chembl-activity
  - passage-boundary
- assessment_id: resistance
  area: evidence
  topic: Individual resistance-barrier claim
  outcome: unknown
  summary: No Q-specific passage or resistance mechanism is established by the inspected
    sources. The record has no resistance items, and a future individual assertion
    would need exact evidence.
  target_ids:
  - antibioticmech:aro-63b276648e
  evidence_ids:
  - native
  - passage-boundary
  - adopted2021
- assessment_id: mechanism
  area: evidence
  topic: Target, mode and causal assertions
  outcome: unknown
  summary: No native named protein, pathway, mode, target or causal graph is asserted,
    so a structured adapter is not applicable to a native protein claim. Biosynthetic
    regulator results and fasamycin target assignments do not establish a P/Q antibacterial
    target.
  target_ids:
  - antibioticmech:aro-63b276648e
  evidence_ids:
  - native
  - adopted2021
  - primary2020
- assessment_id: producer
  area: evidence
  topic: Original producer versus family producer
  outcome: supported
  summary: The original 2020 abstract identifies the exact new P/Q compounds from
    Streptomyces sp. KIB-1414. Do not substitute S. formicae KY5 from the different
    adopted 2021 study. Native has no producer annotation; detailed production conditions
    remain limited by main-text access.
  target_ids:
  - antibioticmech:aro-63b276648e
  evidence_ids:
  - primary2020
  - adopted2021
  - publisher-access
- assessment_id: completeness
  area: completeness
  topic: Optional evidence and unresolved structural depth
  outcome: unknown
  summary: Activity and producer annotations could be added after appropriate source
    adjudication; their absence is not a required-field defect. No Q-specific structure
    correction follows from the 2026 congener revisions. No clinical, dataset, discussion
    or regulatory claim is present.
  target_ids:
  - antibioticmech:aro-63b276648e
  evidence_ids:
  - native
  - search
  - primary2020-si
  - revision-boundary
  - publisher-access
- assessment_id: audit
  area: provenance
  topic: Status, history and maintained owners
  outcome: supported
  summary: The entire native record and all three seed/reseed events were read. Thirteen
    initial captures remain preserved in twenty-three expanded inputs; actual ARO
    and PubChem owners were traced. SEEDED status is retained, and no native field
    or history event was changed.
  target_ids:
  - antibioticmech:aro-63b276648e
  evidence_ids:
  - native
  - owners
  - gates
- assessment_id: validation
  area: schema
  topic: Deterministic native checks
  outcome: supported
  summary: Schema, strict, molecular consistency and source mint checks pass. Scientific
    access limits remain separate from deterministic validation.
  target_ids:
  - antibioticmech:aro-63b276648e
  evidence_ids:
  - gates
  - chemistry
findings: []
actions:
- action_id: A1
  description: 'Optional future curation: recover the original 2020 main text and
    adjudicate exact formicamycin Q activity, production and structural reasoning
    before adding primary observations.'
  finding_ids: []
  target_ids:
  - antibioticmech:aro-63b276648e
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/formicamycin-q.yaml
    role: Future curator-owned activity_spectrum, producer and evidence annotations
  acceptance_checks:
  - Verify the original compound-number mapping, table entries and full method, preserving
    exact units, relation, strain and Not Determined states. Keep ChEMBL evidence
    labeled as database evidence until independently verified.
  - Retain Streptomyces sp. KIB-1414 as the source organism at the documented resolution;
    do not import KY5 production or C/J/L passage results.
  - Reconcile any future exact P/Q structure evidence directly, rather than applying
    B/D/I corrections by analogy. Preserve the current source agreement and the original
    assignment history.
  - Use the validated curation writer and accurate curation history only in a separately
    authorized task; optional fields do not require completion.
limitations:
- The 2020 primary main text returned 403. Complete original abstract and exact-congener
  SI structure/NMR and mass pages were inspected, but original assay table, detailed
  extraction/production methods, yields, full assay conditions and absolute-configuration
  argument remain unavailable. The raw 2D correlations and CD calculations were not
  independently reanalyzed.
- The exact ChEMBL activity extract is database-tier evidence. The assay description
  uses B. subtilis ATCC 6633 while its normalized organism is B. spizizenii; no taxonomic
  or clinical-breakpoint inference is made.
- The 2021 adopted original was read for its relevant introduction, production context,
  Table 2 and methods/discussion. It measures other congeners and does not fill the
  exact P/Q primary assay gap.
- The 2026 structures of other congeners are not direct P/Q structure determinations.
  The ordinary stored strings omit explicit axial stereo; this does not imply a racemate.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native or maintained file was edited. All 23 inputs and preserved 13 original
  hashes were rechecked. Optional links, tags and notes were checked specifically
  for formicamycin Q.
- The supplementary PDF was downloaded earlier in this session and independently inspected
  for this exact target; its original public URL, timestamp and hash are retained.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://doi.org/10.1021/acs.jnatprod.0c00161
- https://doi.org/10.1016/j.chembiol.2020.12.011
tags:
- formicamycin-q
- polyketide
- bounded-primary-access
```
