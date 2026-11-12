# Review of cloxacillin

- Review: 20261021T133835Z-cloxacillin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T13:22:51Z
- Finished UTC: 2026-10-21T13:38:35Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Neutral cloxacillin has the supported 2S,5R,6R penam structure and antibacterial activity. Independent structures agree, including a documented standard-InChI tautomer round-trip difference. The PBP assertion is supported by original acyl-enzyme work, and MdtEF-dependent cloxacillin resistance is supported by a separate original overexpression study. One minor correction concerns four branded sodium products currently typed as exact chemical synonyms. All thirteen adopted bibliography leads were resolved with explicit inspection limits.

## Scope And Provenance

Entire SEEDED, EXACT record: definition, nineteen names, four parents, three activity roles, all chemical fields, eleven chemical links, three drug links, two document links, two source concepts, one resistance edge, one target and five history events.

Selection: Queue 315 in isolated batch 032. Initial thirteen hashes preserved; actual ARO source, resistance, target and role-map inputs appended for seventeen unchanged inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:49566 | data/antibiotics/antibacterial/cloxacillin.yaml | generated | cloxacillin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema validation | passed | True | CHEBI:49566 | Exit 0. |
| Documented strict validation | passed | True | CHEBI:49566 | Exit 0; no ERROR rows. |
| Native molecular consistency | passed | False | CHEBI:49566 | Exit 0; native standard keys, composition, charge, masses and both minted identifiers agree. |
| Initial direct bond-order comparison | failed | False | CHEBI:49566 | Exit 1 at native-inchi direct graph assertion. Standard InChI reconstructs the side-chain amide as an imidic-acid tautomer; the identical standard key and atom-mapped follow-up resolve this comparison failure. |
| Tautomer-aware exact structure comparison | passed | False | CHEBI:49566 | Exit 0; eleven authority/native encodings share the standard key, composition and three configured centers, with mutual chirality-aware mappings after canonical-tautomer normalization. |
| Source and adopted-lead reconciliation | passed | False | CHEBI:49566 | Exit 0; seventeen hashes, nineteen names, five history events, thirteen adopted PMID leads and both mechanism rows reconcile. |
| Initial structured mdtE query | failed | False | CHEBI:49566 | Exit 2 from sandbox DNS failure; approved-network retry succeeded. |
| Structured mdtE retry | passed | False | CHEBI:49566 | Exit 0; b3513/mdtE gene hit and zero iModulons. |
| Structured PBP context | passed | False | CHEBI:49566 | Exit 0; no genes or iModulons returned for this query. No summarize call applies. |
| Authoritative full QC | failed | True | CHEBI:49566 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:49566 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:49566 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:49566 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:49566 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:49566 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:49566 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:49566 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:49566 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral penam structure

identity: supported. Targets: CHEBI:49566.

The three configured centers and composition agree; standard-InChI tautomer reconstruction is distinguished from a true structural conflict.

### Branded products typed as exact molecule names

nomenclature: concern. Targets: CHEBI:49566.

Cloxapen, Orbenin, Syntarpen and Tegopen are verified sodium-product names and should retain product-aware typing.

### Penicillin class, semisynthetic and antibacterial/allergen roles

grounding: supported. Targets: CHEBI:49566.

Chemical graph, source terms, clinical/allergy abstracts and official products support these scoped classifications.

### PBP direct interaction and biological target scope

evidence: supported. Targets: CHEBI:49566.

Original PBP5 acyl-enzyme structure supports interaction with a PBP family member. It does not by itself identify the lethal transpeptidase, and the native PRIMARY_EVIDENCE_NEEDED qualification remains appropriate.

### MdtEF-TolC cloxacillin resistance

evidence: supported. Targets: CHEBI:49566.

The 2003 exact-compound experiment supports the relation in an overexpression/TolC-dependent context; other substrates in 2004/2002 are not substituted.

### External chemical, drug and document mappings

identity: supported. Targets: CHEBI:49566.

Inspected exact graphs agree; broader drug/document records remain in their own fields. LINCS and restricted registry bodies remain unresolved, without a wrong-ID conclusion.

### All adopted leads, actual owners and history

provenance: supported. Targets: CHEBI:49566.

Seventeen hashes, five history events and thirteen bibliography dispositions reconcile.

### Focused native checks

schema: supported. Targets: CHEBI:49566.

Schema and strict checks pass; the diagnosed supplemental graph-comparison failure does not indicate invalid native chemistry.

### Optional mechanistic and quantitative enrichment

completeness: supported. Targets: CHEBI:49566.

Bounded primary evidence could be added through separate curation. Absence of optional MIC, clinical status or causal graphs is not a required-field defect.

## Findings

### F1: Four branded sodium products are typed as exact neutral-acid synonyms

minor / open / confirmed; issue key: chebi-49566-branded-sodium-products-exact-synonyms.

Cloxapen, Orbenin, Syntarpen and Tegopen are EXACT_SYNONYM entries on neutral cloxacillin. Official named-product documents establish sodium formulations, and current ChEBI explicitly calls Orbenin a brand name. These aliases are appropriate contextual product names but not exact molecular-form synonyms. The acid structure and conventional generic names are unaffected.

## Recommended Actions And Acceptance Checks

### A1

