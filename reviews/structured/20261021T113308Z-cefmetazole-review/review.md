# Cefmetazole: coherent free acid with sodium-form PBP experiments and unresolved CfxA substrate scope

- Review: 20261021T113308Z-cefmetazole-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T11:08:31Z
- Finished UTC: 2026-10-21T11:33:08Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native cefmetazole graph, systematic names and checked chemical identifiers agree. Original CS-1170 experiments directly support PBP binding and cell-wall enzyme inhibition at the active-moiety level, but depict the sodium salt. The retained CfxA entry is accurately labeled as a database assertion; the inspected original CfxA paper tests cefoxitin rather than cefmetazole. No confirmed required native correction was demonstrated. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position 227; one exact record in path order, captured before judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:3489 | data/antibiotics/antibacterial/cefmetazole.yaml | generated | cefmetazole |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:3489 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:3489 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:3489 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:3489 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:3489 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:3489 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:3489 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:3489 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:3489 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:3489 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:3489 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:3489 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Maintained sources and history

provenance: supported. Targets: CHEBI:3489.

Source concepts, source-owned assertions and seeding history are coherent. New primary observations require the native validated writer and curation event; source corrections must be reproducible.

### Focused native checks

schema: supported. Targets: CHEBI:3489.

Documented schema and strict validation passed; independent chemistry also passed. Deterministic checks do not establish scientific completeness or native REVIEWED status.

### Exact acid and contextual forms

identity: supported. Targets: CHEBI:3489.

The exact neutral structure and systematic names agree across inspected sources. The original sodium reagent is distinguished from the native acid.

### PBP binding and cell-wall endpoints

evidence: supported. Targets: CHEBI:3489.

The broad native target is honestly database-qualified; original sodium-form binding and enzyme experiments can support bounded primary enrichment. Morphological and synergy inferences must remain separate from direct binding.

### CfxA exact-substrate support

evidence: unknown. Targets: CHEBI:3489.

The database assertion is reproduced, but the inspected founding CfxA paper establishes cefoxitin experiments and does not resolve exact cefmetazole substrate support.

### Antibacterial role and population/material limits

scope: supported. Targets: CHEBI:3489.

Primary experiments support the antibacterial active moiety. Clinical, animal and nanomaterial-combination observations have distinct scopes.

### Optional primary enrichment

completeness: unknown. Targets: CHEBI:3489.

