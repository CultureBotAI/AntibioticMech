# Cefamandole: coherent neutral identity; qualify salt-dependent activity and OmpK35 loss

- Review: 20261021T110855Z-cefamandole
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:55:27Z
- Finished UTC: 2026-10-21T11:08:55Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The neutral cefamandole identity and source provenance are coherent, and all focused validators pass. The CARD reduced-permeability assertion has a real OmpK35-loss context but remains explicitly a database assertion. Original antibacterial papers support the active moiety while requiring salt, assay and population qualifications. One informational finding identifies a bounded evidence-enrichment route; no required identity or role correction is established. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole CHEBI:3480 record, including definition, all eleven synonyms, three parents, two roles, class, structure descriptors, six chemical xrefs, three drug xrefs, five document xrefs, two source concepts, one resistance mechanism and four history events; all five adopted citation leads.

Selection: Queue 211; original capture preserved and actual ARO owner inputs appended.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:3480 | data/antibiotics/antibacterial/cefamandole.yaml | generated | cefamandole |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:3480 | Actual focused command exited 0. |
| strict | passed | True | CHEBI:3480 | Actual focused command exited 0. |
| chemistry | passed | False | CHEBI:3480 | Actual focused command exited 0. Batch022 lacks RDKit; batch019 interpreter was used against batch022 inputs. |
| Authoritative full QC | failed | True | CHEBI:3480 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:3480 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:3480 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:3480 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:3480 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:3480 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:3480 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:3480 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:3480 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Neutral structure, synonyms, ontology and xrefs

identity: supported. Targets: CHEBI:3480.

The exact neutral identity is coherent across adopted and inspected official chemical sources. The historical L-Cefamandole alias is source-attested; its text alone is insufficient to infer a distinct opposite stereoisomer. Patent and subscription-registry verification remain bounded.

### Maintained inputs and generated ownership

provenance: supported. Targets: CHEBI:3480.

The merged ChEBI/ARO source provenance and history are coherent. Source-owned resistance qualifications have an established maintained overlay; primary native additions belong to the exact native record.

### Antibacterial role and exact supplied material

quantity: supported. Targets: CHEBI:3480.

Inspected primary studies support cefamandole antibacterial activity with explicit sodium or unresolved material-form qualifications. They do not demonstrate that every measurement used neutral free acid. No native numerical assay currently overstates that distinction.

### OmpK35 database assertion

scope: supported. Targets: CHEBI:3480.

The imported assertion has a supported loss-of-entry-porin interpretation. The native database caveat avoids a false primary-evidence claim; qualification and narrow primary evidence would improve it.

### Optional PBP, spectrum and graph content

completeness: unknown. Targets: CHEBI:3480.

No exact PBP binding experiment was independently verified. Hydrolysis and porin-loss results should not be repurposed as direct target binding, and allergy studies do not supply antibacterial mechanisms. Missing optional fields are not errors.

### Deterministic checks

schema: supported. Targets: CHEBI:3480.

Actual focused schema, strict and chemistry checks pass without implying scientific status promotion.

## Findings

### F1: Qualify OmpK35 loss and preserve material-form limits when adding primary evidence

informational / open / confirmed; issue key: cefamandole-qualified-primary-evidence-enrichment.

The coherent seeded record could be strengthened by a maintained OmpK35-loss qualification and narrow primary activity evidence. The existing database caveat is honest, so this is an optional enrichment opportunity rather than an unsupported role or compulsory missing-field defect. Related salt/prodrug studies and population summaries require explicit scope.

## Recommended Actions And Acceptance Checks

### A1

Add bounded evidence qualifications through the correct maintained owner and curate only exact supported observations.

