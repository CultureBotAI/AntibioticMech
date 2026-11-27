# Review cefaclor exact identity and PBP evidence

- Review: 20261021T105902Z-cefaclor-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:44:46Z
- Finished UTC: 2026-10-21T10:59:02Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native anhydrous cefaclor graph and antibacterial classification are supported. One major exact-xref defect maps the acid to a monohydrate ChEMBL entity. The parent CHEMBL680 matches exactly. The imported PBP and H. influenzae target-alteration claims remain honestly database-labelled; primary transformation experiments support bounded resistance enrichment.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position204; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:3478 | data/antibiotics/antibacterial/cefaclor.yaml | generated | cefaclor |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:3478 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:3478 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:3478 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:3478 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:3478 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:3478 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:3478 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:3478 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:3478 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:3478 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:3478 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:3478 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral parent

identity: supported. Targets: CHEBI:3478.

Internal encodings, masses, source mints and current ChEBI/PubChem identity agree. No parent structure change is proposed.

### Source and history ownership

provenance: supported. Targets: CHEBI:3478.

Both source concepts and four dated seed/reseed events are coherent. Original hashes remain intact; no native-only correction is proposed.

### Structured gene context

scope: supported. Targets: CHEBI:3478.

Required adapter-first lookup completed. Contextual gene search hits do not establish target engagement.

### Optional blank domains

completeness: supported. Targets: CHEBI:3478.

No blank optional causal graph, producer, activity or clinical field is itself a defect. Any enrichment must preserve exact material, taxon, strain and assay scope.

### Anhydrous molecule versus hydrate xref

grounding: concern. Targets: CHEBI:3478.

Exact CHEMBL1201018 points to a monohydrate. CHEMBL680, ChEBI, PubChem and KEGG match the native anhydrous structure.

### Cephalosporin class and antimicrobial drug context

grounding: supported. Targets: CHEBI:3478.

Native chloro/aminophenylacetamido cephalosporin structure and broad antibacterial drug filing are supported. All three native configured centres are R; no new stereochemistry is imposed.

### PBP target assertion

evidence: supported. Targets: CHEBI:3478.

The native database source and PRIMARY_EVIDENCE_NEEDED status honestly state their limits. Retrieved derivative-binding and other-antibiotic competition data are not direct exact-cefaclor binding evidence.

### H. influenzae PBP3 alteration

evidence: supported. Targets: CHEBI:3478.

The imported target-alteration assertion has contextual primary association and transformation support. Do not convert linked SNP association into proof of one substitution or transfer E. coli adapter IDs to H. influenzae.

### Drug, document and remaining source links

provenance: supported. Targets: CHEBI:3478.

KEGG and DrugCentral placements are coherent; patents resolve as broader documents. HMDB/DrugBank/LINCS/Reaxys independent access limits remain explicit.

## Findings

### F1: Replace or withhold the hydrate ChEMBL exact xref

major / open / confirmed; issue key: cefaclor-chembl-hydrate-exact-xref.

CHEMBL1201018 denotes cefaclor monohydrate with an explicit additional water fragment and a different full key. The native exact record denotes anhydrous cefaclor. CHEMBL680 is the explicitly linked parent and matches the native graph. This is a chemical-form mismatch, not a stereochemical correction to cefaclor.

## Recommended Actions And Acceptance Checks

### A1

Adjudicate the hydrate mapping in the maintained ARO/xref extraction path.

- Withhold CHEMBL1201018 as an exact xref or explicitly qualify a supported hydrate relation. Consider CHEMBL680 as the exact replacement using the verified complete key.
- Retain ARO provenance and reproduce the correction through extraction/seeding; do not add water to the native acid to fit the wrong accession.
- Run focused schema/strict, identity and duplicate/xref gates, source provenance and full corpus reproduction after curation.

### A2

Optionally add bounded primary ftsI resistance evidence and retain target evidence limits.

