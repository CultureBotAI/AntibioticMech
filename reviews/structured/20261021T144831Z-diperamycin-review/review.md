# Diperamycin: supported natural-product record with a later stereochemical assignment to adjudicate

- Review: 20261021T144831Z-diperamycin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:27:15Z
- Finished UTC: 2026-10-21T14:48:31Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The original isolation paper supports the neutral diperamycin connectivity, producer and antibacterial definition. Native and current ChEBI agree but leave all ten stereocentres unspecified. A 2024 primary study assigns stereochemistry by NMR comparison and biosynthetic analogy, providing a substantive follow-up whose inferential basis must be retained. No confirmed required native correction is established in this review. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 367; one exact record. All 13 initial hashes are preserved within 25 expanded source/context inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65799 | data/antibiotics/antibacterial/diperamycin.yaml | generated | diperamycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Structured-source applicability | not_applicable | False | CHEBI:65799 | The native record contains no named protein, gene, pathway or transcriptomic claim. Additional biosynthesis literature was used for identity and producer scope, not to infer an antibacterial target or iModulon mechanism. |
| Focused chemistry verification | passed | False | CHEBI:65799 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:65799 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:65799 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:65799 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65799 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65799 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65799 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65799 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65799 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65799 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65799 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65799 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Planar molecular identity and later stereochemistry

identity: unknown. Targets: CHEBI:65799.

Native connectivity, formula, charge and masses match the original neutral isolate and current ChEBI. All ten centres remain unspecified. The 2024 complete assignment warrants source-aware adjudication; its NMR/biosynthetic inference does not establish a proven wrong native epimer or justify claiming a racemate.

### Exact ChEBI concept, systematic synonym, parent and xref

grounding: supported. Targets: CHEBI:65799.

CHEBI:65799 resolves and reproduces the native graph and systematic name. The cyclodepsipeptide parent is broader. Reaxys is retained as an unresolved independent equivalence boundary; source propagation alone does not validate its graph.

### Producer and antibacterial definition

evidence: supported. Targets: CHEBI:65799.

The sole adopted original supports the source producer/strain and the reported Gram-positive activity including the historical E. seriolicida and MRSA panel. The later CS113R producer is additional evidence, not a correction of MK393-AF2.

### Antibacterial category and activity roles

scope: supported. Targets: CHEBI:65799.

Purified neutral diperamycin has original bacterial growth inhibition measurements. The category and both antimicrobial/antibacterial roles are supported. Assay negatives for particular Gram-negative strains do not negate this classification.

### Optional activity_spectrum enrichment

completeness: supported. Targets: CHEBI:65799.

Original strain-specific agar MICs are available with medium and incubation qualifiers. Their absence is not a schema defect. Any future enrichment must preserve neutral isolate provenance, exact strain, historical name, upper-bound values and separate fish-pathogen/mycobacterial conditions.

### Unpopulated molecular targets, resistance and causal mechanisms

completeness: unknown. Targets: CHEBI:65799.

No native mechanism or resistance claim requires correction. The original MIC/MTT phenotypes and later biosynthetic genetics do not establish an antibacterial binding target. No inferred exporter annotation is promoted to measured drug resistance.

### Optional structured producers and biosynthesis

completeness: supported. Targets: CHEBI:65799.

MK393-AF2/FERM P-16079 is an original characterized producer; CS113R is a later genetically studied producer with a defined rifampicin-selected background. These may support future structured enrichment with their original experimental scope. Empty optional producer fields are not a defect.

### Clinical products and host endpoints

scope: not_applicable. Targets: CHEBI:65799.

No FDA or other clinical product assertion occurs. Tumour-cell and acute mouse results are bounded host endpoints, not a clinical-use or safety claim.

### Dataset memberships and causal graphs

scope: not_applicable. Targets: CHEBI:65799.

No structured dataset memberships or causal graph occurs. Neither the native definition nor class identity implies such fields must be populated.

### Adopted primary lead, source mint and history

provenance: supported. Targets: CHEBI:65799.

The sole adopted PMID10048567 was fully read, including actual structure and assay tables. The single source concept, source mint/version and three seed/reseed events are coherent. SEEDED status is retained and all initial input hashes are preserved.

### Focused validation and scientific limits

schema: supported. Targets: CHEBI:65799.

Schema, strict and chemistry checks pass. They do not settle the later inferential stereochemical assignment or independently resolve the inaccessible Reaxys record.

## Findings

### F1: Adjudicate the later stereochemical assignment before claiming a fully specified natural structure

informational / open / provisional; issue key: diperamycin-later-stereochemical-assignment.

The inherited graph omits all ten stereocentres. The 2024 original supplies an explicit assignment using NMR comparison with aurantimycin A and biosynthetic-domain similarity. The inspected evidence supports a concrete follow-up, not a confirmed wrong-epimer correction or automatic adoption of every stereobond. Preserve the original planar record and distinguish measured connectivity from inferred absolute stereochemistry until that adjudication is documented.

