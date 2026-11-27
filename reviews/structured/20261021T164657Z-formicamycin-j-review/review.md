# Formicamycin J: crystal-confirmed constitution with congener-specific antibacterial and passage evidence

- Review: 20261021T164657Z-formicamycin-j-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T16:37:16Z
- Finished UTC: 2026-10-21T16:46:57Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Native constitution and two R stereocentres agree with current chemical authorities and the unchanged structure confirmed by the 2026 formicamycin J crystal. Original J-specific MIC and serial-passage experiments support the antibacterial classification, with assay and strain limits. No confirmed native correction is identified. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 465; thirteen original input hashes preserved within twenty-three expanded inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-274dd73c04 | data/antibiotics/antibacterial/formicamycin-j.yaml | generated | formicamycin J |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-274dd73c04 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-274dd73c04 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-274dd73c04 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | antibioticmech:aro-274dd73c04 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-274dd73c04 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-274dd73c04 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-274dd73c04 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-274dd73c04 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-274dd73c04 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-274dd73c04 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-274dd73c04 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-274dd73c04 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact congener, constitution and chemical form

identity: supported. Targets: antibioticmech:aro-274dd73c04.

Native J constitution, neutral formula and R,R centres match the unchanged crystal-confirmed molecule. Axial configuration is established in the primary paper but is not explicit in the ordinary stored strings; unencoded axis is not a racemate claim.

### Minted ARO identity and exact chemical xrefs

grounding: supported. Targets: antibioticmech:aro-274dd73c04.

The ARO mint reproduces and all three chemical identifiers resolve to the named congener with mutually coherent structure data. The broader polyketide parent is appropriate. No drug-level accession is present.

### Antibacterial eligibility and family definition

scope: supported. Targets: antibioticmech:aro-274dd73c04.

Primary isolated-compound results support the named natural congener as an antibacterial polyketide. The class is supported by exact-congener measurements rather than solely by family membership. The native definition explicitly describes congeners collectively and its resistance wording must remain family context.

### MIC endpoints, original material and organism scope

evidence: supported. Targets: antibioticmech:aro-274dd73c04.

The original Table 1 compound mapping and SI assay conditions were verified. Qualifiers, µM units, unnamed MRSA isolate, E. faecium B16.06226 and limited B. subtilis identification must remain explicit. The additional2021 J MICs are a separate assay in µg/mL against named ATCC strains.

### Resistance-selection claim

evidence: supported. Targets: antibioticmech:aro-274dd73c04.

J was directly included in the 2017 serial-passage experiment, supporting failure to select elevated MIC under the reported conditions. It is not proof of universal resistance impossibility.

### Mode, molecular target and causal scope

evidence: unknown. Targets: antibioticmech:aro-274dd73c04.

No native mode, molecular target or causal graph is asserted. The original authors leave the formicamycin antibacterial target unresolved. Fasamycin FabF inhibition and biosynthetic For regulators must not be converted into drug targets. The native has no named protein/pathway claim triggering a structured-adapter cross-check.

### Original production material

evidence: supported. Targets: antibioticmech:aro-274dd73c04.

Original isolation supports S. formicae KY5 as producer. I/J were purified from standard solid MS cultures; retain exact compound and culture conditions if producer claims are later added. No native producer claim is present.

### Optional observations, datasets and discussions

completeness: unknown. Targets: antibioticmech:aro-274dd73c04.

Activity and producer evidence could be curated with exact material and assay context; their absence is not a required-field error. Do not force a mechanism or causal chain from the available inhibition or biosynthesis results. No clinical, regulatory, dataset or discussion assertion is present to validate.

### Source ownership, status and history

provenance: supported. Targets: antibioticmech:aro-274dd73c04.

All native fields and three seed/reseed events were read. The thirteen initial captures were verified before judgment and ten actual-owner/guidance inputs appended. SEEDED status is retained; neither a passing contract nor this review promotes it to REVIEWED.

### Actual focused native checks

schema: supported. Targets: antibioticmech:aro-274dd73c04.

Focused schema, strict and chemical consistency checks pass. They complement, but do not replace, the primary evidence audit.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optional future curation: add exact formicamycin J activity and producer evidence with the original assay/material boundaries.

