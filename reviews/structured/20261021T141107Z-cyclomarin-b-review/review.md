# Cyclomarin B: coherent source graph with unresolved exact activity and epoxide assignment

- Review: 20261021T141107Z-cyclomarin-b-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T13:49:18Z
- Finished UTC: 2026-10-21T14:11:07Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native graph agrees with current ChEBI and PubChem and with the original B constitution: an epoxide-bearing congener lacking the hydroxylated leucine substituent of A. No required native correction is established. Exact B antibacterial evidence and independent epoxide absolute assignment remain unresolved; neither the 2024 A correction nor that paper’s conflicting B drawing is transferred to B. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire cyclomarin B record, actual ARO and PubChem owners, all adopted citation leads, exact chemical equivalence and bounded primary structure, activity, mechanism and producer follow-up.

Selection: Queue position 337; one entire exact record. All 13 original input hashes were preserved within 31 expanded inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-0f5084fe9f | data/antibiotics/antibacterial/cyclomarin-b.yaml | generated | cyclomarin B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-0f5084fe9f | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-0f5084fe9f | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-0f5084fe9f | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | antibioticmech:aro-0f5084fe9f | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-0f5084fe9f | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-0f5084fe9f | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-0f5084fe9f | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-0f5084fe9f | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-0f5084fe9f | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-0f5084fe9f | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-0f5084fe9f | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-0f5084fe9f | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact molecular graph and natural-product assignment

identity: unknown. Targets: antibioticmech:aro-0f5084fe9f.

Constitution, formula and current exact xrefs are coherent. The A-specific stereo correction creates a B follow-up question but does not independently prove the B configuration wrong.

### All native chemical and family xrefs

grounding: supported. Targets: antibioticmech:aro-0f5084fe9f.

All asserted native chemical links match the complete current graph, and the ARO family parent resolves. Database agreement alone does not certify every historical experimental material.

### Definition, classification and all adopted lead dispositions

evidence: unknown. Targets: antibioticmech:aro-0f5084fe9f.

The sole adopted 2016 lead concerns A/C/D, not a new B experiment. The family classification remains an accurately labeled database assertion; this bounded search neither proves B inactive nor establishes a required role deletion.

### Optional exact activity_spectrum

completeness: unknown. Targets: antibioticmech:aro-0f5084fe9f.

No B-specific antibacterial assay was verified. No A, C, derivative, family-screen or crude-extract result should be assigned to B to fill the optional field.

### Optional targets, mechanisms and resistance

completeness: unknown. Targets: antibioticmech:aro-0f5084fe9f.

There are no native target or resistance objects. A-specific ClpC1/ClpC2 studies and family-level abstract statements do not establish the exact congener’s binding or genetic-resistance phenotype; missing optional objects are not a schema defect.

### Optional producer/biosynthetic annotation

provenance: unknown. Targets: antibioticmech:aro-0f5084fe9f.

Original isolation provides producer context but has an internal CNB-982/CNB-382 strain discrepancy. The adjacent exact MIBiG row is D and cannot be joined to this congener. Producer enrichment should preserve original strain spelling, material identity and the level of biosynthetic evidence.

### Clinical products, causal graphs, datasets and host activities

scope: not_applicable. Targets: antibioticmech:aro-0f5084fe9f.

No clinical product, approval, causal graph or dataset claim is populated. Historical antiinflammatory/host-cell observations and parasite growth assays are distinct from clinical antibacterial use and do not require filling every optional domain.

### Owner capture and generated history

provenance: supported. Targets: antibioticmech:aro-0f5084fe9f.

All initial hashes are preserved, actual ARO/PubChem owners are identified, and the three SEEDED history events are consistent with the sparse generated record. A future correction must survive reseeding and retain explicit source conflicts.

### Focused validation

schema: supported. Targets: antibioticmech:aro-0f5084fe9f.

The record passes actual schema, strict and chemistry checks. These gates do not replace primary-source identity or material adjudication.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Resolve B-specific structure/activity questions before adding primary claims.