- Preserve recipient Rd ATCC51097, donor ftsI source, MIC1to16ug/mL, medium and selection context. Keep clinical-isolate associations distinct from transformation evidence.
- Do not infer unmodified cefaclor PBP affinity from Bolton-Hunter derivatives or from ampicillin/cefotaxime/faropenem competition panels.
- If extracting2018 MICs, inspect its supplementary table and resolve isolate/species qualifiers before assigning taxon-level resistance observations.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/cefaclor.yaml; Entire native YAML and source/history blocks | supports | Entire neutral-parent record read. All native synonyms, chemical encodings, roles, parents, exact/drug/document cross-references, source concepts and history events were assessed. Native SEEDED status remains unchanged. |
| chemistry | Independent RDKit calculations; 204-chemistry.json | supports | Both SMILES and InChI reproduce the native full key, formula, charge, masses and configured stereochemistry. Both ARO and ChEBI source mints independently match. |
| owners | data/raw/chebi_antimicrobials.tsv;data/raw/aro_antibiotics.tsv; Exact adopted rows; extractor/seeder; original and expanded inspect captures | supports | ChEBI supplies the neutral structure and synonyms; ARO supplies class and complementary mappings. Actual owners were appended while preserving original hashes. The ignored-inclusive curation/conf search found no exact correction for these specific findings. |
| adapter | iModulonDB; 203-204-adapter-catalog.json;203-204-adapter-pbp.txt;204-adapter-ftsi.txt | supports | Catalog and gene searches were executed before web follow-up. The catalog has no H. influenzae dataset. E. coli/modulome penicillin query returns b2430/yfeW, PBP4B; ftsI returns b0084. No iModulon component was returned, so no component summary was applicable. These are contextual gene matches, not drug-binding evidence or cross-species protein identity. |
| authorities | https://www.ebi.ac.uk/chebi/CHEBI:3478; 204-ols.json;204-chebi.html;204-aro-stanzas.txt | supports | Current ChEBI neutral structure matches the native graph. Adopted ARO class and compound definitions were read in the separately hashed local ontology cache. The broad cephalosporin parents are compatible with the graph. Current registry labels are not clinical approval evidence. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/51039; 204-pubchem.json | supports | The current PubChem full stereochemical key and neutral molecular formula agree exactly with the native structure. |
| drugcentral | https://drugcentral.org/drugcard/525; 204-drugcentral.html; drug card identity section | supports | DrugCentral resolves the expected parent name, CAS and formula but also lists product/form synonyms. Native drug_xrefs placement permits that drug-level context; it does not make every product synonym an exact chemical equivalence. |
| chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL1201018.json; 204-chembl.json; hierarchy and full molecular structure | refutes | Native exact xref CHEMBL1201018 has a disconnected water molecule, C15H14ClN3O4S.H2O and full key WKJGTOYAEQDNIA-IOOZKYRYSA-N. Its hierarchy explicitly names CHEMBL680 as parent/active entity. CHEMBL680 has the exact native anhydrous key QYIYFLOTGYLRGG-GPCCPHFNSA-N. The mismatch originates in the adopted ARO xref. |
| parent | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL680.json; Current parent molecular graph | supports | CHEMBL680 independently matches the native complete key and formula. It is a candidate exact-xref replacement after maintained source adjudication; the native graph should not gain water to accommodate a wrong link. |
| kegg | https://rest.kegg.jp/get/C06877; 204-kegg.txt/.mol;204-keggdrug.txt | supports | KEGG C06877 MOL independently gives QYIYFLOTGYLRGG-GPCCPHFNSA-N. Drug D00256 explicitly names cefaclor anhydrous and has the same formula. These placements are coherent. |
| documents | patent:US3925372;patent:DE2408698; 204-patent-US.html;204-patent-DE.html, document titles/scope | supports | Both patent identifiers resolve to alpha-aminoacyl-3-halo cephalosporin documents. Document placement is appropriate; titles and scope were inspected, not every example or claim. Wikipedia is retained only as a document link. |
| adopted | PMID:10230635;10930630;11963587;12485718;12569987;15812119;18969055;29017833;10435677;29352811;3055170;15673804;11585791;6810737; 204-core-fixed.json; all14 metadata records and all12 available complete abstracts | supports | 10230635 concerns new derivatives;10930630/12569987 concern IgE recognition;12485718/18969055 are analytical derivatization methods;29017833 is an allergy review. 11963587 reports a466-isolate respiratory susceptibility panel (disc/E-test, population MIC90);15812119 is a pediatric clinical comparison. 10435677 is the cefaclor review cited by ARO. 29352811 is the resistance study inspected in full. Parent PBP/beta-lactamase/cephalosporin references are reviews;15673804 and6810737 lack abstracts. Host, derivative and population endpoints are not direct target binding. |
| resistance2018 | https://doi.org/10.1186/s13104-018-3169-0; PMID29352811/PMC5775570; full main Methods, Results, Discussion, limitations and Figure2 caption | supports | Clinical-isolate analysis associates ftsI/PBP3 variants with cefaclor and other beta-lactam MICs. SNPs are correlated, so individual causal substitutions are not established by this association. The authors identify phenotype/genotype discordance and possible H. haemolyticus/fuzzy-species classification in two isolates. Supplementary isolate MIC table was not extracted. Preserve these limits rather than treating every PBP3 substitution as resistance. |
| transformants | https://doi.org/10.1128/AAC.45.6.1693-1699.2001; PMID11353613/PMC90533; full relevant Methods/Results and Tables1–3 | supports | H. influenzae Rd ATCC51097 cefaclor MIC is1ug/mL; transformants with ftsI DNA from H17, KK01 or ME870 each have16ug/mL in Table3. Selective plates contained5 or10ug/mL cefaclor. This supports a causal ftsI-associated reduction in susceptibility in the stated background, not a universal effect of one mutation. Media contain supplemented Mueller-Hinton and cultures at37C/7%CO2. PBP affinity assays use radiobenzylpenicillin; displayed direct competition panels test ampicillin, cefotaxime and faropenem, not cefaclor. |
| binding-boundary | https://pubmed.ncbi.nlm.nih.gov/6373702/; Complete primary abstract, DOI10.7164/antibiotics.37.389 | context_only | The1984 paper labels cefaclor derivatives using Bolton-Hunter reagent. Their PBP1a/1b affinity is not automatically the unmodified parent cefaclor affinity. The native family-level target remains PRIMARY_EVIDENCE_NEEDED; no derivative affinity or non-cefaclor competition result is promoted as exact parent binding. |