- Use original 2017 compound 13 and its qualifiers/µM values with SI strain and method details; attach claim-level citations.
- Keep resistance passage limited to compounds 6, 13 and 15; preserve the 2021 J assay separately if used. Do not infer a direct antibacterial target from the for biosynthetic genes.
- Use the validated native curation writer and accurate LLM-assisted curation event only in a separately authorized curation task; absent optional fields do not require a change.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/formicamycin-j.yaml; Initial target capture; entire native record independently read | supports | The exact J record is an ARO-minted SEEDED antibacterial with one family-level definition citing PMID:33440167, broader polyketide parent ARO:3005171, three chemical xrefs, neutral PubChem structure and three seed/reseed events. No synonyms, activity observations, molecular targets, resistance items, producer, clinical products, causal graphs or curator mechanism assertions are present. |
| owners | 465-inputs-expanded.json; 464466-raw-rows.json; Complete ARO row 484; PubChem structure row 195; exact decisions and curator-inventory matching | supports | ARO owns the label, definition, classification and chemical links; PubChem enrichment owns the molecular graph. The exact target has no adopted ChEBI inventory row or exact decision/curator override in the inspected inputs. Actual raw ARO/PubChem owners and enrichment transform were captured before detailed judgment; all original thirteen hashes were preserved. The native minted identifier independently reproduces the ARO source-id mint. |
| local-search | 464466-local-paths.txt; Ignored-inclusive name, ARO and ChEBI search | context_only | Search covered data, curation, conf, scripts, src, reports and reviews, including hidden and ignored files. Exact matching rows were read. Missing optional collections are not treated as schema defects. |
| aro | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3007597; ARO:3007597 label, definition, definition citation and xrefs | supports | Current ARO resolves formicamycin J, retains the same family-worded definition and PMID:33440167, and links CHEBI:219490 and PubChem 146684590. It is a database assertion, not an independently measured congener-specific resistance mechanism. |
| parent | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3005171; ARO:3005171 label and definition | supports | The asserted parent resolves to polyketide with antibiotic activity, a broader chemical/activity class; it is not asserted as an exact molecular xref. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/219490/; CHEBI:219490 default structure and identity | supports | Current ChEBI returns formicamycin J with the same neutral formula, two assigned R centres and InChIKey TVYNBNZEEHEPOX-XHDOVSQSSA-N as native. The axial configuration is not explicitly encoded in this standard structure representation. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/146684590/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON; CID 146684590 molecular properties | supports | Current PubChem exactly reproduces the native stored graph and molecular properties, key TVYNBNZEEHEPOX-XHDOVSQSSA-N. This check establishes agreement with the stored structure, subject to the primary stereochemical evidence and axial-representation limit. |
| chemistry | 465-chemistry.json; 464466-focused.py; RDKit 2026.03.5; 019 interpreter executed against 047 cwd | supports | Both native SMILES and InChI parse and mutually agree; formula, charge, reported mass precision and ARO mint checks pass. Two tetrahedral stereocentres are assigned R. Deterministic consistency does not establish correctness of a historical natural-product assignment. |
| xref-comparison | 464466-xref-check.json; 464466-xref-check.py; Independent native/ChEBI/PubChem comparison for record 465 | supports | Independent molecular parsing reproduces identical native/current ChEBI/current PubChem keys. No changed connectivity or point-stereo conflict was identified; ordinary structure strings do not explicitly express the biaryl axis. |
| lead-index | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28EXT_ID%3A33440167%20OR%20DOI%3A10.1039/C6SC04265A%20OR%20DOI%3A10.1021/acs.jnatprod.6c00145%29%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=100; Complete original abstracts and bibliographic metadata for PMID:33440167, PMID:28507698 and PMID:41988676 | context_only | The sole adopted PMID resolves to the 2021 biosynthetic regulation paper. Original 2017 discovery and 2026 structural-revision papers were followed and inspected as primary sources; the complete three abstracts were read. Abstracts are not substituted for the tables, structures and methods inspected below. |
| primary2017 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5414599/fullTextXML; DOI:10.1039/C6SC04265A; Figure 1, Table 1, isolation, antibacterial activity and resistance-selection results | supports | Original Figure 1 assigns formicamycin J as compound 13. Table 1 reports B. subtilis &lt;20, clinical MRSA 0.625 and VRE 1.25 µM for isolated 13. Compound 13 was also among the three congeners tested for MRSA resistance selection; no increased MIC was observed under that experiment. The inequality qualifiers are retained. The paper leaves the formicamycin molecular target unresolved; the established fasamycin FabF target is not automatically assigned to formicamycins. |
| primary2017-si | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5414599/supplementaryFiles; SI sections 1b, 1e and 1g; pp. 2–5, 47–50 and 56 | supports | J was isolated as 3 mg; original 1H/13C/2D NMR and HRMS gave C30H26Cl4O8, [M+H]+ observed 655.0464. Producer S. formicae KY5 was grown on soya-flour mannitol agar at 30°C; I/J used extraction and repeated chromatographic purification from the standard MS culture. MICs used 1 mL LB without NaCl in 24-well plates, starting OD600 0.08–0.15, 40 µL stock in water or methanol, static 30°C overnight and absence of observable growth. VRE was E. faecium B16.06226; MRSA was an unnamed hospital patient isolate validated by the source-described test; B. subtilis laboratory strain identifier is not given. Exact antibiotic susceptibility cannot be generalized to the species. |
| primary2017-figure | https://doi.org/10.1039/C6SC04265A; Original Figure 1 actually viewed; substituent table rows 12, 13 and 14 | supports | Compound13 has four chlorines and both ortho and para E-ring methoxy groups. It is distinct from compound 12 and from the brominated compound 14. Figure numbering is specific to 2017 and differs from 2026. |
| passage2017 | https://doi.org/10.1039/C6SC04265A; Main resistance-selection results; SI section 1g, p.56 | supports | The original serial-passage experiment selected compounds 6, 13 and 15 only (C, J and L). SI specifies MRSA exposure to 0.35, 0.1 and 0.4 µg/mL respectively, overnight growth then a further 19 generations and repeat MIC determination, with a no-formicamycin control. No MIC rise was detected in the reported experiment. This supports a bounded J observation; it is not evidence that every congener prevents resistance or that no resistance mechanism can exist. |
| adopted2021 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8062789/fullTextXML; PMID:33440167; introduction/discussion, Table 2, production methods and STAR Methods MIC assay | supports | The adopted original is a biosynthetic regulatory study. Its introduction and discussion repeat family-level MRSA/VRE and resistance-barrier context from Qin 2017; regulation of production is not evidence that the regulatory proteins are drug targets. Table 2 directly tests J and gives MIC 4 µg/mL for MRSA ATCC BAA-1717 and MSSA ATCC6538P. This differs from the 2017 0.625 µM unnamed-MRSA result in isolate, method and units, so the two are preserved separately. The 2021 resazurin method uses DMSO stocks, 1–256 µg/mL in LB or TSB with 5% DMSO, culture dilutions from 0.5 McFarland, 37°C, and color read 4 h after dye addition. It does not specify a distinct medium assignment or complete pre-dye incubation duration for each displayed result. |
| revision2026 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13532170/fullTextXML; PMID:41988676; Results, Table 1 actually viewed and compound-specific X-ray crystallographic data | supports | Formicamycin J is compound 4 in this paper. Table 1 explicitly retains the structure as published, with both E-ring methoxy groups, Sa axis and 10R,19R stereocentres. CCDC 2498174 reports Flack 0.028(7), Hooft 0.024(8), and a DMSO-containing crystal of C30H26Cl4O8; lattice DMSO does not change the neutral molecular identity. |
| crystal-table | https://doi.org/10.1021/acs.jnatprod.6c00145; Table 1 image actually inspected; exact J row | supports | J row says structure as published and shows its ORTEP; the I-specific methoxy revision does not change J, which has both groups. |
| gates | 465-focused-results.json; Actual focused schema, strict and chemistry command results | supports | All three focused executions exited 0. Native schema/strict used the 047 environment; independent RDKit chemistry used the existing 019 interpreter against 047 cwd. This confirms deterministic consistency, not scientific sign-off. |

