# Butremycin: inherited C3 stereochemistry conflicts with the primary natural product

- Review: 20261021T103515Z-butremycin
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:11:09Z
- Finished UTC: 2026-10-21T10:35:15Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Natural butremycin has primary culture-production and weak antibacterial evidence. A confirmed blocker remains: the native and current ChEBI structures encode paper-numbered C2=S, C3=R, whereas the original paper explicitly assigns relative 2S*,3S* and the follow-up identifies the product as 3S. Both native strings are internally consistent and pass deterministic checks, so this is a scientific identity conflict rather than a parsing defect. PubChem/NPAtlas cannot be substituted wholesale because they also differ in tautomer and alkene-geometry representation. One informational follow-up concerns primary activity and producer enrichment after identity adjudication.

## Scope And Provenance

Whole CHEBI152570 seed, including definition, exact systematic synonym, five parents, antibacterial role, fully specified stereochemical structure, masses, source concept/mint and three history entries. Both adopted citation leads were inspected.

Selection: Queue 175; exact preserved initial capture and path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:152570 | data/antibiotics/antibacterial/butremycin.yaml | generated | butremycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:152570 | Actual focused command exited 0. |
| strict | passed | True | CHEBI:152570 | Actual focused command exited 0. |
| chemistry | passed | False | CHEBI:152570 | Actual focused command exited 0. Both strings parse and agree with the asserted key, formula, charge, masses and source mint. This internal agreement does not resolve the primary-literature C3 stereochemistry conflict. |
| Independent mapping of paper-numbered C2 and C3 | passed | False | CHEBI:152570 | Both native strings give C2=S, C3=R. The sole tetrahedral alcohol carbon is C3, adjacent to N-bearing tetramic C2 and methylene C4. PubChem/NPAtlas give C2=S, C3=S. Passing this diagnostic establishes the discrepancy, not a clean identity verdict. |
| Authoritative full QC | failed | True | CHEBI:152570 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:152570 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:152570 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:152570 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:152570 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:152570 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:152570 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:152570 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:152570 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Natural-product C3 stereochemistry

identity: concern. Targets: CHEBI:152570.

Native C2S/C3R conflicts with the original relative C2S*/C3S* relationship and follow-up 3S identification. This is a diastereomer distinction, not merely an unspecified absolute enantiomer or harmless tautomer spelling.

### Internal structure and alternative database boundaries

representation: supported. Targets: CHEBI:152570.

The native strings parse and agree internally. Alternative databases differ in multiple representation dimensions, so a wholesale replacement would lose supported alkene geometry and change the selected tautomer.

### Definition, parent classes and activity role

grounding: concern. Targets: CHEBI:152570.

The scaffold classes and source definition are appropriate for natural butremycin. Exact identity remains blocked by the encoded C3 epimer, so the natural-product activity cannot be considered independently verified for the current full structure.

### Weak antibacterial observations

evidence: supported. Targets: CHEBI:152570.

The original isolated compound has explicit weak MIC data. No claim that the C3R epimer is inactive, or that all MRSA isolates are susceptible, follows.

### Micromonospora K310 source and biosynthetic context

provenance: supported. Targets: CHEBI:152570.

The natural-product isolation sentence is supported by pure-culture fermentation and exact strain accession. Engineered expression hosts and enzyme-donor strains must remain distinct from the natural producer.

### No established exact antibacterial target

completeness: unknown. Targets: CHEBI:152570.

No direct antibacterial target or killing chain was established by the two adopted papers. Tailoring hydroxylases synthesize product rather than being demonstrated inhibited antimicrobial targets; the co-isolated compound's quorum-sensing discussion does not transfer.

### Both adopted citation dispositions

provenance: supported. Targets: CHEBI:152570.

The 2014 isolation/weak-activity paper and 2015 biosynthetic-conversion paper were inspected in complete main text. Read scope and supplementary/figure limits are explicit.

### Inherited structure and future evidence ownership

ownership: supported. Targets: CHEBI:152570.

ChEBI source/extractor/seeder own identity correction; exact primary additions belong to the actual native record after identity adjudication. All initial hashes remain unchanged.

### Focused checks versus scientific identity

schema: supported. Targets: CHEBI:152570.

Documented per-record gates and internal chemistry pass, with no inference of scientific sign-off. The newly demonstrated literature conflict remains open.

## Findings

### F1: Resolve the inherited C3 epimer before treating this as exact natural butremycin

blocker / open / confirmed; issue key: butremycin-source-c3-epimer-conflicts-primary.

Both native strings encode paper C2=S, C3=R. The accessible original paper explicitly assigns relative 2S*,3S* and rejects the 2S*,3R* alternative; original Figure 1 and the later 3S product identification corroborate that difference. Current ChEBI carries the same conflict, including the systematic synonym. Internal parser agreement does not validate the source against primary chemistry.

### F2: After identity correction, add narrowly scoped primary activity and culture-production evidence

informational / open / confirmed; issue key: butremycin-qualified-activity-producer-enrichment.

Primary weak MIC and pure-culture production observations are available but not yet represented as record evidence. Their absence is an optional enrichment opportunity. Biosynthetic enzymes, engineered production hosts and compound 3 quorum-sensing discussion must not become antibacterial target claims.

## Recommended Actions And Acceptance Checks

### A1

Adjudicate the source stereochemistry and implement a reproducible identity correction.