Use the existing ARO:0000011 synonym_exclusions configuration to prevent these four product names from regenerating as EXACT_SYNONYM. If retaining them, implement a reproducible per-source synonym-type override to emit BRAND_NAME with product context; do not assume that override already exists or edit generated YAML directly. Keep neutral cloxacillin chemistry and generic names unchanged.

- Regeneration no longer presents Cloxapen, Orbenin, Syntarpen or Tegopen as exact neutral-acid aliases; preserved product names use BRAND_NAME with source provenance.
- Retain LQOLIRLGBULYKD-JKIFEVAISA-N, all three penam stereocenters and existing qualified mechanism/source/history objects.
- Rerun documented schema/strict validation and required corpus gates after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/cloxacillin.yaml; Entire YAML, including database-only mechanism notes and five history events | supports | Neutral cloxacillin is distinct from sodium formulations. The molecular target requires primary evidence and the MdtEF resistance edge cites a database assertion. No quantitative MIC, clinical-approval assertion, producer or causal graph is present. |
| chemistry | CHEBI:49566; PubChem:6098; ChEMBL:CHEMBL891; KEGG:C06923/D07733; PDB-CCD:CXN; 315-authority-chemistry.json;315-chemistry-initial-failure.json;315-chemistry-tautomer.py/.log | supports | Eleven inspected native/authority encodings yield LQOLIRLGBULYKD-JKIFEVAISA-N, C19H18ClN3O5S, charge 0 and the three configured penam centers. Native SMILES, ChEBI molfile, chemical-authority graphs and PDB CCD describe the same acid. Standard InChI round trips reconstruct the side-chain amide as an imidic-acid tautomer, explaining the failed direct bond-order match; canonical-tautomer mutual chirality-aware mappings agree without a stereo inversion. Masses agree. This normalization difference is not a demonstrated identity defect. |
| authority | https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:49566; 315-chebi.json: definition, names, structure, ontology relations and accession groups | supports | Current ChEBI supports the definition, penicillin/semisynthetic/allergen parents and antibacterial roles, including inherited antimicrobial role. It separately identifies the conjugate base and labels Orbenin as a brand name. Exact systematic names agree with the 2S,5R,6R graph. The additional current bibliography is not silently adopted as frozen evidence. |
| aro | https://purl.obolibrary.org/obo/aro.obo; Current official 310-aro-current.obo reused;315-aro-selected.json for ARO0000011,3000008,3000749,3000788 | supports | Current ARO retains the native source identity, aliases, class, cloxacillin PBP relation and MdtEF-TolC resistance relation. The maintained target role table and seeder add the explicit PRIMARY_EVIDENCE_NEEDED qualification. The native resistance note is database provenance, not a claim that the ontology-linked H-NS paper directly measured cloxacillin. |
| brands | Philippines FDA comparator list 2019; Polish register Syntarpen 10718; FDA proprietary-name review 2012; 315-brands-philippines.pdf printed page 30 visually inspected;315-syntarpen.pdf sections 1–3;315-tegopen.pdf printed page 17 / PDF page 26 visually inspected | supports | The Philippines FDA table identifies CLOXAPEN and ORBENIN as comparator products containing cloxacillin as sodium, with dosage forms and strengths. The Polish official Syntarpen SmPC identifies a 1 g injection vial containing cloxacillin sodium. The FDA name-review appendix identifies Tegopen as a proprietary name whose ingredient is cloxacillin sodium. These establish product-name scope for native synonym indices 14, 16, 17, 18, not exact neutral-acid identity. Historical availability or withdrawal statements are not imported as current clinical status. |
| pbp | PMID:20726582; DOI:10.1021/bi100879m; PDB:3MZD; 315-pbp5.html: Methods, cloxacillin Results, Figure 2B and Tables 1–2 | supports | The original structure shows cloxacillin acylating soluble E. coli PBP5, a DD-carboxypeptidase. Table 1 specifies a 10 mM, 60 minute soak and 1.9 angstrom diffraction structure; the chlorophenyl side chain has weak density and zero-occupancy modeling. It is a covalent ring-opened acyl-enzyme complex, not an intact free-acid crystal or proof that PBP5 is the lethal transpeptidase target. Table 2 kinetic constants were imported from an earlier paper, so they are not represented as newly measured cloxacillin kinetics. The Methods reagent list does not independently establish the cloxacillin salt/batch. This supplies bounded family-level direct interaction support while preserving the native primary-evidence qualification. |
| efflux2003 | PMID:12937021; DOI:10.1128/AAC.47.9.3030-3033.2003; 315-efflux2003.html: entire original article, especially cloning methods and Table 3 MCIPC column | supports | The original experiment overexpressed mdtEF from pHSG399 in E. coli KAM3, an acrB-deficient TG1 derivative. Serial twofold YT-agar assays used 10^4 exponential-phase cells grown with chloramphenicol and were repeated at least three times. Cloxacillin is explicitly MCIPC: MIC 0.78 microgram/mL for KAM3/vector versus 12.5 for pHSGmdtEF. In TG1ΔtolC, cloxacillin remained 0.78 with or without pHSGmdtEF. This supports MdtEF/TolC-dependent resistance in the tested overexpression backgrounds. It is not a direct cloxacillin transport-rate measurement, a clinical resistance breakpoint or a claim about all natural isolates; reagent salt/form was not independently established. |
| efflux-boundary | PMID:14973023; PMID:11914367; PMID:19329985; 315-mdte.html and 315-evga.html complete Methods/Results;315-efflux-core.json complete 2009 abstract | context_only | The ontology-linked 2004 H-NS study tests oxacillin, not cloxacillin; its fluorescence assays use ethidium/rhodamine. The 2002 EvgA paper establishes YhiUV/MdtEF regulation and TolC dependence using other substrates. Neither is substituted for an exact cloxacillin experiment. The 2009 YdeO original abstract explicitly reports cloxacillin resistance suppressed by mdtEF or tolC deletion, but the full article remained subscription-restricted and no quantitative or material details are adopted from it. The independent 2003 exact-compound experiment supplies the needed positive support. |
| links | KEGG:C06923/D07733; PDB-CCD:CXN; VSDB:1859; DrugCentral:720; Patent:US2996501; Wikipedia:Cloxacillin; 315-kegg-*.txt/.mol;315-pdb.json;315-vsdb.html;315-drugcentral.html;315-patent.html;315-wikipedia.html | supports | KEGG and PDB exact molecular graphs agree. VSDB 1859 gives the native key, stereochemical SMILES and acid formula. DrugCentral 720 and the RCSB-carried DrugBank link resolve to cloxacillin drug context, where salt/product aliases remain contextual. The patent is a broader synthetic isoxazolyl-penicillin document and includes the ortho-chlorophenyl/methyl member; it is not treated as a neutral-acid clinical claim. Wikipedia resolves to the expected article and is document context only. |
| leads | Ten frozen ChEBI citations and three ARO definition citations; 315-leads.json;315-lead-dispositions.json | supports | All thirteen adopted leads were resolved. Eleven supplied abstracts were read; the non-availability commentary PMID 27889744 and beta-lactamase review PMID 15673804 supplied no abstracts, and full text was not obtained. Allergy/IgE evidence supports bounded allergen context. PK, prophylaxis, esophagitis and seizure reports retain clinical material and study scope; none is relabeled as direct PBP or efflux evidence. |
| adapter | iModulonDB e_coli/modulome; Current catalog 308-adapter-datasets.txt;315-adapter-mdtE.txt and 315-adapter-pbp.txt | context_only | Both 315-specific queries preceded open mechanism research. mdtE resolves to b3513, with zero iModulons; the penicillin-binding query has no hits. These are search/catalog outcomes, not negative mechanistic evidence or drug transport measurements. |
| owners | ChEBI/ARO source tables, ARO edge tables, conf/aro_target_roles.tsv and seeder; 315-source-audit.json;315-lead-dispositions.json;315-320-local-hits.txt | supports | Seventeen captured inputs and all five history events are unchanged. Nineteen names, exact structures, three roles, chemical/drug/document links and both qualified mechanism objects reconcile with maintained sources. The existing conf/sources.yaml synonym_exclusions lane can prevent regeneration of wrongly exact product names; a BRAND_NAME override would require an explicit maintained type mapping. |
| validation | Documented native validators and supplemental molecular/source reconciliation; 315-focused-results.json;315-schema.log;315-strict.log;315-authority-chemistry.json;315-source-audit.json | supports | Schema, strict, native chemistry, tautomer-aware authority comparisons and source reconciliation pass. The initial direct graph comparison and initial adapter query failed for documented reasons and are retained as actual check outcomes. Required full-corpus gates remain separate. |
| search | Exact source and identifier discovery; Ignored-inclusive rg in curation,conf,scripts,data/raw for cloxacillin,CHEBI49566,ARO0000011 and molecular key; exact MED bibliography query; official product and original mechanism searches | context_only | Ignored files were included. LINCS LSM15183 remains independently unresolved: the direct resolver failed and the limited HMS20200624 SDF has no exact entry among 639 records. This is not evidence that the global LINCS identifier is invalid. Reaxys/Beilstein and independent CAS registry records were not obtained. |