No natural producer, exact free-acid MIC observation or complete downstream causal graph was established for adoption. Empty optional fields alone are not defects.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/cefmetazole.yaml; Complete native YAML, all source concepts and every history event. | supports | The complete exact record and all populated assertions were inspected. This observation does not modify the generated record or promote SEEDED status. |
| owners | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; scripts/seed_from_sources.py; 227-raw-rows.json and actual maintained owner files. | supports | ChEBI supplies identity, names, definition and its document/citation leads; ARO supplies the joined classification and its assertions. Initial hashes are preserved, with actual additional owner inputs appended before detailed judgment. Any correction must survive reseeding. |
| search | 227-local-hits.txt; 227-owner-hits.txt; Exact identifier, label, full key and slug; maintained inputs and related forms. | supports | The ignored-inclusive search distinguished the exact record from related compounds and source references. No exact corrective overlay was identified in the inspected maintained inputs. |
| chemistry | 227-chemistry.json; 227-230-external-chemistry.json; Native SMILES/InChI and independently parsed official PubChem, ChEMBL, KEGG and DrugCentral structures. | supports | Native encodings agree with SNBUBQHDYVFSQF-HIFRSBDPSA-N, C15H17N7O5S3, charge 0 and the retained masses. All inspected independent structure representations agree with the specified stereochemistry. Calculations used the existing batch019 RDKit interpreter against unchanged batch023 inputs. |
| identity | CHEBI:3489; PubChem:42008; CHEMBL1201195; KEGG:C08103; KEGG:D00910; drugcentral:539; Current ChEBI/OLS, PubChem CAS resolution, ChEMBL and official raw KEGG/DrugCentral structures. | supports | All checked graphs specify neutral (6R,7S) cefmetazole, with the cyanomethylthioacetamido, 7-alpha-methoxy and N-methyltetrazolylthiomethyl groups. CAS 56796-20-4 resolves to the matching PubChem entry. The cephalosporin parents and antimicrobial/antibacterial roles fit the graph and activity evidence. Beilstein 5406306 and LINCS LSM-5594 remain source-attested; the LINCS public route supplied no inspectable content. DrugBank and Wikipedia returned access failures. |
| pbp | PMID:365089; DOI:10.1128/AAC.14.5.780; PMC352550; All original pp780–785; Figure 1 and Tables 1–2 visually inspected. | supports | CS-1170 is drawn with COONa and the matching cefmetazole moiety. E. coli K-12 JE1011, P. mirabilis ATCC15290 and P. morganii IFO3045 membrane preparations were tested. E. coli competition with 14C-penicillin G gives Table 1 molar ratios for 50% inhibition: PBP1A/1Bs 0.4/0.4, PBP3 0.7 and PBP2 &gt;125; these are relative competition values, not micromolar Kd. Direct 14C-CS-1170 binding corroborates the pattern. Table 2 reports cell-free cross-linking inhibition at 0.4 micrograms/mL and D-alanine carboxypeptidase IA/IB inhibition at 0.06/0.004 micrograms/mL. Membrane/enzyme preparation details refer partly to earlier methods. The sodium material must not become an exact free-acid assay without qualification. |
| cfxa | PMID:8517690; DOI:10.1128/AAC.37.5.1028; PMC187887; Original pp1028–1032 and 1035: methods, Tables 1–3, relevant results and discussion; not an exhaustive sequence-alignment reanalysis. | supports | The B. vulgatus CLA341 determinant was cloned into B. fragilis backgrounds; insertional inactivation reduced the cefoxitin phenotype. Table 1 on p1030 measures cefoxitin/ampicillin MIC and cefoxitin degradation. Table 2 on p1031 lists cephaloridine, cephalothin, penicillin G, ampicillin, cefotaxime, cefoxitin and nitrocefin, with inhibitors separately. The inspected experimental sections do not test cefmetazole. Cefoxitin bioassay/HPLC degradation despite below-detection spectrophotometry is not cefmetazole-specific hydrolysis evidence. This limits primary support without proving the native database assertion false. |
| aro | ARO:3004001; ARO:3003001; ARO:3000749; Exact adopted antibiotic, resistance and target rows plus corresponding ARO stanzas. | supports | The native CfxA resistance edge and generic PBP target reproduce the database provenance. PRIMARY_EVIDENCE_NEEDED and unspecified organism/assay are retained honestly. The ARO cache was read from the original checkout without alteration; its recorded SHA-256 is d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4. |
| activity | PMID:8452349; PMID:23140947; PMID:23705013; Complete adopted abstracts and metadata. | supports | 8452349 compares cefmetazole and cefazolin in rabbit S. aureus abscesses and in vitro inoculum contexts; 23140947 is a small retrospective pyelonephritis comparison, not randomized efficacy proof. 23705013 evaluates nanomaterial enhancement against N. gonorrhoeae; its combination effects must not be assigned to cefmetazole alone. Full original methods were not independently recovered for these three papers. |
| remaining-leads | PMID:10109799; PMID:2416589; PMID:2692950; PMID:29017833; PMID:3055170; PMID:11585791; PMID:15673804; PMID:6810737; DOI:10.1007/BF03298293; All remaining adopted/target/parent MED metadata and available abstracts; Crossref metadata for the distinct DOI-only source. | supports | 10109799 is cost modeling; 2416589 concerns mouse IgG1/IgE; 2692950 is a cefmetazole overview and 29017833 an allergy review. PBP and ESBL reviews supply class context; 15673804 and 6810737 have metadata only. DOI 10.1007/BF03298293 resolves to the 1979 item Cefmetazole: A Second Cephamycin and is distinct from the 1989 PMID2692950 review. Its full text was not inspected. |
| adapter | 227-230-adapter-datasets.json; 227-230-adapter-cfxA.json; 227-230-adapter-pbp.json; Structured iModulonDB catalog and matching E. coli searches before open-ended mechanism research. | supports | kg-microbe-sources imodulondb --timeout 15 datasets and search --organism e_coli --dataset modulome --query cfxA / --query penicillin all exited 0. The catalog has no Bacteroides dataset. cfxA returned no genes or modules; penicillin returned yfeW/b2430 (PBP4B) and no modules. These are annotation/search outcomes, not direct binding, resistance or negative biological evidence. |