- Use the maintained CARD evidence overlay for the imported edge and preserve its database status. Make the loss-of-porin interpretation explicit; do not relabel the ordinary porin as a direct inhibitory target or its presence as the resistance-causing state.
- Any primary susceptibility observation must retain the exact genotype, assay and endpoint, without converting a twofold shift to a clinical resistant category or transferring direct permeability measurements from other drugs. Resolve supplied material where an exact chemical-form claim requires it.
- For older activity data, preserve the explicit sodium material in the 1973 study and unresolved supplied form in the 1974 study. Keep cumulative population results separate from individual strain MICs, and distinguish MIC, MBC and hydrolysis assays.
- Do not infer direct PBP binding from drug databases, beta-lactam class membership or antibody epitopes. Inspect an exact primary target experiment before adding a protein target or causal binding edge.
- Apply separately authorized native additions with write_validated_antibiotic and record_curation_event, preserve provenance, and run focused and applicable shared gates after any overlay or curation change.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/cefamandole.yaml; Complete native YAML and all history events. | supports | SEEDED/EXACT neutral cefamandole has one REDUCED_PERMEABILITY entry labeled Klebsiella pneumoniae OmpK35, explicitly qualified as a CARD/ARO database assertion rather than a primary citation. No direct molecular target, quantitative activity, producer, clinical status or causal graph is asserted. Their optional absence alone is not an error. |
| source | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_resistance_edges.tsv; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; scripts/card_evidence_reviews.py; Exact ChEBI row 75, ARO row 296 and resistance row 3995; relevant extraction, concept merging, resistance attachment and overlay code. | supports | Source rows reproduce the identity, roles, synonyms, references and resistance assertion. ChEBI identity takes precedence in the joined concept; ARO supplies the exact cefamandole concept and the OmpK35 edge. No corresponding target edge exists in the inspected maintained target inventory. The overlay can qualify an unchanged imported assertion while retaining CARD ownership. Initial 13 input hashes are preserved, with six additional actual ARO/overlay inputs appended from the pre-assessment supplemental capture. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:3480; https://pubchem.ncbi.nlm.nih.gov/compound/456255; https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL1146.json; Current ChEBI entry, exact PubChem property response and ChEMBL structure. | supports | The neutral C18H18N6O5S2 graph and full key OLVCFLKTBJRLHI-AXAPSJFSSA-N agree across inspected sources. The (6R,7R) cephalosporin and (R)-mandelamido stereochemistry, tetrazole substitution, charge and masses are coherent. CAS 34444-01-4 and Beilstein 5406309 are source-attested. Parents CHEBI:23066 and CHEBI:72588, roles CHEBI:33281 and CHEBI:36047, and the ARO cephalosporin class agree with the adopted sources. Current ChEBI also presents an antibacterial-agent role; this does not make the dated inherited role list erroneous. |
| chemical-xrefs | https://rest.kegg.jp/get/C06879; https://card.mcmaster.ca/ontology/40926; KEGG compound entry and MOL; CARD ARO:3003999 entry and chemical identifiers. | supports | Independently parsed KEGG, ChEMBL and CARD chemical structures reproduce the native full key. KEGG PubChem 9096 denotes a substance identifier, not a conflicting compound CID. CARD confirms the cefamandole source concept, cephalosporin classification and FAM synonym. |
| drug-xrefs | https://go.drugbank.com/drugs/DB01326; https://drugcentral.org/drugcard/527; https://rest.kegg.jp/get/D02344; DrugBank public identity fields, DrugCentral entry and raw structures, KEGG drug flat record. | supports | All three drug entries concern cefamandole. DrugBank and DrugCentral exact standard identifiers agree with the neutral graph; independently parsed DrugCentral InChI and SMILES reproduce its full key. KEGG D02344 gives the neutral formula and compound cross-link C06879. Drug-centric clinical, formulation and PBP annotations are context only; they are not imported as new exact-material primary claims. |
| document-xrefs | https://patents.google.com/patent/US3641021A/en; https://patents.google.com/patent/US3840531A/en; https://patents.google.com/patent/DE2018600A1/en; https://patents.google.com/patent/DE2312997A1/en; https://en.wikipedia.org/wiki/Cefamandole; Patent titles, metadata and selected synthesis/description passages; Wikipedia chemical identity fields. | partial | The four patent numbers resolve to cephalosporin synthesis documents related to the source concept; the patents contain broader series and near analogues and are document links rather than exact standalone assay citations. The Wikipedia document concerns cefamandole and gives matching neutral identity while discussing formulations more broadly. Full patent claims and every synthetic example were not independently audited. |
| activity1973 | PMID:4790616; DOI:10.1128/AAC.3.6.657; PMC444475; All five original scanned pages 657–661, including Figure 1 and Tables 1–6, visually inspected. | supports | Eykyn et al. explicitly introduce the sodium salt as the material; the neutral COOH drawing does not override that wording. The study tests 1,213 clinical isolates. Agar MIC uses Oxoid DST agar, usually approximately 10^4 organisms and 18 h at 37 °C; MBC uses broth followed by subculture. Tables include population cumulative percentages and inoculum-dependent effects, not one representative strain MIC for each taxon. These data support antibacterial active-moiety context, not an unqualified free-acid test or direct PBP binding. |
| activity1974 | PMID:15828189; DOI:10.1128/AAC.6.2.177; PMC444624; All six original scanned pages 177–182, including Methods, Tables 1–11 and Discussion, visually inspected. | supports | Neu describes cefamandole supplied by Lilly without establishing the salt form in the inspected material description. Twofold broth assays generally use brain heart infusion medium, approximately 10^4 CFU and 18 h at 35 °C; MBC uses subculture. Medium, inoculum, strain and MIC/MBC differences matter. Direct beta-lactamase hydrolysis assays show substrate/enzyme-dependent effects, including crude Proteus morganii 771 hydrolysis. Neither broad spectrum nor hydrolysis supplies direct PBP-binding evidence, and population tables should not become invented strain observations. The paper is from 1974 despite its later-looking PMID. |
| other-primary-leads | PMID:12569987 DOI:10.1046/j.1365-2222.2002.01492.x; PMID:12833570 DOI:10.1002/jmr.621; Complete adopted abstracts and metadata. | context_only | The former examines fine antibody/IgE antigenic specificity involving beta-lactams; the latter studies synthetic cephalosporin antigenic determinants and antibody recognition. These are immunochemistry contexts, not antibacterial MIC, PBP-target or bacterial resistance experiments. Full texts were not used to assert further claims. |
| review-lead | PMID:29017833; DOI:10.1016/j.jaip.2017.08.027; Complete adopted review abstract and metadata. | context_only | This secondary review concerns beta-lactam allergy and cross-reactivity. It is a literature/context lead, not independently inspected primary antimicrobial evidence. |
| card | https://card.mcmaster.ca/ontology/40737; ARO:3003966; Complete relevant CARD definition, parent relation, cefamandole edge, model and cited reference. | supports | CARD describes OmpK35 as an entry porin whose loss limits drug diffusion and places the determinant under resistance through absence. The exact cefamandole edge is present. The native entry preserves the imported database status, but a qualification should make loss explicit. The model reference protein from HS11286 must not be mistaken for the primary experimental strain. |
| porin-primary | PMID:27645385; DOI:10.1128/JB.00590-16; https://pmc.ncbi.nlm.nih.gov/articles/PMC5105900/; Indexed original PMC Methods, relevant Results/Discussion and Table 1; direct archive routes were challenged. | supports | The primary experiment uses K. pneumoniae ATCC 11296 and clean porin deletions. Cefamandole MICs are 4 µg/mL in the parent, 8 in ΔompK35 and 4 in ΔompK36. Twofold broth microdilution uses LB plus 5 mM MgCl2, approximately 10^3 cells and 16 h at 37 °C. This is a modest susceptibility shift, not a breakpoint classification. Direct permeability measurements concern other beta-lactams; no cefamandole-specific influx coefficient or target binding is established. The supplied cefamandole salt is not resolved. |
| adapter | 211-imodulondb-datasets.txt; Structured public catalog consulted before web research. | context_only | The catalog has no covered Klebsiella dataset for the native OmpK35 context. An E. coli homolog annotation would not resolve this strain-specific assertion, so no unrelated module was substituted. Catalog absence is not negative biological evidence. Command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1 uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb --timeout 15 datasets; exit 0. |
| local-search | 211-local-hits.txt; 211-maintained-search.txt; 211-inclusive-file-hits.txt; Name, exact identifiers, key and slug searches with hidden and ignored files included. | context_only | Matches include source inventories, this record, distinct sodium/nafate/O-formyl records, queues, path ledger and generated maps. No exact maintained corrective decision or evidence overlay was found. The FDA inventory concerns related drug-product context, not a native clinical-status assertion in this record. |
| validation | 211-focused-results.json; 211-chemistry.json; 211-schema.log; 211-strict.log; Actual focused schema/strict commands and independent structure/mint checks. | supports | All focused checks exit 0. Native SMILES and InChI reproduce the formula, charge, masses and full key; source mints reproduce from ARO:3003999 and CHEBI:3480. Independent chemistry used batch019 RDKit against unchanged batch022 inputs. |