## Limits And Additional Notes

- Independent original records for LINCS LSM15183, Reaxys/Beilstein and CAS were not obtained. HMDB and direct DrugBank returned 403; DrugBank association was inspected through its explicitly labeled RCSB drug-context record. The limited HMS archive miss is not a global absence result.
- The native Methocillin S alias remains source-concordant, but its exact named-product/form history was not independently established; it is not included in the confirmed four-name finding.
- Most adopted literature leads were abstract-only. Two leads supplied no abstract. New current ChEBI bibliography beyond the frozen ten was not exhaustively reviewed.
- The exact cloxacillin reagent salt/batch was not independently specified in the inspected efflux/PBP work. Sodium product documents establish product boundaries, not the assay material in unrelated studies.
- The 2010 PBP5 source demonstrates a soluble carboxypeptidase acyl-enzyme complex; its reagent list omits an unambiguous cloxacillin preparation. Weak side-chain density and imported kinetic constants limit structural/kinetic inference.
- The 2003 resistance experiment uses plasmid overexpression and a sensitized laboratory background. It supports a bounded efflux-related phenotype, not clinical resistance of every organism carrying mdtEF. The 2009 YdeO full article remained subscription-restricted; its abstract is only corroborative.
- Standard InChI parsing reconstructs an imidic-acid tautomer; the initial direct bond-order comparison failed but tautomer-aware comparisons preserve the molecular key and stereo. The failure is retained rather than hidden.
- Initial adapter DNS lookup failed and was retried successfully. Europe PMC XML retrievals failed 500 but original PMC HTML succeeded; initial Syntarpen certificate validation failed in urllib but normal curl retrieval succeeded. Nature PDF routes returned HTML access/challenge content, not a paper PDF.
- Focused native checks do not replace separately recorded required full-corpus gates or authorize REVIEWED status.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Native records, maintained sources and history remain unchanged.
- The batch 019 RDKit interpreter was used against batch 032 native paths; native schema/strict checks used the batch 032 environment.
- Current structured catalog coverage was reused from 308; 315-specific queries were executed before primary mechanism web research.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T133835Z-cloxacillin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of cloxacillin
started_at: '2026-10-21T13:22:51Z'
finished_at: '2026-10-21T13:38:35Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Entire native record independently compared with preserved ChEBI/ARO
    inputs, molecular authorities, official named-product documents and original transporter/PBP
    studies.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Exact neutral identity and qualified database mechanisms supported;
  minor product-name typing correction