- Map original paper positions to every encoded stereocentre, explicitly checking C2/C3. Reconcile the 2014 relative assignment with the 2015 authentic-sample coelution result; preserve the distinction between relative assignment, literature absolute designation and an independent absolute determination.
- Correct the maintained ChEBI-derived structure and systematic synonym together through a documented exact-source correction or upstream resolution. The scratch single-C3 inversion key IJOMIIDEKGZJJF-PQYAVTRXSA-N is a diagnostic candidate only; confirm the entire structure, selected tautomer and alkene geometries before adoption.
- Do not substitute PubChem 139588066 or NPAtlas NPA017854 wholesale: their current representation shifts the tetramic enol and omits the native macrocyclic E/Z annotations. If the external CHEBI grounding cannot be reconciled, explicitly adjudicate it through maintained source/decision ownership instead of asserting a false EXACT match.
- Regenerate through the documented pipeline, check SMILES/InChI/key/formula/charge/stereochemistry and source mint coherently, and run focused and shared native checks. Use validated curation/history entrypoints; leave scientific status unchanged until all review requirements are met.

### A2

Curate exact primary observations only after the structural identity is resolved.

- Attach PMID 24534843 at the narrow supported claim: Table 3 MIC of 50 micrograms/mL for ATCC 25923, ATCC 25922 and EMRSA 15, and &gt;50 for SMRSA 105, 124 and 116. Preserve comparator, units, 18-hour Mueller–Hinton broth conditions, optical no-growth endpoint and the strict greater-than censoring. These are individual test results, not MIC50 panel statistics or clinical breakpoints.
- For producer_organisms, use pure-culture fermentation/isolation evidence for Micromonospora sp. K310 and independently verified strain accession KF803252.1/taxon 1453323. Do not claim that the 16S accession is a biosynthetic gene cluster or that every related species produces the compound.
- Separate engineered E. coli production and hydroxylase-mediated conversion in PMID 25711294 from natural production. Do not add these tailoring enzymes as inhibited molecular targets, and do not transfer the other compound's methylthioadenosine/quorum-sensing pathway to butremycin.
- Use write_validated_antibiotic and record_curation_event on data/antibiotics/antibacterial/butremycin.yaml for separately authorized curation, preserve additions across reseeding and run applicable validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/butremycin.yaml; Entire record including all structural descriptors and three history events. | supports | SEEDED/EXACT ChEBI record. The definition describes the 3-hydroxyl derivative of ikarugamycin isolated from Micromonospora sp. K310. It has no curated evidence objects, target, mode of action, causal graph, activity spectrum, producer object or resistance mechanism; these absent optional fields are not independently classified as errors. |
| source | data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Exact source row 2734; source quality/role filter, structure import and citation-lead handling. | supports | The source row reproduces the native definition, exact synonym, five parents, antibacterial role and full structures. Both citation leads are retained in the inventory. Extractor lines 329–332 intentionally keep source literature leads out of record evidence until a curator determines which exact claim they support. No exact corrective curator/decision row was found in the hidden-and-ignored-inclusive maintained search. All 13 initial source hashes remain unchanged. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:152570; Complete official page including structure, ontology, species and names. | supports | Current ChEBI matches the native C29H38N2O5 neutral structure, key IJOMIIDEKGZJJF-KSCHHOEWSA-N, average mass 494.632 and monoisotopic mass 494.27807. Parents CHEBI24995, CHEBI26188, CHEBI38164, CHEBI51689 and CHEBI52898 are lactam, polyketide, organic heteropentacyclic compound, enone and azamacrocycle. CHEBI33282 is antibacterial agent. The source systematic synonym agrees with the source structure, including the conflicting alcohol stereocentre. Broader bacterial/marine metabolite roles and functional-parent relation to ikarugamycin are not missing antimicrobial-role errors. |
| chemistry | 175-chemistry.json; Independent SMILES/InChI parsing and source-mint calculation. | supports | Both native strings parse as one neutral molecule with ten assigned tetrahedral centres and specified macrocyclic E/Z geometry. Their exact key, composition, charge, masses and mint reproduce. These are internal-consistency results; they do not independently establish that the encoded C3 epimer is the natural product. |
| stereo | 175-stereo-check.py; 175-stereo-check.json; Graph-based paper-position mapping, independently checked from both strings. | refutes | The sole tetrahedral alcohol carbon is paper C3: native SMILES atom25 is R, next to N-bearing tetramic C2 atom21=S and methylene C4 atom27. Independent InChI parsing yields the same C2S/C3R pair. PubChem/NPAtlas yield C2S/C3S. Inverting only native C3 produces diagnostic key IJOMIIDEKGZJJF-PQYAVTRXSA-N while retaining native tautomer and specified alkene geometry; this is a candidate for adjudication, not a validated complete replacement. |
| primary2014-identity | PMID:24534843; DOI:10.3390/md12020999; https://pmc.ncbi.nlm.nih.gov/articles/PMC3944527/; Complete original main text and author-deposited PDF; Figure 1 p1001 and Figure 3/p1003 visually inspected. | refutes | Compound 2 is butremycin. The paper establishes the 3-hydroxylated PTM skeleton and explicitly assigns relative 2S*,3S*, rejecting 2S*,3R* using the small H2–H3 coupling. Figure 1 depicts the corresponding C3 alcohol orientation. The relative conflict suffices to distinguish the native diastereomer; it does not require treating the paper's relative assignment as a new absolute crystallographic determination. |
| primary2014-activity | PMID:24534843; DOI:10.3390/md12020999; Table 3 and Methods 3.6; table cells checked independently of flattened text. | partial | Natural butremycin MIC is 50 micrograms/mL against S. aureus ATCC 25923, E. coli ATCC 25922 and EMRSA 15; values are &gt;50 for SMRSA 105, 124 and 116. Assays use Mueller–Hinton broth, OD620-standardized cultures and no-growth endpoint after 18 hours at 37 degrees C. These are weak antibacterial results, not MBCs or universal clinical resistance breakpoints. The tested natural material is not evidence for the native C3R epimer. |
| primary2014-production | PMID:24534843; DOI:10.3390/md12020999; Sections 2.2–2.3, 3.3–3.5: repeated colony purification, fermentation and purified product isolation. | supports | The investigators isolated a pure K310 culture from Ghanaian mangrove river sediment, fermented it and purified 46.6 mg of compound 2 from culture material. This supports culture-associated production by the named strain, beyond merely detecting a metabolite in an environmental extract. It does not map a genetically demonstrated K310 biosynthetic pathway. Quorum-sensing and methylthioadenosine degradation discussion concerns compound 3, not butremycin. |
| primary2015 | PMID:25711294; DOI:10.1039/C5CC00843C; https://pubs.rsc.org/en/content/articlepdf/2015/cc/c5cc00843c; Complete three-page publisher PDF text extraction successfully inspected; p5335 product paragraph and p5336 footnote 18; 175-2015-inspected-notes.txt records access scope. | supports | The follow-up infers 3S product configuration from coelution with an authentic K310 sample on several phases, including a chiral phase. It reports engineered E. coli BAP1 production using ikarugamycin genes and a Lysobacter hydroxylase, plus enzymatic conversion experiments. These are biosynthetic tailoring experiments, not antimicrobial target inhibition. Binary retrieval and later screenshot/open attempts returned 403; no 2015 figure image or unavailable supplementary data was inspected. |
| genbank | https://www.ncbi.nlm.nih.gov/nuccore/KF803252.1; Complete official GenBank flat file for KF803252.1. | supports | The 1455-base partial 16S record explicitly identifies Micromonospora sp. K310, strain K310, taxon 1453323, Ghanaian mangrove-river sediment and PMID 24534843. It is an organism identity accession, not a butremycin biosynthetic gene-cluster sequence. |
| alternative-databases | https://www.npatlas.org/explore/compounds/NPA017854; https://pubchem.ncbi.nlm.nih.gov/compound/139588066; Complete NPAtlas entry and official PubChem name-query property response. | partial | Both name butremycin and encode C2S/C3S, but use key GVTUJXRGYOLNJB-WGOSSAFXSA-N with a different tetramic enol placement and unspecified macrocyclic alkene geometry. They corroborate the local C3 distinction but are not structure-exact equivalents of the current ChEBI string and cannot be adopted wholesale. A PubChem query for the native full key returned 404; that is an access/result limit, not proof that no other database contains it. |
| adapter | Structured-source applicability assessed before open-ended web research; Complete native record and previously inspected iModulonDB dataset catalog. | context_only | The record asserts no gene, protein, regulator, stress-response or transcriptomic dataset. No native expression claim required an iModulonDB query. Newly inspected biosynthetic enzymes and engineered E. coli hosts do not justify antimicrobial molecular targets; no transcriptomic claim is added. |
| search | 175-local-hits.txt; 175-maintained-search.txt; 175-inclusive-file-hits.txt; Exact identifier, label, slug and both full-key stems; hidden and ignored files included. | context_only | The broader search found native/raw entries, path ledger, generated chemical maps and readiness-queue lead. No separate maintained correction or primary curated evidence object was found in the stated scope. Generated maps and historical reports are not scientific evidence. |
| validation | 175-focused-results.json; 175-schema.log; 175-strict.log; Actual documented per-record schema and strict commands plus independent chemistry. | supports | All three actual focused checks exit 0. A separate successful stereochemical diagnostic demonstrates why those checks do not establish literature-concordant identity. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; docs/record-review-profile.md; docs/record-reviews.md; CLAUDE.md; Native exact-structure contract and evidence/status requirements. | supports | Wrong chemical identity is a blocker even when strings agree internally. Required evidence must match exact stereochemical scope; optional producer, mechanism and AST fields are not automatically required omissions. |