- Locate a B-specific antibacterial assay and independent epoxide assignment; the A correction and conflicting2024 B drawing are insufficient substitutes.
- Preserve the current source classification as qualified while unresolved; do not claim inactivity from this bounded search.
- Preserve congener identity and distinguish the D-specific MIBiG row from any family biosynthetic evidence.
- Optional enrichment is not required solely because a field is unpopulated; use the authorized curation/history workflow for any eventual addition.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/cyclomarin-b.yaml; Entire YAML, chemical_structure, xrefs, class, definition, source and all three history events | supports | The SEEDED, MINTED antibacterial record contains one ARO family class and a PubChem-derived graph with 11 assigned centres. There are no populated molecular_targets, resistance, activity_spectrum, clinical products, producers, causal_graphs or datasets. No native patent/document identifier or separate synonym list requires disposition. All three history events describe generated seeding/reseeding. |
| owners | data/raw/aro_antibiotics.tsv;data/raw/pubchem_structures.tsv; ARO row 454; PubChem row 168; source extractor, structure enrichment, seeder and decisions ownership | supports | The ARO row owns the definition, class and adopted references; PubChem owns the complete chemical structure. There is no exact ChEBI seed row or ARO target/resistance row for this record in the inspected source subsets. The adjacent MIBiG BGC0000333 row is cyclomarin D and is not an exact A/B/C producer join. All 13 original input hashes were preserved while actual owners and relevant context expanded the capture to 31 inputs. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Exact identity, source assertion scope, evidence placement and optional completeness | supports | A shared name does not establish exact molecular equivalence. Original materials, congener identity and experimental endpoints must remain explicit. Missing optional annotations or an unrecovered citation alone are not confirmed native defects. |
| chemistry | Independent batch019 RDKit calculation against batch034 cwd; 337-chemistry.json;336338-xref-chemistry.py/.json | supports | Native SMILES and InChI parse to the same neutral graph, full key HSTKEHHVGUSTOW-PMBWZYFTSA-N, and 11 assigned stereocentres. Formula, rounded masses and minted identifier reproduce. Independent exact-source comparison includes all stereochemical layers and calculated ring sizes. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/218852/; CHEBI:218852, default structure and chemical data | supports | Current ChEBI exactly matches the native full molecular graph. This confirms the inherited database encoding, not an independent experimental proof of every absolute configuration. Unrelated upstream ontology parents not asserted in the native record were not imported as native findings. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/21593897/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON; CID21593897 complete property response | supports | Current PubChem exactly matches the retained native structure, charge and stereochemical key. |
| aro | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3007542; ARO:3007542 term and ARO:3007540 parent | context_only | The exact term, definition and cyclomarin-antibiotic parent resolve consistently with the native source assertions. A family classification is not itself a congener-specific MIC or target experiment. |
| original1999 | https://www.researchgate.net/profile/Paul-Jensen-6/publication/231532514_Cyclomarins_A-C_New_Antiinflammatory_Cyclic_Peptides_Produced_by_a_Marine_Bacterium_Streptomyces_sp/links/5e189c22299bf10bc3a131a2/Cyclomarins-A-C-New-Antiinflammatory-Cyclic-Peptides-Produced-by-a-Marine-Bacterium-Streptomyces-sp.pdf; DOI:10.1021/ja992482o; full four-page main text through public author-deposited PDF reader, pages11273-11276 | supports | Original isolation distinguishes A, B and C. B lacks the hydroxylated leucine substituent of A but retains the epoxide; C retains that hydroxylated residue and has a terminal alkene instead of the epoxide. A diacetate was crystallized; common amino-acid configurations were anchored by hydrolysis/chiral comparison. The paper does not report a B- or C-specific antibacterial assay. The introduction names producer CNB-982, while the experimental fermentation paragraph prints CNB-382; that internal strain conflict needs preservation before exact producer annotation. |
| original1999-si | https://ndownloader.figshare.com/files/5766324; Original 26-page SI; cover/contents, A and B spectra, B HRFAB and A-diacetate crystallographic tables visually inspected | supports | The official scanned SI supplies original spectra and crystal-coordinate tables. B has formula C56H82N8O10 and an epoxide-bearing NMR assignment in the main paper. Only A diacetate has the reported crystal structure; B was not independently crystallographically assigned. The images were inspected for source/material scope, not subjected to an independent spectral fit or complete coordinate refinement. |
| adopted2016 | https://doi.org/10.1039/C6OB00800C; PMID:27241518; complete original abstract and publisher landing metadata | context_only | The adopted article reports total synthesis and biological evaluation of cyclomarins A, C and D. Its abstract describes ClpC1 and the parasite diadenosine triphosphate hydrolase as targets at paper/family scope. B is not one of the named synthesized congeners. The complete methods and SI were not recovered, so exact material-specific target and potency details are not inferred from this abstract. |
| 2024-main | https://doi.org/10.1021/acs.orglett.4c03473; PMID:39486397 / PMC11574846; full main text, Figure1 and Table1 | supports | The original synthesizes natural S-epoxide cyclomarin A, its R-epoxide epimer CymA-prime, cyclomarin C and metamarin. It identifies the original A crystal/rendered-structure discrepancy and compares NMR with natural and earlier synthetic material. Table1 reports separate measurements for the two A epimers and C; B was neither synthesized nor tested in this study. |
| 2024-si | https://ndownloader.figshare.com/files/50156627; SI pagesS2-S3, S19-S21 and S23-S30; actual S23 and S25 structure/NMR comparison images | supports | The SI explicitly contrasts the S crystal structure with the historical R drawing and compares diagnostic NMR signals of both synthetic epimers with natural A. Synthetic C is separately prepared and characterized. Mtb testing used twofold dilutions in 7H9 without Tween80, 10^4 H37Rv CFU per well, seven days at 37 C, then 18 hours with alamarBlue; MIC is the lowest concentration giving at least 90% inhibition. W2 parasite IC50 used 72-hour exposure and flow cytometry, with biological and technical triplicates. The earlier values collected on S30 are inherited comparators, not newly measured data. |
| 2024-figure | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4166/11574846/f60aee8f6b6c/ol4c03473_0001.jpg; Actual Figure1 chemical structures visually inspected | context_only | Figure1 distinguishes A, A-prime and C, but its B drawing has a terminal alkene and lacks the hydroxylated leucine substituent. That B drawing conflicts with the original B formula and epoxide assignment. It is not used as evidence to replace B’s native graph or to transfer the A-specific stereochemical correction. |
| adapter | https://imodulondb.org/api/datasets; 336338-adapter.json; pre-web structured query, m_tuberculosis/modulome/clpC1 | context_only | The catalog-supported structured query returned Rv3596c/clpC1 and zero iModulons before open protein-mechanism follow-up. This is a gene annotation result, not evidence of compound binding, antibacterial activity or resistance. No congener-specific result is inferred. |
| producer-context | PMID:18331040; Complete original 2008 abstract; adjacent native MIBiG source subset | context_only | The original biosynthesis abstract describes labeling of A in Streptomyces sp. CNB-982 and the cyclomarin/cyclomarazine cluster in Salinispora arenicola CNS205. The local exact-key MIBiG row is D, not this record. Neither a locus-level family annotation nor production of D alone establishes an exact A/B/C producer observation. Full original biosynthetic methods were not used. |
| search | Ignored-inclusive repository searches and public primary discovery; 336338-local-focused.txt; initial exact-record local hits;336338-discovery.json;336338-b-specific.json | context_only | Ignored-inclusive searches covered exact names, keys and identifiers. Existing research/history artifacts were discovery leads only. Exact B queries did not recover a congener-specific antibacterial experiment in this bounded search; that is an access/completeness limit, not proof of inactivity or absence of all literature. |
| access | Public retrieval manifests; 336338-fetch1.json through336338-fetch7.json | context_only | Official chemical records, 2024 full text and the 1999/2024 ACS SI were recovered. The 1999 main PDF was readable through the web reader, while direct download returned 403 and screenshot calls supplied no image pixels; only its official SI and the 2024 reproduction were visually inspected. RSC 2016 full/SI routes returned 403/404, and CCDC direct coordinate routes returned 404. Failed downloads were not treated as papers. |
| gates | Actual focused native checks; 337-focused-results.json; schema and strict logs | supports | Focused chemistry, YAML schema and strict checks all exited 0. These checks establish encoding and schema consistency but do not independently resolve historical natural-product identity or experimental material mapping. |
| b-boundary | Original B assignment versus current graph and later A correction; 336338-xref-chemistry.json; 1999 main Table1 and official SI;2024 Figure1 | context_only | The native and both official chemical records encode the same eleven-centre B graph with an R epoxide. The original B constitution includes the epoxide, unlike the 2024 B drawing. The original independently crystallized only A; the 2024 study synthesized and reconciled only the A epimers. No inspected B-specific stereochemical experiment establishes a required flip of the native epoxide. |