scientific_review: true
summary: Neutral cloxacillin has the supported 2S,5R,6R penam structure and antibacterial
  activity. Independent structures agree, including a documented standard-InChI tautomer
  round-trip difference. The PBP assertion is supported by original acyl-enzyme work,
  and MdtEF-dependent cloxacillin resistance is supported by a separate original overexpression
  study. One minor correction concerns four branded sodium products currently typed
  as exact chemical synonyms. All thirteen adopted bibliography leads were resolved
  with explicit inspection limits.
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
  - path: data/antibiotics/antibacterial/cloxacillin.yaml
    sha256: 0d494a57f97ab98d25f6679336374a7d415e1dfe755506effec977a405ef3790
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
    role: Adopted ARO synonyms and class
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: Adopted PBP target assertion
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: Adopted MdtEF resistance assertion
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: Target relation classification
scope:
  description: 'Entire SEEDED, EXACT record: definition, nineteen names, four parents,
    three activity roles, all chemical fields, eleven chemical links, three drug links,
    two document links, two source concepts, one resistance edge, one target and five
    history events.'
  selection: Queue 315 in isolated batch 032. Initial thirteen hashes preserved; actual
    ARO source, resistance, target and role-map inputs appended for seventeen unchanged
    inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:49566
targets:
- target_id: CHEBI:49566
  path: data/antibiotics/antibacterial/cloxacillin.yaml
  label: cloxacillin
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
    path: data/raw/chebi_role_names.tsv
    role: Adopted activity-role labels
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO synonyms and class
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Adopted PBP target assertion
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Adopted MdtEF resistance assertion
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Target relation classification
checks:
- check_id: schema
  name: Documented schema validation
  status: passed
  required: true
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cloxacillin.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0.
  target_ids:
  - CHEBI:49566
  evidence_ids:
  - validation
- check_id: strict
  name: Documented strict validation
  status: passed
  required: true
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cloxacillin.yaml --out /private/tmp/am-review-session/315-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; no ERROR rows.
  target_ids:
  - CHEBI:49566
  evidence_ids:
  - validation
- check_id: native-chemistry
  name: Native molecular consistency
  status: passed
  required: false
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    315 > /private/tmp/am-review-session/315-focused-run.log
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; native standard keys, composition, charge, masses and both minted
    identifiers agree.
  target_ids:
  - CHEBI:49566
  evidence_ids:
  - chemistry
  - validation
- check_id: initial-graph-comparison
  name: Initial direct bond-order comparison
  status: failed
  required: false
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/315-chemistry.py
    > /private/tmp/am-review-session/315-chemistry.log
  exit_code: 1
  expected_exit_code: 0
  summary: Exit 1 at native-inchi direct graph assertion. Standard InChI reconstructs
    the side-chain amide as an imidic-acid tautomer; the identical standard key and
    atom-mapped follow-up resolve this comparison failure.
  target_ids:
  - CHEBI:49566
  evidence_ids:
  - chemistry
- check_id: normalized-comparison
  name: Tautomer-aware exact structure comparison
  status: passed
  required: false
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/315-chemistry-tautomer.py
    > /private/tmp/am-review-session/315-chemistry-tautomer.log
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; eleven authority/native encodings share the standard key, composition
    and three configured centers, with mutual chirality-aware mappings after canonical-tautomer
    normalization.
  target_ids:
  - CHEBI:49566
  evidence_ids:
  - chemistry
- check_id: source-ledger
  name: Source and adopted-lead reconciliation
  status: passed
  required: false
  command: .venv/bin/python /private/tmp/am-review-session/315-ledger.py
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; seventeen hashes, nineteen names, five history events, thirteen
    adopted PMID leads and both mechanism rows reconcile.
  target_ids:
  - CHEBI:49566
  evidence_ids:
  - owners
  - leads
  - validation
- check_id: adapter-initial
  name: Initial structured mdtE query
  status: failed
  required: false
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset modulome --query mdtE
    > /private/tmp/am-review-session/315-adapter-mdtE.txt
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 from sandbox DNS failure; approved-network retry succeeded.
  target_ids:
  - CHEBI:49566
  evidence_ids:
  - adapter
