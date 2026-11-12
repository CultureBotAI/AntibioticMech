# Dextrofloxacin: exact R-enantiomer and qualified primary mechanism evidence

- Review: 20261021T143320Z-dextrofloxacin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:11:41Z
- Finished UTC: 2026-10-21T14:33:20Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The neutral R-enantiomer identity is consistent across native encodings, current ChEBI and the XED chemical component. Original experiments support antibacterial activity and gyrase/topoisomerase IV inhibition for DR-3354. The LytA crystal contains dextrofloxacin, while associated enzyme assays used racemic ofloxacin; those endpoints must remain separate. No confirmed native defect was found. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 358; one exact record. All 13 original input hashes are preserved within 31 expanded inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:46577 | data/antibiotics/antibacterial/dextrofloxacin.yaml | generated | dextrofloxacin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:46577 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:46577 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:46577 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:46577 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:46577 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:46577 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:46577 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:46577 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:46577 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:46577 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:46577 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:46577 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral R-enantiomer

identity: supported. Targets: CHEBI:46577.

The full graph, name, definition, chemical role and stereochemical synonyms agree. Neither the S-enantiomer nor the racemate is substituted by a name-only match.

### Chemical and drug cross-references

grounding: supported. Targets: CHEBI:46577.

ChEBI and XED structures agree; the PDB authority maps DB03034 by exact InChIKey. Direct DrugBank access remains limited, so the latter verification is explicitly indirect through its mapped source.

### Antibacterial eligibility and broad mechanism

scope: supported. Targets: CHEBI:46577.

Exact DR-3354 has measured antibacterial activity and gyrase/TopoIV inhibition, supporting the populated broad microbial mode. Lower potency than S-ofloxacin does not make the R-enantiomer inactive. No clinical approval claim is inferred from the retained ontology drug role.

### Optional direct molecular targets

completeness: supported. Targets: CHEBI:46577.

Gyrase/topoisomerase IV primary follow-up is available. LytA has exact-R structural occupancy but racemate functional assay scope; target enrichment must separate those evidence types. Optional target absence is not a schema defect.

### Optional activity_spectrum

completeness: supported. Targets: CHEBI:46577.

The exact-R E. coli KL-16 phenotype is supported. Quantitative curation should verify original Table1 typography and complete assay conditions; no ratio or enzyme IC50 should be substituted for a clinical susceptibility category.

### Optional resistance evidence

evidence: unknown. Targets: CHEBI:46577.

No native resistance entry is populated. Wastewater qnrS association and an abstract-level summary of GrlA mutants are insufficient for a compound-specific allele/strain entry without the corresponding original rows.

### All ten adopted literature leads

evidence: supported. Targets: CHEBI:46577.

All ten original abstracts and metadata were inspected. Two early studies support identity/activity, the 2005 paper supplies bounded structural/functional evidence, and remaining studies are modeling, pharmacokinetic or analytical context. They are not silently converted to primary antimicrobial evidence.

### Clinical products, producer, causal graph and datasets

scope: not_applicable. Targets: CHEBI:46577.

No such native assertions are populated. Tablet dissolution and fish disposition papers do not establish a dextrofloxacin-only product or microbial producer. No causal chain is inferred from the historical stacking model.

### Source ownership, status and generated history

provenance: supported. Targets: CHEBI:46577.

Actual ChEBI ownership and the four generated-history events are coherent. The record remains SEEDED, and all initially captured inputs were preserved.

### Focused native gates

schema: supported. Targets: CHEBI:46577.

Schema, strict and independent chemistry pass. Shared corpus gates are attached separately by root.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optionally curate exact-R phenotype and microbial target evidence with the original material and assay scope.