## Limits And Additional Notes

- Direct HMDB requests returned HTTP403. Reaxys, where present, remains source-asserted without an independent public registry comparison. No mapping is removed merely for limited access.
- Focused schema and strict checks passed in batch021; chemistry used the batch019 RDKit interpreter against unchanged batch021 inputs. Shared required corpus gates will be inserted before save.
- No current clinical recommendation, jurisdictional approval or exhaustive resistance/producer survey is claimed. Historical assays do not define current clinical breakpoints.
- DrugBank direct retrieval returned403; LINCS resolver was attempted and its access result is retained in scratch. Current ChEBI preserves both mappings; independent exact registry verification is incomplete.
- 2018 main text was inspected but its supplementary isolate table was not extracted. The2001 full relevant main text and tables were inspected. The1984 modified-probe binding paper was abstract-only. Other adopted studies were inspected at metadata/abstract depth.
- A preliminary guessed ChEMBL908 request was discarded; verified parent CHEMBL680 was obtained from the actual CHEMBL1201018 hierarchy. Initial EPMC query grouping was corrected and all14 intended records resolved.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T105902Z-cefaclor-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review cefaclor exact identity and PBP evidence
started_at: '2026-10-21T10:44:46Z'
finished_at: '2026-10-21T10:59:02Z'
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
summary: The native anhydrous cefaclor graph and antibacterial classification are
  supported. One major exact-xref defect maps the acid to a monohydrate ChEMBL entity.
  The parent CHEMBL680 matches exactly. The imported PBP and H. influenzae target-alteration
  claims remain honestly database-labelled; primary transformation experiments support
  bounded resistance enrichment.