- check_id: adapter-mdtE
  name: Structured mdtE retry
  status: passed
  required: false
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset modulome --query mdtE
    > /private/tmp/am-review-session/315-adapter-mdtE.txt
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; b3513/mdtE gene hit and zero iModulons.
  target_ids:
  - CHEBI:49566
  evidence_ids:
  - adapter
- check_id: adapter-pbp
  name: Structured PBP context
  status: passed
  required: false
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset modulome --query 'penicillin-binding'
    > /private/tmp/am-review-session/315-adapter-pbp.txt
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; no genes or iModulons returned for this query. No summarize call
    applies.
  target_ids:
  - CHEBI:49566
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
  - CHEBI:49566
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
  - CHEBI:49566
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
  - CHEBI:49566
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
  - CHEBI:49566
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
  - CHEBI:49566
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
  - CHEBI:49566
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
  - CHEBI:49566
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
  - CHEBI:49566
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
  - CHEBI:49566
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/cloxacillin.yaml
  locator: Entire YAML, including database-only mechanism notes and five history events
  accessed_at: '2026-10-21T13:34:57Z'
  support: supports
  summary: Neutral cloxacillin is distinct from sodium formulations. The molecular
    target requires primary evidence and the MdtEF resistance edge cites a database
    assertion. No quantitative MIC, clinical-approval assertion, producer or causal
    graph is present.
- evidence_id: chemistry
  kind: validation
  reference: CHEBI:49566; PubChem:6098; ChEMBL:CHEMBL891; KEGG:C06923/D07733; PDB-CCD:CXN
  locator: 315-authority-chemistry.json;315-chemistry-initial-failure.json;315-chemistry-tautomer.py/.log
  accessed_at: '2026-10-21T13:34:57Z'
  support: supports
  summary: Eleven inspected native/authority encodings yield LQOLIRLGBULYKD-JKIFEVAISA-N,
    C19H18ClN3O5S, charge 0 and the three configured penam centers. Native SMILES,
    ChEBI molfile, chemical-authority graphs and PDB CCD describe the same acid. Standard
    InChI round trips reconstruct the side-chain amide as an imidic-acid tautomer,
    explaining the failed direct bond-order match; canonical-tautomer mutual chirality-aware
    mappings agree without a stereo inversion. Masses agree. This normalization difference
    is not a demonstrated identity defect.
  snapshot_sha256: 2a18199ee4198dc9e38990812684951684fcbaddde8f3abca4f36dd22fec30bb
- evidence_id: authority
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:49566
  locator: '315-chebi.json: definition, names, structure, ontology relations and accession
    groups'
  accessed_at: '2026-10-21T13:28:59.415335Z'
  support: supports
  summary: Current ChEBI supports the definition, penicillin/semisynthetic/allergen
    parents and antibacterial roles, including inherited antimicrobial role. It separately
    identifies the conjugate base and labels Orbenin as a brand name. Exact systematic
    names agree with the 2S,5R,6R graph. The additional current bibliography is not
    silently adopted as frozen evidence.
  snapshot_sha256: 29a54ec2c2b5f5121fc33f4aad6a4a974a9f30dd7b20701a1e3aee9517a1ad9d
- evidence_id: aro
  kind: database
  reference: https://purl.obolibrary.org/obo/aro.obo
  locator: Current official 310-aro-current.obo reused;315-aro-selected.json for ARO0000011,3000008,3000749,3000788
  accessed_at: '2026-10-21T13:34:57Z'
  support: supports
  summary: Current ARO retains the native source identity, aliases, class, cloxacillin
    PBP relation and MdtEF-TolC resistance relation. The maintained target role table
    and seeder add the explicit PRIMARY_EVIDENCE_NEEDED qualification. The native
    resistance note is database provenance, not a claim that the ontology-linked H-NS
    paper directly measured cloxacillin.
  snapshot_sha256: d49d34f066b3e45ae72e201818e57ced8f53cc9ea8e8cb10107ce38afbc3fe9a
- evidence_id: brands
  kind: authority
  reference: Philippines FDA comparator list 2019; Polish register Syntarpen 10718;
    FDA proprietary-name review 2012
  locator: 315-brands-philippines.pdf printed page 30 visually inspected;315-syntarpen.pdf
    sections 1–3;315-tegopen.pdf printed page 17 / PDF page 26 visually inspected
  accessed_at: '2026-10-21T13:29:31.655021Z'
  support: supports
  summary: The Philippines FDA table identifies CLOXAPEN and ORBENIN as comparator
    products containing cloxacillin as sodium, with dosage forms and strengths. The
    Polish official Syntarpen SmPC identifies a 1 g injection vial containing cloxacillin
    sodium. The FDA name-review appendix identifies Tegopen as a proprietary name
    whose ingredient is cloxacillin sodium. These establish product-name scope for
    native synonym indices 14, 16, 17, 18, not exact neutral-acid identity. Historical
    availability or withdrawal statements are not imported as current clinical status.
  snapshot_sha256: 00b710a9484690df8f1d9ba02d2be6acf7208c306df2237ee77047c355e340ec
