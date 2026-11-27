# Cefpirome: zwitterionic identity and antibacterial scope supported; clarify one acid-form synonym

- Review: 20261021T114950Z-cefpirome
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T11:39:20Z
- Finished UTC: 2026-10-21T11:49:50Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Cefpirome is correctly represented by the net-neutral 6R,7R, Z-oxime zwitterionic graph. Inspected official chemical representations agree, and primary experiments support antibacterial activity and context-dependent resistance. The two CARD entries retain their explicit database provenance. One minor nomenclature clarification is proposed: the imported systematic acid-ending synonym does not explicitly represent the carboxylate charge of this exact structure. No molecular-graph replacement or salt reassignment is warranted.

## Scope And Provenance

Entire CHEBI:3503 record, including definition, seven synonyms, three parent terms, activity role, chemical descriptors, six chemical xrefs, two drug xrefs, document link, two source concepts, two resistance entries and four history events. All five adopted citation leads were read at abstract level and dispositioned.

Selection: Queue 243; initial capture retained and actual ARO identity/resistance inputs appended before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:3503 | data/antibiotics/antibacterial/cefpirome.yaml | generated | cefpirome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:3503 | Actual focused command exited 0. |
| strict | passed | True | CHEBI:3503 | Actual focused command exited 0. |
| chemistry | passed | False | CHEBI:3503 | Actual focused command exited 0. Batch019 RDKit parsed the batch025 record and reproduced both source mints. |
| Authoritative full QC | failed | True | CHEBI:3503 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:3503 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:3503 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:3503 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:3503 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:3503 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:3503 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:3503 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:3503 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact zwitterionic cefpirome structure

identity: supported. Targets: CHEBI:3503.

The 6R,7R and Z-oxime structure, net charge, masses, source mints and inspected official cross-references are coherent. Original Figure 1 also depicts the inner salt. Salt preparations and encyclopedia identifier discrepancies do not change native identity.

### Systematic acid-ending synonym

identity: concern. Targets: CHEBI:3503.

The exact-name list contains a pyridinium/carboxylic-acid wording beside the correct carboxylate name. Resolve this literal charge-state ambiguity through source nomenclature while preserving the correct graph.

### Antibacterial filing and activity role

scope: supported. Targets: CHEBI:3503.

Exact cefpirome experiments support antibacterial activity with strain, enzyme and assay dependence. The sulfate-labelled synthesis MICs retain material scope; the adopted disk study is not a killing experiment. No native quantitative observation needs correction.

### ACC-1 and Omp36 database assertions

evidence: supported. Targets: CHEBI:3503.

Both current CARD relationships match the imported objects and their honest evidence type. ACC-1 primary experiments support elevated MICs without an exact cefpirome kinetic result. Omp36 concerns altered porin variants; primary abstract scope is preserved and mature/precursor numbering remains to be reconciled if enriched.

### All five adopted citation leads

evidence: supported. Targets: CHEBI:3503.

All available abstracts were inspected. Activity, renal toxicity and allergy/review sources are separated by actual experimental scope; none is used as general proof for every native field.

### Optional mechanism and activity enrichment

completeness: unknown. Targets: CHEBI:3503.

The seed has no quantitative activity, mode, target, producer, graph or dataset assertions. Their absence alone is not a scientific error. Any enrichment must attach exact primary evidence, preserve the salt/material and isolate context, and avoid treating generic PBP database annotations as a direct experiment.

### Maintained provenance and proposed fix

ownership: supported. Targets: CHEBI:3503.

The name belongs to ChEBI inventory/extraction/seeding. ARO resistance assertions have their own adopted edge table. Fifteen initial/appended inputs remain unchanged; no native scientific-status transition is implied.

### Focused schema and chemistry checks

schema: supported. Targets: CHEBI:3503.

All focused checks pass. Name precision and primary experimental scope require scientific review beyond deterministic validation.

## Findings

### F1: Clarify the acid-ending systematic synonym for the zwitterion

minor / open / provisional; issue key: cefpirome-systematic-acid-name-charge-qualification.

synonyms[2] explicitly contains pyridinium but ends in cepham-4-carboxylic acid, whereas the native graph, original cefpirome drawing and other systematic synonym contain carboxylate. Read literally, the acid form would carry an extra proton and net positive charge. Confirm whether a documented historical inner-salt naming convention justifies retaining this exact name; otherwise qualify or replace it with a name matching the zwitterion. This is a name-precision question, not a recommendation to alter the stored structure.

## Recommended Actions And Acceptance Checks

### A1

Resolve the systematic synonym charge qualification through the maintained source path.