## Limits And Additional Notes

- The 1999 main text was fully readable through the public author-PDF web reader, but direct download returned 403 and screenshot calls supplied no image pixels. Official SI images and the 2024 reproduced crystal/drawing comparison were inspected; original crystal coordinates and all spectra were not independently refined or fitted.
- The 2024 main text and SI methods, final materials and structure/NMR comparison sections were read, with Figure1 and SI S23/S25 visually inspected. All synthetic intermediates, raw spectra and UPLC traces were not independently reanalyzed.
- The adopted 2016 original was read at complete-abstract and publisher-metadata depth. Its main text/SI were not recovered after 403/404 responses; congener-specific numerical or mechanistic details were not invented.
- The original producer paper contains CNB-982/CNB-382 spelling conflict. The 2008 biosynthetic source was read at complete-abstract depth, and the adjacent MIBiG exact source row is D. No exact producer annotation was transferred automatically.
- No B-specific antibacterial measurement or independent absolute epoxide determination was verified in the bounded search. The 2024 Figure1 B drawing conflicts with original constitution and was not used for a correction; absence of a recovered assay is not proof of inactivity.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native record, maintained source, status or history was edited.
- Schema/strict used the batch034 environment; standalone RDKit used the existing batch019 interpreter against batch034 cwd.
- Optional links, tags, field paths and congener-specific claims were checked for this exact target.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T141107Z-cyclomarin-b-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cyclomarin B: coherent source graph with unresolved exact activity and epoxide
  assignment'