## Limits And Additional Notes

- The adopted 2021 paper was inspected at complete abstract and relevant original introduction, production, Table 2, discussion and assay-method depth. The 2017 structure/activity/results and SI exact-congener characterization, production and MIC/resistance methods were inspected. Unrelated biosynthetic experiments were not independently replicated.
- The 2026 original structural results, relevant exact-congener table/figures and crystallographic data were read; the deposited CIF coordinates and raw NMR time-domain data were not independently re-refined. J was directly crystallized; adjacent I revision is not transferred to J.
- The ordinary native structure strings do not encode the biaryl atropisomer. This is recorded as a representation limitation, not evidence of a racemate or a separate assigned wrong stereoisomer.
- Original MIC inequality symbols are retained; the 2017 unnamed MRSA and B. subtilis identifiers limit strain-level reuse. The 2021 protocol does not completely resolve per-strain medium and pre-dye incubation time. No clinical efficacy, clinical breakpoint or species-wide resistance claim is made.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Native and maintained files were not edited. All twenty-three source inputs and original captures were rechecked. Optional links, tags and notes were checked specifically for formicamycin J.
- Primary source snapshots originally fetched by root were independently read; their actual fetch timestamps and SHA256 hashes are retained. No source-authority consensus is substituted for primary structure adjudication.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T164657Z-formicamycin-j-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Formicamycin J: crystal-confirmed constitution with congener-specific antibacterial
  and passage evidence'
