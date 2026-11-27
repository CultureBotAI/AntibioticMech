# Review of carbomycin

- Review: 20261021T105307Z-carbomycin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:32:40Z
- Finished UTC: 2026-10-21T10:53:07Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native structure is internally coherent and agrees with current PubChem5287879, CCD CAI and CHEMBL1231649 carbomycin A. Published chembl:CHEMBL3989435 instead differs at one epoxide stereocenter and violates the same-structure xref contract. Antibacterial activity and macrolide class are supported. All five resistance items honestly retain CARD provenance; historical hypotheses and induction assays must not be promoted to direct CarA transport or carbomycin-specific ribosome-protection measurements.

## Scope And Provenance

Entire exact MINTED/SEEDED record, three history events, all five resistance objects, actual ARO/PubChem source rows and seeder ownership; all 16 adopted compound, determinant and parent PMID leads; selected original structure, production and resistance studies.

Selection: Queue198; root original13 captured inputs retained, six actual ARO/PubChem/evidence owner inputs appended before detailed inspection.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-27630f7c54 | data/antibiotics/antibacterial/carbomycin.yaml | generated | carbomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema check | passed | True | antibioticmech:aro-27630f7c54 | Exit0. |
| Documented strict check | passed | True | antibioticmech:aro-27630f7c54 | Exit0, zeroERRORrows. |
| Supplemental graph comparison | passed | False | antibioticmech:aro-27630f7c54 | Exit0: internal graph consistency verified and external mismatch explicitly detected; this is not a clean-xref assertion. |
| Structured source applicability | passed | False | antibioticmech:aro-27630f7c54 | Catalog inspected before resistance-protein web follow-up; none of the four source species is covered. |
| Authoritative full QC | failed | True | antibioticmech:aro-27630f7c54 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-27630f7c54 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-27630f7c54 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-27630f7c54 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-27630f7c54 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-27630f7c54 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-27630f7c54 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-27630f7c54 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-27630f7c54 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Stored exact carbomycin A graph

identity: supported. Targets: antibioticmech:aro-27630f7c54.

Internal graph and currentPubChem/exactChEMBL/CCD agree; no derivative or salt is substituted.

### Exact ChEMBL mapping

grounding: concern. Targets: antibioticmech:aro-27630f7c54.

CHEMBL3989435 conflicts at one configured epoxide center; CHEMBL1231649 is a verified exact candidate.

### Antibacterial macrolide classification

grounding: supported. Targets: antibioticmech:aro-27630f7c54.

Native sixteen-member lactone and original carbomycin A microbial studies support the filing.

### Producer definition citation

evidence: unknown. Targets: antibioticmech:aro-27630f7c54.

Producer context is independently corroborated, but the full 1952 cited paper was unavailable.

### Five CARD resistance entries

evidence: supported. Targets: antibioticmech:aro-27630f7c54.

All reproduce honest imported evidence; primary abstracts and later family experiments provide bounded support without reclassifying historical export speculation as proof.

### Optional primary ribosome evidence

completeness: supported. Targets: antibioticmech:aro-27630f7c54.

A bounded archaeal binding study is available for future enrichment; absence of a native target is not a demonstrated required-field defect.

### References and history

provenance: supported. Targets: antibioticmech:aro-27630f7c54.

All16 adopted/parent PMID records resolve at stated depths; three history events and actual owner paths were inspected.

### Focused checks

schema: supported. Targets: antibioticmech:aro-27630f7c54.

Schema/strict pass; supplemental chemistry explicitly detects external stereochemical mismatch.

## Findings

### F1: The published ChEMBL exact xref identifies a different epoxide stereoisomer

major / open / confirmed; issue key: aro-27630f7c54-chembl-epoxide-stereoisomer-xref.

chembl:CHEMBL3989435 currently resolves to FQVHOULQCKDUCY-PRPXPMGXSA-N while the native graph and PubChem5287879 are FQVHOULQCKDUCY-OGHXVOSASA-N. Graph mapping identifies a single S-to-R epoxide change(native atom13, ChEMBL atom46, zero-based). Equal formula and connectivity do not satisfy exact structural identity. Preserve the supported native carbomycin A graph; withhold the conflicting exact xref and consider the independently verified CHEMBL1231649 mapping through a reproducible source correction.

## Recommended Actions And Acceptance Checks

### A1