## Limits And Additional Notes

- All 13 original input hashes remain unchanged; actual ARO source and overlay owners were appended from a separate pre-assessment capture. No original capture was replaced.
- All five adopted abstracts were read. The 1973 and 1974 antibacterial papers were fully inspected as original scanned pages. The allergy primary papers remain abstract-level context and the 2017 review is not classified as primary evidence.
- The 2016 porin paper was inspected through indexed original PMC Methods, relevant Results/Discussion and its table after direct PMC/publisher/author-repository routes were challenged or unavailable. Original figure images and supplemental files were not audited; the failed PDF/BioC attempts are not evidence.
- Supplied sodium, lithium comparator and nafate material must not be silently assigned to neutral free acid. The 1974 and porin-study material form remains unresolved; the neutral chemical drawing alone does not establish the supplied salt.
- Beilstein was checked through official source attestations, not a subscription registry. Four patent records were inspected at metadata and selected-description level, not as exhaustive claim or synthetic-example audits. The document links are therefore only partially verified.
- The L-Cefamandole alias is retained as an adopted-source attestation; no independent historical naming analysis was performed, and no opposite-stereoisomer conclusion is made from its prefix.
- The structured adapter has no matching Klebsiella dataset. This limits that cross-check without undermining the primary bacterial experiment.
- This is a partial scientific review because some full-text and document-level verification remains bounded. Passing schema, strict and independent chemistry does not constitute native scientific sign-off.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T110855Z-cefamandole
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cefamandole: coherent neutral identity; qualify salt-dependent activity and
  OmpK35 loss'