- Use DR-3354/R-ofloxacin rows separately from racemic ofloxacin and DR-3355.
- Verify original assay table units and complete material/medium/incubation details before adding numerical activity_spectrum entries.
- Keep gyrase supercoiling and TopoIV decatenation IC50 separate from whole-cell MIC, and map any mutant result to its exact original row.
- For LytA distinguish exact-R crystallographic occupancy from racemic enzyme-inhibition assays and avoid claiming a demonstrated growth-inhibition causal chain.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/dextrofloxacin.yaml; Entire 99-line record, synonyms, definition, three parents, two roles, mode/scope, all xrefs, source and four history events | supports | The exact SEEDED record asserts the R-enantiomer, microbial nucleic-acid-synthesis inhibition and CAS, XED and DrugBank groundings. It contains no target, resistance, activity_spectrum, clinical product, producer, causal graph or dataset annotation. History documents seeding, not prior primary scientific sign-off. |
| owner | data/raw/chebi_antimicrobials.tsv; Exact ChEBI row870; maintained classifier/enricher/seeder and source-role configuration | supports | The actual source row reproduces identity, ten literature leads and chemical links. The broad mode is generated from ChEBI topoisomerase/DNA-synthesis roles; the microbial-target scope is supported by the topoisomerase IV role. Original captured hashes remain unchanged and expanded owner/context paths are recorded. |
| chemistry | Independent RDKit2026.03.5, batch019 interpreter against batch036 cwd; 358-chemistry.json;358360-xref-chemistry.json | supports | SMILES and InChI independently reproduce neutral C18H20FN3O4, key GSDSWSVVBLHKDQ-SNVBAGLBSA-N and one assigned R centre. Rounded masses and source mint reproduce. This is the R-enantiomer, not levofloxacin or a racemic graph. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/46577/; Current complete CHEBI:46577 identity, structure, names, parents and role response | supports | Current ChEBI agrees with the complete native graph and R nomenclature. The parent classes and retained antimicrobial/drug roles resolve; source-role assertions distinguish topoisomerase IV from broad DNA-synthesis context. |
| xed | https://data.rcsb.org/rest/v1/core/chemcomp/XED; Chemical component XED descriptors, systematic name and resource mappings | supports | XED InChI and CACTVS stereochemical SMILES reproduce the native R key and neutral formula. Its default OpenEye SMILES omits the centre, so the full descriptor set was compared. RCSB explicitly maps DrugBank DB03034 by matching InChIKey and preserves the historical D-Levofloxacin synonym. Direct DrugBank returned 403; that page was not treated as independently read. |
| structure2005 | https://doi.org/10.1074/jbc.M501236200; Adopted PMID15769740; original author-hosted full-text Experimental Procedures and Results, pages19949/19952; Figure3 caption; PDB2BML | supports | Crystallization used commercial racemic ofloxacin. The 2.6-angstrom LytA choline-binding-domain structure fits dextrofloxacin in one ChBS2 site, providing exact R-ligand structural evidence. DEAE elution and cell-wall-degradation assays instead used racemic ofloxacin, so their inhibitory concentrations are not exact-R potency measurements. This is binding evidence, not proof that LytA inhibition causes DR-3354 bacterial growth inhibition. |
| pdb | https://data.rcsb.org/rest/v1/core/entry/2BML; Current experimental structure and citation metadata | supports | 2BML independently resolves the 2005 pneumococcal LytA study and X-ray structure at 2.6 angstroms. It complements XED identity; it does not convert racemate enzyme-assay results into purified-enantiomer values. |
| adopted-2824776 | https://pubmed.ncbi.nlm.nih.gov/2824776/; Original complete abstract and metadata through Europe PMC core | supports | 1987 asymmetric synthesis and biological evaluation of both enantiomers. The original abstract explicitly reports bacteria and purified gyrase assays and greater S potency; full publisher text returned 403, so individual strain values and synthetic stereochemical proofs were not independently reconstructed. |
| adopted-2079448 | https://pubmed.ncbi.nlm.nih.gov/2079448/; Original complete abstract and metadata through Europe PMC core | supports | 1990 comparative DR-3355 paper explicitly identifies DR-3354 as R-(+)-ofloxacin and reports lower antibacterial potency. Its abstract does not establish an exact-R animal protective dose; the mouse superiority sentence concerns DR-3355. Publisher full text returned 403. |
| adopted-1992111 | https://pubmed.ncbi.nlm.nih.gov/1992111/; Original complete abstract and metadata through Europe PMC core | context_only | 1991 N1-substituent QSAR/receptor-model study. Abstract is theoretical structure-activity context; exact dextrofloxacin rows and experimental sources were not exposed and no quantitative claim is transferred. |
| adopted-17870541 | https://pubmed.ncbi.nlm.nih.gov/17870541/; Original complete abstract and metadata through Europe PMC core | context_only | 2007 human oral-bioavailability HQSAR training/test-set study. No exact-R antibacterial or microbial-target experiment is established from the abstract. |
| adopted-17937485 | https://pubmed.ncbi.nlm.nih.gov/17937485/; Original complete abstract and metadata through Europe PMC core | context_only | 2007 molecular-dynamics comparison of S/R ofloxacin binding to oligonucleotide sequences. Simulated energies and proposed contacts are not an experimentally measured microbial protein target. |
| adopted-25069865 | https://pubmed.ncbi.nlm.nih.gov/25069865/; Original complete abstract and metadata through Europe PMC core | context_only | 2014 enantioselective monoclonal-antibody/immunoassay and epitope-modeling study. Exact optical isomers are distinguished, but hapten recognition is not antibacterial mechanism. |
| adopted-26179954 | https://pubmed.ncbi.nlm.nih.gov/26179954/; Original complete abstract and metadata through Europe PMC core | context_only | 2015 chiral-HPLC pharmacokinetics in Pagrosomus major. Enantioselective disposition is contextual; no exact-R antimicrobial endpoint is measured in the abstract. |
| adopted-29513966 | https://pubmed.ncbi.nlm.nih.gov/29513966/; Original complete abstract and metadata through Europe PMC core | context_only | 2018 dissolution/electrophoresis of racemic ofloxacin tablets and levofloxacin tablets. Formulation dissolution is not a dextrofloxacin-only clinical product or antibacterial assay. |
| adopted-32208173 | https://pubmed.ncbi.nlm.nih.gov/32208173/; Original complete abstract and metadata through Europe PMC core | context_only | 2020 wastewater enantiomer profiling and community qnrS load association. These ecological data do not demonstrate a dextrofloxacin-specific resistance allele, causal mutation, or exact-R MIC. |
| primary1996 | https://doi.org/10.1128/AAC.40.8.1775; PMID8843280; original author-hosted full-text Methods, Results and rendered Table1, pages1775-1779 | supports | Daiichi synthesized DR-3354 separately from the S isomer. E. coli KL-16 agar-dilution MICs used approximately 5×10^4 CFU per spot and complete visible-growth inhibition. R activity was 32-fold weaker than S, and pUC9 supercoiling inhibition was 50-fold weaker. Purified gyrase experiments and competition against radiolabeled S-ofloxacin support an enzyme-DNA-complex mechanism. The proposed four-versus-two-molecule stacking explanation remains a model, not a solved binding structure. |
| primary1997 | https://doi.org/10.1128/AAC.41.11.2362; PMID9371334 / PMC164129; complete original abstract | supports | Reconstituted S. aureus FDA209-P topoisomerase IV was assayed by kinetoplast-DNA decatenation and quantitative electrophoresis. DR-3354 IC50 was 97 micrograms/mL, separately from levofloxacin 2.3. These are enzyme-inhibition values, not MICs. The abstract also reports altered GrlA enzymes, but does not expose each DR-3354 mutant result; no allele-specific resistance observation is added from that summary. |
| adapter | https://imodulondb.org/api/datasets; 358359-adapter-results.json; structured queries before open protein follow-up | context_only | E. coli precise1k queries resolve gyrA/b2231, gyrB/b3699 and parC/b3019 but return zero components. These are annotation/context results, not compound binding. The catalog has no pneumococcal dataset for transferring the LytA observation; no absence of biology is inferred. |
| search | Ignored-inclusive local search and public original-source follow-up; 358360-local-focused.txt;358-discovery.json;358360-fetch1-4.json | context_only | Every adopted PMID abstract was inspected and disposed by material/endpoint. Additional 1996/1997 originals support the exact-R mechanism. Publisher/PDF/figure routes returned 403,404 or HTML challenge; author-hosted full-text methods/results were read through the browser, while the actual scanned Table1 and Figure3 pixels were not retrieved. |
| gates | Focused schema, strict and chemistry execution; 358-focused-results.json;358-schema.log;358-strict.log | supports | All focused checks exit 0. The schema/strict commands used batch036; standalone RDKit used the existing locked batch019 interpreter against batch036 cwd. |