started_at: '2026-10-21T13:49:18Z'
finished_at: '2026-10-21T14:11:07Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the native record. The complete YAML
    and actual owner rows were read after verifying the initial capture. Official
    structures were independently parsed and original publications inspected at explicitly
    stated depth. Other review drafts were not used as scientific evidence.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: 'The native graph agrees with current ChEBI and PubChem and with the original
  B constitution: an epoxide-bearing congener lacking the hydroxylated leucine substituent
  of A. No required native correction is established. Exact B antibacterial evidence
  and independent epoxide absolute assignment remain unresolved; neither the 2024
  A correction nor that paper’s conflicting B drawing is transferred to B. Scientific
  assessment retains the stated evidence limits; full verification is blocked by the
  shared native-library failure.'
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
  - path: data/antibiotics/antibacterial/cyclomarin-b.yaml
    sha256: b4c1a8349aedeee21a7c6cce70a282e7a4179fe423a0c73aa502835598678346
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
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
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
  - path: data/raw/mibig_producers.tsv
    sha256: d55289619e77e035ed437d432dd692ab382f254c3841c9a314752ef22578a01b
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
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
  - path: scripts/extract_mibig_producers.py
    sha256: a078cdf4c9b2d09999800ab7ae03f93d3972f29b7d2f460ebbbe7d7ec6b31c53
    role: context
targets:
- target_id: antibioticmech:aro-0f5084fe9f
  path: data/antibiotics/antibacterial/cyclomarin-b.yaml
  label: cyclomarin B
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: ARO identity, definition, class and adopted references
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: PubChem exact structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Chemical structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated native source fields
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Identity grounding overrides
scope:
  description: Entire cyclomarin B record, actual ARO and PubChem owners, all adopted
    citation leads, exact chemical equivalence and bounded primary structure, activity,
    mechanism and producer follow-up.
  selection: Queue position 337; one entire exact record. All 13 original input hashes
    were preserved within 31 expanded inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-0f5084fe9f
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-0f5084fe9f
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    337 (cwd /private/tmp/antibioticmech-record-reviews-034)
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
  - antibioticmech:aro-0f5084fe9f
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cyclomarin-b.yaml (cwd /private/tmp/antibioticmech-record-reviews-034)
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
  - antibioticmech:aro-0f5084fe9f
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cyclomarin-b.yaml --out /private/tmp/am-review-session/337-strict.tsv
    (cwd /private/tmp/antibioticmech-record-reviews-034)
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
  - antibioticmech:aro-0f5084fe9f
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
  - antibioticmech:aro-0f5084fe9f
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
  - antibioticmech:aro-0f5084fe9f
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
  - antibioticmech:aro-0f5084fe9f
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
  - antibioticmech:aro-0f5084fe9f
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
  - antibioticmech:aro-0f5084fe9f
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
  - antibioticmech:aro-0f5084fe9f
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
  - antibioticmech:aro-0f5084fe9f
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
  - antibioticmech:aro-0f5084fe9f
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/cyclomarin-b.yaml
  locator: Entire YAML, chemical_structure, xrefs, class, definition, source and all
    three history events
  accessed_at: '2026-10-21T14:09:22Z'
  support: supports
  summary: The SEEDED, MINTED antibacterial record contains one ARO family class and
    a PubChem-derived graph with 11 assigned centres. There are no populated molecular_targets,
    resistance, activity_spectrum, clinical products, producers, causal_graphs or
    datasets. No native patent/document identifier or separate synonym list requires
    disposition. All three history events describe generated seeding/reseeding.
  snapshot_sha256: e3f7cfb7013513a4b5c13a2ba3db78575ff1de4289b4daa99e2c302bdccff9c3
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv;data/raw/pubchem_structures.tsv
  locator: ARO row 454; PubChem row 168; source extractor, structure enrichment, seeder
    and decisions ownership
  accessed_at: '2026-10-21T14:09:22Z'
  support: supports
  summary: The ARO row owns the definition, class and adopted references; PubChem
    owns the complete chemical structure. There is no exact ChEBI seed row or ARO
    target/resistance row for this record in the inspected source subsets. The adjacent
    MIBiG BGC0000333 row is cyclomarin D and is not an exact A/B/C producer join.
    All 13 original input hashes were preserved while actual owners and relevant context
    expanded the capture to 31 inputs.
  snapshot_sha256: e3f7cfb7013513a4b5c13a2ba3db78575ff1de4289b4daa99e2c302bdccff9c3
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Exact identity, source assertion scope, evidence placement and optional
    completeness
  accessed_at: '2026-10-21T14:09:22Z'
  support: supports
  summary: A shared name does not establish exact molecular equivalence. Original
    materials, congener identity and experimental endpoints must remain explicit.
    Missing optional annotations or an unrecovered citation alone are not confirmed
    native defects.