- Verify whether the exact pyridinium/carboxylic-acid wording has an explicit authoritative inner-salt convention. Retain it with a justified interpretation or correct/qualify it to carboxylate as appropriate.
- Preserve the existing net-zero zwitterionic graph, two R centres, Z oxime, formula, full key and correct source mints. Do not replace it with cefpirome sulfate or a cation merely to accommodate a name.
- Reproduce any accepted correction through the ChEBI inventory/extractor/seeder, inspect the regenerated synonym list, and run focused schema/strict, chemical identity, provenance and applicable reproducibility checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/cefpirome.yaml; Entire YAML including both resistance objects and four history events. | supports | The SEEDED/EXACT record has an internally consistent zwitterionic structure and two explicitly identified CARD database resistance assertions. It does not assert MICs, exact primary targets, mode of action, producer, clinical approval, causal graph or transcriptomic dataset. Optional unpopulated fields are not treated as required-field failures. |
| source | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_resistance_edges.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; conf/sources.yaml; Exact ChEBI row 88, ARO row 356 and resistance rows 4055–4056; extraction and attach_aro_mechanism code. | supports | ChEBI supplies the chemical identity, definition, seven aliases, parent terms and antimicrobial role. ARO supplies the cephalosporin class and two exact resistance edges, whose evidence notes identify them as database assertions. The source bibliography has four ChEBI PMIDs and one ARO review PMID. The shared CHEBI:3503 prefix search also encountered fentin chloride CHEBI:35036; exact-row selection excluded that unrelated compound. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:3503; Full current visible entry: definition, structure, names, roles, outgoing/incoming relations and xrefs. | supports | The entry matches the native graph, formula C22H22N6O5S2, charge 0, masses and full key DKOQGJHPHLTOJR-WHRDSVKCSA-N. CHEBI:23066 is the cephalosporin class; CHEBI:37940 is cyclopentapyridine, both broader terms. The current entry explicitly distinguishes cefpirome sulfate by a functional-parent relationship. It retains the same acid-ending legacy IUPAC name alongside the carboxylate synonym. The current antibacterial role is additional source context; the captured seed retains its antimicrobial ancestor. |
| chemical-xrefs | https://pubchem.ncbi.nlm.nih.gov/compound/5479539; https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL65794.json; https://rest.kegg.jp/get/C11199; https://rest.kegg.jp/get/D07649; https://drugcentral.org/drugcard/553; https://card.mcmaster.ca/ontology/42781; Complete chemical responses; seven independently parsed representations from five services. | supports | ChEMBL SMILES/InChI, PubChem SMILES/InChI, KEGG MOL, DrugCentral InChI and CARD SMILES all reproduce the native full key, formula, net charge, two R stereocentres and Z oxime. KEGG D07649 explicitly maps to C11199. DrugCentral 553 supplies the matching structure through its actual /drug/553/inchi link after an incorrect /structures route returned 404; salt aliases on that page do not replace the represented graph. |
| name-charge | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/5479539/property/MolecularFormula,SMILES,InChI,InChIKey,IUPACName/JSON; https://www.ebi.ac.uk/chebi/CHEBI:3503; Official computed carboxylate name compared with native synonyms[2], synonyms[3] and explicit [n+]/[O-] graph. | partial | The exact graph contains a permanently charged pyridinium and a carboxylate. The systematic name in synonyms[2] instead terminates in carboxylic acid without an anion or inner-salt qualification. Read literally, that protonated group would not describe the net-zero graph. The other systematic synonym and PubChem name correctly say carboxylate. This is a bounded exact-name precision issue; historical acid-name usage may need explicit treatment rather than a change to the correct molecule. |
| other-identifiers | https://www.ebi.ac.uk/chebi/CHEBI:3503; https://en.wikipedia.org/wiki/Cefpirome; https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=200907062979706702; Official CAS/Reaxys attestation, encyclopedia page identity and J-GLOBAL exact substance identity. | partial | ChEBI, KEGG and CARD attest CAS84957-29-9; ChEBI attests Reaxys4241500, whose paid registry record was not inspected. J-GLOBAL reports the matching zwitterionic full key and carboxylate nomenclature. The encyclopedia link resolves to cefpirome but its displayed stereochemical identifier differs from the mutually agreeing official structures; its chemical fields were not used as authoritative correction evidence. The document link itself is not an exact structure xref. |
| card | https://card.mcmaster.ca/ontology/42781; https://card.mcmaster.ca/ontology/38215; https://card.mcmaster.ca/ontology/39969; Full identity, definition, parent/subterm, resistance-model and publication sections. | supports | ARO:3004726 is cefpirome under the fourth-generation cephalosporin class and broader ARO:0000032. ACC-1 ARO:3001815 explicitly confers cefpirome resistance through antibiotic inactivation. Omp36 ARO:3003385 explicitly concerns mutant forms with reduced permeability; its model names G133D, not arbitrary wild-type Omp36. Both native objects accurately identify their evidence as database assertions. The current pages provide specific primary leads but are not themselves primary experiments. |
| adapter | kg-microbe-sources imodulondb --timeout 15 datasets; Structured catalog command before web research, using PYTHONDONTWRITEBYTECODE=1. | context_only | An initial sandbox DNS failure was retained; an approved read-only retry returned the public catalog. No Klebsiella aerogenes, Klebsiella pneumoniae or Hafnia dataset matched the native porin or ACC-1 context. A generic E. coli dataset was not treated as a matching clinical/heterologous ACC-1 experiment. No relevant module was queried or used; catalog noncoverage is not negative biological evidence. |
| synthesis | PMID:3142844; https://doi.org/10.7164/antibiotics.41.1374; Selected original pages: introduction/chemistry and antibacterial discussion 1374–1377; Figure 1 and Table 1 on 1374/1378 visually inspected; table footnotes. | supports | The original paper identifies cefpirome as HR810/II-1 and draws the pyridinium+/carboxylate− structure. The synthesis distinguishes dihydroiodide and sulfate preparations. Table 1 labels tested compound 1 cefpirome sulfate; serial-dilution MICs use Mueller-Hinton medium and 5 × 10^4 CFU/mL. Its reported 0.31 µg/mL for S. aureus SG511 and 1.56 µg/mL for P. aeruginosa1771 are salt-material observations, not unqualified new MICs for an isolated zwitterionic solid. No related analogue result was transferred to cefpirome. |
| activity-stability | PMID:3492175; https://doi.org/10.1128/AAC.30.5.713; https://pmc.ncbi.nlm.nih.gov/articles/PMC176519/?page=1; All six original scanned pages 713–718 personally read, including Methods and Tables 1–5. | supports | Hoechst cefpirome was tested by agar dilution in modified Mueller-Hinton medium with about 10^4 CFU per spot, 18–20 h at 37°C. Table 3 reports strain-dependent activity, including E. coli GN5482 at 0.1 µg/mL and E. cloacae GN7471 at 0.78 µg/mL. Stability and enzyme affinity vary with beta-lactamase source; some hydrolysis occurs, including type Va/b and Bacteroides preparations. Proposed penetration or target-affinity contributions are not direct measurements in this paper. Its material counterion is unspecified. The native definition does not contain a universal stability claim. |
| acc1-primary | PMID:10428914; https://doi.org/10.1128/AAC.43.8.1924; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC89392/; Entire main article text, Methods, Tables 1–4 and figure captions; exact cefpirome row in Table 2. | supports | The cloned ACC-1 experiment raises cefpirome MIC in E. coli MV1190 from 0.03 to 1 µg/mL; the transconjugant comparison is 0.03 to 0.25 µg/mL and the clinical K. pneumoniae KUS value is 4 µg/mL. These are reduced-susceptibility observations in specified host/vector backgrounds, not a modern breakpoint assertion. Table 3 has no cefpirome kinetic row, so an exact cefpirome hydrolysis rate is not established here. The native database mechanism remains qualified. The correct PMCID was verified through the PubMed index; a mistakenly fetched unrelated PMC89395 page was excluded. |
| omp36-primary | PMID:15081418; https://doi.org/10.1016/j.bbrc.2004.03.130; Complete indexed original abstract; public full-text routes attempted but not successfully inspected. | partial | The study identifies Gly112Asp in the conserved L3 region of Omp36 from clinical Enterobacter aerogenes strains C and 3, associated with high beta-lactam resistance and previously characterized altered pore properties. The paper title includes cefpirome. CARD labels the full-sequence variant G133D; these positions should be reconciled with signal-peptide/mature-protein numbering before variant-level enrichment, rather than assumed to be contradictory. The abstract does not supply the exact cefpirome MIC table or an isolated causal reconstruction. |
| adopted-activity | PMID:1287135; https://doi.org/10.1080/1120009X.1992.11739188; PMID:26004702; Complete indexed abstracts of both adopted studies. | supports | 1287135 reports agar-dilution activity in 100 E. faecalis and 100 staphylococcal isolates, with substantial mec-status-dependent variation; population MIC50/MIC90 values are not single-strain observations. 26004702 evaluates 141 clinical isolates by Kirby-Bauer disk diffusion. Its use of bactericidal wording does not turn disk inhibition into a killing assay. Both support antibacterial context but their full Methods and material identities were not inspected. |
| adopted-host | PMID:26870331; https://doi.org/10.3892/br.2015.528; Complete indexed abstract. | context_only | The study concerns renal cell viability and clinical serum creatinine during cefepime/cefpirome treatment. Its IC50 is a host-cell toxicity measurement, not a bacterial MIC or a microbial target assay. No renal or target claim was introduced into the record. |
| adopted-reviews | PMID:29017833; https://doi.org/10.1016/j.jaip.2017.08.027; PMID:9211085; https://doi.org/10.2165/00003495-199754010-00013; Complete indexed abstracts of both reviews. | context_only | 29017833 reviews beta-lactam allergy and cross-reactivity. 9211085 is the ARO-linked cefpirome pharmacology/clinical review. These are useful source-context leads, not primary microbial target, resistance or regulatory evidence. The review definition does not justify universal susceptibility or an unqualified approval assertion. |
| search | 243-inclusive-file-hits.txt; exact public drug/source queries on 2026-10-21; Exact identifier/name/key and bounded source-paper searches. | context_only | Hidden and ignored files were included across the declared repository areas. The search located native/raw rows, queue/path locks and generated mappings, with no exact curator overlay or corrective decision found. A prefix collision with fentin chloride was recognized and excluded from exact-target assessment. Public searches located primary synthesis/activity papers and official identity records; no universal absence claim was made. |
| validation | 243-focused-results.json; 243-chemistry.json; 243-external-chemistry.json; Actual focused commands and independent chemical parses. | supports | Schema, strict and chemistry commands exit 0. Native chemical representations and source mints agree. Seven independently parsed official representations from five services agree in exact full key, formula, charge and stereochemistry. |

