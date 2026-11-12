# Review of cefixime

- Review: 20261021T112849Z-cefixime-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T11:08:27Z
- Finished UTC: 2026-10-21T11:28:49Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The neutral anhydrous cefixime graph agrees with current ChEBI, PubChem, ChEMBL and both KEGG identifiers. Both CDC/FDA AR Isolate Bank MIC observations, including isolate identities, broth microdilution, units, breakpoint edition and the &gt; qualifier, match their official sources. Compound-specific PBP2 binding and gonococcal resistance experiments were inspected. Supplementary data support cefixime susceptibility shifts for five imported beta-lactamase alleles in recombinant E. coli. The meningococcal PBP2 and BlaS1 routes remain honestly labeled database assertions with unresolved exact causal support; the BlaS1 deletion experiment did not change the measured cefixime disc phenotype. All 26 adopted or parent MED records resolve at their declared inspection depth. No confirmed required native correction was demonstrated. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact SEEDED cefixime record, all seven history events, eight database resistance entries, the PBP family target, two curated MIC/BioSample observations, chemical/document/drug identifiers, actual owner rows and all 26 adopted or parent PMID leads.

Selection: Queue 225. Original 13 initial inputs preserved; three actual ARO owner inputs appended before detailed judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:472657 | data/antibiotics/antibacterial/cefixime.yaml | generated | cefixime |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema check | passed | True | CHEBI:472657 | Exit 0. |
| Documented strict check | passed | True | CHEBI:472657 | Exit 0; zero ERROR rows. |
| Supplemental exact graph comparison | passed | False | CHEBI:472657 | Exit 0 using the 019 interpreter against 023 files. |
| Structured catalog initial attempt | failed | False | CHEBI:472657 | Sandbox network name resolution failed, exit 2; the same public read was retried successfully with network access. |
| Structured catalog retry | passed | False | CHEBI:472657 | Network-enabled retry passed, exit 0; catalog inspected before protein web research. |
| Structured protein query | passed | False | CHEBI:472657 | Found e_coli/modulome/b0084, with no component hits. |
| Structured protein query | passed | False | CHEBI:472657 | Found p_aeruginosa/precise364/PA4110, with no component hits; not allele-specific PDC-3/PDC-5 evidence. |
| Structured protein query | passed | False | CHEBI:472657 | No hit; not negative biological evidence. |
| Authoritative full QC | failed | True | CHEBI:472657 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:472657 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:472657 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:472657 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:472657 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:472657 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:472657 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:472657 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:472657 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact chemical form and stereochemistry

identity: supported. Targets: CHEBI:472657.

All compared exact structures agree with neutral anhydrous cefixime.

### Chemical class, roles and identifier placement

grounding: supported. Targets: CHEBI:472657.

Exact chemical xrefs, broader parents and contextual drug/patent links are consistently separated at the inspected depth.

### Two curated MIC and BioSample observations

evidence: supported. Targets: CHEBI:472657.

Both official observations agree with values, qualifier, method, units, isolates, BioSamples and breakpoint edition.

### PBP direct binding

evidence: supported. Targets: CHEBI:472657.

Primary cefixime-acylated PBP2 structure supports the family-level target; native evidence remains honestly database-qualified pending primary curation.

### Five enzyme alleles and gonococcal PBP2

evidence: supported. Targets: CHEBI:472657.

Recombinant enzyme-expression susceptibility results and gonococcal penA experiments support bounded routes; no clinical-host or hydrolysis overgeneralization is made.

### Meningococcal PBP2 and BlaS1 causal evidence

evidence: unknown. Targets: CHEBI:472657.

Historical citation taxon scope, later meningococcal association and unchanged BlaS1 deletion disc phenotypes leave exact causal support unresolved. These limits do not prove the database assertions false.

### All leads, source owners and seven history events

provenance: supported. Targets: CHEBI:472657.

The source and curator-owned slices are distinct; all 26 adopted/parent MED records resolve at declared depth.

### Focused deterministic checks

schema: supported. Targets: CHEBI:472657.