- evidence_id: chemistry
  kind: validation
  reference: Independent batch019 RDKit calculation against batch034 cwd
  locator: 337-chemistry.json;336338-xref-chemistry.py/.json
  accessed_at: '2026-10-21T14:09:22Z'
  support: supports
  summary: Native SMILES and InChI parse to the same neutral graph, full key HSTKEHHVGUSTOW-PMBWZYFTSA-N,
    and 11 assigned stereocentres. Formula, rounded masses and minted identifier reproduce.
    Independent exact-source comparison includes all stereochemical layers and calculated
    ring sizes.
  snapshot_sha256: 66cbbe67723c340f859e5c622eaa5ee0980c9acdf50247da17764e05d6f35dd2
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/218852/
  locator: CHEBI:218852, default structure and chemical data
  accessed_at: '2026-10-21T13:59:44.114838Z'
  support: supports
  summary: Current ChEBI exactly matches the native full molecular graph. This confirms
    the inherited database encoding, not an independent experimental proof of every
    absolute configuration. Unrelated upstream ontology parents not asserted in the
    native record were not imported as native findings.
  snapshot_sha256: df2e1b41de404c84e104eca47e44c4750bf074bdb6ebb3b3df08fa1ebf9b9707
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/21593897/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON
  locator: CID21593897 complete property response
  accessed_at: '2026-10-21T13:59:44.116383Z'
  support: supports
  summary: Current PubChem exactly matches the retained native structure, charge and
    stereochemical key.
  snapshot_sha256: a5e2e98cb9c593e2d82bcc283745d2fa34ba78fcdfa63d1bbbae69e74b9a814c
- evidence_id: aro
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3007542
  locator: ARO:3007542 term and ARO:3007540 parent
  accessed_at: '2026-10-21T13:59:44.118033Z'
  support: context_only
  summary: The exact term, definition and cyclomarin-antibiotic parent resolve consistently
    with the native source assertions. A family classification is not itself a congener-specific
    MIC or target experiment.
  snapshot_sha256: e110e5bf29d21ab9a826ad14696a70157c9e021c8f2d4de4b99c0d6870e89e9c
- evidence_id: original1999
  kind: primary_source
  reference: https://www.researchgate.net/profile/Paul-Jensen-6/publication/231532514_Cyclomarins_A-C_New_Antiinflammatory_Cyclic_Peptides_Produced_by_a_Marine_Bacterium_Streptomyces_sp/links/5e189c22299bf10bc3a131a2/Cyclomarins-A-C-New-Antiinflammatory-Cyclic-Peptides-Produced-by-a-Marine-Bacterium-Streptomyces-sp.pdf
  locator: DOI:10.1021/ja992482o; full four-page main text through public author-deposited
    PDF reader, pages11273-11276
  accessed_at: '2026-10-21T14:09:22Z'
  support: supports
  summary: Original isolation distinguishes A, B and C. B lacks the hydroxylated leucine
    substituent of A but retains the epoxide; C retains that hydroxylated residue
    and has a terminal alkene instead of the epoxide. A diacetate was crystallized;
    common amino-acid configurations were anchored by hydrolysis/chiral comparison.
    The paper does not report a B- or C-specific antibacterial assay. The introduction
    names producer CNB-982, while the experimental fermentation paragraph prints CNB-382;
    that internal strain conflict needs preservation before exact producer annotation.
- evidence_id: original1999-si
  kind: primary_source
  reference: https://ndownloader.figshare.com/files/5766324
  locator: Original 26-page SI; cover/contents, A and B spectra, B HRFAB and A-diacetate
    crystallographic tables visually inspected
  accessed_at: '2026-10-21T14:01:38.835700Z'
  support: supports
  summary: The official scanned SI supplies original spectra and crystal-coordinate
    tables. B has formula C56H82N8O10 and an epoxide-bearing NMR assignment in the
    main paper. Only A diacetate has the reported crystal structure; B was not independently
    crystallographically assigned. The images were inspected for source/material scope,
    not subjected to an independent spectral fit or complete coordinate refinement.
  snapshot_sha256: c38f4a6bd806274cfb32174299f742c6a7e29799139da5ca0e4779cd18b435bc