## Limits And Additional Notes

- All native fields and exact maintained source rows were read. The original thirteen input hashes were preserved and two actual ARO inputs appended before assessment; all fifteen remain unchanged.
- The 1986 antibacterial/stability paper was read from all six original scans. The synthesis paper was read selectively for chemistry, Figure 1, Table 1 and associated activity discussion; its full experimental section and all analogue tables were not read. Its quantitative cefpirome table explicitly uses sulfate.
- The ACC-1 main article text and tables were read through the verified legacy PMC URL after current URLs challenged. A preliminary unrelated PMC89395 page was recognized by title and excluded; the actual source is PMC89392. Cefpirome kinetic measurements are absent from its Table 3, despite the verified elevated-MIC phenotype.
- The complete Omp36 abstract was inspected; publisher and public-copy routes did not yield an inspected full text. Exact cefpirome MIC values and the mature-versus-precursor numbering reconciliation remain bounded limitations. The current CARD model identifies mutant rather than wild-type porin scope.
- All five adopted citation abstracts were read. Full papers for PMID1287135 and PMID26004702 and the full renal study/reviews were not inspected. No host-cell IC50, disk inhibition, review claim or salt result was converted into an unqualified native MIC or microbial target assertion.
- The acid-ending systematic synonym finding is provisional because legacy naming conventions may explain the wording. Its literal charge ambiguity merits source-level clarification without treating the coherent graph as wrong.
- CAS and Reaxys numbers were checked against official public cross-reference attestations; paid registry contents were not accessed. DrugCentral structure retrieval succeeded through the page’s actual InChI link. The Wikipedia page is not used as authoritative chemical evidence.
- The iModulonDB catalog was inspected before web research; no matching native organism dataset was applicable. No expression module or dataset assertion informed the verdict. Optional missing fields are not required-field errors; native status remains SEEDED.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T114950Z-cefpirome
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cefpirome: zwitterionic identity and antibacterial scope supported; clarify
  one acid-form synonym'