## Recommended Actions And Acceptance Checks

### A1

Adjudicate the 2024 stereochemical assignment and document its experimental and inferential basis.

- Map every proposed stereocentre to Figure 5 and distinguish original NMR connectivity, relative comparisons and biosynthetic absolute-configuration inference.
- Keep aurantimycin A crystallography and legacy drawing correction separate from diperamycin; do not label the latter as directly X-ray determined.
- If a revised graph is accepted, regenerate all structure fields coherently and reconcile exact xrefs and synonyms through maintained inputs; otherwise record why the planar form is retained.
- Run focused chemistry/schema/strict and corpus provenance/reproduction checks after any future curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/diperamycin.yaml; Complete native record: definition, one systematic synonym, parent, two roles, full structure, Reaxys xref, source concept and three history events | supports | The EXACT/SEEDED ChEBI record has neutral C38H64N8O14 and an unstereospecified molecular graph. It has no mode, molecular target, resistance, activity_spectrum, clinical product, structured producer, causal graph or dataset assertion. Its definition separately names the original producer and antibacterial phenotype. |
| owners | data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Exact ChEBI row 1310; original input receipt and expanded owners | supports | The adopted row supplies CHEBI:65799, one systematic synonym, the cyclodepsipeptide parent, both activity roles and Reaxys8468749. PMID10048567 is its sole adopted primary lead. No other source concept is merged into this record. Source and generated history were checked; original hashes remain unchanged. |
| chemistry | Independent RDKit2026.03.5, batch019 interpreter against batch037 cwd; 367-chemistry.json; both native encodings and source mint | supports | SMILES and InChI reproduce IHQIMVZJVJTKSV-UHFFFAOYSA-N, neutral C38H64N8O14, masses and source mint. All ten stereogenic carbon centres are unassigned. This is an incomplete stereochemical description, not evidence of a racemate, mixture or wrong epimer. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/65799/; Current complete CHEBI:65799 term, default structure, names, relations, source citation and registry identifier | supports | Current ChEBI reproduces the native structure, systematic name, definition, broader CHEBI:35213 cyclodepsipeptide parent, activity roles and Reaxys identifier. Its graph remains stereochemically unspecified, with a 2013 modification date. The producer metadata names S. griseoaurantiacus MK393 AF2 and the original paper. |
| original-identity | https://doi.org/10.7164/antibiotics.51.1087; PMID10048567; full 1998 paper pages 1087–1092; actual Figure 1 and Tables 4/5 viewed | supports | The authors isolated 100.9 mg of chromatographically purified white neutral powder. Figure 1 gives the same planar connectivity without stereobonds. Table 4 reports C38H64N8O14 and optical rotation +25.7 at 20 degrees C, c 1.0 in methanol. Its sodium-containing mass-spectral ion is an analytical adduct, not a sodium-salt product. The paper says further structural details would appear elsewhere. |
| original-producer | https://doi.org/10.7164/antibiotics.51.1087; Pages 1087–1090; taxonomic comparison, strain deposit and fermentation/isolation | supports | The Yokohama soil isolate MK393-AF2 was assigned to S. griseoaurantiacus by the reported morphological, physiological and chemotaxonomic comparison; deposit FERM P-16079 is stated. Production used a 27-degree-C, seven-day fermentation, followed by solvent extraction and successive chromatography. This directly supports the native producer statement at the original identification scope. |
| original-activity | https://doi.org/10.7164/antibiotics.51.1087; Page 1088 Methods; actual Table 6 page 1092, all organism rows read | supports | Serial agar dilution used Mueller-Hinton agar, 37 degrees C for 18 hours for routine bacteria. Purified diperamycin MICs include S. aureus FDA209P 0.10, MRSA No. 5/No. 17/16526 0.10 and MRSA 04282 0.20 micrograms/mL. E. coli NIHJ/BE1121/BE1186, S. dysenteriae JS11910 and P. aeruginosa A3 were &gt;100. Enterococcus seriolicida 4038 was 0.20 on brain-heart-infusion agar with 2% NaCl at 27 degrees C for 18 hours. Preserve historical organism names and the distinct medium; inoculum and detailed MIC-reading rule are not specified locally. |
| original-boundaries | https://doi.org/10.7164/antibiotics.51.1087; Page 1088 methods; actual Tables 6/7 page 1092 and toxicity paragraph | context_only | M. smegmatis ATCC 607 and C. albicans 3147 each have reported MIC 12.5 micrograms/mL; the mycobacterial method uses nutrient agar plus 1% glycerol, 37 degrees C for 42 hours. A Candida-specific method is not given locally. Tumour-cell growth IC50 values come from MTT experiments and are not antibacterial endpoints. The reported acute mouse toxicity and cell effects do not establish clinical safety, therapeutic efficacy or an antibacterial molecular target. |
| later-connectivity | https://doi.org/10.3390/ijms25042347; PMID38397022/PMC10888640; Results 2.3, Methods 3.6/3.7 and actual Figure 4 | supports | The 2024 study purified 1.1 mg from Streptomyces sp. CS113R, a rifampicin-selected derivative of CS113. HRMS and 1D/2D NMR support diperamycin connectivity and distinguish it from isobaric aurantimycin A. The detected ammonium adduct does not establish an ammonium salt. Preparative HPLC used acetonitrile/0.1% aqueous TFA; no counterion stoichiometry is established. No new antibacterial MIC panel is reported. |
| later-stereochemistry | https://doi.org/10.3390/ijms25042347; Results 2.3/2.5, actual Figure 5 and supplement Table S3 | supports | The authors supply a fully stereodrawn diperamycin structure, including L-Thr, D-Pip, N-OH-beta-MeO-L-Ala, L-Pip and N-OH-D-Ala. Absolute assignments are inferred from NMR comparison with aurantimycin A and PKS/NRPS domain similarity; no direct diperamycin X-ray or chiral degradation determination is reported. They also correct the earlier aurantimycin polyketide drawing. The explicit all-centre assignment is a curation lead, but its inferential basis must not be rewritten as direct absolute-configuration measurement. |
| later-figure | https://pub.mdpi-res.com/ijms/ijms-25-02347/article_deploy/html/images/ijms-25-02347-g005.png; Actual Figure 5 image, diperamycin upper structure and aurantimycin lower comparator | supports | All ten diperamycin centres have stereobonds in the displayed structure. The upper molecule has a straight hexyl polyketide substituent and threonine; the lower aurantimycin comparator instead has a branched side chain and hydroxyleucine. These are distinct constitutional isomers despite the same molecular formula. The native planar graph matches the diperamycin connectivity, without asserting this later stereochemical assignment. |
| later-supplement | https://mdpi-res.com/d_attachment/ijms/ijms-25-02347/article_deploy/ijms-25-02347-s001.zip; Supplement PDF: actual Table S3 page 4; table/caption inventory and structural methods | supports | Table S3 lists the assigned residues and NMR data in DMSO-d6 at 500 MHz and 24 degrees C. The supplement contains biosynthetic gene/primer tables, NMR spectra and mutant/complementation figures. It was inspected for the basis of the structural assignment; spectra and PCR gels were not independently reprocessed. The initial MDPI supplement route returned 403; the public publisher ZIP succeeded. |
| biosynthesis-boundary | https://doi.org/10.3390/ijms25042347; Results 2.4/2.5, Methods 3.1–3.5 and Conclusions | context_only | The dpnS2 and dpnZ mutants lost the product; dpnZ complementation restored it, whereas the dpnO2 mutant retained production. This supports biosynthetic involvement. Many individual enzyme functions remain predictions and the paper calls for further experiments. Biosynthetic enzymes and annotated exporters are not demonstrated antibacterial targets or resistance determinants merely because they occur in the cluster. |
| analogue-original | https://doi.org/10.7164/antibiotics.48.119; PMID7706121; original pages 119–122 structure-elucidation scope and actual Figures 1/2 | context_only | The 1995 original establishes aurantimycin A by crystallography and chiral amino-acid analysis, not diperamycin. This is reference 18 in the 2024 article; the later X-ray sentence points to reference 19, which is the planar 1998 diperamycin paper. The related-compound crystallographic experiment must not be attributed to diperamycin. The review did not independently refine the aurantimycin crystal or adjudicate every bond in its legacy drawing. |
| reaxys | https://www.reaxys.com/reaxys/secured/hopinto.do?context=R&amp;query=IDE.RN%3D8468749; Exact native Reaxys registry route; current ChEBI propagated registry entry | unknown | The public exact route returned 403; no independently readable Reaxys structure was obtained. Current ChEBI repeats the identifier, which verifies provenance only. No paid retrieval or authenticated access was attempted. |
| search | Ignored-inclusive local reference search and EuropePMC primary discovery; 366367-local-focused.txt;367-discovery.json;367-pubmed-search.json | context_only | The bounded exact-name structural discovery retrieved the 1998 original and 2024 biosynthesis/structure study, plus a later review. No additional original structure paper was located in these queries; this does not prove none exists. The secondary review was not substituted for primary evidence. |
| gates | Focused schema, strict and standalone chemistry; 367-focused-results.json | supports | All three focused executions passed. Native gates used batch037; standalone RDKit used the existing batch019 interpreter against batch037 cwd. |