started_at: '2026-10-21T16:37:16Z'
finished_at: '2026-10-21T16:46:57Z'
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
summary: Native constitution and two R stereocentres agree with current chemical authorities
  and the unchanged structure confirmed by the 2026 formicamycin J crystal. Original
  J-specific MIC and serial-passage experiments support the antibacterial classification,
  with assay and strain limits. No confirmed native correction is identified. Scientific
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
  - path: data/antibiotics/antibacterial/formicamycin-j.yaml
    sha256: 9624ea40a76d107c5a8f29bc500e9abdacd7e41fb78c9a30743a1f8986ec27c5
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
- target_id: antibioticmech:aro-274dd73c04
  path: data/antibiotics/antibacterial/formicamycin-j.yaml
  label: formicamycin J
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
  selection: Queue position 465; thirteen original input hashes preserved within twenty-three
    expanded inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-274dd73c04
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-274dd73c04
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/464466-focused.py
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-274dd73c04
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/formicamycin-j.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-274dd73c04
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/formicamycin-j.yaml --out /private/tmp/am-review-session/465-strict.tsv
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
  - antibioticmech:aro-274dd73c04
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
  - antibioticmech:aro-274dd73c04
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
  - antibioticmech:aro-274dd73c04
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
  - antibioticmech:aro-274dd73c04
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
  - antibioticmech:aro-274dd73c04
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
  - antibioticmech:aro-274dd73c04
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
  - antibioticmech:aro-274dd73c04
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
  - antibioticmech:aro-274dd73c04
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
  - antibioticmech:aro-274dd73c04
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/formicamycin-j.yaml
  locator: Initial target capture; entire native record independently read
  accessed_at: '2026-10-21T16:43:44Z'
  support: supports
  summary: The exact J record is an ARO-minted SEEDED antibacterial with one family-level
    definition citing PMID:33440167, broader polyketide parent ARO:3005171, three
    chemical xrefs, neutral PubChem structure and three seed/reseed events. No synonyms,
    activity observations, molecular targets, resistance items, producer, clinical
    products, causal graphs or curator mechanism assertions are present.
  snapshot_sha256: d8f5f8138596015366e88e3d944a6d74a36594a9137ccb079779e7d4c2c238c4
- evidence_id: owners
  kind: record_content
  reference: 465-inputs-expanded.json; 464466-raw-rows.json
  locator: Complete ARO row 484; PubChem structure row 195; exact decisions and curator-inventory
    matching
  accessed_at: '2026-10-21T16:43:44Z'
  support: supports
  summary: ARO owns the label, definition, classification and chemical links; PubChem
    enrichment owns the molecular graph. The exact target has no adopted ChEBI inventory
    row or exact decision/curator override in the inspected inputs. Actual raw ARO/PubChem
    owners and enrichment transform were captured before detailed judgment; all original
    thirteen hashes were preserved. The native minted identifier independently reproduces
    the ARO source-id mint.
  snapshot_sha256: 91e8a15793d2d9ea9e3bc9128a9231efbd656ede78b22f24ce3b5efdb76409b9
- evidence_id: local-search
  kind: search
  reference: 464466-local-paths.txt
  locator: Ignored-inclusive name, ARO and ChEBI search
  accessed_at: '2026-10-21T16:43:44Z'
  support: context_only
  summary: Search covered data, curation, conf, scripts, src, reports and reviews,
    including hidden and ignored files. Exact matching rows were read. Missing optional
    collections are not treated as schema defects.
  search_scope: rg --no-ignore --hidden -il 'formicamycin[ -][ijk]|300759[678]|2194(84|90|96)'
    data curation conf scripts src reports reviews
  snapshot_sha256: c9966b2586637c621e458ecec012069041a7c4c233a6ae7e04abc61c386a678b