- evidence_id: adopted2016
  kind: primary_source
  reference: https://doi.org/10.1039/C6OB00800C
  locator: PMID:27241518; complete original abstract and publisher landing metadata
  accessed_at: '2026-10-21T13:59:44.773088Z'
  support: context_only
  summary: The adopted article reports total synthesis and biological evaluation of
    cyclomarins A, C and D. Its abstract describes ClpC1 and the parasite diadenosine
    triphosphate hydrolase as targets at paper/family scope. B is not one of the named
    synthesized congeners. The complete methods and SI were not recovered, so exact
    material-specific target and potency details are not inferred from this abstract.
  snapshot_sha256: 9bda548da7d19582fd198a3b8eb748dac327f19e74de984564e991176422cb87
- evidence_id: 2024-main
  kind: primary_source
  reference: https://doi.org/10.1021/acs.orglett.4c03473
  locator: PMID:39486397 / PMC11574846; full main text, Figure1 and Table1
  accessed_at: '2026-10-21T14:00:20.751210Z'
  support: supports
  summary: The original synthesizes natural S-epoxide cyclomarin A, its R-epoxide
    epimer CymA-prime, cyclomarin C and metamarin. It identifies the original A crystal/rendered-structure
    discrepancy and compares NMR with natural and earlier synthetic material. Table1
    reports separate measurements for the two A epimers and C; B was neither synthesized
    nor tested in this study.
  snapshot_sha256: aa9632186cb112dc95861b098f33aeb98720a4d68d3a42d05b01c0b094eb2f1b
- evidence_id: 2024-si
  kind: primary_source
  reference: https://ndownloader.figshare.com/files/50156627
  locator: SI pagesS2-S3, S19-S21 and S23-S30; actual S23 and S25 structure/NMR comparison
    images
  accessed_at: '2026-10-21T14:01:38.834451Z'
  support: supports
  summary: The SI explicitly contrasts the S crystal structure with the historical
    R drawing and compares diagnostic NMR signals of both synthetic epimers with natural
    A. Synthetic C is separately prepared and characterized. Mtb testing used twofold
    dilutions in 7H9 without Tween80, 10^4 H37Rv CFU per well, seven days at 37 C,
    then 18 hours with alamarBlue; MIC is the lowest concentration giving at least
    90% inhibition. W2 parasite IC50 used 72-hour exposure and flow cytometry, with
    biological and technical triplicates. The earlier values collected on S30 are
    inherited comparators, not newly measured data.
  snapshot_sha256: e9b412afa2090b9d22c069b907715113a50362bf64df4e91cf6e1d76cbe4a913
- evidence_id: 2024-figure
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4166/11574846/f60aee8f6b6c/ol4c03473_0001.jpg
  locator: Actual Figure1 chemical structures visually inspected
  accessed_at: '2026-10-21T14:01:01.295250Z'
  support: context_only
  summary: Figure1 distinguishes A, A-prime and C, but its B drawing has a terminal
    alkene and lacks the hydroxylated leucine substituent. That B drawing conflicts
    with the original B formula and epoxide assignment. It is not used as evidence
    to replace B’s native graph or to transfer the A-specific stereochemical correction.
  snapshot_sha256: 5c807c7cfc2ee00bd9ce1f45e33fa8ae374175f6bbc0ee41dda467af0ba03e19
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: 336338-adapter.json; pre-web structured query, m_tuberculosis/modulome/clpC1
  accessed_at: '2026-10-21T14:09:22Z'
  support: context_only
  summary: The catalog-supported structured query returned Rv3596c/clpC1 and zero
    iModulons before open protein-mechanism follow-up. This is a gene annotation result,
    not evidence of compound binding, antibacterial activity or resistance. No congener-specific
    result is inferred.
  snapshot_sha256: 4d460d464ba79e442cbfb8994710ffdf8f20d763b7cc699de4145db9cbc4f0e4
- evidence_id: producer-context
  kind: primary_source
  reference: PMID:18331040
  locator: Complete original 2008 abstract; adjacent native MIBiG source subset
  accessed_at: '2026-10-21T14:01:20.385527Z'
  support: context_only
  summary: The original biosynthesis abstract describes labeling of A in Streptomyces
    sp. CNB-982 and the cyclomarin/cyclomarazine cluster in Salinispora arenicola
    CNS205. The local exact-key MIBiG row is D, not this record. Neither a locus-level
    family annotation nor production of D alone establishes an exact A/B/C producer
    observation. Full original biosynthetic methods were not used.
  snapshot_sha256: b218751b926b1bf816bbcea15d7eebb074f486b222ee7390189d8af307aed0e2
