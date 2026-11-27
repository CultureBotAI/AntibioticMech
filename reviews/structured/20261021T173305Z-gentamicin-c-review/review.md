# Review of gentamicin C

- Review: 20261021T173305Z-gentamicin-c-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T17:15:13Z
- Finished UTC: 2026-10-21T17:33:05Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native source explicitly denotes a gentamicin-component mixture, which cannot be represented by the one configured neutral graph assigned to this record. Current exact cross-references also conflate a different stereoisomer and a generic pentacation. This is a blocker identity failure despite passing focused validators. One independently verified product alias is also incorrectly typed as an exact chemical synonym. Database mechanism claims remain qualified; primary assays are scoped to their actual mixture, component and salt materials.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position 496; original 13 input hashes preserved and five actual ARO/PubChem owner inputs appended before detailed assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-6407ce57f1 | data/antibiotics/antibacterial/gentamicin-c.yaml | generated | gentamicin C |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-6407ce57f1 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-6407ce57f1 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-6407ce57f1 | Actual focused execution exited 0. |
| Independent authority and atom-mapped stereochemistry comparison | passed | False | antibioticmech:aro-6407ce57f1 | Twelve encodings compared; one inversion maps the native graph to ChEMBL384124 and two map it to independently grounded C1a. The ChEBI75616 graph has charge +5 and two wildcard atoms. |
| Input, reference, source and history ledger | passed | False | antibioticmech:aro-6407ce57f1 | All 18 inputs unchanged, original 13 preserved; all 29 adopted/current leads, 14 resistance edges and four chronological events checked. |
| Structured source catalog | passed | False | antibioticmech:aro-6407ce57f1 | Catalog inspected before bacterial mechanism follow-up. |
| Structured rrsB query | passed | False | antibioticmech:aro-6407ce57f1 | rrsB returned no gene/component; mexC returned PA4599 gene metadata and no iModulon. No component summary applies; membership does not establish resistance. |
| Structured mexC query | passed | False | antibioticmech:aro-6407ce57f1 | rrsB returned no gene/component; mexC returned PA4599 gene metadata and no iModulon. No component summary applies; membership does not establish resistance. |
| Authoritative full QC | failed | True | antibioticmech:aro-6407ce57f1 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-6407ce57f1 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-6407ce57f1 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-6407ce57f1 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-6407ce57f1 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-6407ce57f1 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-6407ce57f1 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-6407ce57f1 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-6407ce57f1 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Explicit mixture versus one configured molecular structure

identity: concern. Targets: antibioticmech:aro-6407ce57f1.

The source concept is explicitly a component mixture and cannot satisfy the one-structure corpus boundary. No inference from undefined stereochemistry is involved.

### Exact chemical cross-reference incompatibility

grounding: concern. Targets: antibioticmech:aro-6407ce57f1.

The native single graph disagrees with ChEMBL at a configured tetrahedral centre and is not equivalent to the generic +5 ChEBI species. C1a comparator mapping rules out a safe relabel-only repair.

### Aminoglycoside parent and antibacterial context

nomenclature: supported. Targets: antibioticmech:aro-6407ce57f1.

The component scaffolds and original susceptibility work support the broad antibiotic classification, but do not cure the mixture/individual identity failure.

### Cidomycin exact chemical synonym

grounding: concern. Targets: antibioticmech:aro-6407ce57f1.

The official source defines a sulfate injectable product; current EXACT_SYNONYM typing drops that product/material scope.

### Qualified 16S-rRNA database target

evidence: supported. Targets: antibioticmech:aro-6407ce57f1.

Original component/model binding evidence is relevant to the family mechanism. Native provenance remains explicitly database-tier and PRIMARY_EVIDENCE_NEEDED; exact native-graph binding is not claimed verified.

### Fourteen current resistance edges and primary context

evidence: unknown. Targets: antibioticmech:aro-6407ce57f1.

All current ARO edges persist. Material identity, strain, expression and medium effects limit component-level interpretation; MexCD-OprJ abstracts expose a context conflict that is retained for follow-up rather than generalized to absence of resistance.

### Optional evidence and source-specific material

completeness: supported. Targets: antibioticmech:aro-6407ce57f1.

No optional MIC, producer, clinical or causal object is falsely asserted. Exact component claims require separately verified records after resolving the identity boundary.

### Reproducible exclusion and provenance

ownership: supported. Targets: antibioticmech:aro-6407ce57f1.

Source owners, enrichment and exclusion lane are identified; original hashes and chronological events are preserved.

## Findings

### F1: An explicit gentamicin mixture is represented as one incompatible molecular identity