## Limits And Additional Notes

- The 2024 stereochemical assignment is explicitly inferential from NMR comparison and biosynthesis. No new direct absolute-configuration experiment for diperamycin was located in the inspected original and supplement. A complete replacement stereograph was not independently reconstructed.
- The 1998 paper was read in full with actual Figure 1 and Tables 4–7. The 2024 main text, key Figures 4/5 and supplement structural table were read; raw NMR spectra, PCR gels and the related aurantimycin crystal coordinates were not independently reprocessed.
- The exact Reaxys public route returned 403. Current ChEBI preserves that registry identifier but does not independently establish its molecular equivalence.
- Original assay methods omit inoculum, detailed MIC-reading rule and a Candida-specific protocol. The 2024 HPLC purification uses TFA but does not establish a defined TFA salt; its ammonium MS adduct is not evidence of a formulated ammonium salt.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native/source/status/history was edited. Optional links, tags and notes were checked against diperamycin.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T144831Z-diperamycin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Diperamycin: supported natural-product record with a later stereochemical
  assignment to adjudicate'
started_at: '2026-10-21T14:27:15Z'
finished_at: '2026-10-21T14:48:31Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Independent whole-record and actual source-row read after capture
    verification, fresh chemical consistency calculation, current ChEBI comparison,
    complete original isolation paper reading, actual structure/activity tables and
    later primary structure/biosynthesis assessment with explicit measurement-versus-inference
    boundaries.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: The original isolation paper supports the neutral diperamycin connectivity,
  producer and antibacterial definition. Native and current ChEBI agree but leave
  all ten stereocentres unspecified. A 2024 primary study assigns stereochemistry
  by NMR comparison and biosynthetic analogy, providing a substantive follow-up whose
  inferential basis must be retained. No confirmed required native correction is established
  in this review. Scientific assessment retains the stated evidence limits; full verification
  is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/diperamycin.yaml
    sha256: eb8ba8f71edbd21115081da50f3973cc0d38d0e50a5e4a983644fd33e39aa742
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
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
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
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
targets:
- target_id: CHEBI:65799
  path: data/antibiotics/antibacterial/diperamycin.yaml
  label: diperamycin
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
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 367; one exact record. All 13 initial hashes are preserved
    within 25 expanded source/context inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65799