Repair the ChEMBL cross-reference reproducibly while retaining source provenance and the supported native structure.

- Preserve the imported ARO mapping as source history; make a maintained extraction/seeder correction or structure-aware xref gate with explicit provenance. Do not silently edit only the generated YAML or pretend the current ChEBI-only gate already handles ChEMBL.
- Ensure chembl:CHEMBL3989435 is no longer emitted as an exact xref to this graph. If adopting chembl:CHEMBL1231649, verify neutral formula, connectivity, all 17 centers, double-bond geometry and full key against the native graph; retain the native structure unless separately justified evidence changes it.
- Regenerate using the source workflow; confirm the correction survives reseeding and the source row remains traceable. Run focused schema/strict plus required source/reference/history and full-corpus gates; an explicit remote/local graph regression must detect the mapped epoxide mismatch.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/carbomycin.yaml; Entire YAML, all five resistance objects and three history events | supports | The record is MINTED/SEEDED, stores one neutral epoxyenone macrolide graph and three exact xrefs. Five resistance entries explicitly cite database assertions rather than primary evidence. No native MIC, molecular target, mechanism graph or curated producer object is asserted. |
| chemistry | PubChem:5287879;CHEMBL3989435;CHEMBL1231649;CCD:CAI; 198-chemistry.py/.json;198-pubchem.json;198-chembl.json;198-chembl-exact.json;198-cai.json | supports | Native SMILES/InChI/key, neutral C42H67NO16, masses and 17 configured centers agree internally. Current PubChem5287879, CCD CAI and CHEMBL1231649 share FQVHOULQCKDUCY-OGHXVOSASA-N. CHEMBL3989435 has FQVHOULQCKDUCY-PRPXPMGXSA-N. Whole-graph mapping isolates one epoxide difference: native SMILES atom13(S) maps to ChEMBL atom46(R), zero-based; native InChI t30+ versus t30-. Formula/connectivity agreement alone cannot validate this exact xref. |
| chembl-conflict | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL3989435.json; Current complete structure API response198-chembl.json | refutes | The published ChEMBL accession resolves to a configured stereoisomer differing from the stored graph. Exact-key API search returns CHEMBL1231649 labelled CARBOMYCIN A; the separate detail response confirms full-key and SMILES agreement. This establishes the bounded xref conflict without requiring the native graph to be replaced. |
| source-conflict | ARO:3001228; 198-aro-stanzas.txt;198-aro_antibiotics.json;198-card.html | partial | Adopted ARO and currentCARD link both the conflicting ChEMBL accession and PubChem5287879. CurrentCARD displays the ChEMBL SMILES. This is a source-level discrepancy propagated by the seeder, not an isolated manual YAML edit. Generic carbomycin remains the imported label; exact native graph is carbomycin A. |
| production | https://doi.org/10.7164/antibiotics.37.118; 198-halstedii.pdf complete main text;Methods p119,Table2 p122,Fig3 p123 independently viewed | supports | The1984 study states that carbomycin A(deltamycin A4) was produced by fermentation of S.halstedii subsp.deltae FERM-P2504 and purified in the authors laboratory. Original substrate formula C42H67NO16 and epoxyenone constitution agree with the native compound; derivatives P1/P2/P3 are separate structures. Deepoxidation assays on other microbes do not make those organisms natural producers. This source supports producer context but its schematic alone does not independently rederive all absolute stereocenters. |
| definition | PMID:24542077;PMID:3036668; 198-core.json;original1952 metadata and complete1987 abstract | partial | The adopted1952 source resolves as Some properties of magnamycin; a new antibiotic, with no indexed abstract. Its exact two-species claim could not be checked from the original text. The1987 cloning abstract independently describes S.thermotolerans as a carbomycin producer; the 1984 fermentation source supports the S.halstedii side. Do not claim that the unavailable1952 paper was inspected or proves both species. |
| erm-resistance | PMID:10517588;3020383;2753855;3036668;1691981;9055987; Complete abstracts198-core.json and198-carb-core.json;PMC163745/PMC210198 HTML abstract/archive pages | partial | SrmA introduces one A2058 methyl group in S.ambofaciens with an MLS-I phenotype, though the retrieved abstract does not name carbomycin. tlrA expression confers carbomycin resistance in S.griseofuscus; independent work shows A2058 dimethylation. carA/carB cloning confers carbomycin resistance; additional1990carB work demonstrates A2058 monomethylation with different whole-cell and isolated-ribosome resistance magnitudes. ErmSV1997 specifically tests translational attenuator-lac induction by carbomycin, not a carbomycin methylation rate or MIC. These support bounded mechanisms without converting every imported edge to primary evidence. |
| cara-history | PMID:1612454;PMID:27006457; 198-core.json complete1992abstract;198-abcf.xml full mainMethods/Results | context_only | The1992 CarA/TlrC/SrmB paper proposes ATP-driven export from sequence similarity, not a direct transport measurement. The2016 ABC-F study directly tests Vga(A)/Lsa(A) protection and lincomycin displacement; it does not directly test CarA. Its S.aureus RN4220 carbomycin A susceptibility comparison shows fourfold reduced susceptibility with vga(A), using broth dilution and induced expression. This is family/context evidence, not a purified CarA-carbomycin experiment. CurrentCARD target-protection classification can remain honestly database-supported. |
| binding | PMID:12150912;PDB:1K8A; 198-extra-core.json complete abstract;198-pdb.json deposition and198-cai.json exact ligand | partial | The2002 original abstract and 3.0 angstrom deposition show carbomycin A bound in the Haloarcula marismortui large-subunit exit tunnel near the peptidyl-transferase center. CCD CAI matches native full chemistry. This archaeal structural model is a bounded direct-binding example; it is not a bacterial strain MIC or proof that every ribosomal protein is a direct target. Full publisher text returned403; raw diffraction data were not reprocessed. |
| other-leads | All16 adopted compound,determinant and parent PMID records; 198-core.json;198-lead-dispositions.json | context_only | All16 records resolve;15 complete abstracts were read and 1952 PMID24542077 has none. Parent27480866 tests ceftriaxone/azithromycin in mouse pneumonia;15544496 and 11324679 are macrolide reviews, not exact carbomycin experiments.1761231 studies S.lividans lrm/mgt rather than directly testing S.ambofaciens srmA. Remaining ErmS papers concern induction, methylation substrate mapping and cloning;6163765 concerns diverse induction/methylation phenotypes. Their individual depths and limits are preserved. |
| adapter | iModulonDB; 198-imodulondb-datasets.txt | context_only | Catalog inspected before web follow-up. S.ambofaciens, S.fradiae, S.thermotolerans andS.viridochromogenes lack covered dataset keys; S.albidoflavus andS.coelicolor entries are not species matches. Exact source-gene queries are not applicable. In particular an unrelated carA gene in another organism must not be substituted for the antibiotic-resistance ABC-F protein. Dataset absence is not negative resistance evidence. |
| owners | data/raw/aro_antibiotics.tsv;scripts/extract_source_inventory.py;scripts/seed_from_sources.py; Exact adopted row and gate_xrefs;198-xref-hits.txt | supports | ARO extraction carries the source xrefs; seeder normalizes and emits them while its current structure-comparison gate uses ChEBI keys. Thus this ChEMBL conflict needs a reproducible upstream correction or a maintained source/structure-aware gate, not a native-only deletion. No exact existing correction was found in the ignored-inclusive curation/conf/native-corpus search. |
| validation | Focused schema/strict/chemistry; 198-strict.tsv;198-chemistry.json | supports | Schema/strict exit0; supplemental019 RDKit interpreter against020 files exit0 with explicit external mismatch output. These focused checks do not substitute for required shared corpus gates. |