started_at: '2026-10-21T11:39:20Z'
finished_at: '2026-10-21T11:49:50Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author the seed. Preserved initial inputs, inspected
    the entire native record and maintained source rows before assessment, independently
    parsed official chemical representations and read original chemical/activity and
    resistance evidence.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'Cefpirome is correctly represented by the net-neutral 6R,7R, Z-oxime zwitterionic
  graph. Inspected official chemical representations agree, and primary experiments
  support antibacterial activity and context-dependent resistance. The two CARD entries
  retain their explicit database provenance. One minor nomenclature clarification
  is proposed: the imported systematic acid-ending synonym does not explicitly represent
  the carboxylate charge of this exact structure. No molecular-graph replacement or
  salt reassignment is warranted.'
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
  - path: data/antibiotics/antibacterial/cefpirome.yaml
    sha256: 3b1380a7084ed7473372af6fb56014c2e642063d4f7179a47a0a44f167e0b4ed
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
targets:
- target_id: CHEBI:3503
  path: data/antibiotics/antibacterial/cefpirome.yaml
  label: cefpirome
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
    role: Adopted ARO identity and bibliography
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Adopted ARO resistance assertions
scope:
  description: Entire CHEBI:3503 record, including definition, seven synonyms, three
    parent terms, activity role, chemical descriptors, six chemical xrefs, two drug
    xrefs, document link, two source concepts, two resistance entries and four history
    events. All five adopted citation leads were read at abstract level and dispositioned.
  selection: Queue 243; initial capture retained and actual ARO identity/resistance
    inputs appended before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:3503
  exclusions:
  - target: Cefpirome sulfate, other salts, conjugate ions, stereoisomers and related
      cephalosporins
    reason: The native record is the zwitterion. A salt-labelled quantitative experiment
      can support active-moiety context but must retain the exact tested material
      if curated.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Actual focused command exited 0.
  target_ids:
  - CHEBI:3503
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefpirome.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Actual focused command exited 0.
  target_ids:
  - CHEBI:3503
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefpirome.yaml --out /private/tmp/am-review-session/243-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Actual focused command exited 0. Batch019 RDKit parsed the batch025 record
    and reproduced both source mints.
  target_ids:
  - CHEBI:3503
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 243
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
  - CHEBI:3503
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
  - CHEBI:3503
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
  - CHEBI:3503
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
  - CHEBI:3503
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
  - CHEBI:3503
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
  - CHEBI:3503
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
  - CHEBI:3503
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
  - CHEBI:3503
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
  - CHEBI:3503
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/cefpirome.yaml
  locator: Entire YAML including both resistance objects and four history events.
  accessed_at: '2026-10-21T11:47:59Z'
  support: supports
  summary: The SEEDED/EXACT record has an internally consistent zwitterionic structure
    and two explicitly identified CARD database resistance assertions. It does not
    assert MICs, exact primary targets, mode of action, producer, clinical approval,
    causal graph or transcriptomic dataset. Optional unpopulated fields are not treated
    as required-field failures.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_resistance_edges.tsv;
    scripts/extract_source_inventory.py; scripts/seed_from_sources.py; conf/sources.yaml
  locator: Exact ChEBI row 88, ARO row 356 and resistance rows 4055–4056; extraction
    and attach_aro_mechanism code.
  accessed_at: '2026-10-21T11:47:59Z'
  support: supports
  summary: ChEBI supplies the chemical identity, definition, seven aliases, parent
    terms and antimicrobial role. ARO supplies the cephalosporin class and two exact
    resistance edges, whose evidence notes identify them as database assertions. The
    source bibliography has four ChEBI PMIDs and one ARO review PMID. The shared CHEBI:3503
    prefix search also encountered fentin chloride CHEBI:35036; exact-row selection
    excluded that unrelated compound.
  snapshot_sha256: b20a2acfbec577122d29bc8aa1d32360a6ae4468d0f9462c81c21ffa9576ae69
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:3503
  locator: 'Full current visible entry: definition, structure, names, roles, outgoing/incoming
    relations and xrefs.'
  accessed_at: '2026-10-21T11:47:59Z'
  support: supports
  summary: The entry matches the native graph, formula C22H22N6O5S2, charge 0, masses
    and full key DKOQGJHPHLTOJR-WHRDSVKCSA-N. CHEBI:23066 is the cephalosporin class;
    CHEBI:37940 is cyclopentapyridine, both broader terms. The current entry explicitly
    distinguishes cefpirome sulfate by a functional-parent relationship. It retains
    the same acid-ending legacy IUPAC name alongside the carboxylate synonym. The
    current antibacterial role is additional source context; the captured seed retains
    its antimicrobial ancestor.
  snapshot_sha256: 23a6908a8c3f978423ca1d1522dd65dc00aa2fa4017e8bff4870a7347e760e11