checks:
- check_id: structured-adapter
  name: Structured-source applicability
  status: not_applicable
  required: false
  target_ids:
  - CHEBI:65799
  summary: The native record contains no named protein, gene, pathway or transcriptomic
    claim. Additional biosynthesis literature was used for identity and producer scope,
    not to infer an antibacterial target or iModulon mechanism.
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65799
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/366367-focused.py
    (cwd /private/tmp/antibioticmech-record-reviews-037)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65799
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/diperamycin.yaml (cwd /private/tmp/antibioticmech-record-reviews-037)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65799
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/diperamycin.yaml --out /private/tmp/am-review-session/367-strict.tsv
    (cwd /private/tmp/antibioticmech-record-reviews-037)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:65799
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
  - CHEBI:65799
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
  - CHEBI:65799
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
  - CHEBI:65799
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
  - CHEBI:65799
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
  - CHEBI:65799
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
  - CHEBI:65799
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
  - CHEBI:65799
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
  - CHEBI:65799
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/diperamycin.yaml
  locator: 'Complete native record: definition, one systematic synonym, parent, two
    roles, full structure, Reaxys xref, source concept and three history events'
  accessed_at: '2026-10-21T14:47:42Z'
  support: supports
  summary: The EXACT/SEEDED ChEBI record has neutral C38H64N8O14 and an unstereospecified
    molecular graph. It has no mode, molecular target, resistance, activity_spectrum,
    clinical product, structured producer, causal graph or dataset assertion. Its
    definition separately names the original producer and antibacterial phenotype.
  snapshot_sha256: 8dba1c940ffb355facf80886400db93a2427ae7038f62074a99ac2dcfb60e542
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: Exact ChEBI row 1310; original input receipt and expanded owners
  accessed_at: '2026-10-21T14:47:42Z'
  support: supports
  summary: The adopted row supplies CHEBI:65799, one systematic synonym, the cyclodepsipeptide
    parent, both activity roles and Reaxys8468749. PMID10048567 is its sole adopted
    primary lead. No other source concept is merged into this record. Source and generated
    history were checked; original hashes remain unchanged.
  snapshot_sha256: 8dba1c940ffb355facf80886400db93a2427ae7038f62074a99ac2dcfb60e542
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit2026.03.5, batch019 interpreter against batch037 cwd
  locator: 367-chemistry.json; both native encodings and source mint
  accessed_at: '2026-10-21T14:47:42Z'
  support: supports
  summary: SMILES and InChI reproduce IHQIMVZJVJTKSV-UHFFFAOYSA-N, neutral C38H64N8O14,
    masses and source mint. All ten stereogenic carbon centres are unassigned. This
    is an incomplete stereochemical description, not evidence of a racemate, mixture
    or wrong epimer.
  snapshot_sha256: 34e429f668b40430652702ece81ae70ac8534f8fcd9dde043b9e2c727c439cde
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/65799/
  locator: Current complete CHEBI:65799 term, default structure, names, relations,
    source citation and registry identifier
  accessed_at: '2026-10-21T14:40:00.330550Z'
  support: supports
  summary: Current ChEBI reproduces the native structure, systematic name, definition,
    broader CHEBI:35213 cyclodepsipeptide parent, activity roles and Reaxys identifier.
    Its graph remains stereochemically unspecified, with a 2013 modification date.
    The producer metadata names S. griseoaurantiacus MK393 AF2 and the original paper.
  snapshot_sha256: ddad18b56fe35519a1cc39758795985bbd3304268cb541b9e6fd3716375a7218