## Limits And Additional Notes

- The original 1952 PMID24542077 has no indexed abstract and full text was not obtained. Both named producer contexts are independently corroborated by later primary sources; the exact coverage of the native definition_source remains unresolved.
- Most historical resistance papers were read as complete abstracts. PMC163745 andPMC210198 HTML yielded abstract/archive pages; fullTextXML requests failed500 and linked PDF retrievals returned download-preparation HTML, not PDFs. No compound-specific MIC or purified enzymatic rate was invented from those abstracts.
- The1992 CarA source infers export from sequence similarity. The full 2016 ABC-F paper tests Vga(A)/Lsa(A), not CarA; its direct displacement assay uses lincomycin. Carbomycin A susceptibility context is distinct from a direct CarA protection experiment. Supplemental quantitativeMIC tables were not adopted.
- The2002 primary abstract and PDB1K8A/CCDCAI were inspected; publisher fulltext returned403. The archaeal model supports a bounded binding context but is not evidence of bacterial species susceptibility. Absolute stereochemistry was not independently rederived from raw diffraction.
- The1984 full paper and Fig3 were inspected. Its carbomycin A substrate, deepoxidized products and microbial transformations remain separate; schematic constitution is not treated as a fresh absolute-stereochemical assignment.
- Current public ChEMBL conflict is a confirmed exact-xref defect; biological activity of the conflicting epimer was not evaluated. Correcting the xref does not require deciding that every historical generic carbomycin sample was chemically homogeneous.
- No exhaustive clinical, producer-taxonomy or resistance survey was undertaken.020 lacksRDKit; supplemental chemistry used019 interpreter against020 files. Required shared checks are distinct from the focused checks recorded here.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 19 repository input hashes and the externalARO cache hash remain unchanged; no native or saved-bundle changes. Generic initialChEBI context inputs were retained for provenance but actual record ownership isARO/PubChem.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T105307Z-carbomycin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of carbomycin
started_at: '2026-10-21T10:32:40Z'
finished_at: '2026-10-21T10:53:07Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Native carbomycin A graph supported; major ChEMBL exact-cross-reference
  stereochemical conflict