- evidence_id: pbp
  kind: primary_source
  reference: PMID:20726582; DOI:10.1021/bi100879m; PDB:3MZD
  locator: '315-pbp5.html: Methods, cloxacillin Results, Figure 2B and Tables 1–2'
  accessed_at: '2026-10-21T13:30:00.646359Z'
  support: supports
  summary: The original structure shows cloxacillin acylating soluble E. coli PBP5,
    a DD-carboxypeptidase. Table 1 specifies a 10 mM, 60 minute soak and 1.9 angstrom
    diffraction structure; the chlorophenyl side chain has weak density and zero-occupancy
    modeling. It is a covalent ring-opened acyl-enzyme complex, not an intact free-acid
    crystal or proof that PBP5 is the lethal transpeptidase target. Table 2 kinetic
    constants were imported from an earlier paper, so they are not represented as
    newly measured cloxacillin kinetics. The Methods reagent list does not independently
    establish the cloxacillin salt/batch. This supplies bounded family-level direct
    interaction support while preserving the native primary-evidence qualification.
  snapshot_sha256: 48d7dcdfb072631228f3b859f69d4161626d397d21c9c9531a1fedf46983bf38
- evidence_id: efflux2003
  kind: primary_source
  reference: PMID:12937021; DOI:10.1128/AAC.47.9.3030-3033.2003
  locator: '315-efflux2003.html: entire original article, especially cloning methods
    and Table 3 MCIPC column'
  accessed_at: '2026-10-21T13:31:46.514392Z'
  support: supports
  summary: 'The original experiment overexpressed mdtEF from pHSG399 in E. coli KAM3,
    an acrB-deficient TG1 derivative. Serial twofold YT-agar assays used 10^4 exponential-phase
    cells grown with chloramphenicol and were repeated at least three times. Cloxacillin
    is explicitly MCIPC: MIC 0.78 microgram/mL for KAM3/vector versus 12.5 for pHSGmdtEF.
    In TG1ΔtolC, cloxacillin remained 0.78 with or without pHSGmdtEF. This supports
    MdtEF/TolC-dependent resistance in the tested overexpression backgrounds. It is
    not a direct cloxacillin transport-rate measurement, a clinical resistance breakpoint
    or a claim about all natural isolates; reagent salt/form was not independently
    established.'
  snapshot_sha256: ccd76f77ad7f08596977351fd4e341ad31866c95131d5e0dcb010e6d1ec4a3c0
- evidence_id: efflux-boundary
  kind: primary_source
  reference: PMID:14973023; PMID:11914367; PMID:19329985
  locator: 315-mdte.html and 315-evga.html complete Methods/Results;315-efflux-core.json
    complete 2009 abstract
  accessed_at: '2026-10-21T13:30:00.645942Z'
  support: context_only
  summary: The ontology-linked 2004 H-NS study tests oxacillin, not cloxacillin; its
    fluorescence assays use ethidium/rhodamine. The 2002 EvgA paper establishes YhiUV/MdtEF
    regulation and TolC dependence using other substrates. Neither is substituted
    for an exact cloxacillin experiment. The 2009 YdeO original abstract explicitly
    reports cloxacillin resistance suppressed by mdtEF or tolC deletion, but the full
    article remained subscription-restricted and no quantitative or material details
    are adopted from it. The independent 2003 exact-compound experiment supplies the
    needed positive support.
  snapshot_sha256: 0af99e60c2ecb3162c98b2d5f64f17d0144dcc38dce2178d79e650362c580947
- evidence_id: links
  kind: authority
  reference: KEGG:C06923/D07733; PDB-CCD:CXN; VSDB:1859; DrugCentral:720; Patent:US2996501;
    Wikipedia:Cloxacillin
  locator: 315-kegg-*.txt/.mol;315-pdb.json;315-vsdb.html;315-drugcentral.html;315-patent.html;315-wikipedia.html
  accessed_at: '2026-10-21T13:29:31.654905Z'
  support: supports
  summary: KEGG and PDB exact molecular graphs agree. VSDB 1859 gives the native key,
    stereochemical SMILES and acid formula. DrugCentral 720 and the RCSB-carried DrugBank
    link resolve to cloxacillin drug context, where salt/product aliases remain contextual.
    The patent is a broader synthetic isoxazolyl-penicillin document and includes
    the ortho-chlorophenyl/methyl member; it is not treated as a neutral-acid clinical
    claim. Wikipedia resolves to the expected article and is document context only.
  snapshot_sha256: ba1ce3cd89dc9e004c4bb640797fbd5deaf68b3b3c7f9f6af015291b671beb7d
- evidence_id: leads
  kind: database
  reference: Ten frozen ChEBI citations and three ARO definition citations
  locator: 315-leads.json;315-lead-dispositions.json
  accessed_at: '2026-10-21T13:34:57Z'
  support: supports
  summary: All thirteen adopted leads were resolved. Eleven supplied abstracts were
    read; the non-availability commentary PMID 27889744 and beta-lactamase review
    PMID 15673804 supplied no abstracts, and full text was not obtained. Allergy/IgE
    evidence supports bounded allergen context. PK, prophylaxis, esophagitis and seizure
    reports retain clinical material and study scope; none is relabeled as direct
    PBP or efflux evidence.
  snapshot_sha256: 049a198fc89342bd5eb3e7f61ca42051515b26a116593977c1a3a2ce261e29b8
- evidence_id: adapter
  kind: database
  reference: iModulonDB e_coli/modulome
  locator: Current catalog 308-adapter-datasets.txt;315-adapter-mdtE.txt and 315-adapter-pbp.txt
  accessed_at: '2026-10-21T13:34:57Z'
  support: context_only
  summary: Both 315-specific queries preceded open mechanism research. mdtE resolves
    to b3513, with zero iModulons; the penicillin-binding query has no hits. These
    are search/catalog outcomes, not negative mechanistic evidence or drug transport
    measurements.
  snapshot_sha256: 1d057cb89c5b22a1e3342fd24ded088b5b8300ab32573758c4c418bca31a4932