- evidence_id: original-identity
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.51.1087
  locator: PMID10048567; full 1998 paper pages 1087–1092; actual Figure 1 and Tables
    4/5 viewed
  accessed_at: '2026-10-21T14:40:25.594857Z'
  support: supports
  summary: The authors isolated 100.9 mg of chromatographically purified white neutral
    powder. Figure 1 gives the same planar connectivity without stereobonds. Table
    4 reports C38H64N8O14 and optical rotation +25.7 at 20 degrees C, c 1.0 in methanol.
    Its sodium-containing mass-spectral ion is an analytical adduct, not a sodium-salt
    product. The paper says further structural details would appear elsewhere.
  snapshot_sha256: 386b329b585a4af6a71ebc865588f06174b67f2bb5bf694fc034de3471bdf478
- evidence_id: original-producer
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.51.1087
  locator: Pages 1087–1090; taxonomic comparison, strain deposit and fermentation/isolation
  accessed_at: '2026-10-21T14:40:25.594857Z'
  support: supports
  summary: The Yokohama soil isolate MK393-AF2 was assigned to S. griseoaurantiacus
    by the reported morphological, physiological and chemotaxonomic comparison; deposit
    FERM P-16079 is stated. Production used a 27-degree-C, seven-day fermentation,
    followed by solvent extraction and successive chromatography. This directly supports
    the native producer statement at the original identification scope.
  snapshot_sha256: 386b329b585a4af6a71ebc865588f06174b67f2bb5bf694fc034de3471bdf478
- evidence_id: original-activity
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.51.1087
  locator: Page 1088 Methods; actual Table 6 page 1092, all organism rows read
  accessed_at: '2026-10-21T14:40:25.594857Z'
  support: supports
  summary: Serial agar dilution used Mueller-Hinton agar, 37 degrees C for 18 hours
    for routine bacteria. Purified diperamycin MICs include S. aureus FDA209P 0.10,
    MRSA No. 5/No. 17/16526 0.10 and MRSA 04282 0.20 micrograms/mL. E. coli NIHJ/BE1121/BE1186,
    S. dysenteriae JS11910 and P. aeruginosa A3 were >100. Enterococcus seriolicida
    4038 was 0.20 on brain-heart-infusion agar with 2% NaCl at 27 degrees C for 18
    hours. Preserve historical organism names and the distinct medium; inoculum and
    detailed MIC-reading rule are not specified locally.
  snapshot_sha256: 386b329b585a4af6a71ebc865588f06174b67f2bb5bf694fc034de3471bdf478
- evidence_id: original-boundaries
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.51.1087
  locator: Page 1088 methods; actual Tables 6/7 page 1092 and toxicity paragraph
  accessed_at: '2026-10-21T14:40:25.594857Z'
  support: context_only
  summary: M. smegmatis ATCC 607 and C. albicans 3147 each have reported MIC 12.5
    micrograms/mL; the mycobacterial method uses nutrient agar plus 1% glycerol, 37
    degrees C for 42 hours. A Candida-specific method is not given locally. Tumour-cell
    growth IC50 values come from MTT experiments and are not antibacterial endpoints.
    The reported acute mouse toxicity and cell effects do not establish clinical safety,
    therapeutic efficacy or an antibacterial molecular target.
  snapshot_sha256: 386b329b585a4af6a71ebc865588f06174b67f2bb5bf694fc034de3471bdf478
- evidence_id: later-connectivity
  kind: primary_source
  reference: https://doi.org/10.3390/ijms25042347
  locator: PMID38397022/PMC10888640; Results 2.3, Methods 3.6/3.7 and actual Figure
    4
  accessed_at: '2026-10-21T14:40:25.600278Z'
  support: supports
  summary: The 2024 study purified 1.1 mg from Streptomyces sp. CS113R, a rifampicin-selected
    derivative of CS113. HRMS and 1D/2D NMR support diperamycin connectivity and distinguish
    it from isobaric aurantimycin A. The detected ammonium adduct does not establish
    an ammonium salt. Preparative HPLC used acetonitrile/0.1% aqueous TFA; no counterion
    stoichiometry is established. No new antibacterial MIC panel is reported.
  snapshot_sha256: 8c08b0bb732fb60ef3ea0353218272480ddb4e7dec921bc55ba1bb68d7c8b900