## Limits And Additional Notes

- Initial capture preceded assessment; all 13 source input hashes remain unchanged. Complete record, exact maintained row and relevant source config/extraction/seeding code were inspected.
- The complete 2014 main text, tables and original Figures 1 and 3 were inspected. Supplementary captions were read and Figure S1 inspected visually; the entire NMR dataset was not independently reprocessed.
- The 2014 main text and Figure S1 print [M+H]+ 495.2781, whereas the neutral formula mass is 494.27807 and its protonated exact mass would be approximately 495.28535. This source numerical inconsistency is preserved; it does not justify changing the native neutral formula or masses, and the stereochemical finding rests on graph mapping, original drawing and explicit relative assignment.
- The 2015 publisher PDF text extraction succeeded once and all three pages were read. Subsequent direct download, screenshot and open requests returned 403; inspected passage and access notes are retained, not mislabeled as a binary PDF snapshot. Supporting-information routes returned 404 and a thesis download produced a bot challenge.
- Original 2014 relative stereochemistry independently establishes the C2/C3 conflict. The later 3S assignment corroborates it but is based on authentic-sample chromatographic comparison; a complete independent absolute-configuration redetermination was not performed here.
- PubChem and NPAtlas agree with each other but differ from ChEBI in tautomer placement, alkene specification and C3 configuration. Neither is treated as an automatically correct complete replacement.
- No exact antibacterial target, causal mechanism, resistance determinant or comprehensive public dataset inventory was established. No native expression claim required iModulonDB.
- The observed weak antibacterial activity belongs to the natural product. This review does not prove the encoded C3R epimer inactive or establish any clinical-use claim.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T103515Z-butremycin
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Butremycin: inherited C3 stereochemistry conflicts with the primary natural
  product'