scientific_review: true
summary: The native structure is internally coherent and agrees with current PubChem5287879,
  CCD CAI and CHEMBL1231649 carbomycin A. Published chembl:CHEMBL3989435 instead differs
  at one epoxide stereocenter and violates the same-structure xref contract. Antibacterial
  activity and macrolide class are supported. All five resistance items honestly retain
  CARD provenance; historical hypotheses and induction assays must not be promoted
  to direct CarA transport or carbomycin-specific ribosome-protection measurements.
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
  - path: data/antibiotics/antibacterial/carbomycin.yaml
    sha256: 3c307b032507595363924a312954a8a70c669217bd9696ac6fe382a0e5bc3fe4
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
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: context
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
  - path: scripts/card_evidence_reviews.py
    sha256: f9ec8aff30066bf04b9c2757af7d6f5d179d045e57b9f3b352bbed0b851f50a8
    role: context
scope:
  description: Entire exact MINTED/SEEDED record, three history events, all five resistance
    objects, actual ARO/PubChem source rows and seeder ownership; all 16 adopted compound,
    determinant and parent PMID leads; selected original structure, production and
    resistance studies.
  selection: Queue198; root original13 captured inputs retained, six actual ARO/PubChem/evidence
    owner inputs appended before detailed inspection.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-27630f7c54
targets:
- target_id: antibioticmech:aro-27630f7c54
  path: data/antibiotics/antibacterial/carbomycin.yaml
  label: carbomycin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual ARO structure/claim source or maintained evidence review
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Actual ARO structure/claim source or maintained evidence review
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Actual ARO structure/claim source or maintained evidence review
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Actual ARO structure/claim source or maintained evidence review
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Actual ARO structure/claim source or maintained evidence review
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Actual ARO structure/claim source or maintained evidence review
checks:
- check_id: schema
  name: Documented schema check
  status: passed
  required: true
  summary: Exit0.
  target_ids:
  - antibioticmech:aro-27630f7c54
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/carbomycin.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented strict check
  status: passed
  required: true
  summary: Exit0, zeroERRORrows.
  target_ids:
  - antibioticmech:aro-27630f7c54
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/carbomycin.yaml --out /private/tmp/am-review-session/198-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Supplemental graph comparison
  status: passed
  required: false
  summary: 'Exit0: internal graph consistency verified and external mismatch explicitly
    detected; this is not a clean-xref assertion.'
  target_ids:
  - antibioticmech:aro-27630f7c54
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/198-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: adapter-catalog
  name: Structured source applicability
  status: passed
  required: false
  summary: Catalog inspected before resistance-protein web follow-up; none of the
    four source species is covered.
  target_ids:
  - antibioticmech:aro-27630f7c54
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets > /private/tmp/am-review-session/198-imodulondb-datasets.txt
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:aro-27630f7c54
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
  - antibioticmech:aro-27630f7c54
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
  - antibioticmech:aro-27630f7c54
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
  - antibioticmech:aro-27630f7c54
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
  - antibioticmech:aro-27630f7c54
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
  - antibioticmech:aro-27630f7c54
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
  - antibioticmech:aro-27630f7c54
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
  - antibioticmech:aro-27630f7c54
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
  - antibioticmech:aro-27630f7c54
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/carbomycin.yaml
  locator: Entire YAML, all five resistance objects and three history events
  accessed_at: '2026-10-21T10:52:09Z'
  support: supports
  summary: The record is MINTED/SEEDED, stores one neutral epoxyenone macrolide graph
    and three exact xrefs. Five resistance entries explicitly cite database assertions
    rather than primary evidence. No native MIC, molecular target, mechanism graph
    or curated producer object is asserted.