blocker / open / confirmed; issue key: gentamicin-c-mixture-assigned-single-incompatible-structure.

ARO0000014 and the native definition explicitly describe a C-component mixture, but the native assigns one neutral stereoisomer and exact chemical xrefs. Current ChEMBL384124 is a configured epimer of that graph; CHEBI75616 is a generic pentacation with R groups. The independently grounded C1a structure also differs from the native at two configured centres. Exclude the mixture concept through the maintained decision lane; do not rename the existing graph to C1a or move mixture-level resistance claims onto a selected component.

### F2: Cidomycin is typed as an exact chemical synonym without its product scope

minor / open / confirmed; issue key: gentamicin-c-cidomycin-product-alias-exact-typing.

The official Cidomycin SmPC identifies a gentamicin sulfate injectable product, not the neutral configured graph. The source-derived EXACT_SYNONYM typing should be suppressed or explicitly product-qualified in any retained representation. This bounded finding does not adjudicate all eight other aliases.

## Recommended Actions And Acceptance Checks

### A1

Record a justified EXCLUDE for ARO:0000014 in curation/decisions.tsv and regenerate the eligible corpus through the maintained source lane. Preserve raw mixture metadata and provenance; independently review exact C congeners before any separate addition or claim reassignment. Consider source eligibility safeguards for explicit ARO antibiotic-mixture ancestry without treating partial stereochemistry as a mixture.

- Confirm the mixture concept is excluded reproducibly while raw evidence remains available.
- Do not transfer mixture-level target/resistance claims to the native epimer or to C1a without independent material-specific evidence.
- Run native schema, strict term, reference/history/corpus checks and QC after documented regeneration.

### A2

If the source concept or its aliases are represented elsewhere after identity resolution, use the maintained source synonym controls to qualify Cidomycin as a trade/product name or exclude it from exact chemical synonyms. Preserve its gentamicin sulfate product context.