Focused schema, strict and supplemental chemistry checks passed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/cefixime.yaml; Entire native YAML, including two activity observations and seven history events | supports | Exact neutral cefixime is SEEDED. Eight resistance entries explicitly cite CARD/ARO as database assertions; the PBP family target explicitly needs primary evidence and lacks organism/assay specification. Five history events are source seeding, followed by resistant-taxa and BioSample curation. There is no populated mode, target scope, producer or causal graph. |
| chemistry | CHEBI:472657; PubChem:5362065; CHEMBL1541; KEGG:D00258; KEGG:C06881; 225-chemistry.py/.json and authority structure snapshots | supports | Native SMILES and InChI agree with full key OKBVVJOGVLARMR-QSWIMTSFSA-N, formula C16H15N5O7S2, charge 0 and masses. Current ChEBI, PubChem, ChEMBL and both KEGG graphs match the 6R/7R, Z-oxime neutral anhydrous free acid. This does not equate the exact record to cefixime trihydrate or a salt. |
| grounding | ARO:3000646; CHEBI:23066; ARO:0000032; CHEBI:33281; CHEBI:36047; 225-ols.json; 225-aro-stanzas.txt; 225-card.html; 225-drugcentral.html; 225-kegg.txt | supports | Compound, cephalosporin parent/class, antimicrobial and antibacterial roles agree with native identity and owner rows. All eight determinant CURIEs and the PBP family CURIE resolve in the adopted ARO cache; current CARD preserves the imported relationships. CAS 79350-37-1 is corroborated through authorities, not direct registry access. DrugCentral 537 and KEGG D00258 resolve in drug context; DrugBank DB00671 is corroborated through ChEBI/DrugCentral rather than a directly inspected DrugBank record. Beilstein 6025058 was not independently resolved. |
| patents | patent:EP30630; patent:US4409214; 225-patent-ep.html and 225-patent-us.html | context_only | The abbreviated patent links resolve through EP0030630B1 and US4409214A, members of the same cephalosporin patent family. The US text includes the syn carboxymethoxyimino aminothiazolyl vinyl cephalosporin in its named compound M / compound 13 context. These document references are not exact chemical xrefs, and family-wide activity is not imported as a cefixime-specific MIC. The attempted EP0030630A1 URL returned 404; the inspected B1 document succeeded. |
| adopted-leads | 26 adopted or parent PMID records; 225-core.json; 225-lead-dispositions.json | context_only | All 26 MED records resolve. All 24 returned complete abstracts were read. Parent reviews 15673804 and 6810737 have metadata only. Original full text was additionally inspected for 16940068, 23587946 and 33416461, together with the 2016 two-species review 27690121. Original 15699201 methods/results/tables/discussion were read through the public author-uploaded text; local download failed. Each remaining lead is individually scoped in the disposition ledger. |
| enzyme-panel | PMID:33416461; DOI:10.1099/mgen.0.000500; 225-primary-ctxm.xml; supplementary Table S1 (225-mgen-7-500-s002.xlsx, rows 52-59); Figure S6 (225-mgen-7-500-s001.pdf) | supports | The original recombinant E. coli BW25113/pGDP1 broth microdilution experiment reports cefixime MIC 0.25 micrograms/mL for control, &gt;256 for CMY-2, 32 for CTX-M-3, 4 for CTX-M-27, and &gt;256 for both PDC-3 and PDC-5. This supports allele-specific susceptibility shifts in that expression system. It is not direct cefixime hydrolysis kinetics or proof of clinical resistance in every native host; the source expressly lacks a P. aeruginosa cefixime breakpoint. Direct PMC supplementary routes returned challenge HTML, but the Europe PMC supplementary ZIP was successfully retrieved and its real XLSX/PDF inspected. |
| gonococcal-resistance | PMID:16940068; PMID:23587946; 225-nmen-original.html and 225-ngon-full.html, original methods/results/tables and discussion | supports | Despite the scratch filename, PMID16940068 is a gonococcal, not meningococcal, study of mosaic PBP2 substitutions and cefixime susceptibility. PMID23587946 tests H041 penA substitutions in gonococcal backgrounds, supporting a causal contribution of altered PBP2 to expanded-spectrum cephalosporin resistance. Effects depend on allele and genetic background. These support the gonococcal ARO route, not automatic transfer of the same experiment to N. meningitidis. |
| meningococcal-scope | ARO:3003937; PMID:27690121; DOI:10.3201/eid3110.250464; 225-aro-stanzas.txt; 225-primary-nmen-review.xml; 225-nmen2025.html | partial | The meningococcal ARO term has a source-label typo and a historical citation set containing gonococcal primary experiments. The 2016 review treats both species and reports meningococcal penicillin/third-generation cephalosporin observations, including unpublished penA327 transformation context; this is not a fully inspected exact cefixime causal experiment. The 2025 original Thai urethritis study reports N. meningitidis NM7 with elevated cefixime susceptibility-test values and a mosaic penA2840 related to gonococcal penA60. It supports a bounded exact-species association, not isolated allele causality. The native entry is honestly database-level; primary causal support remains unresolved. |
| blas-scope | ARO:3005111; PMID:15699201; PMID:9103972; 225-blas2005-web-observations.json; original 2005 Tables 3 and 6 via public author-uploaded text; 225-core.json and 225-blas1997-orbi.html | partial | The cited 2005 M. smegmatis experiment reports cefixime 5 micrograms/disc with 0 mm zones for parent, delta-blaS1, complement and vector strains; 30 micrograms/disc gives 0 mm for delta-blaS1 and delta-blaS1 delta-blaE strains. Thus that tested phenotype does not demonstrate a BlaS1-dependent cefixime susceptibility change. Zero disc zones are not MICs, and unchanged susceptibility does not rule out cefixime hydrolysis or resistance contributions under other conditions. The cited 1997 purified-enzyme paper was read at complete-abstract depth; its full kinetic table was not open. The author-repository bitstream returned a request-copy HTML page, not an accessible PDF; no request was sent. |
| pbp | PMID:31362987; DOI:10.1074/jbc.RA119.009942; 225-pbp-full.html, original crystallographic methods, results and cefixime complex | supports | The original N. gonorrhoeae PBP2 transpeptidase-domain study includes a cefixime-acylated crystal structure at 1.7 angstrom resolution, with a covalent Ser310 linkage. Crystals were soaked with 50 mM cefixime for 5-7 minutes; part of the oxime side chain was disordered. This is direct compound-specific target evidence for the studied construct, distinct from clinical susceptibility. It could support a primary molecular-target enrichment without collapsing the taxon-agnostic native PBP family to one species. |
| cdc1280 | https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=10571&amp;PanelID=10; 225-cdc1280.html and 225-biosample1280.xml | supports | Official source identifies AR Bank 1280 / NEW-37, N. gonorrhoeae, BioSample SAMN35332250 and urethral-swab origin. Cefixime 1 microgram/mL equals native 1 mg/L, with R interpreted under CLSI 2026 M100 Ed36. The page explicitly calls these broth microdilution modal MICs. BioSample confirms isolate and NCBITaxon:485. The strain slot is used for isolate context, not an invented strain designation. |
| cdc1281 | https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=10572&amp;PanelID=10; 225-cdc1281.html and 225-biosample1281.xml | supports | Official source identifies AR Bank 1281 / NEW-38, N. gonorrhoeae, BioSample SAMN35332251 and urine origin. Cefixime &gt;1 microgram/mL equals native &gt;1 mg/L, and the native qualifier is preserved. R, CLSI 2026 M100 Ed36, broth microdilution and modal MIC match. BioSample confirms isolate and NCBITaxon:485. The page notes penA60.001, but these isolate observations alone do not establish allele causality. |
| adapter | iModulonDB structured source adapter; 225-imodulondb-datasets.txt; 225-imodulondb-ftsi.txt; 225-imodulondb-ampc.txt; 225-imodulondb-ctxm.txt | context_only | Catalog and matching organism queries preceded open-ended protein research. E. coli ftsI resolved to e_coli/modulome/b0084 and P. aeruginosa ampC to p_aeruginosa/precise364/PA4110, each with zero component hits. CTX-M returned no hit. No matching Neisseria, Citrobacter, Klebsiella or M. smegmatis dataset was available in the inspected catalog. These annotations neither verify specific resistance alleles nor supply direct target, phenotype or negative evidence. |
| owners | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_resistance_edges.tsv; data/raw/aro_target_edges.tsv; 225 owner-row snapshots and 225-local-hits.txt | supports | ChEBI owns chemical identity, synonyms, definition, parents, roles and its citation leads. ARO owns imported classification, target and resistance assertions. Source-row corrections belong in the maintained inventory/transform and must survive reseeding. The two curated activity observations belong to the native record and require the validated writer plus an accurate curation event for any future change. No separate exact-compound curator overlay was found in the bounded ignored-inclusive search. |
| validation | Focused native schema and strict validators; supplemental graph check; 225-strict.tsv; 225-chemistry.json | supports | Schema and strict commands passed with exit 0; strict has zero ERROR rows. Supplemental exact graph comparison passed using the existing 019 interpreter against 023 files. Required shared corpus gates are separate. |