started_at: '2026-10-21T10:11:09Z'
finished_at: '2026-10-21T10:35:15Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author the record. Preserved initial captures, read
    the complete native record and maintained row/configuration/transforms, independently
    mapped stereocentres from both native structure strings, and inspected original
    isolation and biosynthetic-conversion papers. Coordinator independently corroborated
    the C2/C3 mapping and original Figure 1.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'Natural butremycin has primary culture-production and weak antibacterial
  evidence. A confirmed blocker remains: the native and current ChEBI structures encode
  paper-numbered C2=S, C3=R, whereas the original paper explicitly assigns relative
  2S*,3S* and the follow-up identifies the product as 3S. Both native strings are
  internally consistent and pass deterministic checks, so this is a scientific identity
  conflict rather than a parsing defect. PubChem/NPAtlas cannot be substituted wholesale
  because they also differ in tautomer and alkene-geometry representation. One informational
  follow-up concerns primary activity and producer enrichment after identity adjudication.'
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
  - path: data/antibiotics/antibacterial/butremycin.yaml
    sha256: aeac906ae943bba8cd55c8a943f9ca494c5b41702229a1605b570e633550d308
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
targets:
- target_id: CHEBI:152570
  path: data/antibiotics/antibacterial/butremycin.yaml
  label: butremycin
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
  description: Whole CHEBI152570 seed, including definition, exact systematic synonym,
    five parents, antibacterial role, fully specified stereochemical structure, masses,
    source concept/mint and three history entries. Both adopted citation leads were
    inspected.
  selection: Queue 175; exact preserved initial capture and path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:152570
  exclusions:
  - target: Ikarugamycin, compound 3 methylthioinosine derivative, other PTMs and
      engineered expression hosts as exact equivalents
    reason: These are different molecules or experimental biological systems. Their
      activities, pathways and production assignments cannot transfer to butremycin.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Actual focused command exited 0.
  target_ids:
  - CHEBI:152570
  evidence_ids:
  - validation
  - chemistry
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/butremycin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Actual focused command exited 0.
  target_ids:
  - CHEBI:152570
  evidence_ids:
  - validation
  - chemistry
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/butremycin.yaml --out /private/tmp/am-review-session/175-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Actual focused command exited 0. Both strings parse and agree with the
    asserted key, formula, charge, masses and source mint. This internal agreement
    does not resolve the primary-literature C3 stereochemistry conflict.
  target_ids:
  - CHEBI:152570
  evidence_ids:
  - validation
  - chemistry
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache .venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 175
  exit_code: 0
  expected_exit_code: 0
- check_id: stereo-mapping
  name: Independent mapping of paper-numbered C2 and C3
  status: passed
  required: false
  summary: Both native strings give C2=S, C3=R. The sole tetrahedral alcohol carbon
    is C3, adjacent to N-bearing tetramic C2 and methylene C4. PubChem/NPAtlas give
    C2=S, C3=S. Passing this diagnostic establishes the discrepancy, not a clean identity
    verdict.
  target_ids:
  - CHEBI:152570
  evidence_ids:
  - stereo
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache .venv/bin/python
    /private/tmp/am-review-session/175-stereo-check.py
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
  - CHEBI:152570
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
  - CHEBI:152570
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
  - CHEBI:152570
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
  - CHEBI:152570
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
  - CHEBI:152570
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
  - CHEBI:152570
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
  - CHEBI:152570
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
  - CHEBI:152570
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
  - CHEBI:152570
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/butremycin.yaml
  locator: Entire record including all structural descriptors and three history events.
  accessed_at: '2026-10-21T10:34:50Z'
  support: supports
  summary: SEEDED/EXACT ChEBI record. The definition describes the 3-hydroxyl derivative
    of ikarugamycin isolated from Micromonospora sp. K310. It has no curated evidence
    objects, target, mode of action, causal graph, activity spectrum, producer object
    or resistance mechanism; these absent optional fields are not independently classified
    as errors.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: Exact source row 2734; source quality/role filter, structure import and
    citation-lead handling.
  accessed_at: '2026-10-21T10:34:50Z'
  support: supports
  summary: The source row reproduces the native definition, exact synonym, five parents,
    antibacterial role and full structures. Both citation leads are retained in the
    inventory. Extractor lines 329–332 intentionally keep source literature leads
    out of record evidence until a curator determines which exact claim they support.
    No exact corrective curator/decision row was found in the hidden-and-ignored-inclusive
    maintained search. All 13 initial source hashes remain unchanged.
  snapshot_sha256: 8eefe5c3001d658afc36f1c668e7cc46b3cc089be1cb1a32374b9450e82c3c0e
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:152570
  locator: Complete official page including structure, ontology, species and names.
  accessed_at: '2026-10-21T10:34:50Z'
  support: supports
  summary: Current ChEBI matches the native C29H38N2O5 neutral structure, key IJOMIIDEKGZJJF-KSCHHOEWSA-N,
    average mass 494.632 and monoisotopic mass 494.27807. Parents CHEBI24995, CHEBI26188,
    CHEBI38164, CHEBI51689 and CHEBI52898 are lactam, polyketide, organic heteropentacyclic
    compound, enone and azamacrocycle. CHEBI33282 is antibacterial agent. The source
    systematic synonym agrees with the source structure, including the conflicting
    alcohol stereocentre. Broader bacterial/marine metabolite roles and functional-parent
    relation to ikarugamycin are not missing antimicrobial-role errors.
  snapshot_sha256: be8b67bba2c53f456f5859d45611150b8c3b3e16d79090ed99da911e40063cba