- Compare against the official product14742 SmPC and ensure no sulfate-product clinical claim is assigned to a single neutral congener.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/gentamicin-c.yaml; Entire native record, including all four history events | supports | The SEEDED, MINTED record explicitly defines a mixture of C1, C1a and C2 yet assigns one neutral C19H39N5O7 structure. It has nine EXACT_SYNONYM aliases, five xrefs, one aminoglycoside parent, one qualified database 16S-rRNA target and 14 qualified database resistance edges. No MIC, producer object, clinical approval or causal graph is asserted. |
| mixture | ARO:0000014; ARO:3000707; 496-aro-blocks.json; official ontology426-current-aro.obo, provenance426-fetch2-results.json | supports | Current ARO still expressly defines the C1/C1a/C2 mixture and places it under antibiotic mixture. The native wording is therefore not merely an ambiguous short name or a consequence of unspecified stereochemistry. Enriching this source concept with a single PubChem graph does not make it one chemical structure. |
| chemistry | PubChem:3084091; ChEMBL:CHEMBL384124; CHEBI:27784; PubChem:72396; 496-authority-chemistry.json; current official structure snapshots and ChEBI molfile | supports | Native SMILES/InChI and PubChem3084091 agree at VEGXETMJINRLTH-ALRICIOSSA-N. ChEMBL384124 has the same constitution but HKHRZCBZSA-N stereochemistry: native atom16 inversion is necessary and sufficient for reciprocal chirality-aware matching. C1a ChEBI27784/PubChem72396 instead give BOZYPMBZSA-N and require inversions at native atoms5 and16. These zero-based atom indices are documented with mappings/neighborhoods. The native is therefore neither the asserted ChEMBL stereoisomer nor verified C1a; a simple C1a relabel is not justified. |
| cation | CHEBI:75616; 496-chebi75616.json and official molfile | supports | The asserted exact ChEBI xref is gentamicin C(5+), defined generically by protonation of any gentamicin C component. Its molfile has charge +5 and two R-group wildcard atoms, and no exact InChI. It is not equivalent to the native neutral, fully specified graph. |
| primary-mixture | PMID:32601158; DOI:10.1128/AAC.00533-20; 496-PMC7449222.html; abstract/introduction, initial characterization and susceptibility results, isolation and susceptibility Methods; Figure1 viewed in496-2020-fig1.jpg | supports | The original study isolates C1, C1a, C2 and C2a from commercial gentamicin sulfate and shows distinct congener structures. Purified free bases were converted back to sulfate salts for testing. CLSI broth microdilution used cation-adjusted Mueller-Hinton broth and defined incubation/inoculum conditions. The mixture/component distinction directly supports the identity boundary; no isolated-sulfate MIC is attributed to the native free-base stereoisomer. Table1 was only partly inspected and no quantitative row is adopted. |
| biosynthesis | PMID:25641167; DOI:10.1016/j.chembiol.2014.12.012; 496-PMC4340712.xml; abstract and introductory pathway paragraphs P0–P5 in text derivative | supports | This original biosynthesis paper describes the gentamicin C complex as five components and distinguishes precursor gentamicin X2 and G418 from final C congeners. It independently supports the mixture/material boundary. Later enzyme experiments in the article are not claimed fully inspected for this record. |
| binding | PMID:9822590; DOI:10.1093/emboj/17.22.6437; 496-PMC1170992.html; complete original abstract and landing text | supports | The original compares binding of three C components to ribosomes/model RNA, but its solved RNA-bound NMR structure is specifically gentamicin C1a. It supports the general RNA-target mechanism at stated component/model scope, not equivalence of the mixture or native epimer graph to the C1a ligand. The PDF request returned HTML; full paper inspection is not claimed. |
| brand | Cidomycin SmPC, product14742; 496-cidomycin.html; official sections1,2 and5.1; updated12August2025 | supports | The authority identifies Cidomycin80mg/2ml solution for injection as a gentamicin sulfate medicine, each ampoule/vial containing sulfate equivalent to80mg gentamicin base; section5.1 expressly calls gentamicin a mixture. This establishes Cidomycin as a product alias, not an exact synonym of the native neutral molecular graph. Other brand-like aliases are not automatically adjudicated from their spelling. |
| leads | All 29 frozen/current ARO PMID leads; 496-current-leads.json; 496-source-audit.json | supports | All MED identifiers resolve. Twenty-seven complete supplied abstracts were read; two historical review leads have no supplied abstract and remain metadata-only. Each lead has an explicit disposition covering enzyme methylation, ribosomal mutation, efflux, strain and culture-condition limits. The historical definition references are reviews; exact current drug edges remain database assertions rather than invented primary citations. |
| resistance | PMID:8849250; PMID:18474583; PMID:12499164; Complete original abstracts in496-current-leads.json; per-edge disposition in496-source-audit.json | supports | The two MexCD-OprJ original abstracts report increased gentamicin/aminoglycoside susceptibility in nfxB-overexpression contexts, rather than a universal resistance phenotype. The EmrE abstract reports a gentamicin effect under low-ionic-strength nutrient-broth conditions, not LB/MHB. These delimit the generic source edges and warrant context-specific follow-up; inaccessible main texts and unresolved exact component materials prevent a blanket edge-removal conclusion. |
| adapter | iModulonDB e_coli/precise1k and p_aeruginosa/precise364; 496-imodulon-datasets.json;496-imodulon-rrsB.json;496-imodulon-mexC.json | supports | Catalog-first queries found no rrsB hit and one MexC gene record PA4599 with no iModulon. These results establish catalog availability only; no expression, binding or resistance inference is made. |
| owners | ARO extraction, PubChem enrichment and exclusion decisions; 496-inspect.json;496-source-audit.json;496-raw-rows.json;ignored-inclusive496-owners-search.json | supports | All original13 and five appended actual-owner hashes remain unchanged. Seventeen exact raw rows and four chronological history events reproduce the native source/enrichment. Maintained curation/decisions.tsv supports EXCLUDE decisions, with existing mixture precedents. Local searches included ignored files; raw source preservation and deliberate exclusion are distinct from erasing source claims. |

## Limits And Additional Notes