## Limits And Additional Notes

- Two of 26 adopted/parent MED records have metadata only; the other 24 complete abstracts were read. Full texts were inspected for the specifically identified primary/review sources, not every lead. The 1997 BlaS kinetic paper remains abstract-only; an HTML request-copy form must not be mistaken for a PDF.
- The meningococcal PBP2 entry combines a source spelling error and taxon-mixed historical bibliography. A later exact-species cefixime/penA association was inspected, but isolated causal support was not established. Do not silently relabel this entry as gonococcal, because the record already has a separate gonococcal route.
- The cited BlaS1 deletion experiment shows unchanged cefixime disc phenotypes in its tested conditions. It neither establishes a BlaS1-dependent cefixime effect nor disproves biochemical activity. A future curator should seek the exact purified-enzyme substrate data or preserve this conflict in a scoped evidence note/discussion; no unconditional removal or universal absence claim is justified.
- Optional primary target/resistance enrichment must preserve native family-level grounding and add evidence at the molecular target or resistance object, with exact organism, allele and assay context. Curator additions use the validated writer and curation event; any imported-edge correction belongs to the ARO inventory/transform and must survive reseeding, schema and strict checks.
- The source definition describes historical treatment uses, not a claim of current guideline preference or universal efficacy. MICs belong to the two isolates and the stated CLSI edition. Recombinant E. coli expression data are not clinical resistance breakpoints or enzyme hydrolysis measurements.
- CAS and DrugBank were corroborated indirectly through inspected authorities; Beilstein was not independently resolved. DrugCentral was inspected at drug-card scope. Patent documents provide document/family context, not blanket exact-compound experimental evidence.
- The 023 environment lacks RDKit, so supplemental chemistry used the existing 019 interpreter. The initial adapter catalog attempt failed due to sandbox name resolution and the network-enabled retry succeeded. Focused checks do not replace shared corpus gates or confer native REVIEWED status.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 16 captured repository inputs and the separately recorded external ARO cache retain their original hashes. No native record, saved bundle or Git state was modified.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T112849Z-cefixime-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of cefixime
started_at: '2026-10-21T11:08:27Z'
finished_at: '2026-10-21T11:28:49Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
native_verdict: Exact identity and two curated MIC observations supported; two imported
  resistance routes retain bounded primary-source uncertainty