- evidence_id: later-stereochemistry
  kind: primary_source
  reference: https://doi.org/10.3390/ijms25042347
  locator: Results 2.3/2.5, actual Figure 5 and supplement Table S3
  accessed_at: '2026-10-21T14:40:25.600278Z'
  support: supports
  summary: The authors supply a fully stereodrawn diperamycin structure, including
    L-Thr, D-Pip, N-OH-beta-MeO-L-Ala, L-Pip and N-OH-D-Ala. Absolute assignments
    are inferred from NMR comparison with aurantimycin A and PKS/NRPS domain similarity;
    no direct diperamycin X-ray or chiral degradation determination is reported. They
    also correct the earlier aurantimycin polyketide drawing. The explicit all-centre
    assignment is a curation lead, but its inferential basis must not be rewritten
    as direct absolute-configuration measurement.
  snapshot_sha256: 8c08b0bb732fb60ef3ea0353218272480ddb4e7dec921bc55ba1bb68d7c8b900
- evidence_id: later-figure
  kind: primary_source
  reference: https://pub.mdpi-res.com/ijms/ijms-25-02347/article_deploy/html/images/ijms-25-02347-g005.png
  locator: Actual Figure 5 image, diperamycin upper structure and aurantimycin lower
    comparator
  accessed_at: '2026-10-21T14:45:35.055182Z'
  support: supports
  summary: All ten diperamycin centres have stereobonds in the displayed structure.
    The upper molecule has a straight hexyl polyketide substituent and threonine;
    the lower aurantimycin comparator instead has a branched side chain and hydroxyleucine.
    These are distinct constitutional isomers despite the same molecular formula.
    The native planar graph matches the diperamycin connectivity, without asserting
    this later stereochemical assignment.
  snapshot_sha256: 592d53375412596d4e43fefc30115dc13eb4c96a59cb9bae7b61aaab23c522a9
- evidence_id: later-supplement
  kind: primary_source
  reference: https://mdpi-res.com/d_attachment/ijms/ijms-25-02347/article_deploy/ijms-25-02347-s001.zip
  locator: 'Supplement PDF: actual Table S3 page 4; table/caption inventory and structural
    methods'
  accessed_at: '2026-10-21T14:45:47.726025Z'
  support: supports
  summary: Table S3 lists the assigned residues and NMR data in DMSO-d6 at 500 MHz
    and 24 degrees C. The supplement contains biosynthetic gene/primer tables, NMR
    spectra and mutant/complementation figures. It was inspected for the basis of
    the structural assignment; spectra and PCR gels were not independently reprocessed.
    The initial MDPI supplement route returned 403; the public publisher ZIP succeeded.
  snapshot_sha256: e8ec59413da55958c703a43305b65fc095e1f622119fd086dfffe49566898709
- evidence_id: biosynthesis-boundary
  kind: primary_source
  reference: https://doi.org/10.3390/ijms25042347
  locator: Results 2.4/2.5, Methods 3.1–3.5 and Conclusions
  accessed_at: '2026-10-21T14:40:25.600278Z'
  support: context_only
  summary: The dpnS2 and dpnZ mutants lost the product; dpnZ complementation restored
    it, whereas the dpnO2 mutant retained production. This supports biosynthetic involvement.
    Many individual enzyme functions remain predictions and the paper calls for further
    experiments. Biosynthetic enzymes and annotated exporters are not demonstrated
    antibacterial targets or resistance determinants merely because they occur in
    the cluster.
  snapshot_sha256: 8c08b0bb732fb60ef3ea0353218272480ddb4e7dec921bc55ba1bb68d7c8b900
- evidence_id: analogue-original
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.48.119
  locator: PMID7706121; original pages 119–122 structure-elucidation scope and actual
    Figures 1/2
  accessed_at: '2026-10-21T14:45:35.070780Z'
  support: context_only
  summary: The 1995 original establishes aurantimycin A by crystallography and chiral
    amino-acid analysis, not diperamycin. This is reference 18 in the 2024 article;
    the later X-ray sentence points to reference 19, which is the planar 1998 diperamycin
    paper. The related-compound crystallographic experiment must not be attributed
    to diperamycin. The review did not independently refine the aurantimycin crystal
    or adjudicate every bond in its legacy drawing.
  snapshot_sha256: 625ad9cf69a392421821e0c41eb27141511f7aeb31db2e967816b018c746d844