- Twenty-seven of29 adopted/current leads supplied abstracts and were read completely; two review records were metadata-only. Most resistance originals were not read in full, so detailed material and assay support remains unresolved.
- The MexCD-OprJ and EmrE PMC main-text routes returned challenge HTML. Their complete original abstracts show important context limits, but this review does not claim a complete original-table audit or infer universal absence of resistance.
- The 1998 RNA paper was read at complete abstract/landing depth; its PDF request returned HTML. Its C1a NMR structure is not attributed to the mixture or native stereoisomer.
- The 2020 congener study was read at the selected sections and Figure1 stated above; Table1 only partly. The 2015 biosynthesis paper was read at abstract/introduction/pathway depth. Neither is claimed fully reviewed for all downstream experiments.
- The current ChEMBL and ChEBI discrepancies are independently graph-verified database identity conflicts, not a newly proven absolute configuration assignment for a physical native reagent. No automatic replacement graph is proposed.
- Only Cidomycin among the nine aliases was independently verified as a product here. A guessed Garamycin FDA route returned404; J-GLOBAL snapshot retrieval returned503, and neither failed retrieval is treated as inspected source content.
- The PMC7768767 follow-up route failed XML retrieval and returned HTML challenge; no full-original result from that paper is adopted.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Standalone chemistry used batch019 against batch050; native validators, source ledger and contract used batch050.
- No native/source bytes or scientific status were changed. Original input hashes are preserved; the draft records an exclusion recommendation, not an executed exclusion.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T173305Z-gentamicin-c-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of gentamicin C
started_at: '2026-10-21T17:15:13Z'
finished_at: '2026-10-21T17:33:05Z'
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
summary: The native source explicitly denotes a gentamicin-component mixture, which
  cannot be represented by the one configured neutral graph assigned to this record.
  Current exact cross-references also conflate a different stereoisomer and a generic
  pentacation. This is a blocker identity failure despite passing focused validators.
  One independently verified product alias is also incorrectly typed as an exact chemical
  synonym. Database mechanism claims remain qualified; primary assays are scoped to
  their actual mixture, component and salt materials.
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
  - path: data/antibiotics/antibacterial/gentamicin-c.yaml
    sha256: b307020c0603c33989e7fcf9112897cdf36b7cbc17d10f1a2e9bb159c905836d
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
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
targets:
- target_id: antibioticmech:aro-6407ce57f1
  path: data/antibiotics/antibacterial/gentamicin-c.yaml
  label: gentamicin C
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, definition and synonym
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Adopted database target
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Adopted database resistance assertions
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Exact neutral PubChem structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem enrichment producer
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: CARD/ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Native field generation
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding decisions
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Source-scoped definition or synonym controls
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position 496; original 13 input hashes preserved
    and five actual ARO/PubChem owner inputs appended before detailed assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-6407ce57f1
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-6407ce57f1
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    496
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-6407ce57f1
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/gentamicin-c.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-6407ce57f1
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/gentamicin-c.yaml --out /private/tmp/am-review-session/496-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: authority
  name: Independent authority and atom-mapped stereochemistry comparison
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/496-authority-check.py
    > /private/tmp/am-review-session/496-authority-check.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Twelve encodings compared; one inversion maps the native graph to ChEMBL384124
    and two map it to independently grounded C1a. The ChEBI75616 graph has charge
    +5 and two wildcard atoms.
  target_ids:
  - antibioticmech:aro-6407ce57f1
- check_id: ledger
  name: Input, reference, source and history ledger
  command: .venv/bin/python /private/tmp/am-review-session/496-ledger.py > /private/tmp/am-review-session/496-ledger.log
    2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: All 18 inputs unchanged, original 13 preserved; all 29 adopted/current
    leads, 14 resistance edges and four chronological events checked.
  target_ids:
  - antibioticmech:aro-6407ce57f1
- check_id: adapter-catalog
  name: Structured source catalog
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets > /private/tmp/am-review-session/496-imodulon-datasets.json
    2> /private/tmp/am-review-session/496-imodulon-datasets.err
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Catalog inspected before bacterial mechanism follow-up.
  target_ids:
  - antibioticmech:aro-6407ce57f1
- check_id: adapter-rrsB
  name: Structured rrsB query
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset precise1k --query rrsB
    > /private/tmp/am-review-session/496-imodulon-rrsB.json 2> /private/tmp/am-review-session/496-imodulon-rrsB.err
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: rrsB returned no gene/component; mexC returned PA4599 gene metadata and
    no iModulon. No component summary applies; membership does not establish resistance.
  target_ids:
  - antibioticmech:aro-6407ce57f1
- check_id: adapter-mexC
  name: Structured mexC query
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism p_aeruginosa --dataset precise364 --query
    mexC > /private/tmp/am-review-session/496-imodulon-mexC.json 2> /private/tmp/am-review-session/496-imodulon-mexC.err
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: rrsB returned no gene/component; mexC returned PA4599 gene metadata and
    no iModulon. No component summary applies; membership does not establish resistance.
  target_ids:
  - antibioticmech:aro-6407ce57f1
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:aro-6407ce57f1
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
  - antibioticmech:aro-6407ce57f1
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
  - antibioticmech:aro-6407ce57f1
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
  - antibioticmech:aro-6407ce57f1
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
  - antibioticmech:aro-6407ce57f1
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
  - antibioticmech:aro-6407ce57f1
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
  - antibioticmech:aro-6407ce57f1
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
  - antibioticmech:aro-6407ce57f1
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
  - antibioticmech:aro-6407ce57f1
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/gentamicin-c.yaml
  locator: Entire native record, including all four history events
  accessed_at: '2026-10-21T17:25:32Z'
  support: supports
  summary: The SEEDED, MINTED record explicitly defines a mixture of C1, C1a and C2
    yet assigns one neutral C19H39N5O7 structure. It has nine EXACT_SYNONYM aliases,
    five xrefs, one aminoglycoside parent, one qualified database 16S-rRNA target
    and 14 qualified database resistance edges. No MIC, producer object, clinical
    approval or causal graph is asserted.