started_at: '2026-10-21T10:55:27Z'
finished_at: '2026-10-21T11:08:55Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author the seed. Preserved initial hashes and supplemented
    actual ARO owners before assessment; read the complete record, maintained rows
    and transforms, official structures, all adopted abstracts and relevant original
    antibacterial experiments.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: The neutral cefamandole identity and source provenance are coherent, and
  all focused validators pass. The CARD reduced-permeability assertion has a real
  OmpK35-loss context but remains explicitly a database assertion. Original antibacterial
  papers support the active moiety while requiring salt, assay and population qualifications.
  One informational finding identifies a bounded evidence-enrichment route; no required
  identity or role correction is established. Scientific assessment retains the stated
  evidence limits; full verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/cefamandole.yaml
    sha256: b45ae328f38ed0d8d09cbc64eb4364e0ab115efe4cba7a5910d8786e4ad979de
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
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
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
  - path: scripts/card_evidence_reviews.py
    sha256: f9ec8aff30066bf04b9c2757af7d6f5d179d045e57b9f3b352bbed0b851f50a8
    role: context
targets:
- target_id: CHEBI:3480
  path: data/antibiotics/antibacterial/cefamandole.yaml
  label: cefamandole
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
    role: ARO exact concept and classification
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Imported OmpK35 resistance edge
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Imported target edge selection
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Resistance evidence overlay handling
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Maintained resistance-evidence adjudication overlay
scope:
  description: Whole CHEBI:3480 record, including definition, all eleven synonyms,
    three parents, two roles, class, structure descriptors, six chemical xrefs, three
    drug xrefs, five document xrefs, two source concepts, one resistance mechanism
    and four history events; all five adopted citation leads.
  selection: Queue 211; original capture preserved and actual ARO owner inputs appended.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:3480
  exclusions:
  - target: Cefamandole sodium, lithium comparator material, O-formylcefamandole and
      cefamandole nafate
    reason: These are distinct supplied forms or prodrugs; their experiments provide
      qualified active-moiety context rather than proof of neutral free-acid test
      material.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Actual focused command exited 0.
  target_ids:
  - CHEBI:3480
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefamandole.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Actual focused command exited 0.
  target_ids:
  - CHEBI:3480
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefamandole.yaml --out /private/tmp/am-review-session/211-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Actual focused command exited 0. Batch022 lacks RDKit; batch019 interpreter
    was used against batch022 inputs.
  target_ids:
  - CHEBI:3480
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 211
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
  - CHEBI:3480
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
  - CHEBI:3480
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
  - CHEBI:3480
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
  - CHEBI:3480
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
  - CHEBI:3480
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
  - CHEBI:3480
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
  - CHEBI:3480
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
  - CHEBI:3480
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
  - CHEBI:3480
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/cefamandole.yaml
  locator: Complete native YAML and all history events.
  accessed_at: '2026-10-21T11:05:24Z'
  support: supports
  summary: SEEDED/EXACT neutral cefamandole has one REDUCED_PERMEABILITY entry labeled
    Klebsiella pneumoniae OmpK35, explicitly qualified as a CARD/ARO database assertion
    rather than a primary citation. No direct molecular target, quantitative activity,
    producer, clinical status or causal graph is asserted. Their optional absence
    alone is not an error.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_resistance_edges.tsv;
    conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py;
    scripts/card_evidence_reviews.py
  locator: Exact ChEBI row 75, ARO row 296 and resistance row 3995; relevant extraction,
    concept merging, resistance attachment and overlay code.
  accessed_at: '2026-10-21T11:05:24Z'
  support: supports
  summary: Source rows reproduce the identity, roles, synonyms, references and resistance
    assertion. ChEBI identity takes precedence in the joined concept; ARO supplies
    the exact cefamandole concept and the OmpK35 edge. No corresponding target edge
    exists in the inspected maintained target inventory. The overlay can qualify an
    unchanged imported assertion while retaining CARD ownership. Initial 13 input
    hashes are preserved, with six additional actual ARO/overlay inputs appended from
    the pre-assessment supplemental capture.
  snapshot_sha256: c03f893f2aa62bb91c06c1d7dc741fb82080c5046e380afee2b4e12579ffee74
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:3480; https://pubchem.ncbi.nlm.nih.gov/compound/456255;
    https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL1146.json
  locator: Current ChEBI entry, exact PubChem property response and ChEMBL structure.
  accessed_at: '2026-10-21T11:05:24Z'
  support: supports
  summary: The neutral C18H18N6O5S2 graph and full key OLVCFLKTBJRLHI-AXAPSJFSSA-N
    agree across inspected sources. The (6R,7R) cephalosporin and (R)-mandelamido
    stereochemistry, tetrazole substitution, charge and masses are coherent. CAS 34444-01-4
    and Beilstein 5406309 are source-attested. Parents CHEBI:23066 and CHEBI:72588,
    roles CHEBI:33281 and CHEBI:36047, and the ARO cephalosporin class agree with
    the adopted sources. Current ChEBI also presents an antibacterial-agent role;
    this does not make the dated inherited role list erroneous.
  snapshot_sha256: 062b4f543326827161b1f4398451d6e82d907c9654e045bf226cef04d62d52ea