scientific_review: true
summary: The neutral anhydrous cefixime graph agrees with current ChEBI, PubChem,
  ChEMBL and both KEGG identifiers. Both CDC/FDA AR Isolate Bank MIC observations,
  including isolate identities, broth microdilution, units, breakpoint edition and
  the > qualifier, match their official sources. Compound-specific PBP2 binding and
  gonococcal resistance experiments were inspected. Supplementary data support cefixime
  susceptibility shifts for five imported beta-lactamase alleles in recombinant E.
  coli. The meningococcal PBP2 and BlaS1 routes remain honestly labeled database assertions
  with unresolved exact causal support; the BlaS1 deletion experiment did not change
  the measured cefixime disc phenotype. All 26 adopted or parent MED records resolve
  at their declared inspection depth. No confirmed required native correction was
  demonstrated. Scientific assessment retains the stated evidence limits; full verification
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
  - path: data/antibiotics/antibacterial/cefixime.yaml
    sha256: 0be56f6fce4ec99446caae688cd3410272edd3fb4a5b3b196f0ca9d766724837
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
scope:
  description: Entire exact SEEDED cefixime record, all seven history events, eight
    database resistance entries, the PBP family target, two curated MIC/BioSample
    observations, chemical/document/drug identifiers, actual owner rows and all 26
    adopted or parent PMID leads.
  selection: Queue 225. Original 13 initial inputs preserved; three actual ARO owner
    inputs appended before detailed judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:472657
targets:
- target_id: CHEBI:472657
  path: data/antibiotics/antibacterial/cefixime.yaml
  label: cefixime
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
    role: Actual ARO inventory or imported claim owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Actual ARO inventory or imported claim owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Actual ARO inventory or imported claim owner
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefixime.yaml
    role: Curator-owned activity observations and history, changed only via validated
      writer and curation event
checks:
- check_id: schema
  name: Documented schema check
  status: passed
  required: true
  summary: Exit 0.
  target_ids:
  - CHEBI:472657
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefixime.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented strict check
  status: passed
  required: true
  summary: Exit 0; zero ERROR rows.
  target_ids:
  - CHEBI:472657
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefixime.yaml --out /private/tmp/am-review-session/225-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Supplemental exact graph comparison
  status: passed
  required: false
  summary: Exit 0 using the 019 interpreter against 023 files.
  target_ids:
  - CHEBI:472657
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/225-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: adapter-initial
  name: Structured catalog initial attempt
  status: failed
  required: false
  summary: Sandbox network name resolution failed, exit 2; the same public read was
    retried successfully with network access.
  target_ids:
  - CHEBI:472657
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets > /private/tmp/am-review-session/225-imodulondb-datasets.txt
  exit_code: 2
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-catalog
  name: Structured catalog retry
  status: passed
  required: false
  summary: Network-enabled retry passed, exit 0; catalog inspected before protein
    web research.
  target_ids:
  - CHEBI:472657
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets > /private/tmp/am-review-session/225-imodulondb-datasets.txt
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-ftsi
  name: Structured protein query
  status: passed
  required: false
  summary: Found e_coli/modulome/b0084, with no component hits.
  target_ids:
  - CHEBI:472657
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset modulome --query ftsI
    > /private/tmp/am-review-session/225-imodulondb-ftsi.txt
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-ampc
  name: Structured protein query
  status: passed
  required: false
  summary: Found p_aeruginosa/precise364/PA4110, with no component hits; not allele-specific
    PDC-3/PDC-5 evidence.
  target_ids:
  - CHEBI:472657
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism p_aeruginosa --dataset precise364 --query
    ampC > /private/tmp/am-review-session/225-imodulondb-ampc.txt
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-ctxm
  name: Structured protein query
  status: passed
  required: false
  summary: No hit; not negative biological evidence.
  target_ids:
  - CHEBI:472657
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset modulome --query CTX-M
    > /private/tmp/am-review-session/225-imodulondb-ctxm.txt
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
  - CHEBI:472657
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
  - CHEBI:472657
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
  - CHEBI:472657
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
  - CHEBI:472657
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
  - CHEBI:472657
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
  - CHEBI:472657
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
  - CHEBI:472657
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
  - CHEBI:472657
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
  - CHEBI:472657
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/cefixime.yaml
  locator: Entire native YAML, including two activity observations and seven history
    events
  accessed_at: '2026-10-21T11:18:04Z'
  support: supports
  summary: Exact neutral cefixime is SEEDED. Eight resistance entries explicitly cite
    CARD/ARO as database assertions; the PBP family target explicitly needs primary
    evidence and lacks organism/assay specification. Five history events are source
    seeding, followed by resistant-taxa and BioSample curation. There is no populated
    mode, target scope, producer or causal graph.