## Limits And Additional Notes

- All ten adopted abstracts were read. The 1987/1990 publisher full texts were blocked; modeling/analytical leads were read at abstract depth. The 1996 Methods/Results/Table1 and 2005 Experimental Procedures/Results were accessible as author-hosted full-text rendering; actual table/structure image pixels were not successfully retrieved. The 1997 target paper was verified at original abstract depth.
- Direct DrugBank returned 403. XED supplies an explicit exact-InChIKey mapping to DB03034, but that is not a successful independent DrugBank page retrieval.
- Source-only drug-role retention does not assert approval of a dextrofloxacin-only formulation. No clinical efficacy, producer, causal graph or exact-R resistance allele is established here.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native/source/status/history was edited.
- All optional links, tags and notes were checked against dextrofloxacin.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T143320Z-dextrofloxacin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Dextrofloxacin: exact R-enantiomer and qualified primary mechanism evidence'
started_at: '2026-10-21T14:11:41Z'
finished_at: '2026-10-21T14:33:20Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Independent reviewer read the complete native record and actual
    ChEBI row after verifying original captures, computed chemical identity, inspected
    current official groundings and every adopted primary abstract, and read bounded
    original full-text methods/results for exact compound and assay distinctions.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: The neutral R-enantiomer identity is consistent across native encodings,
  current ChEBI and the XED chemical component. Original experiments support antibacterial
  activity and gyrase/topoisomerase IV inhibition for DR-3354. The LytA crystal contains
  dextrofloxacin, while associated enzyme assays used racemic ofloxacin; those endpoints
  must remain separate. No confirmed native defect was found. Scientific assessment
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
  - path: data/antibiotics/antibacterial/dextrofloxacin.yaml
    sha256: c6f8ee7cd9ef679e209d636a283cf3a3a888046044159ddea60bab86b87b92e1
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
- target_id: CHEBI:46577
  path: data/antibiotics/antibacterial/dextrofloxacin.yaml
  label: dextrofloxacin
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
  selection: Queue position 358; one exact record. All 13 original input hashes are
    preserved within 31 expanded inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:46577
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:46577
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/358360-focused.py
    (cwd /private/tmp/antibioticmech-record-reviews-036)
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
  - CHEBI:46577
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/dextrofloxacin.yaml (cwd /private/tmp/antibioticmech-record-reviews-036)
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
  - CHEBI:46577
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/dextrofloxacin.yaml --out /private/tmp/am-review-session/358-strict.tsv
    (cwd /private/tmp/antibioticmech-record-reviews-036)
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
  - CHEBI:46577
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
  - CHEBI:46577
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
  - CHEBI:46577
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
  - CHEBI:46577
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
  - CHEBI:46577
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
  - CHEBI:46577
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
  - CHEBI:46577
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
  - CHEBI:46577
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
  - CHEBI:46577
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/dextrofloxacin.yaml
  locator: Entire 99-line record, synonyms, definition, three parents, two roles,
    mode/scope, all xrefs, source and four history events
  accessed_at: '2026-10-21T14:27:04Z'
  support: supports
  summary: The exact SEEDED record asserts the R-enantiomer, microbial nucleic-acid-synthesis
    inhibition and CAS, XED and DrugBank groundings. It contains no target, resistance,
    activity_spectrum, clinical product, producer, causal graph or dataset annotation.
    History documents seeding, not prior primary scientific sign-off.
  snapshot_sha256: 65183770d185d35acd44f87bdb34e69c10a0c21e7d5dda438d2a98e2dda0afe2
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Exact ChEBI row870; maintained classifier/enricher/seeder and source-role
    configuration
  accessed_at: '2026-10-21T14:27:04Z'
  support: supports
  summary: The actual source row reproduces identity, ten literature leads and chemical
    links. The broad mode is generated from ChEBI topoisomerase/DNA-synthesis roles;
    the microbial-target scope is supported by the topoisomerase IV role. Original
    captured hashes remain unchanged and expanded owner/context paths are recorded.
  snapshot_sha256: 65183770d185d35acd44f87bdb34e69c10a0c21e7d5dda438d2a98e2dda0afe2
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit2026.03.5, batch019 interpreter against batch036 cwd
  locator: 358-chemistry.json;358360-xref-chemistry.json
  accessed_at: '2026-10-21T14:27:04Z'
  support: supports
  summary: SMILES and InChI independently reproduce neutral C18H20FN3O4, key GSDSWSVVBLHKDQ-SNVBAGLBSA-N
    and one assigned R centre. Rounded masses and source mint reproduce. This is the
    R-enantiomer, not levofloxacin or a racemic graph.
  snapshot_sha256: 81ca9ad086eec92dfbe33c225f77fd3276d9c46dc7ae089fd3a346f7fce51f73
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/46577/
  locator: Current complete CHEBI:46577 identity, structure, names, parents and role
    response
  accessed_at: '2026-10-21T14:22:03.073950Z'
  support: supports
  summary: Current ChEBI agrees with the complete native graph and R nomenclature.
    The parent classes and retained antimicrobial/drug roles resolve; source-role
    assertions distinguish topoisomerase IV from broad DNA-synthesis context.
  snapshot_sha256: c447a50aeaa84cbfb08fb6b642e4d713e2fd2f72a239f98c8e584d6554637a47