source:
  git_revision: baf3b3203d748d098686e166cdb2a6138f47eb59
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 5e2e1f975f8aa64f92a06c134c98c750c968fd78f02620a73c9cb611ac018ed8
    role: context
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: context
  - path: conf/sources.yaml
    sha256: 4a2dcd7a3a88953b6cb35b51a48ed77b626c3af2cbb542b0d38ba10540ed7df9
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
  - path: curation/curator_antibiotics.tsv
    sha256: 224cbb7261add427184b2762a29c2ff3e85c85e0a06cf22b144545346487247b
    role: context
  - path: curation/decisions.tsv
    sha256: a5834b44307b0449b0df9362c551b7fcd707f3ae51f73d429d37d51f5a169d61
    role: context
  - path: data/antibiotics/antibacterial/cefaclor.yaml
    sha256: 806709a1379c048ed055c8c442d20fe2784b22e245f46aa9054f7104bab1905b
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: 25f0d80c0bf26da7741a1514a5e1759dde484ab054f0f56df7938bdda8383a91
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
  - path: data/raw/chebi_antimicrobials.tsv
    sha256: 4c33e56c3c342be657309f720f5b5cb9cad1fae13bec202ef99e449503c32004
    role: context
  - path: data/raw/chebi_role_names.tsv
    sha256: 5c476c0aacd7c98d7241d2343a6fc41ee9eb9338077404c5b011a04bf40c6ac5
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: docs/CURATION.md
    sha256: a364598a9c2bdaf9e0e71895d5b7a2fd61d3e726e0ed0da12bd895cc4c30e98c
    role: context
  - path: docs/HARMONIZATION.md
    sha256: fb8b58abca016ca5a7d856fcc6f1ec2deb210e0927394a480853830b39e1f060
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
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
- target_id: CHEBI:3478
  path: data/antibiotics/antibacterial/cefaclor.yaml
  label: cefaclor
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
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity and definition
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Cross-source molecular mapping
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Molecular enrichment transform
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Imported target edges
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Imported resistance edges
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Target role adjudication
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: CARD evidence decisions
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position204; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:3478
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:3478
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    204
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:3478
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefaclor.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:3478
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefaclor.yaml --out /private/tmp/am-review-session/204-strict.tsv
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
  - CHEBI:3478
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
  - CHEBI:3478
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
  - CHEBI:3478
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
  - CHEBI:3478
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
  - CHEBI:3478
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
  - CHEBI:3478
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
  - CHEBI:3478
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
  - CHEBI:3478
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
  - CHEBI:3478
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/cefaclor.yaml
  locator: Entire native YAML and source/history blocks
  accessed_at: '2026-10-21T10:52:24Z'
  support: supports
  summary: Entire neutral-parent record read. All native synonyms, chemical encodings,
    roles, parents, exact/drug/document cross-references, source concepts and history
    events were assessed. Native SEEDED status remains unchanged.
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit calculations
  locator: 204-chemistry.json
  accessed_at: '2026-10-21T10:52:24Z'
  support: supports
  summary: Both SMILES and InChI reproduce the native full key, formula, charge, masses
    and configured stereochemistry. Both ARO and ChEBI source mints independently
    match.
  snapshot_sha256: 98285e71a979652ee6efe986fedb332bc59a23618184452ce214a5e76a9edd61
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv;data/raw/aro_antibiotics.tsv
  locator: Exact adopted rows; extractor/seeder; original and expanded inspect captures
  accessed_at: '2026-10-21T10:52:24Z'
  support: supports
  summary: ChEBI supplies the neutral structure and synonyms; ARO supplies class and
    complementary mappings. Actual owners were appended while preserving original
    hashes. The ignored-inclusive curation/conf search found no exact correction for
    these specific findings.
  search_scope: rg --no-ignore --hidden exact identifier and relevant ChEMBL mapping
    across curation/conf; unrelated CHEBI:34785 substring hit discarded.