- evidence_id: chemical-xrefs
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/5479539; https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL65794.json;
    https://rest.kegg.jp/get/C11199; https://rest.kegg.jp/get/D07649; https://drugcentral.org/drugcard/553;
    https://card.mcmaster.ca/ontology/42781
  locator: Complete chemical responses; seven independently parsed representations
    from five services.
  accessed_at: '2026-10-21T11:47:59Z'
  support: supports
  summary: ChEMBL SMILES/InChI, PubChem SMILES/InChI, KEGG MOL, DrugCentral InChI
    and CARD SMILES all reproduce the native full key, formula, net charge, two R
    stereocentres and Z oxime. KEGG D07649 explicitly maps to C11199. DrugCentral
    553 supplies the matching structure through its actual /drug/553/inchi link after
    an incorrect /structures route returned 404; salt aliases on that page do not
    replace the represented graph.
  snapshot_sha256: eb8a33ac0efdcf43f1fa5172a0b3eee4f15a0f26ebc6166cad63e3ee245f1d2d
- evidence_id: name-charge
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/5479539/property/MolecularFormula,SMILES,InChI,InChIKey,IUPACName/JSON;
    https://www.ebi.ac.uk/chebi/CHEBI:3503
  locator: Official computed carboxylate name compared with native synonyms[2], synonyms[3]
    and explicit [n+]/[O-] graph.
  accessed_at: '2026-10-21T11:47:59Z'
  support: partial
  summary: The exact graph contains a permanently charged pyridinium and a carboxylate.
    The systematic name in synonyms[2] instead terminates in carboxylic acid without
    an anion or inner-salt qualification. Read literally, that protonated group would
    not describe the net-zero graph. The other systematic synonym and PubChem name
    correctly say carboxylate. This is a bounded exact-name precision issue; historical
    acid-name usage may need explicit treatment rather than a change to the correct
    molecule.
  snapshot_sha256: 9fabbb9a3b5a34df0cbff86628709c2112ad95766121c1d5ad2122423b1891ae
- evidence_id: other-identifiers
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:3503; https://en.wikipedia.org/wiki/Cefpirome;
    https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=200907062979706702
  locator: Official CAS/Reaxys attestation, encyclopedia page identity and J-GLOBAL
    exact substance identity.
  accessed_at: '2026-10-21T11:47:59Z'
  support: partial
  summary: ChEBI, KEGG and CARD attest CAS84957-29-9; ChEBI attests Reaxys4241500,
    whose paid registry record was not inspected. J-GLOBAL reports the matching zwitterionic
    full key and carboxylate nomenclature. The encyclopedia link resolves to cefpirome
    but its displayed stereochemical identifier differs from the mutually agreeing
    official structures; its chemical fields were not used as authoritative correction
    evidence. The document link itself is not an exact structure xref.
  snapshot_sha256: 89d7c54d161ef0c1a4c3e60a0e37f134ddc6697928a1bea1e70c0a88866e2a34
- evidence_id: card
  kind: database
  reference: https://card.mcmaster.ca/ontology/42781; https://card.mcmaster.ca/ontology/38215;
    https://card.mcmaster.ca/ontology/39969
  locator: Full identity, definition, parent/subterm, resistance-model and publication
    sections.
  accessed_at: '2026-10-21T11:47:59Z'
  support: supports
  summary: ARO:3004726 is cefpirome under the fourth-generation cephalosporin class
    and broader ARO:0000032. ACC-1 ARO:3001815 explicitly confers cefpirome resistance
    through antibiotic inactivation. Omp36 ARO:3003385 explicitly concerns mutant
    forms with reduced permeability; its model names G133D, not arbitrary wild-type
    Omp36. Both native objects accurately identify their evidence as database assertions.
    The current pages provide specific primary leads but are not themselves primary
    experiments.
  snapshot_sha256: 4011dad9e09e71677fa6b926c267c9c959102b03411441f94fae52ef0723407d