- evidence_id: chemistry
  kind: validation
  reference: PubChem:5287879;CHEMBL3989435;CHEMBL1231649;CCD:CAI
  locator: 198-chemistry.py/.json;198-pubchem.json;198-chembl.json;198-chembl-exact.json;198-cai.json
  accessed_at: '2026-10-21T10:52:09Z'
  support: supports
  summary: 'Native SMILES/InChI/key, neutral C42H67NO16, masses and 17 configured
    centers agree internally. Current PubChem5287879, CCD CAI and CHEMBL1231649 share
    FQVHOULQCKDUCY-OGHXVOSASA-N. CHEMBL3989435 has FQVHOULQCKDUCY-PRPXPMGXSA-N. Whole-graph
    mapping isolates one epoxide difference: native SMILES atom13(S) maps to ChEMBL
    atom46(R), zero-based; native InChI t30+ versus t30-. Formula/connectivity agreement
    alone cannot validate this exact xref.'
  snapshot_sha256: 74c79a6253e0da248639bb144892275205cb91ba3b7dbce1da07c51813abbcbc
- evidence_id: chembl-conflict
  kind: database
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL3989435.json
  locator: Current complete structure API response198-chembl.json
  accessed_at: '2026-10-21T10:52:09Z'
  support: refutes
  summary: The published ChEMBL accession resolves to a configured stereoisomer differing
    from the stored graph. Exact-key API search returns CHEMBL1231649 labelled CARBOMYCIN
    A; the separate detail response confirms full-key and SMILES agreement. This establishes
    the bounded xref conflict without requiring the native graph to be replaced.
  snapshot_sha256: a831d427a4901a3ed926f421e592ca52d88206fa2027ae9f6a32f8ae5120cfd1
- evidence_id: source-conflict
  kind: authority
  reference: ARO:3001228
  locator: 198-aro-stanzas.txt;198-aro_antibiotics.json;198-card.html
  accessed_at: '2026-10-21T10:52:09Z'
  support: partial
  summary: Adopted ARO and currentCARD link both the conflicting ChEMBL accession
    and PubChem5287879. CurrentCARD displays the ChEMBL SMILES. This is a source-level
    discrepancy propagated by the seeder, not an isolated manual YAML edit. Generic
    carbomycin remains the imported label; exact native graph is carbomycin A.
  snapshot_sha256: beaf157190c5b80cb16bb93820048a4afc81be53c2d4fe5cba0504e609e8e661
- evidence_id: production
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.37.118
  locator: 198-halstedii.pdf complete main text;Methods p119,Table2 p122,Fig3 p123
    independently viewed
  accessed_at: '2026-10-21T10:52:09Z'
  support: supports
  summary: The1984 study states that carbomycin A(deltamycin A4) was produced by fermentation
    of S.halstedii subsp.deltae FERM-P2504 and purified in the authors laboratory.
    Original substrate formula C42H67NO16 and epoxyenone constitution agree with the
    native compound; derivatives P1/P2/P3 are separate structures. Deepoxidation assays
    on other microbes do not make those organisms natural producers. This source supports
    producer context but its schematic alone does not independently rederive all absolute
    stereocenters.
  snapshot_sha256: c5bd99bc20fbb6ffa36504dfe89d174c2f7e8d83b9b6d0713dc8366d2bd9bf41
- evidence_id: definition
  kind: primary_source
  reference: PMID:24542077;PMID:3036668
  locator: 198-core.json;original1952 metadata and complete1987 abstract
  accessed_at: '2026-10-21T10:52:09Z'
  support: partial
  summary: The adopted1952 source resolves as Some properties of magnamycin; a new
    antibiotic, with no indexed abstract. Its exact two-species claim could not be
    checked from the original text. The1987 cloning abstract independently describes
    S.thermotolerans as a carbomycin producer; the 1984 fermentation source supports
    the S.halstedii side. Do not claim that the unavailable1952 paper was inspected
    or proves both species.
  snapshot_sha256: 2412a00945ed0cecb281f250a6889afd22412b459900dc6714402d16a3d655bc