- evidence_id: mixture
  kind: authority
  reference: ARO:0000014; ARO:3000707
  locator: 496-aro-blocks.json; official ontology426-current-aro.obo, provenance426-fetch2-results.json
  accessed_at: '2026-10-21T17:25:32Z'
  support: supports
  summary: Current ARO still expressly defines the C1/C1a/C2 mixture and places it
    under antibiotic mixture. The native wording is therefore not merely an ambiguous
    short name or a consequence of unspecified stereochemistry. Enriching this source
    concept with a single PubChem graph does not make it one chemical structure.
  snapshot_sha256: 13f1eed82fd1e372cf174a6d1ee1e848bf9d5870cd7031723f416afb3f18460a
- evidence_id: chemistry
  kind: validation
  reference: PubChem:3084091; ChEMBL:CHEMBL384124; CHEBI:27784; PubChem:72396
  locator: 496-authority-chemistry.json; current official structure snapshots and
    ChEBI molfile
  accessed_at: '2026-10-21T17:25:32Z'
  support: supports
  summary: 'Native SMILES/InChI and PubChem3084091 agree at VEGXETMJINRLTH-ALRICIOSSA-N.
    ChEMBL384124 has the same constitution but HKHRZCBZSA-N stereochemistry: native
    atom16 inversion is necessary and sufficient for reciprocal chirality-aware matching.
    C1a ChEBI27784/PubChem72396 instead give BOZYPMBZSA-N and require inversions at
    native atoms5 and16. These zero-based atom indices are documented with mappings/neighborhoods.
    The native is therefore neither the asserted ChEMBL stereoisomer nor verified
    C1a; a simple C1a relabel is not justified.'
  snapshot_sha256: c37af521df3e6738b0e190c7bfbd3eedabf9c54a5cab9d3f98c1b4635b0eb8fa
- evidence_id: cation
  kind: authority
  reference: CHEBI:75616
  locator: 496-chebi75616.json and official molfile
  accessed_at: '2026-10-21T17:25:32Z'
  support: supports
  summary: The asserted exact ChEBI xref is gentamicin C(5+), defined generically
    by protonation of any gentamicin C component. Its molfile has charge +5 and two
    R-group wildcard atoms, and no exact InChI. It is not equivalent to the native
    neutral, fully specified graph.
  snapshot_sha256: 58648acf5c64898cb1490d1dc9f09a3fc5c3b07ee50435e6269c50e2d90f3bc2
- evidence_id: primary-mixture
  kind: primary_source
  reference: PMID:32601158; DOI:10.1128/AAC.00533-20
  locator: 496-PMC7449222.html; abstract/introduction, initial characterization and
    susceptibility results, isolation and susceptibility Methods; Figure1 viewed in496-2020-fig1.jpg
  accessed_at: '2026-10-21T17:25:32Z'
  support: supports
  summary: The original study isolates C1, C1a, C2 and C2a from commercial gentamicin
    sulfate and shows distinct congener structures. Purified free bases were converted
    back to sulfate salts for testing. CLSI broth microdilution used cation-adjusted
    Mueller-Hinton broth and defined incubation/inoculum conditions. The mixture/component
    distinction directly supports the identity boundary; no isolated-sulfate MIC is
    attributed to the native free-base stereoisomer. Table1 was only partly inspected
    and no quantitative row is adopted.
  snapshot_sha256: 1ff2ec241866ee77117e5422ba749beaf73a23f775f3ee767db361e3617ab715
- evidence_id: biosynthesis
  kind: primary_source
  reference: PMID:25641167; DOI:10.1016/j.chembiol.2014.12.012
  locator: 496-PMC4340712.xml; abstract and introductory pathway paragraphs P0–P5
    in text derivative
  accessed_at: '2026-10-21T17:25:32Z'
  support: supports
  summary: This original biosynthesis paper describes the gentamicin C complex as
    five components and distinguishes precursor gentamicin X2 and G418 from final
    C congeners. It independently supports the mixture/material boundary. Later enzyme
    experiments in the article are not claimed fully inspected for this record.
  snapshot_sha256: 21d4f7a905b7387ebdb0c2096c5a4397f5d69bdf9eceebdac6bdb8fa9627eee7