- evidence_id: adapter
  kind: database
  reference: kg-microbe-sources imodulondb --timeout 15 datasets
  locator: Structured catalog command before web research, using PYTHONDONTWRITEBYTECODE=1.
  accessed_at: '2026-10-21T11:47:59Z'
  support: context_only
  summary: An initial sandbox DNS failure was retained; an approved read-only retry
    returned the public catalog. No Klebsiella aerogenes, Klebsiella pneumoniae or
    Hafnia dataset matched the native porin or ACC-1 context. A generic E. coli dataset
    was not treated as a matching clinical/heterologous ACC-1 experiment. No relevant
    module was queried or used; catalog noncoverage is not negative biological evidence.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: synthesis
  kind: primary_source
  reference: PMID:3142844; https://doi.org/10.7164/antibiotics.41.1374
  locator: 'Selected original pages: introduction/chemistry and antibacterial discussion
    1374–1377; Figure 1 and Table 1 on 1374/1378 visually inspected; table footnotes.'
  accessed_at: '2026-10-21T11:47:59Z'
  support: supports
  summary: The original paper identifies cefpirome as HR810/II-1 and draws the pyridinium+/carboxylate−
    structure. The synthesis distinguishes dihydroiodide and sulfate preparations.
    Table 1 labels tested compound 1 cefpirome sulfate; serial-dilution MICs use Mueller-Hinton
    medium and 5 × 10^4 CFU/mL. Its reported 0.31 µg/mL for S. aureus SG511 and 1.56
    µg/mL for P. aeruginosa1771 are salt-material observations, not unqualified new
    MICs for an isolated zwitterionic solid. No related analogue result was transferred
    to cefpirome.
  snapshot_sha256: 85ab1ce580bbe651ca259fca5bf6c62eee856acf0c997f284a8b00937b649a98
- evidence_id: activity-stability
  kind: primary_source
  reference: PMID:3492175; https://doi.org/10.1128/AAC.30.5.713; https://pmc.ncbi.nlm.nih.gov/articles/PMC176519/?page=1
  locator: All six original scanned pages 713–718 personally read, including Methods
    and Tables 1–5.
  accessed_at: '2026-10-21T11:47:59Z'
  support: supports
  summary: Hoechst cefpirome was tested by agar dilution in modified Mueller-Hinton
    medium with about 10^4 CFU per spot, 18–20 h at 37°C. Table 3 reports strain-dependent
    activity, including E. coli GN5482 at 0.1 µg/mL and E. cloacae GN7471 at 0.78
    µg/mL. Stability and enzyme affinity vary with beta-lactamase source; some hydrolysis
    occurs, including type Va/b and Bacteroides preparations. Proposed penetration
    or target-affinity contributions are not direct measurements in this paper. Its
    material counterion is unspecified. The native definition does not contain a universal
    stability claim.
  snapshot_sha256: 15b6a552693681dc00575f2973e995d498ac21111b073cd4d0e67b2a0d6c2b76
- evidence_id: acc1-primary
  kind: primary_source
  reference: PMID:10428914; https://doi.org/10.1128/AAC.43.8.1924; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC89392/
  locator: Entire main article text, Methods, Tables 1–4 and figure captions; exact
    cefpirome row in Table 2.
  accessed_at: '2026-10-21T11:47:59Z'
  support: supports
  summary: The cloned ACC-1 experiment raises cefpirome MIC in E. coli MV1190 from
    0.03 to 1 µg/mL; the transconjugant comparison is 0.03 to 0.25 µg/mL and the clinical
    K. pneumoniae KUS value is 4 µg/mL. These are reduced-susceptibility observations
    in specified host/vector backgrounds, not a modern breakpoint assertion. Table
    3 has no cefpirome kinetic row, so an exact cefpirome hydrolysis rate is not established
    here. The native database mechanism remains qualified. The correct PMCID was verified
    through the PubMed index; a mistakenly fetched unrelated PMC89395 page was excluded.
  snapshot_sha256: 81357cbe7cb11b4194633083f5b11841588efac9ebcb18f4bcf3eafc20ae9a80
- evidence_id: omp36-primary
  kind: primary_source
  reference: PMID:15081418; https://doi.org/10.1016/j.bbrc.2004.03.130
  locator: Complete indexed original abstract; public full-text routes attempted but
    not successfully inspected.
  accessed_at: '2026-10-21T11:47:59Z'
  support: partial
  summary: The study identifies Gly112Asp in the conserved L3 region of Omp36 from
    clinical Enterobacter aerogenes strains C and 3, associated with high beta-lactam
    resistance and previously characterized altered pore properties. The paper title
    includes cefpirome. CARD labels the full-sequence variant G133D; these positions
    should be reconciled with signal-peptide/mature-protein numbering before variant-level
    enrichment, rather than assumed to be contradictory. The abstract does not supply
    the exact cefpirome MIC table or an isolated causal reconstruction.
  snapshot_sha256: 163da2cae36daf123356f81ad0dfacac51db3c3f324927202bb4988a945186f6
- evidence_id: adopted-activity
  kind: primary_source
  reference: PMID:1287135; https://doi.org/10.1080/1120009X.1992.11739188; PMID:26004702
  locator: Complete indexed abstracts of both adopted studies.
  accessed_at: '2026-10-21T11:47:59Z'
  support: supports
  summary: 1287135 reports agar-dilution activity in 100 E. faecalis and 100 staphylococcal
    isolates, with substantial mec-status-dependent variation; population MIC50/MIC90
    values are not single-strain observations. 26004702 evaluates 141 clinical isolates
    by Kirby-Bauer disk diffusion. Its use of bactericidal wording does not turn disk
    inhibition into a killing assay. Both support antibacterial context but their
    full Methods and material identities were not inspected.
  snapshot_sha256: 1da6ddfc0b6627867ef4915d399296ad8885608b66ec59b5acb52bb3c3069c38