- evidence_id: adapter
  kind: database
  reference: iModulonDB
  locator: 203-204-adapter-catalog.json;203-204-adapter-pbp.txt;204-adapter-ftsi.txt
  accessed_at: '2026-10-21T10:52:24Z'
  support: supports
  summary: Catalog and gene searches were executed before web follow-up. The catalog
    has no H. influenzae dataset. E. coli/modulome penicillin query returns b2430/yfeW,
    PBP4B; ftsI returns b0084. No iModulon component was returned, so no component
    summary was applicable. These are contextual gene matches, not drug-binding evidence
    or cross-species protein identity.
  snapshot_sha256: 98627808541dbd07b37e85a4bfb692fc0fe8a0a9564839813c9f2f9ac41a4a10
- evidence_id: authorities
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:3478
  locator: 204-ols.json;204-chebi.html;204-aro-stanzas.txt
  accessed_at: '2026-10-21T10:52:24Z'
  support: supports
  summary: Current ChEBI neutral structure matches the native graph. Adopted ARO class
    and compound definitions were read in the separately hashed local ontology cache.
    The broad cephalosporin parents are compatible with the graph. Current registry
    labels are not clinical approval evidence.
  snapshot_sha256: e3814549ab328a25364939c7eb36935e3a0525be8bfdac0b91524da6157dbbdb
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/51039
  locator: 204-pubchem.json
  accessed_at: '2026-10-21T10:52:24Z'
  support: supports
  summary: The current PubChem full stereochemical key and neutral molecular formula
    agree exactly with the native structure.
  snapshot_sha256: ab556846e30fa1f2d3ca42429519ea116aeb0e23c56b9bc25bdbe7ed439159ec
- evidence_id: drugcentral
  kind: database
  reference: https://drugcentral.org/drugcard/525
  locator: 204-drugcentral.html; drug card identity section
  accessed_at: '2026-10-21T10:52:24Z'
  support: supports
  summary: DrugCentral resolves the expected parent name, CAS and formula but also
    lists product/form synonyms. Native drug_xrefs placement permits that drug-level
    context; it does not make every product synonym an exact chemical equivalence.
  snapshot_sha256: 74c01de68a127761f3027f90a672e37f840e296ddd1ecf759622c1aeb704bfd3
- evidence_id: chembl
  kind: database
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL1201018.json
  locator: 204-chembl.json; hierarchy and full molecular structure
  accessed_at: '2026-10-21T10:52:24Z'
  support: refutes
  summary: Native exact xref CHEMBL1201018 has a disconnected water molecule, C15H14ClN3O4S.H2O
    and full key WKJGTOYAEQDNIA-IOOZKYRYSA-N. Its hierarchy explicitly names CHEMBL680
    as parent/active entity. CHEMBL680 has the exact native anhydrous key QYIYFLOTGYLRGG-GPCCPHFNSA-N.
    The mismatch originates in the adopted ARO xref.
  snapshot_sha256: 73b5683efde4908497a1daee24999fc2d896031c81f85affa526ae6280e6024c
- evidence_id: parent
  kind: database
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL680.json
  locator: Current parent molecular graph
  accessed_at: '2026-10-21T10:52:24Z'
  support: supports
  summary: CHEMBL680 independently matches the native complete key and formula. It
    is a candidate exact-xref replacement after maintained source adjudication; the
    native graph should not gain water to accommodate a wrong link.
  snapshot_sha256: 1a45654f19f44ad08a503dddeabec7ff5de73ab2485c484ba8d6f6f445413825