- evidence_id: erm-resistance
  kind: primary_source
  reference: PMID:10517588;3020383;2753855;3036668;1691981;9055987
  locator: Complete abstracts198-core.json and198-carb-core.json;PMC163745/PMC210198
    HTML abstract/archive pages
  accessed_at: '2026-10-21T10:52:09Z'
  support: partial
  summary: SrmA introduces one A2058 methyl group in S.ambofaciens with an MLS-I phenotype,
    though the retrieved abstract does not name carbomycin. tlrA expression confers
    carbomycin resistance in S.griseofuscus; independent work shows A2058 dimethylation.
    carA/carB cloning confers carbomycin resistance; additional1990carB work demonstrates
    A2058 monomethylation with different whole-cell and isolated-ribosome resistance
    magnitudes. ErmSV1997 specifically tests translational attenuator-lac induction
    by carbomycin, not a carbomycin methylation rate or MIC. These support bounded
    mechanisms without converting every imported edge to primary evidence.
  snapshot_sha256: 8e40997e1f29147dd0f8038b08224bd77d106005c72eb7cc221d9616cab60844
- evidence_id: cara-history
  kind: primary_source
  reference: PMID:1612454;PMID:27006457
  locator: 198-core.json complete1992abstract;198-abcf.xml full mainMethods/Results
  accessed_at: '2026-10-21T10:52:09Z'
  support: context_only
  summary: The1992 CarA/TlrC/SrmB paper proposes ATP-driven export from sequence similarity,
    not a direct transport measurement. The2016 ABC-F study directly tests Vga(A)/Lsa(A)
    protection and lincomycin displacement; it does not directly test CarA. Its S.aureus
    RN4220 carbomycin A susceptibility comparison shows fourfold reduced susceptibility
    with vga(A), using broth dilution and induced expression. This is family/context
    evidence, not a purified CarA-carbomycin experiment. CurrentCARD target-protection
    classification can remain honestly database-supported.
  snapshot_sha256: 677d3c333b6465f44805d68108fab1916eeaad6a14f7e72d0d8e40c5161e3695
- evidence_id: binding
  kind: primary_source
  reference: PMID:12150912;PDB:1K8A
  locator: 198-extra-core.json complete abstract;198-pdb.json deposition and198-cai.json
    exact ligand
  accessed_at: '2026-10-21T10:52:09Z'
  support: partial
  summary: The2002 original abstract and 3.0 angstrom deposition show carbomycin A
    bound in the Haloarcula marismortui large-subunit exit tunnel near the peptidyl-transferase
    center. CCD CAI matches native full chemistry. This archaeal structural model
    is a bounded direct-binding example; it is not a bacterial strain MIC or proof
    that every ribosomal protein is a direct target. Full publisher text returned403;
    raw diffraction data were not reprocessed.
  snapshot_sha256: 31430f08699f5dab94e9c0b9fe5787684988466ab2d38f016ce699e7481a10e7
- evidence_id: other-leads
  kind: database
  reference: All16 adopted compound,determinant and parent PMID records
  locator: 198-core.json;198-lead-dispositions.json
  accessed_at: '2026-10-21T10:52:09Z'
  support: context_only
  summary: All16 records resolve;15 complete abstracts were read and 1952 PMID24542077
    has none. Parent27480866 tests ceftriaxone/azithromycin in mouse pneumonia;15544496
    and 11324679 are macrolide reviews, not exact carbomycin experiments.1761231 studies
    S.lividans lrm/mgt rather than directly testing S.ambofaciens srmA. Remaining
    ErmS papers concern induction, methylation substrate mapping and cloning;6163765
    concerns diverse induction/methylation phenotypes. Their individual depths and
    limits are preserved.
  snapshot_sha256: 2412a00945ed0cecb281f250a6889afd22412b459900dc6714402d16a3d655bc