- evidence_id: chemistry
  kind: validation
  reference: 175-chemistry.json
  locator: Independent SMILES/InChI parsing and source-mint calculation.
  accessed_at: '2026-10-21T10:34:50Z'
  support: supports
  summary: Both native strings parse as one neutral molecule with ten assigned tetrahedral
    centres and specified macrocyclic E/Z geometry. Their exact key, composition,
    charge, masses and mint reproduce. These are internal-consistency results; they
    do not independently establish that the encoded C3 epimer is the natural product.
  snapshot_sha256: 299f28bdd433e89ad5c5a1103ef7d87af70b0051c295244172f5f106981c87ba
- evidence_id: stereo
  kind: validation
  reference: 175-stereo-check.py; 175-stereo-check.json
  locator: Graph-based paper-position mapping, independently checked from both strings.
  accessed_at: '2026-10-21T10:34:50Z'
  support: refutes
  summary: 'The sole tetrahedral alcohol carbon is paper C3: native SMILES atom25
    is R, next to N-bearing tetramic C2 atom21=S and methylene C4 atom27. Independent
    InChI parsing yields the same C2S/C3R pair. PubChem/NPAtlas yield C2S/C3S. Inverting
    only native C3 produces diagnostic key IJOMIIDEKGZJJF-PQYAVTRXSA-N while retaining
    native tautomer and specified alkene geometry; this is a candidate for adjudication,
    not a validated complete replacement.'
  snapshot_sha256: df61a7afc28c01857743570f3558c6f9aca836a44d1402628eb5d8ed2ed7dc68
- evidence_id: primary2014-identity
  kind: primary_source
  reference: PMID:24534843; DOI:10.3390/md12020999; https://pmc.ncbi.nlm.nih.gov/articles/PMC3944527/
  locator: Complete original main text and author-deposited PDF; Figure 1 p1001 and
    Figure 3/p1003 visually inspected.
  accessed_at: '2026-10-21T10:34:50Z'
  support: refutes
  summary: Compound 2 is butremycin. The paper establishes the 3-hydroxylated PTM
    skeleton and explicitly assigns relative 2S*,3S*, rejecting 2S*,3R* using the
    small H2–H3 coupling. Figure 1 depicts the corresponding C3 alcohol orientation.
    The relative conflict suffices to distinguish the native diastereomer; it does
    not require treating the paper's relative assignment as a new absolute crystallographic
    determination.
  snapshot_sha256: 0a9aa5e1eafd88a7a8127ce72da6400c7a2ac9f914e37d134f7b6f6bef14a4af
- evidence_id: primary2014-activity
  kind: primary_source
  reference: PMID:24534843; DOI:10.3390/md12020999
  locator: Table 3 and Methods 3.6; table cells checked independently of flattened
    text.
  accessed_at: '2026-10-21T10:34:50Z'
  support: partial
  summary: Natural butremycin MIC is 50 micrograms/mL against S. aureus ATCC 25923,
    E. coli ATCC 25922 and EMRSA 15; values are >50 for SMRSA 105, 124 and 116. Assays
    use Mueller–Hinton broth, OD620-standardized cultures and no-growth endpoint after
    18 hours at 37 degrees C. These are weak antibacterial results, not MBCs or universal
    clinical resistance breakpoints. The tested natural material is not evidence for
    the native C3R epimer.
  snapshot_sha256: 75e3d8db92a408f9f4ee53a13012b0fae1c087949174f06a3407d936391592c2
- evidence_id: primary2014-production
  kind: primary_source
  reference: PMID:24534843; DOI:10.3390/md12020999
  locator: 'Sections 2.2–2.3, 3.3–3.5: repeated colony purification, fermentation
    and purified product isolation.'
  accessed_at: '2026-10-21T10:34:50Z'
  support: supports
  summary: The investigators isolated a pure K310 culture from Ghanaian mangrove river
    sediment, fermented it and purified 46.6 mg of compound 2 from culture material.
    This supports culture-associated production by the named strain, beyond merely
    detecting a metabolite in an environmental extract. It does not map a genetically
    demonstrated K310 biosynthetic pathway. Quorum-sensing and methylthioadenosine
    degradation discussion concerns compound 3, not butremycin.
  snapshot_sha256: 75e3d8db92a408f9f4ee53a13012b0fae1c087949174f06a3407d936391592c2