- evidence_id: binding
  kind: primary_source
  reference: PMID:9822590; DOI:10.1093/emboj/17.22.6437
  locator: 496-PMC1170992.html; complete original abstract and landing text
  accessed_at: '2026-10-21T17:25:32Z'
  support: supports
  summary: The original compares binding of three C components to ribosomes/model
    RNA, but its solved RNA-bound NMR structure is specifically gentamicin C1a. It
    supports the general RNA-target mechanism at stated component/model scope, not
    equivalence of the mixture or native epimer graph to the C1a ligand. The PDF request
    returned HTML; full paper inspection is not claimed.
  snapshot_sha256: 217a5d52511e2458eb8e3dcc3b048771426813617de6c51161b5c2b79eb12726
- evidence_id: brand
  kind: authority
  reference: Cidomycin SmPC, product14742
  locator: 496-cidomycin.html; official sections1,2 and5.1; updated12August2025
  accessed_at: '2026-10-21T17:25:32Z'
  support: supports
  summary: The authority identifies Cidomycin80mg/2ml solution for injection as a
    gentamicin sulfate medicine, each ampoule/vial containing sulfate equivalent to80mg
    gentamicin base; section5.1 expressly calls gentamicin a mixture. This establishes
    Cidomycin as a product alias, not an exact synonym of the native neutral molecular
    graph. Other brand-like aliases are not automatically adjudicated from their spelling.
  snapshot_sha256: 4c4eb1040286d87b6dcec60495f64c67955baff210c0e6fdd2a31b9939b48517
- evidence_id: leads
  kind: database
  reference: All 29 frozen/current ARO PMID leads
  locator: 496-current-leads.json; 496-source-audit.json
  accessed_at: '2026-10-21T17:25:32Z'
  support: supports
  summary: All MED identifiers resolve. Twenty-seven complete supplied abstracts were
    read; two historical review leads have no supplied abstract and remain metadata-only.
    Each lead has an explicit disposition covering enzyme methylation, ribosomal mutation,
    efflux, strain and culture-condition limits. The historical definition references
    are reviews; exact current drug edges remain database assertions rather than invented
    primary citations.
  snapshot_sha256: 498de956a125d11b2aa8898da6d328c39ed181c431f983678fe557a60d2ada18
- evidence_id: resistance
  kind: primary_source
  reference: PMID:8849250; PMID:18474583; PMID:12499164
  locator: Complete original abstracts in496-current-leads.json; per-edge disposition
    in496-source-audit.json
  accessed_at: '2026-10-21T17:25:32Z'
  support: supports
  summary: The two MexCD-OprJ original abstracts report increased gentamicin/aminoglycoside
    susceptibility in nfxB-overexpression contexts, rather than a universal resistance
    phenotype. The EmrE abstract reports a gentamicin effect under low-ionic-strength
    nutrient-broth conditions, not LB/MHB. These delimit the generic source edges
    and warrant context-specific follow-up; inaccessible main texts and unresolved
    exact component materials prevent a blanket edge-removal conclusion.
  snapshot_sha256: 6be1ebe234a401eb51511a310887950f87d1303d91fa2a3981d98aed1654aa97
- evidence_id: adapter
  kind: database
  reference: iModulonDB e_coli/precise1k and p_aeruginosa/precise364
  locator: 496-imodulon-datasets.json;496-imodulon-rrsB.json;496-imodulon-mexC.json
  accessed_at: '2026-10-21T17:25:32Z'
  support: supports
  summary: Catalog-first queries found no rrsB hit and one MexC gene record PA4599
    with no iModulon. These results establish catalog availability only; no expression,
    binding or resistance inference is made.
  snapshot_sha256: 5fd29ab32a7c2c7d430aeb83400f2d247fc0d7390afd5d53fa7711ee2173d2dd
- evidence_id: owners
  kind: validation
  reference: ARO extraction, PubChem enrichment and exclusion decisions
  locator: 496-inspect.json;496-source-audit.json;496-raw-rows.json;ignored-inclusive496-owners-search.json
  accessed_at: '2026-10-21T17:25:32Z'
  support: supports
  summary: All original13 and five appended actual-owner hashes remain unchanged.
    Seventeen exact raw rows and four chronological history events reproduce the native
    source/enrichment. Maintained curation/decisions.tsv supports EXCLUDE decisions,
    with existing mixture precedents. Local searches included ignored files; raw source
    preservation and deliberate exclusion are distinct from erasing source claims.
  snapshot_sha256: 498de956a125d11b2aa8898da6d328c39ed181c431f983678fe557a60d2ada18