## Limits And Additional Notes

- Required shared corpus results must be incorporated before final save. Focused success alone does not establish whole-corpus quality.
- No paid source was used. Inaccessible independent registry or article contents remain explicit limits, not evidence of nonexistence.
- Eleven adopted/target/parent MED records were dispositioned; nine indexed abstracts were available and two parent reviews have metadata only. The distinct DOI-only 1979 review was verified at metadata level.
- The 1978 PBP article was read in full; prior referenced preparation protocols were not separately audited. Its drawn sodium salt and relative competition units must be preserved.
- The 1993 CfxA methods, experimental tables and relevant discussion were inspected; sequence alignment pages and every cited follow-up were not exhaustively reanalyzed. Exact cefmetazole primary causal support remains unresolved. A future curator should obtain substrate-specific data before promoting this edge to primary evidence.
- Beilstein, LINCS, DrugBank and Wikipedia independent contents remain unverified. No such access limit is asserted as a broken or wrong identifier.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T113308Z-cefmetazole-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cefmetazole: coherent free acid with sodium-form PBP experiments and unresolved
  CfxA substrate scope'
started_at: '2026-10-21T11:08:31Z'
finished_at: '2026-10-21T11:33:08Z'
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
verdict: blocked
scientific_review: true
summary: The native cefmetazole graph, systematic names and checked chemical identifiers
  agree. Original CS-1170 experiments directly support PBP binding and cell-wall enzyme
  inhibition at the active-moiety level, but depict the sodium salt. The retained
  CfxA entry is accurately labeled as a database assertion; the inspected original
  CfxA paper tests cefoxitin rather than cefmetazole. No confirmed required native
  correction was demonstrated. Scientific assessment retains the stated evidence limits;
  full verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/cefmetazole.yaml
    sha256: ab836462b6fbf26d8f77941ee996d12dff92a3833389b20107a772b073b2ea2c
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
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: context
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: context
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
  - path: scripts/card_evidence_reviews.py
    sha256: f9ec8aff30066bf04b9c2757af7d6f5d179d045e57b9f3b352bbed0b851f50a8
    role: context
targets:
- target_id: CHEBI:3489
  path: data/antibiotics/antibacterial/cefmetazole.yaml
  label: cefmetazole
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
    role: Adopted ARO identity and reference leads
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Adopted PBP target edge
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Target role mapping
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Adopted resistance edge
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Imported-claim adjudication searched
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Claim-review merge implementation
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position 227; one exact record in path order,
    captured before judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:3489
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:3489
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    227
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:3489
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefmetazole.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:3489
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefmetazole.yaml --out /private/tmp/am-review-session/227-strict.tsv
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
  - CHEBI:3489
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
  - CHEBI:3489
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
  - CHEBI:3489
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
  - CHEBI:3489
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
  - CHEBI:3489
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
  - CHEBI:3489
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
  - CHEBI:3489
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
  - CHEBI:3489
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
  - CHEBI:3489
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/cefmetazole.yaml
  locator: Complete native YAML, all source concepts and every history event.
  accessed_at: '2026-10-21T11:32:57Z'
  support: supports
  summary: The complete exact record and all populated assertions were inspected.
    This observation does not modify the generated record or promote SEEDED status.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; scripts/seed_from_sources.py
  locator: 227-raw-rows.json and actual maintained owner files.
  accessed_at: '2026-10-21T11:32:57Z'
  support: supports
  summary: ChEBI supplies identity, names, definition and its document/citation leads;
    ARO supplies the joined classification and its assertions. Initial hashes are
    preserved, with actual additional owner inputs appended before detailed judgment.
    Any correction must survive reseeding.
  snapshot_sha256: b7cd597e7f4ec2415e6470a9eb3356887eb6ab9046100ae0956e57390fee8011