- evidence_id: primary2015
  kind: primary_source
  reference: PMID:25711294; DOI:10.1039/C5CC00843C; https://pubs.rsc.org/en/content/articlepdf/2015/cc/c5cc00843c
  locator: Complete three-page publisher PDF text extraction successfully inspected;
    p5335 product paragraph and p5336 footnote 18; 175-2015-inspected-notes.txt records
    access scope.
  accessed_at: '2026-10-21T10:34:50Z'
  support: supports
  summary: The follow-up infers 3S product configuration from coelution with an authentic
    K310 sample on several phases, including a chiral phase. It reports engineered
    E. coli BAP1 production using ikarugamycin genes and a Lysobacter hydroxylase,
    plus enzymatic conversion experiments. These are biosynthetic tailoring experiments,
    not antimicrobial target inhibition. Binary retrieval and later screenshot/open
    attempts returned 403; no 2015 figure image or unavailable supplementary data
    was inspected.
  snapshot_sha256: 4b5ae3ec4ed54131009f7131d93a7f2cde164d3aefd3a3051351fefd29df83a9
- evidence_id: genbank
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/nuccore/KF803252.1
  locator: Complete official GenBank flat file for KF803252.1.
  accessed_at: '2026-10-21T10:34:50Z'
  support: supports
  summary: The 1455-base partial 16S record explicitly identifies Micromonospora sp.
    K310, strain K310, taxon 1453323, Ghanaian mangrove-river sediment and PMID 24534843.
    It is an organism identity accession, not a butremycin biosynthetic gene-cluster
    sequence.
  snapshot_sha256: cf8b38b2a7061bbc0c80d6e9f3aac3250f171e6f41c2a888e413e4feb359783e
- evidence_id: alternative-databases
  kind: database
  reference: https://www.npatlas.org/explore/compounds/NPA017854; https://pubchem.ncbi.nlm.nih.gov/compound/139588066
  locator: Complete NPAtlas entry and official PubChem name-query property response.
  accessed_at: '2026-10-21T10:34:50Z'
  support: partial
  summary: Both name butremycin and encode C2S/C3S, but use key GVTUJXRGYOLNJB-WGOSSAFXSA-N
    with a different tetramic enol placement and unspecified macrocyclic alkene geometry.
    They corroborate the local C3 distinction but are not structure-exact equivalents
    of the current ChEBI string and cannot be adopted wholesale. A PubChem query for
    the native full key returned 404; that is an access/result limit, not proof that
    no other database contains it.
  snapshot_sha256: cd284c0dde9828f06c3c778705cf700d560906da3864c93b63cad9c491baed39
- evidence_id: adapter
  kind: database
  reference: Structured-source applicability assessed before open-ended web research
  locator: Complete native record and previously inspected iModulonDB dataset catalog.
  accessed_at: '2026-10-21T10:34:50Z'
  support: context_only
  summary: The record asserts no gene, protein, regulator, stress-response or transcriptomic
    dataset. No native expression claim required an iModulonDB query. Newly inspected
    biosynthetic enzymes and engineered E. coli hosts do not justify antimicrobial
    molecular targets; no transcriptomic claim is added.
- evidence_id: search
  kind: search
  reference: 175-local-hits.txt; 175-maintained-search.txt; 175-inclusive-file-hits.txt
  locator: Exact identifier, label, slug and both full-key stems; hidden and ignored
    files included.
  accessed_at: '2026-10-21T10:34:50Z'
  support: context_only
  summary: The broader search found native/raw entries, path ledger, generated chemical
    maps and readiness-queue lead. No separate maintained correction or primary curated
    evidence object was found in the stated scope. Generated maps and historical reports
    are not scientific evidence.
  snapshot_sha256: 92947a6ae9de5b30660813a56f0c84d35195d6509ac7678d9023f7c60aff35b5
  search_scope: rg --no-ignore --hidden across data, curation, conf, scripts, src,
    docs, .claude, reviews and reports for CHEBI:152570, label/slug and native/alternative
    key stems; hidden and ignored files included, excluding .git and .venv internals.
- evidence_id: validation
  kind: validation
  reference: 175-focused-results.json; 175-schema.log; 175-strict.log
  locator: Actual documented per-record schema and strict commands plus independent
    chemistry.
  accessed_at: '2026-10-21T10:34:50Z'
  support: supports
  summary: All three actual focused checks exit 0. A separate successful stereochemical
    diagnostic demonstrates why those checks do not establish literature-concordant
    identity.
  snapshot_sha256: 423b1b6b22d51aadb840ca14f68256d00e397132fbaa6e6d9d504225b3a6a9b2
- evidence_id: rubric
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md; docs/record-review-profile.md;
    docs/record-reviews.md; CLAUDE.md
  locator: Native exact-structure contract and evidence/status requirements.
  accessed_at: '2026-10-21T10:34:50Z'
  support: supports
  summary: Wrong chemical identity is a blocker even when strings agree internally.
    Required evidence must match exact stereochemical scope; optional producer, mechanism
    and AST fields are not automatically required omissions.
assessments:
- assessment_id: identity
  area: identity
  topic: Natural-product C3 stereochemistry
  outcome: concern
  summary: Native C2S/C3R conflicts with the original relative C2S*/C3S* relationship
    and follow-up 3S identification. This is a diastereomer distinction, not merely
    an unspecified absolute enantiomer or harmless tautomer spelling.
  target_ids:
  - CHEBI:152570
  evidence_ids:
  - stereo
  - primary2014-identity
  - primary2015
  - chebi