- evidence_id: search
  kind: search
  reference: Ignored-inclusive repository searches and public primary discovery
  locator: 336338-local-focused.txt; initial exact-record local hits;336338-discovery.json;336338-b-specific.json
  accessed_at: '2026-10-21T14:09:22Z'
  support: context_only
  summary: Ignored-inclusive searches covered exact names, keys and identifiers. Existing
    research/history artifacts were discovery leads only. Exact B queries did not
    recover a congener-specific antibacterial experiment in this bounded search; that
    is an access/completeness limit, not proof of inactivity or absence of all literature.
  snapshot_sha256: 9fb4b589c378661f6c0430828930c41c3b6e959eb27b2e555a11bfafdffeaadc
  search_scope: 2026-10-21; exact cyclomarin names, native identifiers and key, adopted
    PMIDs and original-paper identifiers. Repository searches included hidden and
    ignored files. Public primary-paper retrieval was bounded; broad Europe PMC retrieval
    used its first 100 results and is not an exhaustive literature census.
- evidence_id: access
  kind: search
  reference: Public retrieval manifests
  locator: 336338-fetch1.json through336338-fetch7.json
  accessed_at: '2026-10-21T14:09:22Z'
  support: context_only
  summary: Official chemical records, 2024 full text and the 1999/2024 ACS SI were
    recovered. The 1999 main PDF was readable through the web reader, while direct
    download returned 403 and screenshot calls supplied no image pixels; only its
    official SI and the 2024 reproduction were visually inspected. RSC 2016 full/SI
    routes returned 403/404, and CCDC direct coordinate routes returned 404. Failed
    downloads were not treated as papers.
  snapshot_sha256: f241c87729acc25045e8e7219f0b3c5bc621cdf14816c8569f236d6d91bf68dd
  search_scope: 2026-10-21; exact cyclomarin names, native identifiers and key, adopted
    PMIDs and original-paper identifiers. Repository searches included hidden and
    ignored files. Public primary-paper retrieval was bounded; broad Europe PMC retrieval
    used its first 100 results and is not an exhaustive literature census.
- evidence_id: gates
  kind: validation
  reference: Actual focused native checks
  locator: 337-focused-results.json; schema and strict logs
  accessed_at: '2026-10-21T14:09:22Z'
  support: supports
  summary: Focused chemistry, YAML schema and strict checks all exited 0. These checks
    establish encoding and schema consistency but do not independently resolve historical
    natural-product identity or experimental material mapping.
  snapshot_sha256: d687d890993e5bf1ee0492635f848e8c61581421fc1db9ed43f5b1de8fb24818
- evidence_id: b-boundary
  kind: validation
  reference: Original B assignment versus current graph and later A correction
  locator: 336338-xref-chemistry.json; 1999 main Table1 and official SI;2024 Figure1
  accessed_at: '2026-10-21T14:09:22Z'
  support: context_only
  summary: The native and both official chemical records encode the same eleven-centre
    B graph with an R epoxide. The original B constitution includes the epoxide, unlike
    the 2024 B drawing. The original independently crystallized only A; the 2024 study
    synthesized and reconciled only the A epimers. No inspected B-specific stereochemical
    experiment establishes a required flip of the native epoxide.
  snapshot_sha256: 66cbbe67723c340f859e5c622eaa5ee0980c9acdf50247da17764e05d6f35dd2
assessments:
- assessment_id: identity
  area: identity
  topic: Exact molecular graph and natural-product assignment
  outcome: unknown
  summary: Constitution, formula and current exact xrefs are coherent. The A-specific
    stereo correction creates a B follow-up question but does not independently prove
    the B configuration wrong.
  target_ids:
  - antibioticmech:aro-0f5084fe9f
  evidence_ids:
  - chemistry
  - chebi
  - pubchem
  - original1999
  - 2024-main
  - 2024-si
  - 2024-figure
- assessment_id: groundings
  area: grounding
  topic: All native chemical and family xrefs
  outcome: supported
  summary: All asserted native chemical links match the complete current graph, and
    the ARO family parent resolves. Database agreement alone does not certify every
    historical experimental material.
  target_ids:
  - antibioticmech:aro-0f5084fe9f
  evidence_ids:
  - aro
  - chebi
  - pubchem
  - chemistry
- assessment_id: source-definition
  area: evidence
  topic: Definition, classification and all adopted lead dispositions
  outcome: unknown
  summary: The sole adopted 2016 lead concerns A/C/D, not a new B experiment. The
    family classification remains an accurately labeled database assertion; this bounded
    search neither proves B inactive nor establishes a required role deletion.
  target_ids:
  - antibioticmech:aro-0f5084fe9f
  evidence_ids:
  - aro
  - adopted2016
  - original1999
  - search
- assessment_id: activity
  area: completeness
  topic: Optional exact activity_spectrum
  outcome: unknown
  summary: No B-specific antibacterial assay was verified. No A, C, derivative, family-screen
    or crude-extract result should be assigned to B to fill the optional field.
  target_ids:
  - antibioticmech:aro-0f5084fe9f
  evidence_ids:
  - rubric
  - search
  - 2024-main
  - 2024-si