- evidence_id: adopted-host
  kind: primary_source
  reference: PMID:26870331; https://doi.org/10.3892/br.2015.528
  locator: Complete indexed abstract.
  accessed_at: '2026-10-21T11:47:59Z'
  support: context_only
  summary: The study concerns renal cell viability and clinical serum creatinine during
    cefepime/cefpirome treatment. Its IC50 is a host-cell toxicity measurement, not
    a bacterial MIC or a microbial target assay. No renal or target claim was introduced
    into the record.
  snapshot_sha256: 1da6ddfc0b6627867ef4915d399296ad8885608b66ec59b5acb52bb3c3069c38
- evidence_id: adopted-reviews
  kind: database
  reference: PMID:29017833; https://doi.org/10.1016/j.jaip.2017.08.027; PMID:9211085;
    https://doi.org/10.2165/00003495-199754010-00013
  locator: Complete indexed abstracts of both reviews.
  accessed_at: '2026-10-21T11:47:59Z'
  support: context_only
  summary: 29017833 reviews beta-lactam allergy and cross-reactivity. 9211085 is the
    ARO-linked cefpirome pharmacology/clinical review. These are useful source-context
    leads, not primary microbial target, resistance or regulatory evidence. The review
    definition does not justify universal susceptibility or an unqualified approval
    assertion.
  snapshot_sha256: 1da6ddfc0b6627867ef4915d399296ad8885608b66ec59b5acb52bb3c3069c38
- evidence_id: search
  kind: search
  reference: 243-inclusive-file-hits.txt; exact public drug/source queries on 2026-10-21
  locator: Exact identifier/name/key and bounded source-paper searches.
  accessed_at: '2026-10-21T11:47:59Z'
  support: context_only
  summary: Hidden and ignored files were included across the declared repository areas.
    The search located native/raw rows, queue/path locks and generated mappings, with
    no exact curator overlay or corrective decision found. A prefix collision with
    fentin chloride was recognized and excluded from exact-target assessment. Public
    searches located primary synthesis/activity papers and official identity records;
    no universal absence claim was made.
  snapshot_sha256: 1e8a721753a289fbe2cd13681bb91231af7d018b502d9050c1383437a6d125d4
  search_scope: rg --no-ignore --hidden over data, curation, conf, scripts, src, docs,
    .claude, reviews and reports for cefpirome, CHEBI:3503, full key and source mint;
    public cefpirome/HR810, exact PMIDs/DOIs, ACC-1 and Omp36 searches.
- evidence_id: validation
  kind: validation
  reference: 243-focused-results.json; 243-chemistry.json; 243-external-chemistry.json
  locator: Actual focused commands and independent chemical parses.
  accessed_at: '2026-10-21T11:47:59Z'
  support: supports
  summary: Schema, strict and chemistry commands exit 0. Native chemical representations
    and source mints agree. Seven independently parsed official representations from
    five services agree in exact full key, formula, charge and stereochemistry.
  snapshot_sha256: 2a28516ea38bc94a48599688a3f8ae1309134873752bc9d02a5e36ece746935d
assessments:
- assessment_id: identity
  area: identity
  topic: Exact zwitterionic cefpirome structure
  outcome: supported
  summary: The 6R,7R and Z-oxime structure, net charge, masses, source mints and inspected
    official cross-references are coherent. Original Figure 1 also depicts the inner
    salt. Salt preparations and encyclopedia identifier discrepancies do not change
    native identity.
  target_ids:
  - CHEBI:3503
  evidence_ids:
  - chebi
  - chemical-xrefs
  - synthesis
  - other-identifiers
  - validation
- assessment_id: names
  area: identity
  topic: Systematic acid-ending synonym
  outcome: concern
  summary: The exact-name list contains a pyridinium/carboxylic-acid wording beside
    the correct carboxylate name. Resolve this literal charge-state ambiguity through
    source nomenclature while preserving the correct graph.
  target_ids:
  - CHEBI:3503
  evidence_ids:
  - record
  - chebi
  - name-charge
  - synthesis
- assessment_id: activity
  area: scope
  topic: Antibacterial filing and activity role
  outcome: supported
  summary: Exact cefpirome experiments support antibacterial activity with strain,
    enzyme and assay dependence. The sulfate-labelled synthesis MICs retain material
    scope; the adopted disk study is not a killing experiment. No native quantitative
    observation needs correction.
  target_ids:
  - CHEBI:3503
  evidence_ids:
  - activity-stability
  - synthesis
  - adopted-activity
  - source
- assessment_id: resistance
  area: evidence
  topic: ACC-1 and Omp36 database assertions
  outcome: supported
  summary: Both current CARD relationships match the imported objects and their honest
    evidence type. ACC-1 primary experiments support elevated MICs without an exact
    cefpirome kinetic result. Omp36 concerns altered porin variants; primary abstract
    scope is preserved and mature/precursor numbering remains to be reconciled if
    enriched.
  target_ids:
  - CHEBI:3503
  evidence_ids:
  - card
  - acc1-primary
  - omp36-primary
  - adapter
- assessment_id: citations
  area: evidence
  topic: All five adopted citation leads
  outcome: supported
  summary: All available abstracts were inspected. Activity, renal toxicity and allergy/review
    sources are separated by actual experimental scope; none is used as general proof
    for every native field.
  target_ids:
  - CHEBI:3503
  evidence_ids:
  - adopted-activity
  - adopted-host
  - adopted-reviews