- evidence_id: reaxys
  kind: authority
  reference: https://www.reaxys.com/reaxys/secured/hopinto.do?context=R&query=IDE.RN%3D8468749
  locator: Exact native Reaxys registry route; current ChEBI propagated registry entry
  accessed_at: '2026-10-21T14:45:35.074883Z'
  support: unknown
  summary: The public exact route returned 403; no independently readable Reaxys structure
    was obtained. Current ChEBI repeats the identifier, which verifies provenance
    only. No paid retrieval or authenticated access was attempted.
  snapshot_sha256: f9309c58cd46577a31b29418031ffce2db51222ced7901e7406894ed00da6252
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local reference search and EuropePMC primary discovery
  locator: 366367-local-focused.txt;367-discovery.json;367-pubmed-search.json
  accessed_at: '2026-10-21T14:45:47.726233Z'
  support: context_only
  summary: The bounded exact-name structural discovery retrieved the 1998 original
    and 2024 biosynthesis/structure study, plus a later review. No additional original
    structure paper was located in these queries; this does not prove none exists.
    The secondary review was not substituted for primary evidence.
  snapshot_sha256: 421d7362fd5475ea69c59b7f04062f2c1e8660bd405ed48b0b6ee64a9afb981c
  search_scope: '2026-10-21: diperamycin, CHEBI:65799, Reaxys8468749, adopted PMID10048567
    and exact-name structure/configuration/stereochemistry/antimicrobial queries.
    Local search included hidden and ignored files under data, curation, conf, src,
    scripts, reports and reviews. Current authority and both retrieved originals were
    inspected.'
- evidence_id: gates
  kind: validation
  reference: Focused schema, strict and standalone chemistry
  locator: 367-focused-results.json
  accessed_at: '2026-10-21T14:47:42Z'
  support: supports
  summary: All three focused executions passed. Native gates used batch037; standalone
    RDKit used the existing batch019 interpreter against batch037 cwd.
  snapshot_sha256: f9d0f65d7dfdafffc4ac5bd7db7f0e880716fd109cc98c57769efd8c6ab85f16
assessments:
- assessment_id: identity
  area: identity
  topic: Planar molecular identity and later stereochemistry
  outcome: unknown
  summary: Native connectivity, formula, charge and masses match the original neutral
    isolate and current ChEBI. All ten centres remain unspecified. The 2024 complete
    assignment warrants source-aware adjudication; its NMR/biosynthetic inference
    does not establish a proven wrong native epimer or justify claiming a racemate.
  target_ids:
  - CHEBI:65799
  evidence_ids:
  - chemistry
  - chebi
  - original-identity
  - later-stereochemistry
  - later-figure
  - analogue-original
- assessment_id: grounding
  area: grounding
  topic: Exact ChEBI concept, systematic synonym, parent and xref
  outcome: supported
  summary: CHEBI:65799 resolves and reproduces the native graph and systematic name.
    The cyclodepsipeptide parent is broader. Reaxys is retained as an unresolved independent
    equivalence boundary; source propagation alone does not validate its graph.
  target_ids:
  - CHEBI:65799
  evidence_ids:
  - chebi
  - native
  - chemistry
  - reaxys
- assessment_id: definition
  area: evidence
  topic: Producer and antibacterial definition
  outcome: supported
  summary: The sole adopted original supports the source producer/strain and the reported
    Gram-positive activity including the historical E. seriolicida and MRSA panel.
    The later CS113R producer is additional evidence, not a correction of MK393-AF2.
  target_ids:
  - CHEBI:65799
  evidence_ids:
  - original-producer
  - original-activity
  - later-connectivity
- assessment_id: classification
  area: scope
  topic: Antibacterial category and activity roles
  outcome: supported
  summary: Purified neutral diperamycin has original bacterial growth inhibition measurements.
    The category and both antimicrobial/antibacterial roles are supported. Assay negatives
    for particular Gram-negative strains do not negate this classification.
  target_ids:
  - CHEBI:65799
  evidence_ids:
  - original-identity
  - original-activity
  - chebi
- assessment_id: activity
  area: completeness
  topic: Optional activity_spectrum enrichment
  outcome: supported
  summary: Original strain-specific agar MICs are available with medium and incubation
    qualifiers. Their absence is not a schema defect. Any future enrichment must preserve
    neutral isolate provenance, exact strain, historical name, upper-bound values
    and separate fish-pathogen/mycobacterial conditions.
  target_ids:
  - CHEBI:65799
  evidence_ids:
  - original-activity
  - original-boundaries
- assessment_id: mechanism
  area: completeness
  topic: Unpopulated molecular targets, resistance and causal mechanisms
  outcome: unknown
  summary: No native mechanism or resistance claim requires correction. The original
    MIC/MTT phenotypes and later biosynthetic genetics do not establish an antibacterial
    binding target. No inferred exporter annotation is promoted to measured drug resistance.
  target_ids:
  - CHEBI:65799
  evidence_ids:
  - native
  - original-boundaries
  - biosynthesis-boundary
- assessment_id: producer
  area: completeness
  topic: Optional structured producers and biosynthesis
  outcome: supported
  summary: MK393-AF2/FERM P-16079 is an original characterized producer; CS113R is
    a later genetically studied producer with a defined rifampicin-selected background.
    These may support future structured enrichment with their original experimental
    scope. Empty optional producer fields are not a defect.
  target_ids:
  - CHEBI:65799
  evidence_ids:
  - original-producer
  - later-connectivity
  - biosynthesis-boundary