- evidence_id: chemical-xrefs
  kind: database
  reference: https://rest.kegg.jp/get/C06879; https://card.mcmaster.ca/ontology/40926
  locator: KEGG compound entry and MOL; CARD ARO:3003999 entry and chemical identifiers.
  accessed_at: '2026-10-21T11:05:24Z'
  support: supports
  summary: Independently parsed KEGG, ChEMBL and CARD chemical structures reproduce
    the native full key. KEGG PubChem 9096 denotes a substance identifier, not a conflicting
    compound CID. CARD confirms the cefamandole source concept, cephalosporin classification
    and FAM synonym.
  snapshot_sha256: 527e309e0d678b069f2bcd4efcbaa44f421840c73b4a63082bf2b415f239dc05
- evidence_id: drug-xrefs
  kind: database
  reference: https://go.drugbank.com/drugs/DB01326; https://drugcentral.org/drugcard/527;
    https://rest.kegg.jp/get/D02344
  locator: DrugBank public identity fields, DrugCentral entry and raw structures,
    KEGG drug flat record.
  accessed_at: '2026-10-21T11:05:24Z'
  support: supports
  summary: All three drug entries concern cefamandole. DrugBank and DrugCentral exact
    standard identifiers agree with the neutral graph; independently parsed DrugCentral
    InChI and SMILES reproduce its full key. KEGG D02344 gives the neutral formula
    and compound cross-link C06879. Drug-centric clinical, formulation and PBP annotations
    are context only; they are not imported as new exact-material primary claims.
  snapshot_sha256: 60a718ce76f9ce00be0608c3df4cc037641226acc6d32ab90e84f157e1796f7d
- evidence_id: document-xrefs
  kind: database
  reference: https://patents.google.com/patent/US3641021A/en; https://patents.google.com/patent/US3840531A/en;
    https://patents.google.com/patent/DE2018600A1/en; https://patents.google.com/patent/DE2312997A1/en;
    https://en.wikipedia.org/wiki/Cefamandole
  locator: Patent titles, metadata and selected synthesis/description passages; Wikipedia
    chemical identity fields.
  accessed_at: '2026-10-21T11:05:24Z'
  support: partial
  summary: The four patent numbers resolve to cephalosporin synthesis documents related
    to the source concept; the patents contain broader series and near analogues and
    are document links rather than exact standalone assay citations. The Wikipedia
    document concerns cefamandole and gives matching neutral identity while discussing
    formulations more broadly. Full patent claims and every synthetic example were
    not independently audited.
  snapshot_sha256: 2d368a08e6d1d54e66fe11092e5783dc1f17aa04a54b4bdda6bea1b2ff313e2b