- evidence_id: chemistry
  kind: validation
  reference: CHEBI:472657; PubChem:5362065; CHEMBL1541; KEGG:D00258; KEGG:C06881
  locator: 225-chemistry.py/.json and authority structure snapshots
  accessed_at: '2026-10-21T11:18:04Z'
  support: supports
  summary: Native SMILES and InChI agree with full key OKBVVJOGVLARMR-QSWIMTSFSA-N,
    formula C16H15N5O7S2, charge 0 and masses. Current ChEBI, PubChem, ChEMBL and
    both KEGG graphs match the 6R/7R, Z-oxime neutral anhydrous free acid. This does
    not equate the exact record to cefixime trihydrate or a salt.
  snapshot_sha256: 3a1ed068fe0693a653fbe6d1b40ae20ab4b2fb65c9a23fa7f59a6869512ba8ad
- evidence_id: grounding
  kind: authority
  reference: ARO:3000646; CHEBI:23066; ARO:0000032; CHEBI:33281; CHEBI:36047
  locator: 225-ols.json; 225-aro-stanzas.txt; 225-card.html; 225-drugcentral.html;
    225-kegg.txt
  accessed_at: '2026-10-21T11:18:04Z'
  support: supports
  summary: Compound, cephalosporin parent/class, antimicrobial and antibacterial roles
    agree with native identity and owner rows. All eight determinant CURIEs and the
    PBP family CURIE resolve in the adopted ARO cache; current CARD preserves the
    imported relationships. CAS 79350-37-1 is corroborated through authorities, not
    direct registry access. DrugCentral 537 and KEGG D00258 resolve in drug context;
    DrugBank DB00671 is corroborated through ChEBI/DrugCentral rather than a directly
    inspected DrugBank record. Beilstein 6025058 was not independently resolved.
  snapshot_sha256: ea5de30b632d4f22da5a7830ebbbeed7c47c317b04501217197c2bc21fdd9585
- evidence_id: patents
  kind: primary_source
  reference: patent:EP30630; patent:US4409214
  locator: 225-patent-ep.html and 225-patent-us.html
  accessed_at: '2026-10-21T11:18:04Z'
  support: context_only
  summary: The abbreviated patent links resolve through EP0030630B1 and US4409214A,
    members of the same cephalosporin patent family. The US text includes the syn
    carboxymethoxyimino aminothiazolyl vinyl cephalosporin in its named compound M
    / compound 13 context. These document references are not exact chemical xrefs,
    and family-wide activity is not imported as a cefixime-specific MIC. The attempted
    EP0030630A1 URL returned 404; the inspected B1 document succeeded.
  snapshot_sha256: 867a2a1509cf58a049b20d7c022a8d27035d0df6d1a16ad757f4a4f2cd6f4115
- evidence_id: adopted-leads
  kind: database
  reference: 26 adopted or parent PMID records
  locator: 225-core.json; 225-lead-dispositions.json
  accessed_at: '2026-10-21T11:18:04Z'
  support: context_only
  summary: All 26 MED records resolve. All 24 returned complete abstracts were read.
    Parent reviews 15673804 and 6810737 have metadata only. Original full text was
    additionally inspected for 16940068, 23587946 and 33416461, together with the
    2016 two-species review 27690121. Original 15699201 methods/results/tables/discussion
    were read through the public author-uploaded text; local download failed. Each
    remaining lead is individually scoped in the disposition ledger.
  snapshot_sha256: f3e15faa6a37230b6261d6dff52c2a273d9a65a753c07516d6e350c12b1bfeca