- evidence_id: adapter
  kind: database
  reference: iModulonDB
  locator: 198-imodulondb-datasets.txt
  accessed_at: '2026-10-21T10:52:09Z'
  support: context_only
  summary: Catalog inspected before web follow-up. S.ambofaciens, S.fradiae, S.thermotolerans
    andS.viridochromogenes lack covered dataset keys; S.albidoflavus andS.coelicolor
    entries are not species matches. Exact source-gene queries are not applicable.
    In particular an unrelated carA gene in another organism must not be substituted
    for the antibiotic-resistance ABC-F protein. Dataset absence is not negative resistance
    evidence.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv;scripts/extract_source_inventory.py;scripts/seed_from_sources.py
  locator: Exact adopted row and gate_xrefs;198-xref-hits.txt
  accessed_at: '2026-10-21T10:52:09Z'
  support: supports
  summary: ARO extraction carries the source xrefs; seeder normalizes and emits them
    while its current structure-comparison gate uses ChEBI keys. Thus this ChEMBL
    conflict needs a reproducible upstream correction or a maintained source/structure-aware
    gate, not a native-only deletion. No exact existing correction was found in the
    ignored-inclusive curation/conf/native-corpus search.
  search_scope: rg --no-ignore --hidden -n -i for3001228, carbomycin, CHEMBL3989435,
    CHEMBL1231649 over curation, conf, data/antibiotics; all matched text inspected.
- evidence_id: validation
  kind: validation
  reference: Focused schema/strict/chemistry
  locator: 198-strict.tsv;198-chemistry.json
  accessed_at: '2026-10-21T10:52:09Z'
  support: supports
  summary: Schema/strict exit0; supplemental019 RDKit interpreter against020 files
    exit0 with explicit external mismatch output. These focused checks do not substitute
    for required shared corpus gates.
assessments:
- assessment_id: identity
  area: identity
  topic: Stored exact carbomycin A graph
  outcome: supported
  summary: Internal graph and currentPubChem/exactChEMBL/CCD agree; no derivative
    or salt is substituted.
  target_ids:
  - antibioticmech:aro-27630f7c54
  evidence_ids:
  - chemistry
  - production
- assessment_id: xref
  area: grounding
  topic: Exact ChEMBL mapping
  outcome: concern
  summary: CHEMBL3989435 conflicts at one configured epoxide center; CHEMBL1231649
    is a verified exact candidate.
  target_ids:
  - antibioticmech:aro-27630f7c54
  evidence_ids:
  - chemistry
  - chembl-conflict
  - source-conflict
- assessment_id: class
  area: grounding
  topic: Antibacterial macrolide classification
  outcome: supported
  summary: Native sixteen-member lactone and original carbomycin A microbial studies
    support the filing.
  target_ids:
  - antibioticmech:aro-27630f7c54
  evidence_ids:
  - chemistry
  - production
  - cara-history
- assessment_id: definition
  area: evidence
  topic: Producer definition citation
  outcome: unknown
  summary: Producer context is independently corroborated, but the full 1952 cited
    paper was unavailable.
  target_ids:
  - antibioticmech:aro-27630f7c54
  evidence_ids:
  - definition
  - production
- assessment_id: resistance
  area: evidence
  topic: Five CARD resistance entries
  outcome: supported
  summary: All reproduce honest imported evidence; primary abstracts and later family
    experiments provide bounded support without reclassifying historical export speculation
    as proof.
  target_ids:
  - antibioticmech:aro-27630f7c54
  evidence_ids:
  - erm-resistance
  - cara-history
  - record
- assessment_id: mechanism
  area: completeness
  topic: Optional primary ribosome evidence
  outcome: supported
  summary: A bounded archaeal binding study is available for future enrichment; absence
    of a native target is not a demonstrated required-field defect.
  target_ids:
  - antibioticmech:aro-27630f7c54
  evidence_ids:
  - binding
- assessment_id: provenance
  area: provenance
  topic: References and history
  outcome: supported
  summary: All16 adopted/parent PMID records resolve at stated depths; three history
    events and actual owner paths were inspected.
  target_ids:
  - antibioticmech:aro-27630f7c54
  evidence_ids:
  - other-leads
  - owners
  - record