- evidence_id: search
  kind: search
  reference: 227-local-hits.txt; 227-owner-hits.txt
  locator: Exact identifier, label, full key and slug; maintained inputs and related
    forms.
  accessed_at: '2026-10-21T11:32:57Z'
  support: supports
  summary: The ignored-inclusive search distinguished the exact record from related
    compounds and source references. No exact corrective overlay was identified in
    the inspected maintained inputs.
  search_scope: rg --no-ignore --hidden across the isolated worktree, excluding .git
    and .venv internals; exact identifiers, label, key and slug.
  snapshot_sha256: 2ff0a6edfaef5b726c1782d72676294cdb33eb5aec042576a7c671014eb53563
- evidence_id: chemistry
  kind: validation
  reference: 227-chemistry.json; 227-230-external-chemistry.json
  locator: Native SMILES/InChI and independently parsed official PubChem, ChEMBL,
    KEGG and DrugCentral structures.
  accessed_at: '2026-10-21T11:32:57Z'
  support: supports
  summary: Native encodings agree with SNBUBQHDYVFSQF-HIFRSBDPSA-N, C15H17N7O5S3,
    charge 0 and the retained masses. All inspected independent structure representations
    agree with the specified stereochemistry. Calculations used the existing batch019
    RDKit interpreter against unchanged batch023 inputs.
  snapshot_sha256: 7ba36332f8e33091739e45acaad31ef5ed53e4ce633ff69a1eb9a4c3e40393fc
- evidence_id: identity
  kind: database
  reference: CHEBI:3489; PubChem:42008; CHEMBL1201195; KEGG:C08103; KEGG:D00910; drugcentral:539
  locator: Current ChEBI/OLS, PubChem CAS resolution, ChEMBL and official raw KEGG/DrugCentral
    structures.
  accessed_at: '2026-10-21T11:32:57Z'
  support: supports
  summary: All checked graphs specify neutral (6R,7S) cefmetazole, with the cyanomethylthioacetamido,
    7-alpha-methoxy and N-methyltetrazolylthiomethyl groups. CAS 56796-20-4 resolves
    to the matching PubChem entry. The cephalosporin parents and antimicrobial/antibacterial
    roles fit the graph and activity evidence. Beilstein 5406306 and LINCS LSM-5594
    remain source-attested; the LINCS public route supplied no inspectable content.
    DrugBank and Wikipedia returned access failures.
  snapshot_sha256: e49508094f3d294deb5c365929478b08ce4a485f9e7c6aec7dd2a5f0e4ae3a92
- evidence_id: pbp
  kind: primary_source
  reference: PMID:365089; DOI:10.1128/AAC.14.5.780; PMC352550
  locator: All original pp780–785; Figure 1 and Tables 1–2 visually inspected.
  accessed_at: '2026-10-21T11:32:57Z'
  support: supports
  summary: 'CS-1170 is drawn with COONa and the matching cefmetazole moiety. E. coli
    K-12 JE1011, P. mirabilis ATCC15290 and P. morganii IFO3045 membrane preparations
    were tested. E. coli competition with 14C-penicillin G gives Table 1 molar ratios
    for 50% inhibition: PBP1A/1Bs 0.4/0.4, PBP3 0.7 and PBP2 >125; these are relative
    competition values, not micromolar Kd. Direct 14C-CS-1170 binding corroborates
    the pattern. Table 2 reports cell-free cross-linking inhibition at 0.4 micrograms/mL
    and D-alanine carboxypeptidase IA/IB inhibition at 0.06/0.004 micrograms/mL. Membrane/enzyme
    preparation details refer partly to earlier methods. The sodium material must
    not become an exact free-acid assay without qualification.'
  snapshot_sha256: 476fcfa7fdb499c2bf57388fc03d95d3e72d2ca4ccc267ecb89a6cdb5ae3c4a9