- assessment_id: clinical
  area: scope
  topic: Clinical products and host endpoints
  outcome: not_applicable
  summary: No FDA or other clinical product assertion occurs. Tumour-cell and acute
    mouse results are bounded host endpoints, not a clinical-use or safety claim.
  target_ids:
  - CHEBI:65799
  evidence_ids:
  - native
  - original-boundaries
- assessment_id: dataset
  area: scope
  topic: Dataset memberships and causal graphs
  outcome: not_applicable
  summary: No structured dataset memberships or causal graph occurs. Neither the native
    definition nor class identity implies such fields must be populated.
  target_ids:
  - CHEBI:65799
  evidence_ids:
  - native
- assessment_id: provenance
  area: provenance
  topic: Adopted primary lead, source mint and history
  outcome: supported
  summary: The sole adopted PMID10048567 was fully read, including actual structure
    and assay tables. The single source concept, source mint/version and three seed/reseed
    events are coherent. SEEDED status is retained and all initial input hashes are
    preserved.
  target_ids:
  - CHEBI:65799
  evidence_ids:
  - owners
  - original-identity
  - original-activity
  - chemistry
- assessment_id: validation
  area: schema
  topic: Focused validation and scientific limits
  outcome: supported
  summary: Schema, strict and chemistry checks pass. They do not settle the later
    inferential stereochemical assignment or independently resolve the inaccessible
    Reaxys record.
  target_ids:
  - CHEBI:65799
  evidence_ids:
  - gates
  - chemistry
  - reaxys
  - later-stereochemistry
findings:
- finding_id: F1
  issue_key: diperamycin-later-stereochemical-assignment
  category: identity
  severity: informational
  status: open
  certainty: provisional
  title: Adjudicate the later stereochemical assignment before claiming a fully specified
    natural structure
  description: The inherited graph omits all ten stereocentres. The 2024 original
    supplies an explicit assignment using NMR comparison with aurantimycin A and biosynthetic-domain
    similarity. The inspected evidence supports a concrete follow-up, not a confirmed
    wrong-epimer correction or automatic adoption of every stereobond. Preserve the
    original planar record and distinguish measured connectivity from inferred absolute
    stereochemistry until that adjudication is documented.
  target_ids:
  - CHEBI:65799
  field_paths:
  - chemical_structure.smiles
  - chemical_structure.standard_inchi
  - chemical_structure.standard_inchi_key
  evidence_ids:
  - chemistry
  - original-identity
  - later-stereochemistry
  - later-figure
  - later-supplement
  - analogue-original
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Inherited planar structure and identity source
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated record owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Publication-backed exact structure route if warranted
  rule_id: review-checklist:Identity/Structure/Equivalence
  native_severity: informational
  normalization_reason: A concrete unresolved exact-structure follow-up; the reviewed
    sources do not establish a confirmed native epimer error or mandate an automatic
    replacement.
actions:
- action_id: A1
  description: Adjudicate the 2024 stereochemical assignment and document its experimental
    and inferential basis.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:65799
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Inherited planar structure and identity source
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated record owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Publication-backed exact structure route if warranted
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Map every proposed stereocentre to Figure 5 and distinguish original NMR connectivity,
    relative comparisons and biosynthetic absolute-configuration inference.
  - Keep aurantimycin A crystallography and legacy drawing correction separate from
    diperamycin; do not label the latter as directly X-ray determined.
  - If a revised graph is accepted, regenerate all structure fields coherently and
    reconcile exact xrefs and synonyms through maintained inputs; otherwise record
    why the planar form is retained.
  - Run focused chemistry/schema/strict and corpus provenance/reproduction checks
    after any future curation.
limitations:
- The 2024 stereochemical assignment is explicitly inferential from NMR comparison
  and biosynthesis. No new direct absolute-configuration experiment for diperamycin
  was located in the inspected original and supplement. A complete replacement stereograph
  was not independently reconstructed.
- The 1998 paper was read in full with actual Figure 1 and Tables 4–7. The 2024 main
  text, key Figures 4/5 and supplement structural table were read; raw NMR spectra,
  PCR gels and the related aurantimycin crystal coordinates were not independently
  reprocessed.
- The exact Reaxys public route returned 403. Current ChEBI preserves that registry
  identifier but does not independently establish its molecular equivalence.
- Original assay methods omit inoculum, detailed MIC-reading rule and a Candida-specific
  protocol. The 2024 HPLC purification uses TFA but does not establish a defined TFA
  salt; its ammonium MS adduct is not evidence of a formulated ammonium salt.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native/source/status/history was edited. Optional links, tags and notes were
  checked against diperamycin.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:65799
- https://doi.org/10.7164/antibiotics.51.1087
- https://doi.org/10.3390/ijms25042347
tags:
- diperamycin
- cyclodepsipeptide
- stereochemistry
- primary-evidence
```