- evidence_id: xed
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/chemcomp/XED
  locator: Chemical component XED descriptors, systematic name and resource mappings
  accessed_at: '2026-10-21T14:22:03.087199Z'
  support: supports
  summary: XED InChI and CACTVS stereochemical SMILES reproduce the native R key and
    neutral formula. Its default OpenEye SMILES omits the centre, so the full descriptor
    set was compared. RCSB explicitly maps DrugBank DB03034 by matching InChIKey and
    preserves the historical D-Levofloxacin synonym. Direct DrugBank returned 403;
    that page was not treated as independently read.
  snapshot_sha256: f0f592caf2be05d347b728c253ad0e59a004a46129d9b70507186c9467d3e478
- evidence_id: structure2005
  kind: primary_source
  reference: https://doi.org/10.1074/jbc.M501236200
  locator: Adopted PMID15769740; original author-hosted full-text Experimental Procedures
    and Results, pages19949/19952; Figure3 caption; PDB2BML
  accessed_at: '2026-10-21T14:27:04Z'
  support: supports
  summary: Crystallization used commercial racemic ofloxacin. The 2.6-angstrom LytA
    choline-binding-domain structure fits dextrofloxacin in one ChBS2 site, providing
    exact R-ligand structural evidence. DEAE elution and cell-wall-degradation assays
    instead used racemic ofloxacin, so their inhibitory concentrations are not exact-R
    potency measurements. This is binding evidence, not proof that LytA inhibition
    causes DR-3354 bacterial growth inhibition.
  snapshot_sha256: d1bfc655ec981e235f4c82f7bc9c444918a4de4ae10ba8ef3488cdef09806f5c