- evidence_id: cfxa
  kind: primary_source
  reference: PMID:8517690; DOI:10.1128/AAC.37.5.1028; PMC187887
  locator: 'Original pp1028–1032 and 1035: methods, Tables 1–3, relevant results and
    discussion; not an exhaustive sequence-alignment reanalysis.'
  accessed_at: '2026-10-21T11:32:57Z'
  support: supports
  summary: The B. vulgatus CLA341 determinant was cloned into B. fragilis backgrounds;
    insertional inactivation reduced the cefoxitin phenotype. Table 1 on p1030 measures
    cefoxitin/ampicillin MIC and cefoxitin degradation. Table 2 on p1031 lists cephaloridine,
    cephalothin, penicillin G, ampicillin, cefotaxime, cefoxitin and nitrocefin, with
    inhibitors separately. The inspected experimental sections do not test cefmetazole.
    Cefoxitin bioassay/HPLC degradation despite below-detection spectrophotometry
    is not cefmetazole-specific hydrolysis evidence. This limits primary support without
    proving the native database assertion false.
  snapshot_sha256: 2d18f3088dd0c19303d7b9b57b860cb11c7c45c270d1bc0248c27b70cc7c866a
- evidence_id: aro
  kind: database
  reference: ARO:3004001; ARO:3003001; ARO:3000749
  locator: Exact adopted antibiotic, resistance and target rows plus corresponding
    ARO stanzas.
  accessed_at: '2026-10-21T11:32:57Z'
  support: supports
  summary: The native CfxA resistance edge and generic PBP target reproduce the database
    provenance. PRIMARY_EVIDENCE_NEEDED and unspecified organism/assay are retained
    honestly. The ARO cache was read from the original checkout without alteration;
    its recorded SHA-256 is d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4.
  snapshot_sha256: bbbcc33eb608006041cdd761367990534c07a7e257cf659884c06f2451bace51
- evidence_id: activity
  kind: primary_source
  reference: PMID:8452349; PMID:23140947; PMID:23705013
  locator: Complete adopted abstracts and metadata.
  accessed_at: '2026-10-21T11:32:57Z'
  support: supports
  summary: 8452349 compares cefmetazole and cefazolin in rabbit S. aureus abscesses
    and in vitro inoculum contexts; 23140947 is a small retrospective pyelonephritis
    comparison, not randomized efficacy proof. 23705013 evaluates nanomaterial enhancement
    against N. gonorrhoeae; its combination effects must not be assigned to cefmetazole
    alone. Full original methods were not independently recovered for these three
    papers.
  snapshot_sha256: 88691f0e68e7adf425e8895047cf06f97604597ed24a4e9f6120e03cae7be320
- evidence_id: remaining-leads
  kind: database
  reference: PMID:10109799; PMID:2416589; PMID:2692950; PMID:29017833; PMID:3055170;
    PMID:11585791; PMID:15673804; PMID:6810737; DOI:10.1007/BF03298293
  locator: All remaining adopted/target/parent MED metadata and available abstracts;
    Crossref metadata for the distinct DOI-only source.
  accessed_at: '2026-10-21T11:32:57Z'
  support: supports
  summary: '10109799 is cost modeling; 2416589 concerns mouse IgG1/IgE; 2692950 is
    a cefmetazole overview and 29017833 an allergy review. PBP and ESBL reviews supply
    class context; 15673804 and 6810737 have metadata only. DOI 10.1007/BF03298293
    resolves to the 1979 item Cefmetazole: A Second Cephamycin and is distinct from
    the 1989 PMID2692950 review. Its full text was not inspected.'
  snapshot_sha256: 7734497b6b574bb792298b9de69a280e2d3bb15e84dd0a980e39b3a147bf68dc