assessments:
- assessment_id: identity
  area: identity
  topic: Explicit mixture versus one configured molecular structure
  outcome: concern
  summary: The source concept is explicitly a component mixture and cannot satisfy
    the one-structure corpus boundary. No inference from undefined stereochemistry
    is involved.
  target_ids:
  - antibioticmech:aro-6407ce57f1
  evidence_ids:
  - record
  - mixture
  - primary-mixture
  - biosynthesis
- assessment_id: xrefs
  area: grounding
  topic: Exact chemical cross-reference incompatibility
  outcome: concern
  summary: The native single graph disagrees with ChEMBL at a configured tetrahedral
    centre and is not equivalent to the generic +5 ChEBI species. C1a comparator mapping
    rules out a safe relabel-only repair.
  target_ids:
  - antibioticmech:aro-6407ce57f1
  evidence_ids:
  - chemistry
  - cation
- assessment_id: class
  area: nomenclature
  topic: Aminoglycoside parent and antibacterial context
  outcome: supported
  summary: The component scaffolds and original susceptibility work support the broad
    antibiotic classification, but do not cure the mixture/individual identity failure.
  target_ids:
  - antibioticmech:aro-6407ce57f1
  evidence_ids:
  - mixture
  - primary-mixture
  - chemistry
- assessment_id: alias
  area: grounding
  topic: Cidomycin exact chemical synonym
  outcome: concern
  summary: The official source defines a sulfate injectable product; current EXACT_SYNONYM
    typing drops that product/material scope.
  target_ids:
  - antibioticmech:aro-6407ce57f1
  evidence_ids:
  - record
  - brand
- assessment_id: target
  area: evidence
  topic: Qualified 16S-rRNA database target
  outcome: supported
  summary: Original component/model binding evidence is relevant to the family mechanism.
    Native provenance remains explicitly database-tier and PRIMARY_EVIDENCE_NEEDED;
    exact native-graph binding is not claimed verified.
  target_ids:
  - antibioticmech:aro-6407ce57f1
  evidence_ids:
  - binding
  - record
  - leads
- assessment_id: resistance
  area: evidence
  topic: Fourteen current resistance edges and primary context
  outcome: unknown
  summary: All current ARO edges persist. Material identity, strain, expression and
    medium effects limit component-level interpretation; MexCD-OprJ abstracts expose
    a context conflict that is retained for follow-up rather than generalized to absence
    of resistance.
  target_ids:
  - antibioticmech:aro-6407ce57f1
  evidence_ids:
  - leads
  - resistance
  - adapter
  - mixture
- assessment_id: completeness
  area: completeness
  topic: Optional evidence and source-specific material
  outcome: supported
  summary: No optional MIC, producer, clinical or causal object is falsely asserted.
    Exact component claims require separately verified records after resolving the
    identity boundary.
  target_ids:
  - antibioticmech:aro-6407ce57f1
  evidence_ids:
  - record
  - primary-mixture
  - binding
- assessment_id: ownership
  area: ownership
  topic: Reproducible exclusion and provenance
  outcome: supported
  summary: Source owners, enrichment and exclusion lane are identified; original hashes
    and chronological events are preserved.
  target_ids:
  - antibioticmech:aro-6407ce57f1
  evidence_ids:
  - owners