- evidence_id: pdb
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/entry/2BML
  locator: Current experimental structure and citation metadata
  accessed_at: '2026-10-21T14:23:25.515828Z'
  support: supports
  summary: 2BML independently resolves the 2005 pneumococcal LytA study and X-ray
    structure at 2.6 angstroms. It complements XED identity; it does not convert racemate
    enzyme-assay results into purified-enantiomer values.
  snapshot_sha256: 0fa73da994ec22eefd4360cd87244332d6c7a8a86dc445b3277d69576cfba629
- evidence_id: adopted-2824776
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/2824776/
  locator: Original complete abstract and metadata through Europe PMC core
  accessed_at: '2026-10-21T14:22:04.862901Z'
  support: supports
  summary: 1987 asymmetric synthesis and biological evaluation of both enantiomers.
    The original abstract explicitly reports bacteria and purified gyrase assays and
    greater S potency; full publisher text returned 403, so individual strain values
    and synthetic stereochemical proofs were not independently reconstructed.
  snapshot_sha256: 1b37216e14fe7a8ff6e79a40b77b58496bb0b280083376334705719ec689d8e7
- evidence_id: adopted-2079448
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/2079448/
  locator: Original complete abstract and metadata through Europe PMC core
  accessed_at: '2026-10-21T14:22:04.862901Z'
  support: supports
  summary: 1990 comparative DR-3355 paper explicitly identifies DR-3354 as R-(+)-ofloxacin
    and reports lower antibacterial potency. Its abstract does not establish an exact-R
    animal protective dose; the mouse superiority sentence concerns DR-3355. Publisher
    full text returned 403.
  snapshot_sha256: 1b37216e14fe7a8ff6e79a40b77b58496bb0b280083376334705719ec689d8e7
- evidence_id: adopted-1992111
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/1992111/
  locator: Original complete abstract and metadata through Europe PMC core
  accessed_at: '2026-10-21T14:22:04.862901Z'
  support: context_only
  summary: 1991 N1-substituent QSAR/receptor-model study. Abstract is theoretical
    structure-activity context; exact dextrofloxacin rows and experimental sources
    were not exposed and no quantitative claim is transferred.
  snapshot_sha256: 1b37216e14fe7a8ff6e79a40b77b58496bb0b280083376334705719ec689d8e7