- assessment_id: schema
  area: schema
  topic: Focused checks
  outcome: supported
  summary: Schema/strict pass; supplemental chemistry explicitly detects external
    stereochemical mismatch.
  target_ids:
  - antibioticmech:aro-27630f7c54
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: aro-27630f7c54-chembl-epoxide-stereoisomer-xref
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: The published ChEMBL exact xref identifies a different epoxide stereoisomer
  description: chembl:CHEMBL3989435 currently resolves to FQVHOULQCKDUCY-PRPXPMGXSA-N
    while the native graph and PubChem5287879 are FQVHOULQCKDUCY-OGHXVOSASA-N. Graph
    mapping identifies a single S-to-R epoxide change(native atom13, ChEMBL atom46,
    zero-based). Equal formula and connectivity do not satisfy exact structural identity.
    Preserve the supported native carbomycin A graph; withhold the conflicting exact
    xref and consider the independently verified CHEMBL1231649 mapping through a reproducible
    source correction.
  target_ids:
  - antibioticmech:aro-27630f7c54
  field_paths:
  - xrefs[1]
  evidence_ids:
  - chemistry
  - chembl-conflict
  - source-conflict
  - owners
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted source xref row,regenerated through source workflow
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Exact-xref gate and generation
  rule_id: 'docs/CURATION.md: xrefs denote the same exact structure,including stereochemistry'
  native_severity: major incorrect exact-identity assertion
  normalization_reason: The native compound remains unambiguous and internally valid,
    so this is a major mapping error rather than wholesale wrong-record identity.
    Current native schema/strict checks do not compare the remote ChEMBL graph.
actions:
- action_id: A1
  description: Repair the ChEMBL cross-reference reproducibly while retaining source
    provenance and the supported native structure.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-27630f7c54
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted source xref row,regenerated through source workflow
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Exact-xref gate and generation
  acceptance_checks:
  - Preserve the imported ARO mapping as source history; make a maintained extraction/seeder
    correction or structure-aware xref gate with explicit provenance. Do not silently
    edit only the generated YAML or pretend the current ChEBI-only gate already handles
    ChEMBL.
  - Ensure chembl:CHEMBL3989435 is no longer emitted as an exact xref to this graph.
    If adopting chembl:CHEMBL1231649, verify neutral formula, connectivity, all 17
    centers, double-bond geometry and full key against the native graph; retain the
    native structure unless separately justified evidence changes it.
  - Regenerate using the source workflow; confirm the correction survives reseeding
    and the source row remains traceable. Run focused schema/strict plus required
    source/reference/history and full-corpus gates; an explicit remote/local graph
    regression must detect the mapped epoxide mismatch.
limitations:
- The original 1952 PMID24542077 has no indexed abstract and full text was not obtained.
  Both named producer contexts are independently corroborated by later primary sources;
  the exact coverage of the native definition_source remains unresolved.
- Most historical resistance papers were read as complete abstracts. PMC163745 andPMC210198
  HTML yielded abstract/archive pages; fullTextXML requests failed500 and linked PDF
  retrievals returned download-preparation HTML, not PDFs. No compound-specific MIC
  or purified enzymatic rate was invented from those abstracts.
- The1992 CarA source infers export from sequence similarity. The full 2016 ABC-F
  paper tests Vga(A)/Lsa(A), not CarA; its direct displacement assay uses lincomycin.
  Carbomycin A susceptibility context is distinct from a direct CarA protection experiment.
  Supplemental quantitativeMIC tables were not adopted.
- The2002 primary abstract and PDB1K8A/CCDCAI were inspected; publisher fulltext returned403.
  The archaeal model supports a bounded binding context but is not evidence of bacterial
  species susceptibility. Absolute stereochemistry was not independently rederived
  from raw diffraction.
- The1984 full paper and Fig3 were inspected. Its carbomycin A substrate, deepoxidized
  products and microbial transformations remain separate; schematic constitution is
  not treated as a fresh absolute-stereochemical assignment.
- Current public ChEMBL conflict is a confirmed exact-xref defect; biological activity
  of the conflicting epimer was not evaluated. Correcting the xref does not require
  deciding that every historical generic carbomycin sample was chemically homogeneous.
- No exhaustive clinical, producer-taxonomy or resistance survey was undertaken.020
  lacksRDKit; supplemental chemistry used019 interpreter against020 files. Required
  shared checks are distinct from the focused checks recorded here.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 19 repository input hashes and the externalARO cache hash remain unchanged;
  no native or saved-bundle changes. Generic initialChEBI context inputs were retained
  for provenance but actual record ownership isARO/PubChem.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL3989435.json
- https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL1231649.json
- https://doi.org/10.7164/antibiotics.37.118
- https://doi.org/10.1128/mbio.01975-15
- https://www.rcsb.org/structure/1K8A
tags:
- record-review
- carbomycin
- stereochemical-xref
```