- evidence_id: aro
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3007597
  locator: ARO:3007597 label, definition, definition citation and xrefs
  accessed_at: '2026-10-21T16:38:19.651388Z'
  support: supports
  summary: Current ARO resolves formicamycin J, retains the same family-worded definition
    and PMID:33440167, and links CHEBI:219490 and PubChem 146684590. It is a database
    assertion, not an independently measured congener-specific resistance mechanism.
  snapshot_sha256: 622dcbe1592ac9b72f91f712d281e36018ff0241b951dafcb67ce2d8034ae67f
- evidence_id: parent
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3005171
  locator: ARO:3005171 label and definition
  accessed_at: '2026-10-21T16:38:20.266771Z'
  support: supports
  summary: The asserted parent resolves to polyketide with antibiotic activity, a
    broader chemical/activity class; it is not asserted as an exact molecular xref.
  snapshot_sha256: b1b803e251ea13f0277e11cce1fdf5a7343d52360231e7ad438fcd597778caff
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/219490/
  locator: CHEBI:219490 default structure and identity
  accessed_at: '2026-10-21T16:38:19.307267Z'
  support: supports
  summary: Current ChEBI returns formicamycin J with the same neutral formula, two
    assigned R centres and InChIKey TVYNBNZEEHEPOX-XHDOVSQSSA-N as native. The axial
    configuration is not explicitly encoded in this standard structure representation.
  snapshot_sha256: d744e36d5f9ab9f9f85f96e06552492d1c4ee8b65a58a35e30cbbc142eff3c49
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/146684590/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON
  locator: CID 146684590 molecular properties
  accessed_at: '2026-10-21T16:38:19.307327Z'
  support: supports
  summary: Current PubChem exactly reproduces the native stored graph and molecular
    properties, key TVYNBNZEEHEPOX-XHDOVSQSSA-N. This check establishes agreement
    with the stored structure, subject to the primary stereochemical evidence and
    axial-representation limit.
  snapshot_sha256: d8aee128d37406eddb955f1d3f8e85a476dfc705bdbbea3298b99a296a8a8513
- evidence_id: chemistry
  kind: validation
  reference: 465-chemistry.json; 464466-focused.py
  locator: RDKit 2026.03.5; 019 interpreter executed against 047 cwd
  accessed_at: '2026-10-21T16:43:44Z'
  support: supports
  summary: Both native SMILES and InChI parse and mutually agree; formula, charge,
    reported mass precision and ARO mint checks pass. Two tetrahedral stereocentres
    are assigned R. Deterministic consistency does not establish correctness of a
    historical natural-product assignment.
  snapshot_sha256: 58bd95c6a561ba3974b18e26c5787c832fc2714e371366466021db732b0298a9
- evidence_id: xref-comparison
  kind: validation
  reference: 464466-xref-check.json; 464466-xref-check.py
  locator: Independent native/ChEBI/PubChem comparison for record 465
  accessed_at: '2026-10-21T16:43:44Z'
  support: supports
  summary: Independent molecular parsing reproduces identical native/current ChEBI/current
    PubChem keys. No changed connectivity or point-stereo conflict was identified;
    ordinary structure strings do not explicitly express the biaryl axis.
  snapshot_sha256: d2106f586d83620fa7b70cd7f1e87ce8c205fd0be8218efcefcaabdf398b8c0a
- evidence_id: lead-index
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28EXT_ID%3A33440167%20OR%20DOI%3A10.1039/C6SC04265A%20OR%20DOI%3A10.1021/acs.jnatprod.6c00145%29%20AND%20SRC%3AMED&format=json&resultType=core&pageSize=100
  locator: Complete original abstracts and bibliographic metadata for PMID:33440167,
    PMID:28507698 and PMID:41988676
  accessed_at: '2026-10-21T16:38:20.035325Z'
  support: context_only
  summary: The sole adopted PMID resolves to the 2021 biosynthetic regulation paper.
    Original 2017 discovery and 2026 structural-revision papers were followed and
    inspected as primary sources; the complete three abstracts were read. Abstracts
    are not substituted for the tables, structures and methods inspected below.
  snapshot_sha256: dd9d015a531bb198141c04898cdbf272c3cf489a6957582fc62e97e9efe9662e