- evidence_id: adopted-17870541
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/17870541/
  locator: Original complete abstract and metadata through Europe PMC core
  accessed_at: '2026-10-21T14:22:04.862901Z'
  support: context_only
  summary: 2007 human oral-bioavailability HQSAR training/test-set study. No exact-R
    antibacterial or microbial-target experiment is established from the abstract.
  snapshot_sha256: 1b37216e14fe7a8ff6e79a40b77b58496bb0b280083376334705719ec689d8e7
- evidence_id: adopted-17937485
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/17937485/
  locator: Original complete abstract and metadata through Europe PMC core
  accessed_at: '2026-10-21T14:22:04.862901Z'
  support: context_only
  summary: 2007 molecular-dynamics comparison of S/R ofloxacin binding to oligonucleotide
    sequences. Simulated energies and proposed contacts are not an experimentally
    measured microbial protein target.
  snapshot_sha256: 1b37216e14fe7a8ff6e79a40b77b58496bb0b280083376334705719ec689d8e7
- evidence_id: adopted-25069865
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/25069865/
  locator: Original complete abstract and metadata through Europe PMC core
  accessed_at: '2026-10-21T14:22:04.862901Z'
  support: context_only
  summary: 2014 enantioselective monoclonal-antibody/immunoassay and epitope-modeling
    study. Exact optical isomers are distinguished, but hapten recognition is not
    antibacterial mechanism.
  snapshot_sha256: 1b37216e14fe7a8ff6e79a40b77b58496bb0b280083376334705719ec689d8e7
- evidence_id: adopted-26179954
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/26179954/
  locator: Original complete abstract and metadata through Europe PMC core
  accessed_at: '2026-10-21T14:22:04.862901Z'
  support: context_only
  summary: 2015 chiral-HPLC pharmacokinetics in Pagrosomus major. Enantioselective
    disposition is contextual; no exact-R antimicrobial endpoint is measured in the
    abstract.
  snapshot_sha256: 1b37216e14fe7a8ff6e79a40b77b58496bb0b280083376334705719ec689d8e7
- evidence_id: adopted-29513966
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/29513966/
  locator: Original complete abstract and metadata through Europe PMC core
  accessed_at: '2026-10-21T14:22:04.862901Z'
  support: context_only
  summary: 2018 dissolution/electrophoresis of racemic ofloxacin tablets and levofloxacin
    tablets. Formulation dissolution is not a dextrofloxacin-only clinical product
    or antibacterial assay.
  snapshot_sha256: 1b37216e14fe7a8ff6e79a40b77b58496bb0b280083376334705719ec689d8e7
- evidence_id: adopted-32208173
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/32208173/
  locator: Original complete abstract and metadata through Europe PMC core
  accessed_at: '2026-10-21T14:22:04.862901Z'
  support: context_only
  summary: 2020 wastewater enantiomer profiling and community qnrS load association.
    These ecological data do not demonstrate a dextrofloxacin-specific resistance
    allele, causal mutation, or exact-R MIC.
  snapshot_sha256: 1b37216e14fe7a8ff6e79a40b77b58496bb0b280083376334705719ec689d8e7
- evidence_id: primary1996
  kind: primary_source
  reference: https://doi.org/10.1128/AAC.40.8.1775
  locator: PMID8843280; original author-hosted full-text Methods, Results and rendered
    Table1, pages1775-1779
  accessed_at: '2026-10-21T14:27:04Z'
  support: supports
  summary: Daiichi synthesized DR-3354 separately from the S isomer. E. coli KL-16
    agar-dilution MICs used approximately 5×10^4 CFU per spot and complete visible-growth
    inhibition. R activity was 32-fold weaker than S, and pUC9 supercoiling inhibition
    was 50-fold weaker. Purified gyrase experiments and competition against radiolabeled
    S-ofloxacin support an enzyme-DNA-complex mechanism. The proposed four-versus-two-molecule
    stacking explanation remains a model, not a solved binding structure.
  snapshot_sha256: 41249ea9346171e5139530aee7fa6d67fe9723860d5a634dc2794721e1eed367