- evidence_id: enzyme-panel
  kind: primary_source
  reference: PMID:33416461; DOI:10.1099/mgen.0.000500
  locator: 225-primary-ctxm.xml; supplementary Table S1 (225-mgen-7-500-s002.xlsx,
    rows 52-59); Figure S6 (225-mgen-7-500-s001.pdf)
  accessed_at: '2026-10-21T11:18:04Z'
  support: supports
  summary: The original recombinant E. coli BW25113/pGDP1 broth microdilution experiment
    reports cefixime MIC 0.25 micrograms/mL for control, >256 for CMY-2, 32 for CTX-M-3,
    4 for CTX-M-27, and >256 for both PDC-3 and PDC-5. This supports allele-specific
    susceptibility shifts in that expression system. It is not direct cefixime hydrolysis
    kinetics or proof of clinical resistance in every native host; the source expressly
    lacks a P. aeruginosa cefixime breakpoint. Direct PMC supplementary routes returned
    challenge HTML, but the Europe PMC supplementary ZIP was successfully retrieved
    and its real XLSX/PDF inspected.
  snapshot_sha256: 76429199f62baa3ca6586c9756e2d14fa019ef13dcffb3f3bcb46f8b45823390
- evidence_id: gonococcal-resistance
  kind: primary_source
  reference: PMID:16940068; PMID:23587946
  locator: 225-nmen-original.html and 225-ngon-full.html, original methods/results/tables
    and discussion
  accessed_at: '2026-10-21T11:18:04Z'
  support: supports
  summary: Despite the scratch filename, PMID16940068 is a gonococcal, not meningococcal,
    study of mosaic PBP2 substitutions and cefixime susceptibility. PMID23587946 tests
    H041 penA substitutions in gonococcal backgrounds, supporting a causal contribution
    of altered PBP2 to expanded-spectrum cephalosporin resistance. Effects depend
    on allele and genetic background. These support the gonococcal ARO route, not
    automatic transfer of the same experiment to N. meningitidis.
  snapshot_sha256: 7b51956ec9f6656925eed1c9accc461499037192215feb234d978ccd0b012890
- evidence_id: meningococcal-scope
  kind: primary_source
  reference: ARO:3003937; PMID:27690121; DOI:10.3201/eid3110.250464
  locator: 225-aro-stanzas.txt; 225-primary-nmen-review.xml; 225-nmen2025.html
  accessed_at: '2026-10-21T11:18:04Z'
  support: partial
  summary: The meningococcal ARO term has a source-label typo and a historical citation
    set containing gonococcal primary experiments. The 2016 review treats both species
    and reports meningococcal penicillin/third-generation cephalosporin observations,
    including unpublished penA327 transformation context; this is not a fully inspected
    exact cefixime causal experiment. The 2025 original Thai urethritis study reports
    N. meningitidis NM7 with elevated cefixime susceptibility-test values and a mosaic
    penA2840 related to gonococcal penA60. It supports a bounded exact-species association,
    not isolated allele causality. The native entry is honestly database-level; primary
    causal support remains unresolved.
  snapshot_sha256: 573ee073ead450b45842ba364281a92ecaf9a25c174547e6d1633bdec0b3906a
- evidence_id: blas-scope
  kind: primary_source
  reference: ARO:3005111; PMID:15699201; PMID:9103972
  locator: 225-blas2005-web-observations.json; original 2005 Tables 3 and 6 via public
    author-uploaded text; 225-core.json and 225-blas1997-orbi.html
  accessed_at: '2026-10-21T11:18:04Z'
  support: partial
  summary: The cited 2005 M. smegmatis experiment reports cefixime 5 micrograms/disc
    with 0 mm zones for parent, delta-blaS1, complement and vector strains; 30 micrograms/disc
    gives 0 mm for delta-blaS1 and delta-blaS1 delta-blaE strains. Thus that tested
    phenotype does not demonstrate a BlaS1-dependent cefixime susceptibility change.
    Zero disc zones are not MICs, and unchanged susceptibility does not rule out cefixime
    hydrolysis or resistance contributions under other conditions. The cited 1997
    purified-enzyme paper was read at complete-abstract depth; its full kinetic table
    was not open. The author-repository bitstream returned a request-copy HTML page,
    not an accessible PDF; no request was sent.
  snapshot_sha256: c8ad0ddd8e125029b53047c3282dabcef8dd0d726912a7e91ad1ca44a82fb1a5