- evidence_id: owners
  kind: record_content
  reference: ChEBI/ARO source tables, ARO edge tables, conf/aro_target_roles.tsv and
    seeder
  locator: 315-source-audit.json;315-lead-dispositions.json;315-320-local-hits.txt
  accessed_at: '2026-10-21T13:34:57Z'
  support: supports
  summary: Seventeen captured inputs and all five history events are unchanged. Nineteen
    names, exact structures, three roles, chemical/drug/document links and both qualified
    mechanism objects reconcile with maintained sources. The existing conf/sources.yaml
    synonym_exclusions lane can prevent regeneration of wrongly exact product names;
    a BRAND_NAME override would require an explicit maintained type mapping.
  snapshot_sha256: 8a80fbf763a2175da5ea36e32a3aa3667123c326f2b3506eb9c4ec6454079dd7
- evidence_id: validation
  kind: validation
  reference: Documented native validators and supplemental molecular/source reconciliation
  locator: 315-focused-results.json;315-schema.log;315-strict.log;315-authority-chemistry.json;315-source-audit.json
  accessed_at: '2026-10-21T13:34:57Z'
  support: supports
  summary: Schema, strict, native chemistry, tautomer-aware authority comparisons
    and source reconciliation pass. The initial direct graph comparison and initial
    adapter query failed for documented reasons and are retained as actual check outcomes.
    Required full-corpus gates remain separate.
  snapshot_sha256: 1973f9c92cb565b88c6dac5dcccbd5f844227eb325fe557a5875fe95441aa902
- evidence_id: search
  kind: search
  reference: Exact source and identifier discovery
  locator: Ignored-inclusive rg in curation,conf,scripts,data/raw for cloxacillin,CHEBI49566,ARO0000011
    and molecular key; exact MED bibliography query; official product and original
    mechanism searches
  accessed_at: '2026-10-21T13:34:57Z'
  support: context_only
  summary: 'Ignored files were included. LINCS LSM15183 remains independently unresolved:
    the direct resolver failed and the limited HMS20200624 SDF has no exact entry
    among 639 records. This is not evidence that the global LINCS identifier is invalid.
    Reaxys/Beilstein and independent CAS registry records were not obtained.'
  snapshot_sha256: 72ab9f2c0d5303d759328a4ed641783db2998cebafc0918b127373efac0cba49
  search_scope: Ignored-inclusive rg in curation,conf,scripts,data/raw for cloxacillin,CHEBI49566,ARO0000011
    and molecular key; exact MED bibliography query; official product and original
    mechanism searches
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral penam structure
  outcome: supported
  summary: The three configured centers and composition agree; standard-InChI tautomer
    reconstruction is distinguished from a true structural conflict.
  target_ids:
  - CHEBI:49566
  evidence_ids:
  - chemistry
  - authority
- assessment_id: naming
  area: nomenclature
  topic: Branded products typed as exact molecule names
  outcome: concern
  summary: Cloxapen, Orbenin, Syntarpen and Tegopen are verified sodium-product names
    and should retain product-aware typing.
  target_ids:
  - CHEBI:49566
  evidence_ids:
  - brands
  - authority
  - owners
- assessment_id: class
  area: grounding
  topic: Penicillin class, semisynthetic and antibacterial/allergen roles
  outcome: supported
  summary: Chemical graph, source terms, clinical/allergy abstracts and official products
    support these scoped classifications.
  target_ids:
  - CHEBI:49566
  evidence_ids:
  - chemistry
  - authority
  - leads
  - brands
- assessment_id: target
  area: evidence
  topic: PBP direct interaction and biological target scope
  outcome: supported
  summary: Original PBP5 acyl-enzyme structure supports interaction with a PBP family
    member. It does not by itself identify the lethal transpeptidase, and the native
    PRIMARY_EVIDENCE_NEEDED qualification remains appropriate.
  target_ids:
  - CHEBI:49566
  evidence_ids:
  - record
  - pbp
  - aro
- assessment_id: resistance
  area: evidence
  topic: MdtEF-TolC cloxacillin resistance
  outcome: supported
  summary: The 2003 exact-compound experiment supports the relation in an overexpression/TolC-dependent
    context; other substrates in 2004/2002 are not substituted.
  target_ids:
  - CHEBI:49566
  evidence_ids:
  - efflux2003
  - efflux-boundary
  - aro
- assessment_id: xref
  area: identity
  topic: External chemical, drug and document mappings
  outcome: supported
  summary: Inspected exact graphs agree; broader drug/document records remain in their
    own fields. LINCS and restricted registry bodies remain unresolved, without a
    wrong-ID conclusion.
  target_ids:
  - CHEBI:49566
  evidence_ids:
  - chemistry
  - links
  - search
- assessment_id: provenance
  area: provenance
  topic: All adopted leads, actual owners and history
  outcome: supported
  summary: Seventeen hashes, five history events and thirteen bibliography dispositions
    reconcile.
  target_ids:
  - CHEBI:49566
  evidence_ids:
  - owners
  - leads
  - validation