- assessment_id: representation
  area: representation
  topic: Internal structure and alternative database boundaries
  outcome: supported
  summary: The native strings parse and agree internally. Alternative databases differ
    in multiple representation dimensions, so a wholesale replacement would lose supported
    alkene geometry and change the selected tautomer.
  target_ids:
  - CHEBI:152570
  evidence_ids:
  - chemistry
  - stereo
  - alternative-databases
- assessment_id: grounding
  area: grounding
  topic: Definition, parent classes and activity role
  outcome: concern
  summary: The scaffold classes and source definition are appropriate for natural
    butremycin. Exact identity remains blocked by the encoded C3 epimer, so the natural-product
    activity cannot be considered independently verified for the current full structure.
  target_ids:
  - CHEBI:152570
  evidence_ids:
  - chebi
  - primary2014-identity
  - primary2014-activity
- assessment_id: activity
  area: evidence
  topic: Weak antibacterial observations
  outcome: supported
  summary: The original isolated compound has explicit weak MIC data. No claim that
    the C3R epimer is inactive, or that all MRSA isolates are susceptible, follows.
  target_ids:
  - CHEBI:152570
  evidence_ids:
  - primary2014-activity
- assessment_id: production
  area: provenance
  topic: Micromonospora K310 source and biosynthetic context
  outcome: supported
  summary: The natural-product isolation sentence is supported by pure-culture fermentation
    and exact strain accession. Engineered expression hosts and enzyme-donor strains
    must remain distinct from the natural producer.
  target_ids:
  - CHEBI:152570
  evidence_ids:
  - primary2014-production
  - genbank
  - primary2015
- assessment_id: mechanism
  area: completeness
  topic: No established exact antibacterial target
  outcome: unknown
  summary: No direct antibacterial target or killing chain was established by the
    two adopted papers. Tailoring hydroxylases synthesize product rather than being
    demonstrated inhibited antimicrobial targets; the co-isolated compound's quorum-sensing
    discussion does not transfer.
  target_ids:
  - CHEBI:152570
  evidence_ids:
  - primary2014-production
  - primary2015
  - adapter
- assessment_id: citations
  area: provenance
  topic: Both adopted citation dispositions
  outcome: supported
  summary: The 2014 isolation/weak-activity paper and 2015 biosynthetic-conversion
    paper were inspected in complete main text. Read scope and supplementary/figure
    limits are explicit.
  target_ids:
  - CHEBI:152570
  evidence_ids:
  - source
  - primary2014-identity
  - primary2014-activity
  - primary2015
- assessment_id: ownership
  area: ownership
  topic: Inherited structure and future evidence ownership
  outcome: supported
  summary: ChEBI source/extractor/seeder own identity correction; exact primary additions
    belong to the actual native record after identity adjudication. All initial hashes
    remain unchanged.
  target_ids:
  - CHEBI:152570
  evidence_ids:
  - source
  - record
- assessment_id: validation
  area: schema
  topic: Focused checks versus scientific identity
  outcome: supported
  summary: Documented per-record gates and internal chemistry pass, with no inference
    of scientific sign-off. The newly demonstrated literature conflict remains open.
  target_ids:
  - CHEBI:152570
  evidence_ids:
  - validation
  - stereo
  - rubric
findings:
- finding_id: F1
  issue_key: butremycin-source-c3-epimer-conflicts-primary
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Resolve the inherited C3 epimer before treating this as exact natural butremycin
  description: Both native strings encode paper C2=S, C3=R. The accessible original
    paper explicitly assigns relative 2S*,3S* and rejects the 2S*,3R* alternative;
    original Figure 1 and the later 3S product identification corroborate that difference.
    Current ChEBI carries the same conflict, including the systematic synonym. Internal
    parser agreement does not validate the source against primary chemistry.
  target_ids:
  - CHEBI:152570
  field_paths:
  - chemical_structure.smiles
  - chemical_structure.standard_inchi
  - chemical_structure.standard_inchi_key
  - synonyms[0]
  - grounding_status
  evidence_ids:
  - chebi
  - chemistry
  - stereo
  - primary2014-identity
  - primary2015
  - alternative-databases
  rule_id: 'native-review-checklist: one exact chemical structure and stereochemistry
    supported by primary evidence'
  native_severity: blocker wrong exact stereochemical identity
  normalization_reason: The encoded diastereomer differs at the newly hydroxylated
    centre relative to the adjacent tetramic centre. This is more specific than an
    unresolved absolute-enantiomer assignment and materially changes what the record
    denotes. No universal inactivity claim is made for the encoded epimer.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, stereochemical structure and exact systematic synonym
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source correction or exact structure normalization
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Exact source adjudication policy if needed
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion decision if source identity cannot be reconciled
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Regenerate coherent identity while preserving curated evidence
- finding_id: F2
  issue_key: butremycin-qualified-activity-producer-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: After identity correction, add narrowly scoped primary activity and culture-production
    evidence
  description: Primary weak MIC and pure-culture production observations are available
    but not yet represented as record evidence. Their absence is an optional enrichment
    opportunity. Biosynthetic enzymes, engineered production hosts and compound 3
    quorum-sensing discussion must not become antibacterial target claims.
  target_ids:
  - CHEBI:152570
  field_paths:
  - evidence
  - activity_spectrum
  - producer_organisms
  - biosynthesis_origin
  evidence_ids:
  - primary2014-activity
  - primary2014-production
  - genbank
  - primary2015
  - rubric
  rule_id: 'native-review-checklist: exact-material evidence and optional completeness'
  native_severity: informational optional evidence enrichment
  normalization_reason: Missing optional fields are not the defect; the separate identity
    blocker must be resolved before attaching natural-product experimental results
    to a corrected structure.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/butremycin.yaml
    role: Future primary evidence, activity and producer additions after exact identity
      is corrected