- evidence_id: pbp
  kind: primary_source
  reference: PMID:31362987; DOI:10.1074/jbc.RA119.009942
  locator: 225-pbp-full.html, original crystallographic methods, results and cefixime
    complex
  accessed_at: '2026-10-21T11:18:04Z'
  support: supports
  summary: The original N. gonorrhoeae PBP2 transpeptidase-domain study includes a
    cefixime-acylated crystal structure at 1.7 angstrom resolution, with a covalent
    Ser310 linkage. Crystals were soaked with 50 mM cefixime for 5-7 minutes; part
    of the oxime side chain was disordered. This is direct compound-specific target
    evidence for the studied construct, distinct from clinical susceptibility. It
    could support a primary molecular-target enrichment without collapsing the taxon-agnostic
    native PBP family to one species.
  snapshot_sha256: fa89c604319b696ade4498cc7dd9e8a1f85c2f494ac14a491ecb7defd3daa487
- evidence_id: cdc1280
  kind: authority
  reference: https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=10571&PanelID=10
  locator: 225-cdc1280.html and 225-biosample1280.xml
  accessed_at: '2026-10-21T11:18:04Z'
  support: supports
  summary: Official source identifies AR Bank 1280 / NEW-37, N. gonorrhoeae, BioSample
    SAMN35332250 and urethral-swab origin. Cefixime 1 microgram/mL equals native 1
    mg/L, with R interpreted under CLSI 2026 M100 Ed36. The page explicitly calls
    these broth microdilution modal MICs. BioSample confirms isolate and NCBITaxon:485.
    The strain slot is used for isolate context, not an invented strain designation.
  snapshot_sha256: 6614d1c3cf72ebcf18738c0e6b92edc05baa754d89bfb88737b4352251a02255
- evidence_id: cdc1281
  kind: authority
  reference: https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=10572&PanelID=10
  locator: 225-cdc1281.html and 225-biosample1281.xml
  accessed_at: '2026-10-21T11:18:04Z'
  support: supports
  summary: Official source identifies AR Bank 1281 / NEW-38, N. gonorrhoeae, BioSample
    SAMN35332251 and urine origin. Cefixime >1 microgram/mL equals native >1 mg/L,
    and the native qualifier is preserved. R, CLSI 2026 M100 Ed36, broth microdilution
    and modal MIC match. BioSample confirms isolate and NCBITaxon:485. The page notes
    penA60.001, but these isolate observations alone do not establish allele causality.
  snapshot_sha256: 4a07c05b09006aad1111e7b22975c2f87b14715d5e20e061bb96ebd3330be52c
- evidence_id: adapter
  kind: database
  reference: iModulonDB structured source adapter
  locator: 225-imodulondb-datasets.txt; 225-imodulondb-ftsi.txt; 225-imodulondb-ampc.txt;
    225-imodulondb-ctxm.txt
  accessed_at: '2026-10-21T11:18:04Z'
  support: context_only
  summary: Catalog and matching organism queries preceded open-ended protein research.
    E. coli ftsI resolved to e_coli/modulome/b0084 and P. aeruginosa ampC to p_aeruginosa/precise364/PA4110,
    each with zero component hits. CTX-M returned no hit. No matching Neisseria, Citrobacter,
    Klebsiella or M. smegmatis dataset was available in the inspected catalog. These
    annotations neither verify specific resistance alleles nor supply direct target,
    phenotype or negative evidence.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_resistance_edges.tsv;
    data/raw/aro_target_edges.tsv
  locator: 225 owner-row snapshots and 225-local-hits.txt
  accessed_at: '2026-10-21T11:18:04Z'
  support: supports
  summary: ChEBI owns chemical identity, synonyms, definition, parents, roles and
    its citation leads. ARO owns imported classification, target and resistance assertions.
    Source-row corrections belong in the maintained inventory/transform and must survive
    reseeding. The two curated activity observations belong to the native record and
    require the validated writer plus an accurate curation event for any future change.
    No separate exact-compound curator overlay was found in the bounded ignored-inclusive
    search.
  snapshot_sha256: 0346c1c607c7c107a4a885e0155645baa91a4e5e6813d4bf80a394f8718bab69
  search_scope: rg --no-ignore --hidden across curation, conf, data/antibiotics, scripts
    and docs for cefixime, CHEBI:472657, ARO:3000646 and the exact key; full matching
    adopted rows inspected.
- evidence_id: validation
  kind: validation
  reference: Focused native schema and strict validators; supplemental graph check
  locator: 225-strict.tsv; 225-chemistry.json
  accessed_at: '2026-10-21T11:18:04Z'
  support: supports
  summary: Schema and strict commands passed with exit 0; strict has zero ERROR rows.
    Supplemental exact graph comparison passed using the existing 019 interpreter
    against 023 files. Required shared corpus gates are separate.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact chemical form and stereochemistry
  outcome: supported
  summary: All compared exact structures agree with neutral anhydrous cefixime.
  target_ids:
  - CHEBI:472657
  evidence_ids:
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: Chemical class, roles and identifier placement
  outcome: supported
  summary: Exact chemical xrefs, broader parents and contextual drug/patent links
    are consistently separated at the inspected depth.
  target_ids:
  - CHEBI:472657
  evidence_ids:
  - grounding
  - patents
  - chemistry