- evidence_id: activity1973
  kind: primary_source
  reference: PMID:4790616; DOI:10.1128/AAC.3.6.657; PMC444475
  locator: All five original scanned pages 657–661, including Figure 1 and Tables
    1–6, visually inspected.
  accessed_at: '2026-10-21T11:05:24Z'
  support: supports
  summary: Eykyn et al. explicitly introduce the sodium salt as the material; the
    neutral COOH drawing does not override that wording. The study tests 1,213 clinical
    isolates. Agar MIC uses Oxoid DST agar, usually approximately 10^4 organisms and
    18 h at 37 °C; MBC uses broth followed by subculture. Tables include population
    cumulative percentages and inoculum-dependent effects, not one representative
    strain MIC for each taxon. These data support antibacterial active-moiety context,
    not an unqualified free-acid test or direct PBP binding.
  snapshot_sha256: bdfbdda184c50d534c3bc3176679c9c6922adc11ff8cf1f39f13ff8a73488f9b
- evidence_id: activity1974
  kind: primary_source
  reference: PMID:15828189; DOI:10.1128/AAC.6.2.177; PMC444624
  locator: All six original scanned pages 177–182, including Methods, Tables 1–11
    and Discussion, visually inspected.
  accessed_at: '2026-10-21T11:05:24Z'
  support: supports
  summary: Neu describes cefamandole supplied by Lilly without establishing the salt
    form in the inspected material description. Twofold broth assays generally use
    brain heart infusion medium, approximately 10^4 CFU and 18 h at 35 °C; MBC uses
    subculture. Medium, inoculum, strain and MIC/MBC differences matter. Direct beta-lactamase
    hydrolysis assays show substrate/enzyme-dependent effects, including crude Proteus
    morganii 771 hydrolysis. Neither broad spectrum nor hydrolysis supplies direct
    PBP-binding evidence, and population tables should not become invented strain
    observations. The paper is from 1974 despite its later-looking PMID.
  snapshot_sha256: 3dd321afaa78ea0a4e02b7280d10208d8a87a17fd95bdd2c8f24ee2679f4ebbe
- evidence_id: other-primary-leads
  kind: primary_source
  reference: PMID:12569987 DOI:10.1046/j.1365-2222.2002.01492.x; PMID:12833570 DOI:10.1002/jmr.621
  locator: Complete adopted abstracts and metadata.
  accessed_at: '2026-10-21T11:05:24Z'
  support: context_only
  summary: The former examines fine antibody/IgE antigenic specificity involving beta-lactams;
    the latter studies synthetic cephalosporin antigenic determinants and antibody
    recognition. These are immunochemistry contexts, not antibacterial MIC, PBP-target
    or bacterial resistance experiments. Full texts were not used to assert further
    claims.
  snapshot_sha256: 74da98c9f2582a6ed7c8dd1f7f28f41e17c970191dfcdb7c38c6f44719e28232
- evidence_id: review-lead
  kind: database
  reference: PMID:29017833; DOI:10.1016/j.jaip.2017.08.027
  locator: Complete adopted review abstract and metadata.
  accessed_at: '2026-10-21T11:05:24Z'
  support: context_only
  summary: This secondary review concerns beta-lactam allergy and cross-reactivity.
    It is a literature/context lead, not independently inspected primary antimicrobial
    evidence.
  snapshot_sha256: 74da98c9f2582a6ed7c8dd1f7f28f41e17c970191dfcdb7c38c6f44719e28232
- evidence_id: card
  kind: database
  reference: https://card.mcmaster.ca/ontology/40737; ARO:3003966
  locator: Complete relevant CARD definition, parent relation, cefamandole edge, model
    and cited reference.
  accessed_at: '2026-10-21T11:05:24Z'
  support: supports
  summary: CARD describes OmpK35 as an entry porin whose loss limits drug diffusion
    and places the determinant under resistance through absence. The exact cefamandole
    edge is present. The native entry preserves the imported database status, but
    a qualification should make loss explicit. The model reference protein from HS11286
    must not be mistaken for the primary experimental strain.
  snapshot_sha256: e1098f5f46a24900d2e26d0b550f5205a618a59ee13394dacd0e8c340072ff85
- evidence_id: porin-primary
  kind: primary_source
  reference: PMID:27645385; DOI:10.1128/JB.00590-16; https://pmc.ncbi.nlm.nih.gov/articles/PMC5105900/
  locator: Indexed original PMC Methods, relevant Results/Discussion and Table 1;
    direct archive routes were challenged.
  accessed_at: '2026-10-21T11:05:24Z'
  support: supports
  summary: The primary experiment uses K. pneumoniae ATCC 11296 and clean porin deletions.
    Cefamandole MICs are 4 µg/mL in the parent, 8 in ΔompK35 and 4 in ΔompK36. Twofold
    broth microdilution uses LB plus 5 mM MgCl2, approximately 10^3 cells and 16 h
    at 37 °C. This is a modest susceptibility shift, not a breakpoint classification.
    Direct permeability measurements concern other beta-lactams; no cefamandole-specific
    influx coefficient or target binding is established. The supplied cefamandole
    salt is not resolved.
  snapshot_sha256: b3c81fb4cc032bf44f4b650c97c6f4a166437326257c3a25ca050ee1b6f8aeee