- evidence_id: primary1997
  kind: primary_source
  reference: https://doi.org/10.1128/AAC.41.11.2362
  locator: PMID9371334 / PMC164129; complete original abstract
  accessed_at: '2026-10-21T14:22:50.364193Z'
  support: supports
  summary: Reconstituted S. aureus FDA209-P topoisomerase IV was assayed by kinetoplast-DNA
    decatenation and quantitative electrophoresis. DR-3354 IC50 was 97 micrograms/mL,
    separately from levofloxacin 2.3. These are enzyme-inhibition values, not MICs.
    The abstract also reports altered GrlA enzymes, but does not expose each DR-3354
    mutant result; no allele-specific resistance observation is added from that summary.
  snapshot_sha256: 893113e6706751d2152d9d05df2e527e1fbea40bea07dcce367314abe3720ae5
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: 358359-adapter-results.json; structured queries before open protein follow-up
  accessed_at: '2026-10-21T14:27:04Z'
  support: context_only
  summary: E. coli precise1k queries resolve gyrA/b2231, gyrB/b3699 and parC/b3019
    but return zero components. These are annotation/context results, not compound
    binding. The catalog has no pneumococcal dataset for transferring the LytA observation;
    no absence of biology is inferred.
  snapshot_sha256: 40b08605e857ca5cd8c4ce00031fecfe236a176bab2a9df96019cf67b0027584
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local search and public original-source follow-up
  locator: 358360-local-focused.txt;358-discovery.json;358360-fetch1-4.json
  accessed_at: '2026-10-21T14:22:05.148125Z'
  support: context_only
  summary: Every adopted PMID abstract was inspected and disposed by material/endpoint.
    Additional 1996/1997 originals support the exact-R mechanism. Publisher/PDF/figure
    routes returned 403,404 or HTML challenge; author-hosted full-text methods/results
    were read through the browser, while the actual scanned Table1 and Figure3 pixels
    were not retrieved.
  snapshot_sha256: a86d1077c16fa3f9c232b2beddf3c710dd2215b5b2d3cc2162bcafeb8c4997e3
  search_scope: 2026-10-21; dextrofloxacin, R-ofloxacin, DR-3354, CHEBI:46577, PDB-CCD:XED,
    DB03034 and all ten adopted PMIDs. Local exact-reference search included ignored
    and hidden files. Primary follow-up was bounded to identity, antibacterial eligibility
    and asserted mechanism; no exhaustive literature absence is claimed.
- evidence_id: gates
  kind: validation
  reference: Focused schema, strict and chemistry execution
  locator: 358-focused-results.json;358-schema.log;358-strict.log
  accessed_at: '2026-10-21T14:27:04Z'
  support: supports
  summary: All focused checks exit 0. The schema/strict commands used batch036; standalone
    RDKit used the existing locked batch019 interpreter against batch036 cwd.
  snapshot_sha256: 527ade0c9f608a75647303104373ba2055235bcd2717ed2d76cb71b49c056e38
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral R-enantiomer
  outcome: supported
  summary: The full graph, name, definition, chemical role and stereochemical synonyms
    agree. Neither the S-enantiomer nor the racemate is substituted by a name-only
    match.
  target_ids:
  - CHEBI:46577
  evidence_ids:
  - chemistry
  - chebi
  - xed
  - adopted-2824776
  - adopted-2079448
- assessment_id: groundings
  area: grounding
  topic: Chemical and drug cross-references
  outcome: supported
  summary: ChEBI and XED structures agree; the PDB authority maps DB03034 by exact
    InChIKey. Direct DrugBank access remains limited, so the latter verification is
    explicitly indirect through its mapped source.
  target_ids:
  - CHEBI:46577
  evidence_ids:
  - chebi
  - xed
  - pdb
- assessment_id: classification
  area: scope
  topic: Antibacterial eligibility and broad mechanism
  outcome: supported
  summary: Exact DR-3354 has measured antibacterial activity and gyrase/TopoIV inhibition,
    supporting the populated broad microbial mode. Lower potency than S-ofloxacin
    does not make the R-enantiomer inactive. No clinical approval claim is inferred
    from the retained ontology drug role.
  target_ids:
  - CHEBI:46577
  evidence_ids:
  - primary1996
  - primary1997
  - adopted-2824776
  - adopted-2079448
  - owner
- assessment_id: targets
  area: completeness
  topic: Optional direct molecular targets
  outcome: supported
  summary: Gyrase/topoisomerase IV primary follow-up is available. LytA has exact-R
    structural occupancy but racemate functional assay scope; target enrichment must
    separate those evidence types. Optional target absence is not a schema defect.
  target_ids:
  - CHEBI:46577
  evidence_ids:
  - primary1996
  - primary1997
  - structure2005
  - adapter