- assessment_id: activity
  area: evidence
  topic: Two curated MIC and BioSample observations
  outcome: supported
  summary: Both official observations agree with values, qualifier, method, units,
    isolates, BioSamples and breakpoint edition.
  target_ids:
  - CHEBI:472657
  evidence_ids:
  - cdc1280
  - cdc1281
- assessment_id: target
  area: evidence
  topic: PBP direct binding
  outcome: supported
  summary: Primary cefixime-acylated PBP2 structure supports the family-level target;
    native evidence remains honestly database-qualified pending primary curation.
  target_ids:
  - CHEBI:472657
  evidence_ids:
  - pbp
  - record
- assessment_id: resistance
  area: evidence
  topic: Five enzyme alleles and gonococcal PBP2
  outcome: supported
  summary: Recombinant enzyme-expression susceptibility results and gonococcal penA
    experiments support bounded routes; no clinical-host or hydrolysis overgeneralization
    is made.
  target_ids:
  - CHEBI:472657
  evidence_ids:
  - enzyme-panel
  - gonococcal-resistance
- assessment_id: resistance-limits
  area: evidence
  topic: Meningococcal PBP2 and BlaS1 causal evidence
  outcome: unknown
  summary: Historical citation taxon scope, later meningococcal association and unchanged
    BlaS1 deletion disc phenotypes leave exact causal support unresolved. These limits
    do not prove the database assertions false.
  target_ids:
  - CHEBI:472657
  evidence_ids:
  - meningococcal-scope
  - blas-scope
- assessment_id: provenance
  area: provenance
  topic: All leads, source owners and seven history events
  outcome: supported
  summary: The source and curator-owned slices are distinct; all 26 adopted/parent
    MED records resolve at declared depth.
  target_ids:
  - CHEBI:472657
  evidence_ids:
  - adopted-leads
  - owners
  - record
- assessment_id: schema
  area: schema
  topic: Focused deterministic checks
  outcome: supported
  summary: Focused schema, strict and supplemental chemistry checks passed.
  target_ids:
  - CHEBI:472657
  evidence_ids:
  - validation
findings: []
actions: []
limitations:
- Two of 26 adopted/parent MED records have metadata only; the other 24 complete abstracts
  were read. Full texts were inspected for the specifically identified primary/review
  sources, not every lead. The 1997 BlaS kinetic paper remains abstract-only; an HTML
  request-copy form must not be mistaken for a PDF.
- The meningococcal PBP2 entry combines a source spelling error and taxon-mixed historical
  bibliography. A later exact-species cefixime/penA association was inspected, but
  isolated causal support was not established. Do not silently relabel this entry
  as gonococcal, because the record already has a separate gonococcal route.
- The cited BlaS1 deletion experiment shows unchanged cefixime disc phenotypes in
  its tested conditions. It neither establishes a BlaS1-dependent cefixime effect
  nor disproves biochemical activity. A future curator should seek the exact purified-enzyme
  substrate data or preserve this conflict in a scoped evidence note/discussion; no
  unconditional removal or universal absence claim is justified.
- Optional primary target/resistance enrichment must preserve native family-level
  grounding and add evidence at the molecular target or resistance object, with exact
  organism, allele and assay context. Curator additions use the validated writer and
  curation event; any imported-edge correction belongs to the ARO inventory/transform
  and must survive reseeding, schema and strict checks.
- The source definition describes historical treatment uses, not a claim of current
  guideline preference or universal efficacy. MICs belong to the two isolates and
  the stated CLSI edition. Recombinant E. coli expression data are not clinical resistance
  breakpoints or enzyme hydrolysis measurements.
- CAS and DrugBank were corroborated indirectly through inspected authorities; Beilstein
  was not independently resolved. DrugCentral was inspected at drug-card scope. Patent
  documents provide document/family context, not blanket exact-compound experimental
  evidence.
- The 023 environment lacks RDKit, so supplemental chemistry used the existing 019
  interpreter. The initial adapter catalog attempt failed due to sandbox name resolution
  and the network-enabled retry succeeded. Focused checks do not replace shared corpus
  gates or confer native REVIEWED status.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 16 captured repository inputs and the separately recorded external ARO cache
  retain their original hashes. No native record, saved bundle or Git state was modified.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://doi.org/10.1099/mgen.0.000500
- https://doi.org/10.1074/jbc.RA119.009942
- https://doi.org/10.1099/mic.0.27629-0
- https://wwwnc.cdc.gov/eid/article/31/10/25-0464_article
tags:
- record-review
- cefixime
- resistance-evidence
- curated-mic
```