findings:
- finding_id: F1
  issue_key: gentamicin-c-mixture-assigned-single-incompatible-structure
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: An explicit gentamicin mixture is represented as one incompatible molecular
    identity
  description: ARO0000014 and the native definition explicitly describe a C-component
    mixture, but the native assigns one neutral stereoisomer and exact chemical xrefs.
    Current ChEMBL384124 is a configured epimer of that graph; CHEBI75616 is a generic
    pentacation with R groups. The independently grounded C1a structure also differs
    from the native at two configured centres. Exclude the mixture concept through
    the maintained decision lane; do not rename the existing graph to C1a or move
    mixture-level resistance claims onto a selected component.
  target_ids:
  - antibioticmech:aro-6407ce57f1
  field_paths:
  - identifier
  - definition
  - chemical_structure
  - xrefs
  - source_concepts
  evidence_ids:
  - record
  - mixture
  - chemistry
  - cation
  - primary-mixture
  - biosynthesis
  - owners
  rule_id: '.claude/skills/review-yaml-record/SKILL.md: wrong identity severity; CLAUDE.md:
    one chemical structure per record'
  normalization_reason: 'Blocker: the record fails the explicit one-structure identity
    contract, with independent exact-xref graph conflicts. Passing syntax and internal
    structure checks cannot establish mixture-to-molecule equivalence.'
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained EXCLUDE decision for the mixture source concept
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: ARO mixture identity and source cross-references
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Single-graph enrichment evidence
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Source-to-structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO concept eligibility
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Native regeneration
- finding_id: F2
  issue_key: gentamicin-c-cidomycin-product-alias-exact-typing
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Cidomycin is typed as an exact chemical synonym without its product scope
  description: The official Cidomycin SmPC identifies a gentamicin sulfate injectable
    product, not the neutral configured graph. The source-derived EXACT_SYNONYM typing
    should be suppressed or explicitly product-qualified in any retained representation.
    This bounded finding does not adjudicate all eight other aliases.
  target_ids:
  - antibioticmech:aro-6407ce57f1
  field_paths:
  - synonyms[0]
  evidence_ids:
  - record
  - brand
  - owners
  rule_id: 'src/antibioticmech/schema/antibioticmech.yaml: SynonymTypeEnum'
  normalization_reason: Minor product-versus-chemical synonym typing error, secondary
    to the independently blocking mixture identity defect.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Source synonym assertions
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained source synonym controls
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Native synonym generation
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-6407ce57f1
  description: Record a justified EXCLUDE for ARO:0000014 in curation/decisions.tsv
    and regenerate the eligible corpus through the maintained source lane. Preserve
    raw mixture metadata and provenance; independently review exact C congeners before
    any separate addition or claim reassignment. Consider source eligibility safeguards
    for explicit ARO antibiotic-mixture ancestry without treating partial stereochemistry
    as a mixture.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained EXCLUDE decision for the mixture source concept
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: ARO mixture identity and source cross-references
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Single-graph enrichment evidence
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Source-to-structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO concept eligibility
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Native regeneration
  generator: scripts/extract_source_inventory.py and scripts/seed_from_sources.py
  acceptance_checks:
  - Confirm the mixture concept is excluded reproducibly while raw evidence remains
    available.
  - Do not transfer mixture-level target/resistance claims to the native epimer or
    to C1a without independent material-specific evidence.
  - Run native schema, strict term, reference/history/corpus checks and QC after documented
    regeneration.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:aro-6407ce57f1
  description: If the source concept or its aliases are represented elsewhere after
    identity resolution, use the maintained source synonym controls to qualify Cidomycin
    as a trade/product name or exclude it from exact chemical synonyms. Preserve its
    gentamicin sulfate product context.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Source synonym assertions
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained source synonym controls
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Native synonym generation
  generator: scripts/extract_source_inventory.py and scripts/seed_from_sources.py
  acceptance_checks:
  - Compare against the official product14742 SmPC and ensure no sulfate-product clinical
    claim is assigned to a single neutral congener.
limitations:
- Twenty-seven of29 adopted/current leads supplied abstracts and were read completely;
  two review records were metadata-only. Most resistance originals were not read in
  full, so detailed material and assay support remains unresolved.
- The MexCD-OprJ and EmrE PMC main-text routes returned challenge HTML. Their complete
  original abstracts show important context limits, but this review does not claim
  a complete original-table audit or infer universal absence of resistance.
- The 1998 RNA paper was read at complete abstract/landing depth; its PDF request
  returned HTML. Its C1a NMR structure is not attributed to the mixture or native
  stereoisomer.
- The 2020 congener study was read at the selected sections and Figure1 stated above;
  Table1 only partly. The 2015 biosynthesis paper was read at abstract/introduction/pathway
  depth. Neither is claimed fully reviewed for all downstream experiments.
- The current ChEMBL and ChEBI discrepancies are independently graph-verified database
  identity conflicts, not a newly proven absolute configuration assignment for a physical
  native reagent. No automatic replacement graph is proposed.
- Only Cidomycin among the nine aliases was independently verified as a product here.
  A guessed Garamycin FDA route returned404; J-GLOBAL snapshot retrieval returned503,
  and neither failed retrieval is treated as inspected source content.
- The PMC7768767 follow-up route failed XML retrieval and returned HTML challenge;
  no full-original result from that paper is adopted.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Standalone chemistry used batch019 against batch050; native validators, source ledger
  and contract used batch050.
- No native/source bytes or scientific status were changed. Original input hashes
  are preserved; the draft records an exclusion recommendation, not an executed exclusion.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://pubchem.ncbi.nlm.nih.gov/compound/3084091
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7449222/
- https://www.medicines.org.uk/emc/product/14742/smpc
tags:
- record-review
- gentamicin-c
- mixture-boundary
```