- evidence_id: kegg
  kind: database
  reference: https://rest.kegg.jp/get/C06877
  locator: 204-kegg.txt/.mol;204-keggdrug.txt
  accessed_at: '2026-10-21T10:52:24Z'
  support: supports
  summary: KEGG C06877 MOL independently gives QYIYFLOTGYLRGG-GPCCPHFNSA-N. Drug D00256
    explicitly names cefaclor anhydrous and has the same formula. These placements
    are coherent.
  snapshot_sha256: b19c0647edff34a03bcaa4e1717fc53613a8f048a9aec519922fb8652bd2578b
- evidence_id: documents
  kind: primary_source
  reference: patent:US3925372;patent:DE2408698
  locator: 204-patent-US.html;204-patent-DE.html, document titles/scope
  accessed_at: '2026-10-21T10:52:24Z'
  support: supports
  summary: Both patent identifiers resolve to alpha-aminoacyl-3-halo cephalosporin
    documents. Document placement is appropriate; titles and scope were inspected,
    not every example or claim. Wikipedia is retained only as a document link.
  snapshot_sha256: 8e3dc3e1015b4128ba70a993159a2dcad592482ede8904763dc260c3d64d8609
- evidence_id: adopted
  kind: database
  reference: PMID:10230635;10930630;11963587;12485718;12569987;15812119;18969055;29017833;10435677;29352811;3055170;15673804;11585791;6810737
  locator: 204-core-fixed.json; all14 metadata records and all12 available complete
    abstracts
  accessed_at: '2026-10-21T10:52:24Z'
  support: supports
  summary: 10230635 concerns new derivatives;10930630/12569987 concern IgE recognition;12485718/18969055
    are analytical derivatization methods;29017833 is an allergy review. 11963587
    reports a466-isolate respiratory susceptibility panel (disc/E-test, population
    MIC90);15812119 is a pediatric clinical comparison. 10435677 is the cefaclor review
    cited by ARO. 29352811 is the resistance study inspected in full. Parent PBP/beta-lactamase/cephalosporin
    references are reviews;15673804 and6810737 lack abstracts. Host, derivative and
    population endpoints are not direct target binding.
  snapshot_sha256: 9972e91fecf196aa3d9602e8a467b1d1ef2d8ad1a72fa728898ead86f72b2963
- evidence_id: resistance2018
  kind: primary_source
  reference: https://doi.org/10.1186/s13104-018-3169-0
  locator: PMID29352811/PMC5775570; full main Methods, Results, Discussion, limitations
    and Figure2 caption
  accessed_at: '2026-10-21T10:52:24Z'
  support: supports
  summary: Clinical-isolate analysis associates ftsI/PBP3 variants with cefaclor and
    other beta-lactam MICs. SNPs are correlated, so individual causal substitutions
    are not established by this association. The authors identify phenotype/genotype
    discordance and possible H. haemolyticus/fuzzy-species classification in two isolates.
    Supplementary isolate MIC table was not extracted. Preserve these limits rather
    than treating every PBP3 substitution as resistance.
  snapshot_sha256: d74da6e4fb573e9c9b85f77c6ff2cf8392fc68008b8510e2325c4b3c514fad03
- evidence_id: transformants
  kind: primary_source
  reference: https://doi.org/10.1128/AAC.45.6.1693-1699.2001
  locator: PMID11353613/PMC90533; full relevant Methods/Results and Tables1–3
  accessed_at: '2026-10-21T10:52:24Z'
  support: supports
  summary: H. influenzae Rd ATCC51097 cefaclor MIC is1ug/mL; transformants with ftsI
    DNA from H17, KK01 or ME870 each have16ug/mL in Table3. Selective plates contained5
    or10ug/mL cefaclor. This supports a causal ftsI-associated reduction in susceptibility
    in the stated background, not a universal effect of one mutation. Media contain
    supplemented Mueller-Hinton and cultures at37C/7%CO2. PBP affinity assays use
    radiobenzylpenicillin; displayed direct competition panels test ampicillin, cefotaxime
    and faropenem, not cefaclor.
  snapshot_sha256: 8053f2ee8d1ca7eddd04ec79059d0dc445b7ae15a4a1bcbd0db2b88a182906c3