- evidence_id: adapter
  kind: database
  reference: 211-imodulondb-datasets.txt
  locator: Structured public catalog consulted before web research.
  accessed_at: '2026-10-21T11:05:24Z'
  support: context_only
  summary: 'The catalog has no covered Klebsiella dataset for the native OmpK35 context.
    An E. coli homolog annotation would not resolve this strain-specific assertion,
    so no unrelated module was substituted. Catalog absence is not negative biological
    evidence. Command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache
    PYTHONDONTWRITEBYTECODE=1 uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 datasets; exit 0.'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: local-search
  kind: search
  reference: 211-local-hits.txt; 211-maintained-search.txt; 211-inclusive-file-hits.txt
  locator: Name, exact identifiers, key and slug searches with hidden and ignored
    files included.
  accessed_at: '2026-10-21T11:05:24Z'
  support: context_only
  summary: Matches include source inventories, this record, distinct sodium/nafate/O-formyl
    records, queues, path ledger and generated maps. No exact maintained corrective
    decision or evidence overlay was found. The FDA inventory concerns related drug-product
    context, not a native clinical-status assertion in this record.
  snapshot_sha256: 5adaa3434b0522bc5592ebc80d4c411a705f0620caad5df8d35bb03f44386f2e
  search_scope: rg --no-ignore --hidden across data, curation, conf, scripts, src,
    docs, .claude, reviews and reports for CHEBI:3480, ARO:3003999, OLVCFLKTBJRLHI
    and cefamandole; .git and .venv internals excluded.
- evidence_id: validation
  kind: validation
  reference: 211-focused-results.json; 211-chemistry.json; 211-schema.log; 211-strict.log
  locator: Actual focused schema/strict commands and independent structure/mint checks.
  accessed_at: '2026-10-21T11:05:24Z'
  support: supports
  summary: All focused checks exit 0. Native SMILES and InChI reproduce the formula,
    charge, masses and full key; source mints reproduce from ARO:3003999 and CHEBI:3480.
    Independent chemistry used batch019 RDKit against unchanged batch022 inputs.
  snapshot_sha256: 99629e2ed11a9c571a99e2d9dfb2a9970cb57025b96dcd0ce4fefc3851be13a1
assessments:
- assessment_id: identity
  area: identity
  topic: Neutral structure, synonyms, ontology and xrefs
  outcome: supported
  summary: The exact neutral identity is coherent across adopted and inspected official
    chemical sources. The historical L-Cefamandole alias is source-attested; its text
    alone is insufficient to infer a distinct opposite stereoisomer. Patent and subscription-registry
    verification remain bounded.
  target_ids:
  - CHEBI:3480
  evidence_ids:
  - identity
  - chemical-xrefs
  - drug-xrefs
  - document-xrefs
  - validation
- assessment_id: source
  area: provenance
  topic: Maintained inputs and generated ownership
  outcome: supported
  summary: The merged ChEBI/ARO source provenance and history are coherent. Source-owned
    resistance qualifications have an established maintained overlay; primary native
    additions belong to the exact native record.
  target_ids:
  - CHEBI:3480
  evidence_ids:
  - source
  - record
  - local-search
- assessment_id: activity
  area: quantity
  topic: Antibacterial role and exact supplied material
  outcome: supported
  summary: Inspected primary studies support cefamandole antibacterial activity with
    explicit sodium or unresolved material-form qualifications. They do not demonstrate
    that every measurement used neutral free acid. No native numerical assay currently
    overstates that distinction.
  target_ids:
  - CHEBI:3480
  evidence_ids:
  - activity1973
  - activity1974
  - porin-primary
- assessment_id: resistance
  area: scope
  topic: OmpK35 database assertion
  outcome: supported
  summary: The imported assertion has a supported loss-of-entry-porin interpretation.
    The native database caveat avoids a false primary-evidence claim; qualification
    and narrow primary evidence would improve it.
  target_ids:
  - CHEBI:3480
  evidence_ids:
  - card
  - porin-primary
  - adapter
  - record
- assessment_id: mechanism
  area: completeness
  topic: Optional PBP, spectrum and graph content
  outcome: unknown
  summary: No exact PBP binding experiment was independently verified. Hydrolysis
    and porin-loss results should not be repurposed as direct target binding, and
    allergy studies do not supply antibacterial mechanisms. Missing optional fields
    are not errors.
  target_ids:
  - CHEBI:3480
  evidence_ids:
  - record
  - activity1974
  - other-primary-leads
  - review-lead