- assessment_id: completeness
  area: completeness
  topic: Optional mechanism and activity enrichment
  outcome: unknown
  summary: The seed has no quantitative activity, mode, target, producer, graph or
    dataset assertions. Their absence alone is not a scientific error. Any enrichment
    must attach exact primary evidence, preserve the salt/material and isolate context,
    and avoid treating generic PBP database annotations as a direct experiment.
  target_ids:
  - CHEBI:3503
  evidence_ids:
  - record
  - synthesis
  - activity-stability
  - acc1-primary
  - omp36-primary
- assessment_id: ownership
  area: ownership
  topic: Maintained provenance and proposed fix
  outcome: supported
  summary: The name belongs to ChEBI inventory/extraction/seeding. ARO resistance
    assertions have their own adopted edge table. Fifteen initial/appended inputs
    remain unchanged; no native scientific-status transition is implied.
  target_ids:
  - CHEBI:3503
  evidence_ids:
  - source
  - search
  - validation
- assessment_id: gates
  area: schema
  topic: Focused schema and chemistry checks
  outcome: supported
  summary: All focused checks pass. Name precision and primary experimental scope
    require scientific review beyond deterministic validation.
  target_ids:
  - CHEBI:3503
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: cefpirome-systematic-acid-name-charge-qualification
  category: identity
  severity: minor
  status: open
  certainty: provisional
  title: Clarify the acid-ending systematic synonym for the zwitterion
  description: synonyms[2] explicitly contains pyridinium but ends in cepham-4-carboxylic
    acid, whereas the native graph, original cefpirome drawing and other systematic
    synonym contain carboxylate. Read literally, the acid form would carry an extra
    proton and net positive charge. Confirm whether a documented historical inner-salt
    naming convention justifies retaining this exact name; otherwise qualify or replace
    it with a name matching the zwitterion. This is a name-precision question, not
    a recommendation to alter the stored structure.
  target_ids:
  - CHEBI:3503
  field_paths:
  - synonyms[2].synonym_text
  evidence_ids:
  - record
  - chebi
  - name-charge
  - chemical-xrefs
  - synthesis
  rule_id: 'native-review-checklist: exact synonym and charge-form consistency'
  native_severity: minor
  normalization_reason: A bounded inherited nomenclature ambiguity. The entire molecular
    graph and official exact identifiers agree; possible historical acid-name usage
    is preserved as an unresolved qualification rather than asserted to be a different
    molecule.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted exact synonym source
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reproducible source nomenclature extraction or qualified correction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated synonym owner
actions:
- action_id: A1
  description: Resolve the systematic synonym charge qualification through the maintained
    source path.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:3503
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted exact synonym source
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reproducible source nomenclature extraction or qualified correction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated synonym owner
  acceptance_checks:
  - Verify whether the exact pyridinium/carboxylic-acid wording has an explicit authoritative
    inner-salt convention. Retain it with a justified interpretation or correct/qualify
    it to carboxylate as appropriate.
  - Preserve the existing net-zero zwitterionic graph, two R centres, Z oxime, formula,
    full key and correct source mints. Do not replace it with cefpirome sulfate or
    a cation merely to accommodate a name.
  - Reproduce any accepted correction through the ChEBI inventory/extractor/seeder,
    inspect the regenerated synonym list, and run focused schema/strict, chemical
    identity, provenance and applicable reproducibility checks after separately authorized
    curation.
limitations:
- All native fields and exact maintained source rows were read. The original thirteen
  input hashes were preserved and two actual ARO inputs appended before assessment;
  all fifteen remain unchanged.
- The 1986 antibacterial/stability paper was read from all six original scans. The
  synthesis paper was read selectively for chemistry, Figure 1, Table 1 and associated
  activity discussion; its full experimental section and all analogue tables were
  not read. Its quantitative cefpirome table explicitly uses sulfate.
- The ACC-1 main article text and tables were read through the verified legacy PMC
  URL after current URLs challenged. A preliminary unrelated PMC89395 page was recognized
  by title and excluded; the actual source is PMC89392. Cefpirome kinetic measurements
  are absent from its Table 3, despite the verified elevated-MIC phenotype.
- The complete Omp36 abstract was inspected; publisher and public-copy routes did
  not yield an inspected full text. Exact cefpirome MIC values and the mature-versus-precursor
  numbering reconciliation remain bounded limitations. The current CARD model identifies
  mutant rather than wild-type porin scope.
- All five adopted citation abstracts were read. Full papers for PMID1287135 and PMID26004702
  and the full renal study/reviews were not inspected. No host-cell IC50, disk inhibition,
  review claim or salt result was converted into an unqualified native MIC or microbial
  target assertion.
- The acid-ending systematic synonym finding is provisional because legacy naming
  conventions may explain the wording. Its literal charge ambiguity merits source-level
  clarification without treating the coherent graph as wrong.
- CAS and Reaxys numbers were checked against official public cross-reference attestations;
  paid registry contents were not accessed. DrugCentral structure retrieval succeeded
  through the page’s actual InChI link. The Wikipedia page is not used as authoritative
  chemical evidence.
- The iModulonDB catalog was inspected before web research; no matching native organism
  dataset was applicable. No expression module or dataset assertion informed the verdict.
  Optional missing fields are not required-field errors; native status remains SEEDED.
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