- evidence_id: binding-boundary
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/6373702/
  locator: Complete primary abstract, DOI10.7164/antibiotics.37.389
  accessed_at: '2026-10-21T10:52:24Z'
  support: context_only
  summary: The1984 paper labels cefaclor derivatives using Bolton-Hunter reagent.
    Their PBP1a/1b affinity is not automatically the unmodified parent cefaclor affinity.
    The native family-level target remains PRIMARY_EVIDENCE_NEEDED; no derivative
    affinity or non-cefaclor competition result is promoted as exact parent binding.
assessments:
- assessment_id: chemistry
  area: identity
  topic: Exact neutral parent
  outcome: supported
  summary: Internal encodings, masses, source mints and current ChEBI/PubChem identity
    agree. No parent structure change is proposed.
  target_ids:
  - CHEBI:3478
  evidence_ids:
  - chemistry
  - authorities
  - pubchem
- assessment_id: provenance
  area: provenance
  topic: Source and history ownership
  outcome: supported
  summary: Both source concepts and four dated seed/reseed events are coherent. Original
    hashes remain intact; no native-only correction is proposed.
  target_ids:
  - CHEBI:3478
  evidence_ids:
  - native
  - owners
  - chemistry
- assessment_id: adapter
  area: scope
  topic: Structured gene context
  outcome: supported
  summary: Required adapter-first lookup completed. Contextual gene search hits do
    not establish target engagement.
  target_ids:
  - CHEBI:3478
  evidence_ids:
  - adapter
- assessment_id: optional
  area: completeness
  topic: Optional blank domains
  outcome: supported
  summary: No blank optional causal graph, producer, activity or clinical field is
    itself a defect. Any enrichment must preserve exact material, taxon, strain and
    assay scope.
  target_ids:
  - CHEBI:3478
  evidence_ids:
  - native
- assessment_id: forms
  area: grounding
  topic: Anhydrous molecule versus hydrate xref
  outcome: concern
  summary: Exact CHEMBL1201018 points to a monohydrate. CHEMBL680, ChEBI, PubChem
    and KEGG match the native anhydrous structure.
  target_ids:
  - CHEBI:3478
  evidence_ids:
  - native
  - chembl
  - parent
  - pubchem
  - kegg
- assessment_id: class
  area: grounding
  topic: Cephalosporin class and antimicrobial drug context
  outcome: supported
  summary: Native chloro/aminophenylacetamido cephalosporin structure and broad antibacterial
    drug filing are supported. All three native configured centres are R; no new stereochemistry
    is imposed.
  target_ids:
  - CHEBI:3478
  evidence_ids:
  - chemistry
  - authorities
  - adopted
  - transformants
- assessment_id: target
  area: evidence
  topic: PBP target assertion
  outcome: supported
  summary: The native database source and PRIMARY_EVIDENCE_NEEDED status honestly
    state their limits. Retrieved derivative-binding and other-antibiotic competition
    data are not direct exact-cefaclor binding evidence.
  target_ids:
  - CHEBI:3478
  evidence_ids:
  - native
  - binding-boundary
  - transformants
- assessment_id: resistance
  area: evidence
  topic: H. influenzae PBP3 alteration
  outcome: supported
  summary: The imported target-alteration assertion has contextual primary association
    and transformation support. Do not convert linked SNP association into proof of
    one substitution or transfer E. coli adapter IDs to H. influenzae.
  target_ids:
  - CHEBI:3478
  evidence_ids:
  - resistance2018
  - transformants
  - adapter