- evidence_id: primary2017
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5414599/fullTextXML
  locator: DOI:10.1039/C6SC04265A; Figure 1, Table 1, isolation, antibacterial activity
    and resistance-selection results
  accessed_at: '2026-10-21T16:30:15Z'
  support: supports
  summary: Original Figure 1 assigns formicamycin J as compound 13. Table 1 reports
    B. subtilis <20, clinical MRSA 0.625 and VRE 1.25 µM for isolated 13. Compound
    13 was also among the three congeners tested for MRSA resistance selection; no
    increased MIC was observed under that experiment. The inequality qualifiers are
    retained. The paper leaves the formicamycin molecular target unresolved; the established
    fasamycin FabF target is not automatically assigned to formicamycins.
  snapshot_sha256: 741a682eefa78fdbcfb69b76eddd1d23df3e5bffbb60b2c7df34b51d923083d5
- evidence_id: primary2017-si
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5414599/supplementaryFiles
  locator: SI sections 1b, 1e and 1g; pp. 2–5, 47–50 and 56
  accessed_at: '2026-10-21T16:32:07Z'
  support: supports
  summary: J was isolated as 3 mg; original 1H/13C/2D NMR and HRMS gave C30H26Cl4O8,
    [M+H]+ observed 655.0464. Producer S. formicae KY5 was grown on soya-flour mannitol
    agar at 30°C; I/J used extraction and repeated chromatographic purification from
    the standard MS culture. MICs used 1 mL LB without NaCl in 24-well plates, starting
    OD600 0.08–0.15, 40 µL stock in water or methanol, static 30°C overnight and absence
    of observable growth. VRE was E. faecium B16.06226; MRSA was an unnamed hospital
    patient isolate validated by the source-described test; B. subtilis laboratory
    strain identifier is not given. Exact antibiotic susceptibility cannot be generalized
    to the species.
  snapshot_sha256: c30ad317fb5a4e00f304850ff2bd67d2960f7643f468e35a913bda99aca2f70d
- evidence_id: primary2017-figure
  kind: primary_source
  reference: https://doi.org/10.1039/C6SC04265A
  locator: Original Figure 1 actually viewed; substituent table rows 12, 13 and 14
  accessed_at: '2026-10-21T16:32:07Z'
  support: supports
  summary: Compound13 has four chlorines and both ortho and para E-ring methoxy groups.
    It is distinct from compound 12 and from the brominated compound 14. Figure numbering
    is specific to 2017 and differs from 2026.
  snapshot_sha256: e9f81df7fd0e62cc5f37de12444bb1d23836689cdf043a10f9c04ecd692d7d06
- evidence_id: passage2017
  kind: primary_source
  reference: https://doi.org/10.1039/C6SC04265A
  locator: Main resistance-selection results; SI section 1g, p.56
  accessed_at: '2026-10-21T16:32:07Z'
  support: supports
  summary: The original serial-passage experiment selected compounds 6, 13 and 15
    only (C, J and L). SI specifies MRSA exposure to 0.35, 0.1 and 0.4 µg/mL respectively,
    overnight growth then a further 19 generations and repeat MIC determination, with
    a no-formicamycin control. No MIC rise was detected in the reported experiment.
    This supports a bounded J observation; it is not evidence that every congener
    prevents resistance or that no resistance mechanism can exist.
  snapshot_sha256: c30ad317fb5a4e00f304850ff2bd67d2960f7643f468e35a913bda99aca2f70d
- evidence_id: adopted2021
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8062789/fullTextXML
  locator: PMID:33440167; introduction/discussion, Table 2, production methods and
    STAR Methods MIC assay
  accessed_at: '2026-10-21T16:29:46Z'
  support: supports
  summary: The adopted original is a biosynthetic regulatory study. Its introduction
    and discussion repeat family-level MRSA/VRE and resistance-barrier context from
    Qin 2017; regulation of production is not evidence that the regulatory proteins
    are drug targets. Table 2 directly tests J and gives MIC 4 µg/mL for MRSA ATCC
    BAA-1717 and MSSA ATCC6538P. This differs from the 2017 0.625 µM unnamed-MRSA
    result in isolate, method and units, so the two are preserved separately. The
    2021 resazurin method uses DMSO stocks, 1–256 µg/mL in LB or TSB with 5% DMSO,
    culture dilutions from 0.5 McFarland, 37°C, and color read 4 h after dye addition.
    It does not specify a distinct medium assignment or complete pre-dye incubation
    duration for each displayed result.
  snapshot_sha256: e55b2fd0ccc375fd9d04e77b0102d8588ed7bab670427d6124477a3d2c38cdae