- assessment_id: validation
  area: schema
  topic: Deterministic checks
  outcome: supported
  summary: Actual focused schema, strict and chemistry checks pass without implying
    scientific status promotion.
  target_ids:
  - CHEBI:3480
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: cefamandole-qualified-primary-evidence-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Qualify OmpK35 loss and preserve material-form limits when adding primary
    evidence
  description: The coherent seeded record could be strengthened by a maintained OmpK35-loss
    qualification and narrow primary activity evidence. The existing database caveat
    is honest, so this is an optional enrichment opportunity rather than an unsupported
    role or compulsory missing-field defect. Related salt/prodrug studies and population
    summaries require explicit scope.
  target_ids:
  - CHEBI:3480
  field_paths:
  - resistance_mechanisms[0]
  - activity_spectrum
  - mode_of_action
  - molecular_targets
  evidence_ids:
  - card
  - porin-primary
  - activity1973
  - activity1974
  - record
  - source
  rule_id: 'native-review-checklist: exact tested material, narrow evidence placement
    and direct versus inferred mechanism'
  native_severity: informational evidence enrichment
  normalization_reason: No contradictory native quantitative or direct-target claim
    is present. The source assertion is correctly identified as database evidence;
    additional qualifications improve interpretation without establishing a material
    error.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Maintained qualification of the unchanged CARD resistance assertion
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Apply the maintained evidence-scope qualification on reseeding
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefamandole.yaml
    role: Future separate claim-level primary activity or mechanism evidence
actions:
- action_id: A1
  description: Add bounded evidence qualifications through the correct maintained
    owner and curate only exact supported observations.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:3480
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Maintained qualification of the unchanged CARD resistance assertion
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Apply the maintained evidence-scope qualification on reseeding
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefamandole.yaml
    role: Future separate claim-level primary activity or mechanism evidence
  acceptance_checks:
  - Use the maintained CARD evidence overlay for the imported edge and preserve its
    database status. Make the loss-of-porin interpretation explicit; do not relabel
    the ordinary porin as a direct inhibitory target or its presence as the resistance-causing
    state.
  - Any primary susceptibility observation must retain the exact genotype, assay and
    endpoint, without converting a twofold shift to a clinical resistant category
    or transferring direct permeability measurements from other drugs. Resolve supplied
    material where an exact chemical-form claim requires it.
  - For older activity data, preserve the explicit sodium material in the 1973 study
    and unresolved supplied form in the 1974 study. Keep cumulative population results
    separate from individual strain MICs, and distinguish MIC, MBC and hydrolysis
    assays.
  - Do not infer direct PBP binding from drug databases, beta-lactam class membership
    or antibody epitopes. Inspect an exact primary target experiment before adding
    a protein target or causal binding edge.
  - Apply separately authorized native additions with write_validated_antibiotic and
    record_curation_event, preserve provenance, and run focused and applicable shared
    gates after any overlay or curation change.
limitations:
- All 13 original input hashes remain unchanged; actual ARO source and overlay owners
  were appended from a separate pre-assessment capture. No original capture was replaced.
- All five adopted abstracts were read. The 1973 and 1974 antibacterial papers were
  fully inspected as original scanned pages. The allergy primary papers remain abstract-level
  context and the 2017 review is not classified as primary evidence.
- The 2016 porin paper was inspected through indexed original PMC Methods, relevant
  Results/Discussion and its table after direct PMC/publisher/author-repository routes
  were challenged or unavailable. Original figure images and supplemental files were
  not audited; the failed PDF/BioC attempts are not evidence.
- Supplied sodium, lithium comparator and nafate material must not be silently assigned
  to neutral free acid. The 1974 and porin-study material form remains unresolved;
  the neutral chemical drawing alone does not establish the supplied salt.
- Beilstein was checked through official source attestations, not a subscription registry.
  Four patent records were inspected at metadata and selected-description level, not
  as exhaustive claim or synthetic-example audits. The document links are therefore
  only partially verified.
- The L-Cefamandole alias is retained as an adopted-source attestation; no independent
  historical naming analysis was performed, and no opposite-stereoisomer conclusion
  is made from its prefix.
- The structured adapter has no matching Klebsiella dataset. This limits that cross-check
  without undermining the primary bacterial experiment.
- This is a partial scientific review because some full-text and document-level verification
  remains bounded. Passing schema, strict and independent chemistry does not constitute
  native scientific sign-off.
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