- assessment_id: documents
  area: provenance
  topic: Drug, document and remaining source links
  outcome: supported
  summary: KEGG and DrugCentral placements are coherent; patents resolve as broader
    documents. HMDB/DrugBank/LINCS/Reaxys independent access limits remain explicit.
  target_ids:
  - CHEBI:3478
  evidence_ids:
  - drugcentral
  - kegg
  - documents
  - authorities
findings:
- finding_id: F1
  issue_key: cefaclor-chembl-hydrate-exact-xref
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Replace or withhold the hydrate ChEMBL exact xref
  description: CHEMBL1201018 denotes cefaclor monohydrate with an explicit additional
    water fragment and a different full key. The native exact record denotes anhydrous
    cefaclor. CHEMBL680 is the explicitly linked parent and matches the native graph.
    This is a chemical-form mismatch, not a stereochemical correction to cefaclor.
  target_ids:
  - CHEBI:3478
  field_paths:
  - xrefs
  - chemical_structure
  evidence_ids:
  - native
  - chembl
  - parent
  - owners
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted hydrate ChEMBL mapping
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Exact xref normalization and gate
  rule_id: 'docs/CURATION.md: exact xrefs denote the same structure'
  native_severity: major exact chemical-form mismatch
  normalization_reason: The asserted exact accession has a different composition and
    full key, while the independently corroborated native structure is coherent.
actions:
- action_id: A1
  description: Adjudicate the hydrate mapping in the maintained ARO/xref extraction
    path.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:3478
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted hydrate ChEMBL mapping
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Exact xref normalization and gate
  acceptance_checks:
  - Withhold CHEMBL1201018 as an exact xref or explicitly qualify a supported hydrate
    relation. Consider CHEMBL680 as the exact replacement using the verified complete
    key.
  - Retain ARO provenance and reproduce the correction through extraction/seeding;
    do not add water to the native acid to fit the wrong accession.
  - Run focused schema/strict, identity and duplicate/xref gates, source provenance
    and full corpus reproduction after curation.
- action_id: A2
  description: Optionally add bounded primary ftsI resistance evidence and retain
    target evidence limits.
  finding_ids: []
  target_ids:
  - CHEBI:3478
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefaclor.yaml
    role: Curator-owned evidence via validated writer
  acceptance_checks:
  - Preserve recipient Rd ATCC51097, donor ftsI source, MIC1to16ug/mL, medium and
    selection context. Keep clinical-isolate associations distinct from transformation
    evidence.
  - Do not infer unmodified cefaclor PBP affinity from Bolton-Hunter derivatives or
    from ampicillin/cefotaxime/faropenem competition panels.
  - If extracting2018 MICs, inspect its supplementary table and resolve isolate/species
    qualifiers before assigning taxon-level resistance observations.
limitations:
- Direct HMDB requests returned HTTP403. Reaxys, where present, remains source-asserted
  without an independent public registry comparison. No mapping is removed merely
  for limited access.
- Focused schema and strict checks passed in batch021; chemistry used the batch019
  RDKit interpreter against unchanged batch021 inputs. Shared required corpus gates
  will be inserted before save.
- No current clinical recommendation, jurisdictional approval or exhaustive resistance/producer
  survey is claimed. Historical assays do not define current clinical breakpoints.
- DrugBank direct retrieval returned403; LINCS resolver was attempted and its access
  result is retained in scratch. Current ChEBI preserves both mappings; independent
  exact registry verification is incomplete.
- 2018 main text was inspected but its supplementary isolate table was not extracted.
  The2001 full relevant main text and tables were inspected. The1984 modified-probe
  binding paper was abstract-only. Other adopted studies were inspected at metadata/abstract
  depth.
- A preliminary guessed ChEMBL908 request was discarded; verified parent CHEMBL680
  was obtained from the actual CHEMBL1201018 hierarchy. Initial EPMC query grouping
  was corrected and all14 intended records resolved.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