- evidence_id: revision2026
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13532170/fullTextXML
  locator: PMID:41988676; Results, Table 1 actually viewed and compound-specific X-ray
    crystallographic data
  accessed_at: '2026-10-21T16:29:46Z'
  support: supports
  summary: Formicamycin J is compound 4 in this paper. Table 1 explicitly retains
    the structure as published, with both E-ring methoxy groups, Sa axis and 10R,19R
    stereocentres. CCDC 2498174 reports Flack 0.028(7), Hooft 0.024(8), and a DMSO-containing
    crystal of C30H26Cl4O8; lattice DMSO does not change the neutral molecular identity.
  snapshot_sha256: 55796020973e571658d3a02c0080a44cff02e2bd6113dbfe0c942357eb04354d
- evidence_id: crystal-table
  kind: primary_source
  reference: https://doi.org/10.1021/acs.jnatprod.6c00145
  locator: Table 1 image actually inspected; exact J row
  accessed_at: '2026-10-21T16:30:49Z'
  support: supports
  summary: J row says structure as published and shows its ORTEP; the I-specific methoxy
    revision does not change J, which has both groups.
  snapshot_sha256: e67930cb6a4b34690b126ae1465380bfd7580cad3f7668ebd5fe8dbc3c2dc15c
- evidence_id: gates
  kind: validation
  reference: 465-focused-results.json
  locator: Actual focused schema, strict and chemistry command results
  accessed_at: '2026-10-21T16:43:44Z'
  support: supports
  summary: All three focused executions exited 0. Native schema/strict used the 047
    environment; independent RDKit chemistry used the existing 019 interpreter against
    047 cwd. This confirms deterministic consistency, not scientific sign-off.
  snapshot_sha256: fa39e484c63cf8e534d017b2513e7499f0709e65d7364da4a9f02731ea43632a
assessments:
- assessment_id: identity
  area: identity
  topic: Exact congener, constitution and chemical form
  outcome: supported
  summary: Native J constitution, neutral formula and R,R centres match the unchanged
    crystal-confirmed molecule. Axial configuration is established in the primary
    paper but is not explicit in the ordinary stored strings; unencoded axis is not
    a racemate claim.
  target_ids:
  - antibioticmech:aro-274dd73c04
  evidence_ids:
  - native
  - chemistry
  - xref-comparison
  - chebi
  - pubchem
  - primary2017-figure
  - revision2026
- assessment_id: grounding
  area: grounding
  topic: Minted ARO identity and exact chemical xrefs
  outcome: supported
  summary: The ARO mint reproduces and all three chemical identifiers resolve to the
    named congener with mutually coherent structure data. The broader polyketide parent
    is appropriate. No drug-level accession is present.
  target_ids:
  - antibioticmech:aro-274dd73c04
  evidence_ids:
  - owners
  - aro
  - parent
  - chebi
  - pubchem
  - xref-comparison
- assessment_id: classification
  area: scope
  topic: Antibacterial eligibility and family definition
  outcome: supported
  summary: Primary isolated-compound results support the named natural congener as
    an antibacterial polyketide. The class is supported by exact-congener measurements
    rather than solely by family membership. The native definition explicitly describes
    congeners collectively and its resistance wording must remain family context.
  target_ids:
  - antibioticmech:aro-274dd73c04
  evidence_ids:
  - native
  - parent
  - primary2017
  - adopted2021
- assessment_id: activity
  area: evidence
  topic: MIC endpoints, original material and organism scope
  outcome: supported
  summary: The original Table 1 compound mapping and SI assay conditions were verified.
    Qualifiers, µM units, unnamed MRSA isolate, E. faecium B16.06226 and limited B.
    subtilis identification must remain explicit. The additional2021 J MICs are a
    separate assay in µg/mL against named ATCC strains.
  target_ids:
  - antibioticmech:aro-274dd73c04
  evidence_ids:
  - primary2017
  - primary2017-si
  - adopted2021
- assessment_id: resistance
  area: evidence
  topic: Resistance-selection claim
  outcome: supported
  summary: J was directly included in the 2017 serial-passage experiment, supporting
    failure to select elevated MIC under the reported conditions. It is not proof
    of universal resistance impossibility.
  target_ids:
  - antibioticmech:aro-274dd73c04
  evidence_ids:
  - aro
  - passage2017
  - adopted2021