- assessment_id: activity
  area: completeness
  topic: Optional activity_spectrum
  outcome: supported
  summary: The exact-R E. coli KL-16 phenotype is supported. Quantitative curation
    should verify original Table1 typography and complete assay conditions; no ratio
    or enzyme IC50 should be substituted for a clinical susceptibility category.
  target_ids:
  - CHEBI:46577
  evidence_ids:
  - primary1996
  - primary1997
- assessment_id: resistance
  area: evidence
  topic: Optional resistance evidence
  outcome: unknown
  summary: No native resistance entry is populated. Wastewater qnrS association and
    an abstract-level summary of GrlA mutants are insufficient for a compound-specific
    allele/strain entry without the corresponding original rows.
  target_ids:
  - CHEBI:46577
  evidence_ids:
  - adopted-32208173
  - primary1997
- assessment_id: leads
  area: evidence
  topic: All ten adopted literature leads
  outcome: supported
  summary: All ten original abstracts and metadata were inspected. Two early studies
    support identity/activity, the 2005 paper supplies bounded structural/functional
    evidence, and remaining studies are modeling, pharmacokinetic or analytical context.
    They are not silently converted to primary antimicrobial evidence.
  target_ids:
  - CHEBI:46577
  evidence_ids:
  - structure2005
  - adopted-2824776
  - adopted-2079448
  - adopted-1992111
  - adopted-17870541
  - adopted-17937485
  - adopted-25069865
  - adopted-26179954
  - adopted-29513966
  - adopted-32208173
- assessment_id: other
  area: scope
  topic: Clinical products, producer, causal graph and datasets
  outcome: not_applicable
  summary: No such native assertions are populated. Tablet dissolution and fish disposition
    papers do not establish a dextrofloxacin-only product or microbial producer. No
    causal chain is inferred from the historical stacking model.
  target_ids:
  - CHEBI:46577
  evidence_ids:
  - native
  - adopted-29513966
  - adopted-26179954
  - primary1996
- assessment_id: provenance
  area: provenance
  topic: Source ownership, status and generated history
  outcome: supported
  summary: Actual ChEBI ownership and the four generated-history events are coherent.
    The record remains SEEDED, and all initially captured inputs were preserved.
  target_ids:
  - CHEBI:46577
  evidence_ids:
  - native
  - owner
- assessment_id: schema
  area: schema
  topic: Focused native gates
  outcome: supported
  summary: Schema, strict and independent chemistry pass. Shared corpus gates are
    attached separately by root.
  target_ids:
  - CHEBI:46577
  evidence_ids:
  - gates
  - chemistry
findings: []
actions:
- action_id: A1
  description: Optionally curate exact-R phenotype and microbial target evidence with
    the original material and assay scope.
  finding_ids: []
  target_ids:
  - CHEBI:46577
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/dextrofloxacin.yaml
    role: Curator-owned primary evidence and history
  acceptance_checks:
  - Use DR-3354/R-ofloxacin rows separately from racemic ofloxacin and DR-3355.
  - Verify original assay table units and complete material/medium/incubation details
    before adding numerical activity_spectrum entries.
  - Keep gyrase supercoiling and TopoIV decatenation IC50 separate from whole-cell
    MIC, and map any mutant result to its exact original row.
  - For LytA distinguish exact-R crystallographic occupancy from racemic enzyme-inhibition
    assays and avoid claiming a demonstrated growth-inhibition causal chain.
limitations:
- All ten adopted abstracts were read. The 1987/1990 publisher full texts were blocked;
  modeling/analytical leads were read at abstract depth. The 1996 Methods/Results/Table1
  and 2005 Experimental Procedures/Results were accessible as author-hosted full-text
  rendering; actual table/structure image pixels were not successfully retrieved.
  The 1997 target paper was verified at original abstract depth.
- Direct DrugBank returned 403. XED supplies an explicit exact-InChIKey mapping to
  DB03034, but that is not a successful independent DrugBank page retrieval.
- Source-only drug-role retention does not assert approval of a dextrofloxacin-only
  formulation. No clinical efficacy, producer, causal graph or exact-R resistance
  allele is established here.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native/source/status/history was edited.
- All optional links, tags and notes were checked against dextrofloxacin.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:46577
- https://www.rcsb.org/ligand/XED
- https://doi.org/10.1128/AAC.40.8.1775
- https://doi.org/10.1074/jbc.M501236200
tags:
- dextrofloxacin
- R-ofloxacin
- enantiomer-scope
- gyrase
- topoisomerase-IV
```