- assessment_id: schema
  area: schema
  topic: Focused native checks
  outcome: supported
  summary: Schema and strict checks pass; the diagnosed supplemental graph-comparison
    failure does not indicate invalid native chemistry.
  target_ids:
  - CHEBI:49566
  evidence_ids:
  - validation
  - chemistry
- assessment_id: completeness
  area: completeness
  topic: Optional mechanistic and quantitative enrichment
  outcome: supported
  summary: Bounded primary evidence could be added through separate curation. Absence
    of optional MIC, clinical status or causal graphs is not a required-field defect.
  target_ids:
  - CHEBI:49566
  evidence_ids:
  - record
  - pbp
  - efflux2003
findings:
- finding_id: F1
  issue_key: chebi-49566-branded-sodium-products-exact-synonyms
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: Four branded sodium products are typed as exact neutral-acid synonyms
  description: Cloxapen, Orbenin, Syntarpen and Tegopen are EXACT_SYNONYM entries
    on neutral cloxacillin. Official named-product documents establish sodium formulations,
    and current ChEBI explicitly calls Orbenin a brand name. These aliases are appropriate
    contextual product names but not exact molecular-form synonyms. The acid structure
    and conventional generic names are unaffected.
  target_ids:
  - CHEBI:49566
  field_paths:
  - synonyms[14].synonym_type
  - synonyms[16].synonym_type
  - synonyms[17].synonym_type
  - synonyms[18].synonym_type
  evidence_ids:
  - brands
  - authority
  - owners
  - chemistry
  rule_id: 'review-checklist: Identity and synonym accuracy'
  native_severity: Minor product-name typing gap
  normalization_reason: Product names denote the same active moiety in formulations
    but have overstrong exact chemical typing; this is not a wrong compound graph
    or invented approval finding.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained synonym_exclusions for ARO:0000011
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted product-name aliases
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Synonym typing and regeneration
actions:
- action_id: A1
  description: Use the existing ARO:0000011 synonym_exclusions configuration to prevent
    these four product names from regenerating as EXACT_SYNONYM. If retaining them,
    implement a reproducible per-source synonym-type override to emit BRAND_NAME with
    product context; do not assume that override already exists or edit generated
    YAML directly. Keep neutral cloxacillin chemistry and generic names unchanged.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:49566
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained synonym_exclusions for ARO:0000011
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted product-name aliases
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Synonym typing and regeneration
  acceptance_checks:
  - Regeneration no longer presents Cloxapen, Orbenin, Syntarpen or Tegopen as exact
    neutral-acid aliases; preserved product names use BRAND_NAME with source provenance.
  - Retain LQOLIRLGBULYKD-JKIFEVAISA-N, all three penam stereocenters and existing
    qualified mechanism/source/history objects.
  - Rerun documented schema/strict validation and required corpus gates after separately
    authorized curation.
limitations:
- Independent original records for LINCS LSM15183, Reaxys/Beilstein and CAS were not
  obtained. HMDB and direct DrugBank returned 403; DrugBank association was inspected
  through its explicitly labeled RCSB drug-context record. The limited HMS archive
  miss is not a global absence result.
- The native Methocillin S alias remains source-concordant, but its exact named-product/form
  history was not independently established; it is not included in the confirmed four-name
  finding.
- Most adopted literature leads were abstract-only. Two leads supplied no abstract.
  New current ChEBI bibliography beyond the frozen ten was not exhaustively reviewed.
- The exact cloxacillin reagent salt/batch was not independently specified in the
  inspected efflux/PBP work. Sodium product documents establish product boundaries,
  not the assay material in unrelated studies.
- The 2010 PBP5 source demonstrates a soluble carboxypeptidase acyl-enzyme complex;
  its reagent list omits an unambiguous cloxacillin preparation. Weak side-chain density
  and imported kinetic constants limit structural/kinetic inference.
- The 2003 resistance experiment uses plasmid overexpression and a sensitized laboratory
  background. It supports a bounded efflux-related phenotype, not clinical resistance
  of every organism carrying mdtEF. The 2009 YdeO full article remained subscription-restricted;
  its abstract is only corroborative.
- Standard InChI parsing reconstructs an imidic-acid tautomer; the initial direct
  bond-order comparison failed but tautomer-aware comparisons preserve the molecular
  key and stereo. The failure is retained rather than hidden.
- Initial adapter DNS lookup failed and was retried successfully. Europe PMC XML retrievals
  failed 500 but original PMC HTML succeeded; initial Syntarpen certificate validation
  failed in urllib but normal curl retrieval succeeded. Nature PDF routes returned
  HTML access/challenge content, not a paper PDF.
- Focused native checks do not replace separately recorded required full-corpus gates
  or authorize REVIEWED status.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Native records, maintained sources and history remain unchanged.
- The batch 019 RDKit interpreter was used against batch 032 native paths; native
  schema/strict checks used the batch 032 environment.
- Current structured catalog coverage was reused from 308; 315-specific queries were
  executed before primary mechanism web research.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://pmc.ncbi.nlm.nih.gov/articles/PMC182617/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC2947372/
- https://rejestry.ezdrowie.gov.pl/api/rpl/medicinal-products/10718/characteristic
tags:
- record-review
- cloxacillin
- exact-form
- product-name
```