- evidence_id: adapter
  kind: database
  reference: 227-230-adapter-datasets.json; 227-230-adapter-cfxA.json; 227-230-adapter-pbp.json
  locator: Structured iModulonDB catalog and matching E. coli searches before open-ended
    mechanism research.
  accessed_at: '2026-10-21T11:32:57Z'
  support: supports
  summary: kg-microbe-sources imodulondb --timeout 15 datasets and search --organism
    e_coli --dataset modulome --query cfxA / --query penicillin all exited 0. The
    catalog has no Bacteroides dataset. cfxA returned no genes or modules; penicillin
    returned yfeW/b2430 (PBP4B) and no modules. These are annotation/search outcomes,
    not direct binding, resistance or negative biological evidence.
  snapshot_sha256: 98627808541dbd07b37e85a4bfb692fc0fe8a0a9564839813c9f2f9ac41a4a10
assessments:
- assessment_id: provenance
  area: provenance
  topic: Maintained sources and history
  outcome: supported
  summary: Source concepts, source-owned assertions and seeding history are coherent.
    New primary observations require the native validated writer and curation event;
    source corrections must be reproducible.
  target_ids:
  - CHEBI:3489
  evidence_ids:
  - record
  - owners
  - search
- assessment_id: validation
  area: schema
  topic: Focused native checks
  outcome: supported
  summary: Documented schema and strict validation passed; independent chemistry also
    passed. Deterministic checks do not establish scientific completeness or native
    REVIEWED status.
  target_ids:
  - CHEBI:3489
  evidence_ids:
  - chemistry
- assessment_id: identity
  area: identity
  topic: Exact acid and contextual forms
  outcome: supported
  summary: The exact neutral structure and systematic names agree across inspected
    sources. The original sodium reagent is distinguished from the native acid.
  target_ids:
  - CHEBI:3489
  evidence_ids:
  - identity
  - chemistry
  - pbp
- assessment_id: target
  area: evidence
  topic: PBP binding and cell-wall endpoints
  outcome: supported
  summary: The broad native target is honestly database-qualified; original sodium-form
    binding and enzyme experiments can support bounded primary enrichment. Morphological
    and synergy inferences must remain separate from direct binding.
  target_ids:
  - CHEBI:3489
  evidence_ids:
  - record
  - pbp
  - aro
  - adapter
- assessment_id: resistance
  area: evidence
  topic: CfxA exact-substrate support
  outcome: unknown
  summary: The database assertion is reproduced, but the inspected founding CfxA paper
    establishes cefoxitin experiments and does not resolve exact cefmetazole substrate
    support.
  target_ids:
  - CHEBI:3489
  evidence_ids:
  - cfxa
  - aro
- assessment_id: activity
  area: scope
  topic: Antibacterial role and population/material limits
  outcome: supported
  summary: Primary experiments support the antibacterial active moiety. Clinical,
    animal and nanomaterial-combination observations have distinct scopes.
  target_ids:
  - CHEBI:3489
  evidence_ids:
  - pbp
  - activity
  - remaining-leads
- assessment_id: completeness
  area: completeness
  topic: Optional primary enrichment
  outcome: unknown
  summary: No natural producer, exact free-acid MIC observation or complete downstream
    causal graph was established for adoption. Empty optional fields alone are not
    defects.
  target_ids:
  - CHEBI:3489
  evidence_ids:
  - record
  - pbp
  - activity
findings: []
actions: []
limitations:
- Required shared corpus results must be incorporated before final save. Focused success
  alone does not establish whole-corpus quality.
- No paid source was used. Inaccessible independent registry or article contents remain
  explicit limits, not evidence of nonexistence.
- Eleven adopted/target/parent MED records were dispositioned; nine indexed abstracts
  were available and two parent reviews have metadata only. The distinct DOI-only
  1979 review was verified at metadata level.
- The 1978 PBP article was read in full; prior referenced preparation protocols were
  not separately audited. Its drawn sodium salt and relative competition units must
  be preserved.
- The 1993 CfxA methods, experimental tables and relevant discussion were inspected;
  sequence alignment pages and every cited follow-up were not exhaustively reanalyzed.
  Exact cefmetazole primary causal support remains unresolved. A future curator should
  obtain substrate-specific data before promoting this edge to primary evidence.
- Beilstein, LINCS, DrugBank and Wikipedia independent contents remain unverified.
  No such access limit is asserted as a broken or wrong identifier.
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