actions:
- action_id: A1
  description: Adjudicate the source stereochemistry and implement a reproducible
    identity correction.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:152570
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, stereochemical structure and exact systematic synonym
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source correction or exact structure normalization
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Exact source adjudication policy if needed
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion decision if source identity cannot be reconciled
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Regenerate coherent identity while preserving curated evidence
  acceptance_checks:
  - Map original paper positions to every encoded stereocentre, explicitly checking
    C2/C3. Reconcile the 2014 relative assignment with the 2015 authentic-sample coelution
    result; preserve the distinction between relative assignment, literature absolute
    designation and an independent absolute determination.
  - Correct the maintained ChEBI-derived structure and systematic synonym together
    through a documented exact-source correction or upstream resolution. The scratch
    single-C3 inversion key IJOMIIDEKGZJJF-PQYAVTRXSA-N is a diagnostic candidate
    only; confirm the entire structure, selected tautomer and alkene geometries before
    adoption.
  - 'Do not substitute PubChem 139588066 or NPAtlas NPA017854 wholesale: their current
    representation shifts the tetramic enol and omits the native macrocyclic E/Z annotations.
    If the external CHEBI grounding cannot be reconciled, explicitly adjudicate it
    through maintained source/decision ownership instead of asserting a false EXACT
    match.'
  - Regenerate through the documented pipeline, check SMILES/InChI/key/formula/charge/stereochemistry
    and source mint coherently, and run focused and shared native checks. Use validated
    curation/history entrypoints; leave scientific status unchanged until all review
    requirements are met.
- action_id: A2
  description: Curate exact primary observations only after the structural identity
    is resolved.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:152570
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/butremycin.yaml
    role: Future primary evidence, activity and producer additions after exact identity
      is corrected
  acceptance_checks:
  - 'Attach PMID 24534843 at the narrow supported claim: Table 3 MIC of 50 micrograms/mL
    for ATCC 25923, ATCC 25922 and EMRSA 15, and >50 for SMRSA 105, 124 and 116. Preserve
    comparator, units, 18-hour Mueller–Hinton broth conditions, optical no-growth
    endpoint and the strict greater-than censoring. These are individual test results,
    not MIC50 panel statistics or clinical breakpoints.'
  - For producer_organisms, use pure-culture fermentation/isolation evidence for Micromonospora
    sp. K310 and independently verified strain accession KF803252.1/taxon 1453323.
    Do not claim that the 16S accession is a biosynthetic gene cluster or that every
    related species produces the compound.
  - Separate engineered E. coli production and hydroxylase-mediated conversion in
    PMID 25711294 from natural production. Do not add these tailoring enzymes as inhibited
    molecular targets, and do not transfer the other compound's methylthioadenosine/quorum-sensing
    pathway to butremycin.
  - Use write_validated_antibiotic and record_curation_event on data/antibiotics/antibacterial/butremycin.yaml
    for separately authorized curation, preserve additions across reseeding and run
    applicable validation.
limitations:
- Initial capture preceded assessment; all 13 source input hashes remain unchanged.
  Complete record, exact maintained row and relevant source config/extraction/seeding
  code were inspected.
- The complete 2014 main text, tables and original Figures 1 and 3 were inspected.
  Supplementary captions were read and Figure S1 inspected visually; the entire NMR
  dataset was not independently reprocessed.
- The 2014 main text and Figure S1 print [M+H]+ 495.2781, whereas the neutral formula
  mass is 494.27807 and its protonated exact mass would be approximately 495.28535.
  This source numerical inconsistency is preserved; it does not justify changing the
  native neutral formula or masses, and the stereochemical finding rests on graph
  mapping, original drawing and explicit relative assignment.
- The 2015 publisher PDF text extraction succeeded once and all three pages were read.
  Subsequent direct download, screenshot and open requests returned 403; inspected
  passage and access notes are retained, not mislabeled as a binary PDF snapshot.
  Supporting-information routes returned 404 and a thesis download produced a bot
  challenge.
- Original 2014 relative stereochemistry independently establishes the C2/C3 conflict.
  The later 3S assignment corroborates it but is based on authentic-sample chromatographic
  comparison; a complete independent absolute-configuration redetermination was not
  performed here.
- PubChem and NPAtlas agree with each other but differ from ChEBI in tautomer placement,
  alkene specification and C3 configuration. Neither is treated as an automatically
  correct complete replacement.
- No exact antibacterial target, causal mechanism, resistance determinant or comprehensive
  public dataset inventory was established. No native expression claim required iModulonDB.
- The observed weak antibacterial activity belongs to the natural product. This review
  does not prove the encoded C3R epimer inactive or establish any clinical-use claim.
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