- assessment_id: mechanism-resistance
  area: completeness
  topic: Optional targets, mechanisms and resistance
  outcome: unknown
  summary: There are no native target or resistance objects. A-specific ClpC1/ClpC2
    studies and family-level abstract statements do not establish the exact congener’s
    binding or genetic-resistance phenotype; missing optional objects are not a schema
    defect.
  target_ids:
  - antibioticmech:aro-0f5084fe9f
  evidence_ids:
  - native
  - rubric
  - adapter
  - adopted2016
- assessment_id: producer
  area: provenance
  topic: Optional producer/biosynthetic annotation
  outcome: unknown
  summary: Original isolation provides producer context but has an internal CNB-982/CNB-382
    strain discrepancy. The adjacent exact MIBiG row is D and cannot be joined to
    this congener. Producer enrichment should preserve original strain spelling, material
    identity and the level of biosynthetic evidence.
  target_ids:
  - antibioticmech:aro-0f5084fe9f
  evidence_ids:
  - owners
  - original1999
  - producer-context
- assessment_id: other-domains
  area: scope
  topic: Clinical products, causal graphs, datasets and host activities
  outcome: not_applicable
  summary: No clinical product, approval, causal graph or dataset claim is populated.
    Historical antiinflammatory/host-cell observations and parasite growth assays
    are distinct from clinical antibacterial use and do not require filling every
    optional domain.
  target_ids:
  - antibioticmech:aro-0f5084fe9f
  evidence_ids:
  - native
  - original1999
  - rubric
- assessment_id: provenance
  area: provenance
  topic: Owner capture and generated history
  outcome: supported
  summary: All initial hashes are preserved, actual ARO/PubChem owners are identified,
    and the three SEEDED history events are consistent with the sparse generated record.
    A future correction must survive reseeding and retain explicit source conflicts.
  target_ids:
  - antibioticmech:aro-0f5084fe9f
  evidence_ids:
  - native
  - owners
  - search
- assessment_id: gates
  area: schema
  topic: Focused validation
  outcome: supported
  summary: The record passes actual schema, strict and chemistry checks. These gates
    do not replace primary-source identity or material adjudication.
  target_ids:
  - antibioticmech:aro-0f5084fe9f
  evidence_ids:
  - gates
  - chemistry
findings: []
actions:
- action_id: A1
  description: Resolve B-specific structure/activity questions before adding primary
    claims.
  finding_ids: []
  target_ids:
  - antibioticmech:aro-0f5084fe9f
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cyclomarin-b.yaml
    role: Curator-owned optional primary evidence and history
  acceptance_checks:
  - Locate a B-specific antibacterial assay and independent epoxide assignment; the
    A correction and conflicting2024 B drawing are insufficient substitutes.
  - Preserve the current source classification as qualified while unresolved; do not
    claim inactivity from this bounded search.
  - Preserve congener identity and distinguish the D-specific MIBiG row from any family
    biosynthetic evidence.
  - Optional enrichment is not required solely because a field is unpopulated; use
    the authorized curation/history workflow for any eventual addition.
limitations:
- The 1999 main text was fully readable through the public author-PDF web reader,
  but direct download returned 403 and screenshot calls supplied no image pixels.
  Official SI images and the 2024 reproduced crystal/drawing comparison were inspected;
  original crystal coordinates and all spectra were not independently refined or fitted.
- The 2024 main text and SI methods, final materials and structure/NMR comparison
  sections were read, with Figure1 and SI S23/S25 visually inspected. All synthetic
  intermediates, raw spectra and UPLC traces were not independently reanalyzed.
- The adopted 2016 original was read at complete-abstract and publisher-metadata depth.
  Its main text/SI were not recovered after 403/404 responses; congener-specific numerical
  or mechanistic details were not invented.
- The original producer paper contains CNB-982/CNB-382 spelling conflict. The 2008
  biosynthetic source was read at complete-abstract depth, and the adjacent MIBiG
  exact source row is D. No exact producer annotation was transferred automatically.
- No B-specific antibacterial measurement or independent absolute epoxide determination
  was verified in the bounded search. The 2024 Figure1 B drawing conflicts with original
  constitution and was not used for a correction; absence of a recovered assay is
  not proof of inactivity.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native record, maintained source, status or history was edited.
- Schema/strict used the batch034 environment; standalone RDKit used the existing
  batch019 interpreter against batch034 cwd.
- Optional links, tags, field paths and congener-specific claims were checked for
  this exact target.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://pubchem.ncbi.nlm.nih.gov/compound/21593897
- https://doi.org/10.1021/ja992482o
- https://doi.org/10.1021/acs.orglett.4c03473
tags:
- cyclomarin-b
- exact-congener-scope
- primary-material-boundaries
```