- assessment_id: mechanism
  area: evidence
  topic: Mode, molecular target and causal scope
  outcome: unknown
  summary: No native mode, molecular target or causal graph is asserted. The original
    authors leave the formicamycin antibacterial target unresolved. Fasamycin FabF
    inhibition and biosynthetic For regulators must not be converted into drug targets.
    The native has no named protein/pathway claim triggering a structured-adapter
    cross-check.
  target_ids:
  - antibioticmech:aro-274dd73c04
  evidence_ids:
  - native
  - primary2017
  - adopted2021
- assessment_id: producer
  area: evidence
  topic: Original production material
  outcome: supported
  summary: Original isolation supports S. formicae KY5 as producer. I/J were purified
    from standard solid MS cultures; retain exact compound and culture conditions
    if producer claims are later added. No native producer claim is present.
  target_ids:
  - antibioticmech:aro-274dd73c04
  evidence_ids:
  - primary2017
  - primary2017-si
- assessment_id: completeness
  area: completeness
  topic: Optional observations, datasets and discussions
  outcome: unknown
  summary: Activity and producer evidence could be curated with exact material and
    assay context; their absence is not a required-field error. Do not force a mechanism
    or causal chain from the available inhibition or biosynthesis results. No clinical,
    regulatory, dataset or discussion assertion is present to validate.
  target_ids:
  - antibioticmech:aro-274dd73c04
  evidence_ids:
  - native
  - local-search
  - primary2017-si
  - adopted2021
  - revision2026
- assessment_id: provenance
  area: provenance
  topic: Source ownership, status and history
  outcome: supported
  summary: All native fields and three seed/reseed events were read. The thirteen
    initial captures were verified before judgment and ten actual-owner/guidance inputs
    appended. SEEDED status is retained; neither a passing contract nor this review
    promotes it to REVIEWED.
  target_ids:
  - antibioticmech:aro-274dd73c04
  evidence_ids:
  - native
  - owners
  - gates
- assessment_id: validation
  area: schema
  topic: Actual focused native checks
  outcome: supported
  summary: Focused schema, strict and chemical consistency checks pass. They complement,
    but do not replace, the primary evidence audit.
  target_ids:
  - antibioticmech:aro-274dd73c04
  evidence_ids:
  - gates
  - chemistry
findings: []
actions:
- action_id: A1
  description: 'Optional future curation: add exact formicamycin J activity and producer
    evidence with the original assay/material boundaries.'
  finding_ids: []
  target_ids:
  - antibioticmech:aro-274dd73c04
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/formicamycin-j.yaml
    role: Future curator-owned activity_spectrum and producer annotations
  acceptance_checks:
  - Use original 2017 compound 13 and its qualifiers/µM values with SI strain and
    method details; attach claim-level citations.
  - Keep resistance passage limited to compounds 6, 13 and 15; preserve the 2021 J
    assay separately if used. Do not infer a direct antibacterial target from the
    for biosynthetic genes.
  - Use the validated native curation writer and accurate LLM-assisted curation event
    only in a separately authorized curation task; absent optional fields do not require
    a change.
limitations:
- The adopted 2021 paper was inspected at complete abstract and relevant original
  introduction, production, Table 2, discussion and assay-method depth. The 2017 structure/activity/results
  and SI exact-congener characterization, production and MIC/resistance methods were
  inspected. Unrelated biosynthetic experiments were not independently replicated.
- The 2026 original structural results, relevant exact-congener table/figures and
  crystallographic data were read; the deposited CIF coordinates and raw NMR time-domain
  data were not independently re-refined. J was directly crystallized; adjacent I
  revision is not transferred to J.
- The ordinary native structure strings do not encode the biaryl atropisomer. This
  is recorded as a representation limitation, not evidence of a racemate or a separate
  assigned wrong stereoisomer.
- Original MIC inequality symbols are retained; the 2017 unnamed MRSA and B. subtilis
  identifiers limit strain-level reuse. The 2021 protocol does not completely resolve
  per-strain medium and pre-dye incubation time. No clinical efficacy, clinical breakpoint
  or species-wide resistance claim is made.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Native and maintained files were not edited. All twenty-three source inputs and
  original captures were rechecked. Optional links, tags and notes were checked specifically
  for formicamycin J.
- Primary source snapshots originally fetched by root were independently read; their
  actual fetch timestamps and SHA256 hashes are retained. No source-authority consensus
  is substituted for primary structure adjudication.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://doi.org/10.1039/C6SC04265A
- https://doi.org/10.1016/j.chembiol.2020.12.011
- https://doi.org/10.1021/acs.jnatprod.6c00145
tags:
- formicamycin-j
- polyketide
- crystal-confirmed
```
