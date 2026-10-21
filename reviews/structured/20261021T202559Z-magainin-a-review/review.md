# Magainin A: coherent synthetic peptide with an incorrect natural-production definition

- Review: 20261021T202559Z-magainin-a-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T20:11:19Z
- Finished UTC: 2026-10-21T20:25:59Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The entire native record and actual ARO/PubChem source rows were reviewed. Native and current PubChem encodings agree with an independently constructed 23-residue synthetic magainin A sequence. Original inventor sequence and activity tables support its antibacterial identity. The definition incorrectly attributes this analog to amphibian production, while its adopted paper assays B, G and H. Correct the source-owned definition and its supporting citation without changing the coherent peptide graph.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Assigned queue position 624; one exact native record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-77a152a10f | data/antibiotics/antibacterial/magainin-a.yaml | generated | magainin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-77a152a10f | Actual focused execution exited 0. Chemistry used the 019 interpreter against 063 cwd; schema and strict validation used063. |
| Focused schema verification | passed | True | antibioticmech:aro-77a152a10f | Actual focused execution exited 0. Chemistry used the 019 interpreter against 063 cwd; schema and strict validation used063. |
| Focused strict verification | passed | True | antibioticmech:aro-77a152a10f | Actual focused execution exited 0. Chemistry used the 019 interpreter against 063 cwd; schema and strict validation used063. |
| Authoritative full QC | failed | True | antibioticmech:aro-77a152a10f | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-77a152a10f | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-77a152a10f | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-77a152a10f | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-77a152a10f | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-77a152a10f | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-77a152a10f | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-77a152a10f | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-77a152a10f | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact sequence, termini and stereochemistry

identity: supported. Targets: antibioticmech:aro-77a152a10f.

The complete native graph maps to a23-residue synthetic magainin A, with beta-alanine at position 1, alanine at 8/13/18 and C-terminal amide. Four native/current encodings and an independently assembled primary sequence agree, including all 23 stereocentres. No salt or natural-producer equivalence is inferred.

### Asserted cross-references and peptide class

grounding: supported. Targets: antibioticmech:aro-77a152a10f.

Both asserted xrefs resolve to the intended A concept/graph. The peptide-antibiotic parent is appropriate. There are no native synonyms, document or drug-level xrefs requiring additional dispositions.

### Synthetic analog versus amphibian family

evidence: concern. Targets: antibioticmech:aro-77a152a10f.

The native definition substitutes a natural magainin-family origin for exact synthetic A. Positive inventor synthesis and sequence evidence, plus the original 1989 synthetic comparison, establish the distinction. Adopted PMID2285300 assays B/G/H and does not support the A-specific production claim.

### Exact antibacterial eligibility and assay limits

evidence: supported. Targets: antibioticmech:aro-77a152a10f.

The inventor table contains exact A antibacterial measurements and the 1989 original abstract independently names A in E. coli growth experiments. Values remain bounded by the synthetic preparation and nonstandard short-incubation assay. B/G/H protozoal results, host PKC effects and natural magainin data are not transferred.

### No unasserted molecular target inferred

evidence: unknown. Targets: antibioticmech:aro-77a152a10f.

The native has no molecular target or mechanism object. The 1989 abstract provides membrane-potential and proteolysis comparisons, not a compound-specific protein-binding mechanism. A model liposome experiment does not alone establish a bacterial causal chain.

### Optional structured fields and reading depth

completeness: unknown. Targets: antibioticmech:aro-77a152a10f.

Absent optional activity, producer, resistance and causal graph objects are not defects. Exact source-supported enrichment could be curated separately. The one adopted citation was read in full scanned form; inaccessible1988/1989 originals and a truncated comparator abstract remain explicitly bounded.

### Whole record, actual owners and history

provenance: supported. Targets: antibioticmech:aro-77a152a10f.

Every native field and all three history events were read. Source rows and current authority comparisons establish the origin of the erroneous definition. Original 13 and expanded 21 hashes are unchanged; no native scientific status or history was modified.

## Findings

### F1: The definition assigns a synthetic magainin analog to amphibian production

major / open / confirmed; issue key: magainin-a-synthetic-analog-misattributed-to-amphibian-production.

Exact magainin A is the beta-alanine1/Ala8,13,18, C-terminal-amide synthetic analog documented in the inventor sequence and synthesis. The native definition instead says amphibians produce it as innate immunity. Its cited1990 paper tests B/G/H and distinguishes natural magainins from synthetic analogs; it does not establish natural production of A. Correct the definition and citation while retaining the coherent graph and supported antibacterial classification.

## Recommended Actions And Acceptance Checks

### A1

Correct the ARO-derived definition through maintained source handling and regenerate the record.

- Describe A as a synthetic magainin-2 analog with its verified modifications; distinguish the natural amphibian family from the manufactured compound.
- Attach exact-compound primary sequence/synthesis and antibacterial support, preserving the old ARO provenance without treating PMID2285300 as an A-specific experiment.
- Retain the coherent native graph and PubChem xref; do not transfer B/G/H protozoal measurements, PKC effects or unspecified counterion details.
- Regenerate and run focused and required shared validation checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/magainin-a.yaml; Entire native record, including three history events | supports | ARO-derived magainin A has a neutral single-component peptide graph, two xrefs and a peptide-antibiotic parent/class. The definition asserts amphibian production and antimicrobial activity. No separate structured target, resistance, activity spectrum, producer, product or causal graph objects are present. |
| owners | data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; curation/record_review_queue.tsv; Exact ARO row261, PubChem row86 and readiness row2752 | context_only | ARO owns the name, definition, citation and source concept; PubChem supplies the exact graph. Original 13 captured inputs were preserved and actual owner/context inputs expanded to 21 before detailed assessment. The maintained PubChem script is scripts/enrich_pubchem_structures.py. |
| search | /private/tmp/am-review-session/624-context-search.txt; Hidden- and ignored-inclusive local search | context_only | The bounded search covered native identifiers, magainin names and the structure-key prefix in data/raw, curation, conf, scripts and reports, alongside preserved initial local hits. The imported natural-production sentence reproduces its ARO source. |
| adapter | /private/tmp/am-review-session/624-adapter-scope.json; Applicability determined before open-ended literature research | context_only | The native record names no protein, gene or pathway claim. Amphibian innate immunity is broad producer context, so a protein/pathway adapter query is not applicable to this exact record. No adapter result is implied. |
| aro | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3003567; Current ARO3003567 term, definition, PMID and PubChem xref | partial | The current official term reproduces the native name, natural-production definition, PMID2285300 and CID16132424. Faithful propagation does not independently validate the incorrect producer attribution. |
| parent | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3000053; Current ARO3000053 definition | supports | The peptide-antibiotic parent is compatible with this peptide and the exact antibacterial experiment. Generic membrane language in the class definition is not treated as a demonstrated magainin A molecular target. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/16132424/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON; Asserted exact CID16132424 properties | supports | Current PubChem retains PIMDIROPKFPSDI-BXRJKVPUSA-N, neutral C117H187N31O27S and matching mass values. Its SMILES and InChI were independently parsed. |
| pubchem-sequence | https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/16132424/JSON; Biologic line notation and depositor-supplied synonyms | supports | The structured sequence is H-betaAla-Ile-Gly-Lys-Phe-Leu-His-Ala-Ala-Lys-Lys-Phe-Ala-Lys-Ala-Phe-Val-Ala-Glu-Ile-Met-Asn-Ser-NH2. This authority annotation agrees with independently inspected primary sequence evidence; depositor names alone are not the proof of natural origin. |
| chemistry | /private/tmp/am-review-session/624-authority-chemistry.json; Four native/authority encodings and one independently constructed sequence; residue-to-native atom map | supports | Native SMILES/InChI and current PubChem SMILES/InChI agree. Building the inventor claim 5 sequence from L-amino-acid templates, replacing terminal Gly with beta-alanine and amidating the C terminus reproduces the native key and reciprocal chirality-aware graph matches. There are 23 assigned centres and no unassigned centres. The 2492.0 source weight is compatible with calculated 2492.04 at its reported precision. The source mint also reproduces. |
| adopted1990 | PMID:2285300; DOI:10.1128/AAC.34.9.1824; https://pmc.ncbi.nlm.nih.gov/articles/PMC171939/; All three original scan pages 1824–1826 read; sequence block, methods, results, references and Figure 1 caption | partial | This original synthesizes and assays analogs B, G and H. It distinguishes these from naturally isolated magainins 1/2 and does not supply an A experiment. Protozoal endpoints are morphology, motility and membrane leakage at 50–500 micrograms/mL, not bacterial MICs. Its discussion leaves the precise antiprotozoal mechanism unresolved. The adopted citation cannot support the native claim that amphibians produce exact A. |
| adopted1990-figure | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3953/171939/e5211ed7d174/aac00065-0227.png; Actual Figure 1 scan on p1825 and its full caption | context_only | The scanned images were opened, but panels are extremely dark and detailed morphology cannot be independently resolved. The caption attributes the experiments to B, not A. Caption statements are distinguished from visual confirmation of individual cell changes. |
| adopted1990-end | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3953/171939/11e3ee60a5fc/aac00065-0228.png; Original p1826 discussion and references | context_only | The paper explicitly concludes in-vitro activity for B and G and calls for in-vivo work. Its references lead to the 1988 synthetic analog study. Nothing in this page assigns exact A to an amphibian producer or establishes a specific protein target. |
| patent-sequence | https://patents.google.com/patent/US5221732A/en; Inventor original PDF p5, Table 1 and synthesis; claim 5 on p7; actual Table 1 image inspected | supports | The inventor source defines A as synthetic betaAla1/Ala8,13,18 magainin-2 amide. Claim5 spells out the complete sequence. Solid-phase synthesis and chromatographic purification are described, with greater than 93% HPLC purity. These are positive identity and production data, not an argument from failure to find natural isolation. |
| patent-activity | https://patentimages.storage.googleapis.com/21/09/ae/d05ea212075f40/US5221732.pdf; Original PDF p6, Table 3 columnA and adjacent assay methods; actual table inspected | partial | A has reported 100% growth-inhibition endpoints of 2.5,25,25,1,10,10,10 micrograms/mL against E. coli 25922, K. pneumoniae 13883, P. aeruginosa 27853, S. agalactiae 12386, historical S. faecalis 29212 and S. aureus 29213/25923, respectively. The modified macrodilution assay uses trypticase soy broth, inocula 10^5 and10^6 CFU/mL, 35 °C and 6–9 h OD600 readout. Paired50% endpoints are distinct. Counterion stoichiometry and assignment of each inoculum to a table row are not specified. These preparation-specific values are not clinical breakpoints or MBCs. |
| original1989 | PMID:2544449; DOI:10.1016/0014-5793(89)80627-1; Complete original abstract; full publisher PDF/HTML unavailable | partial | The original explicitly compares synthetic magainin 2 amide with analog A in E. coli growth and membrane-potential experiments, and in cytochrome-oxidase liposomes. It reports stronger growth inhibition by A but a much smaller difference in the model membrane system, with proteolysis suggested as an explanation. Exact strain, reagent form and full quantitative methods were not recovered; these are not inferred from the abstract. |
| lead-3410055 | PMID:3410055; Additional primary discovery lead; abstract depth only | context_only | The 1988 synthetic magainin-2 analog study reports enhanced antimicrobial activity in its complete abstract, but individual A/B tables were inaccessible. |
| lead-2365080 | PMID:2365080; Additional primary discovery lead; abstract depth only | context_only | The 1990 PKC paper explicitly defines B through Ala8,13,18 substitutions in magainin-2 amide; its kinase experiments concern B and are not transferred to A or treated as an antibacterial target. |
| lead-1708887 | PMID:1708887; Additional primary discovery lead; abstract depth only | context_only | The 1991 paper concerns cytolysis of transformed mammalian cells by magainin 2 and synthetic analogs; its abstract does not resolve exact A-specific antibacterial measurements. |
| lead-3277183 | PMID:3277183; Additional primary discovery lead; abstract depth only | context_only | The 1988 paper compares synthetic natural-sequence magainins with isolated peptides; it does not establish natural production of the modified A sequence. |
| lead-3299384 | PMID:3299384; Additional primary discovery lead; abstract depth only | context_only | The 1987 isolation paper describes two natural23-residue peptides from Xenopus skin. Its complete abstract supports family context, not natural biosynthesis of the beta-alanine/Ala-substituted amidated A analog. |
| lead-2980783 | PMID:2980783; Additional primary discovery lead; abstract depth only | context_only | The 1988 omission-analog study supplies only a database-truncated abstract. Its different peptide series is contextual and no result is transferred to A. |
| access | /private/tmp/am-review-session/624-fetch2.json; /private/tmp/am-review-session/624-fetch4.json; /private/tmp/am-review-session/624-fetch5.json; Recorded free public retrieval attempts and bounded title screening | context_only | EuropePMC fullTextXML returned500; PMC PDF routes returned HTML challenges, while all three original scan pages were available. The 1988/1989 Wiley original routes returned403. The broader search was polluted by family literature; the first 100 titles of the refined363-hit result were screened, with the exact adopted original, inventor patent and selected historical comparators followed. No exhaustive family bibliography is claimed. |

## Limits And Additional Notes

- The 1988 and1989 full originals were unavailable through attempted public publisher routes. Complete abstracts were read, and the inventor original patent independently supplied the exact sequence, synthesis and activity tables. The 1988 omission-series abstract is explicitly truncated.
- All three1990 scan pages and the actual Figure 1 scan were inspected, but the image panels are too dark for detailed independent morphology interpretation. Reported results and captions remain distinguished from visible image evidence.
- Patent endpoints are preparation- and protocol-specific. Counterion stoichiometry, per-row assignment of the two inoculum densities and clinical breakpoint relevance are unresolved; none is inferred.
- The bounded discovery reviewed the first 100 refined titles and selected exact sources, not every magainin-family publication.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Original 13 and expanded 21 input hashes remain unchanged; all edits were limited to review scratch artifacts.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T202559Z-magainin-a-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Magainin A: coherent synthetic peptide with an incorrect natural-production
  definition'
started_at: '2026-10-21T20:11:19Z'
finished_at: '2026-10-21T20:25:59Z'
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
summary: The entire native record and actual ARO/PubChem source rows were reviewed.
  Native and current PubChem encodings agree with an independently constructed 23-residue
  synthetic magainin A sequence. Original inventor sequence and activity tables support
  its antibacterial identity. The definition incorrectly attributes this analog to
  amphibian production, while its adopted paper assays B, G and H. Correct the source-owned
  definition and its supporting citation without changing the coherent peptide graph.
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
  - path: data/antibiotics/antibacterial/magainin-a.yaml
    sha256: a87afe79402b57578bb6b325140fbc82a435b76c36b6da0abdfc832639fca522
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
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: curation/record_review_queue.tsv
    sha256: 3828a5120b892ee0ee0b776affc6c3e4f1f1a3355ec4edd30e6005762de00e70
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
    role: context
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
targets:
- target_id: antibioticmech:aro-77a152a10f
  path: data/antibiotics/antibacterial/magainin-a.yaml
  label: magainin A
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, definition and citation
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact PubChem graph
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Assigned queue position 624; one exact native record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-77a152a10f
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0. Chemistry used the 019 interpreter against
    063 cwd; schema and strict validation used063.
  target_ids:
  - antibioticmech:aro-77a152a10f
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    624
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Chemistry used the 019 interpreter against
    063 cwd; schema and strict validation used063.
  target_ids:
  - antibioticmech:aro-77a152a10f
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/magainin-a.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Chemistry used the 019 interpreter against
    063 cwd; schema and strict validation used063.
  target_ids:
  - antibioticmech:aro-77a152a10f
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/magainin-a.yaml --out /private/tmp/am-review-session/624-strict.tsv
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
  - antibioticmech:aro-77a152a10f
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
  - antibioticmech:aro-77a152a10f
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
  - antibioticmech:aro-77a152a10f
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
  - antibioticmech:aro-77a152a10f
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
  - antibioticmech:aro-77a152a10f
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
  - antibioticmech:aro-77a152a10f
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
  - antibioticmech:aro-77a152a10f
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
  - antibioticmech:aro-77a152a10f
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
  - antibioticmech:aro-77a152a10f
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/magainin-a.yaml
  locator: Entire native record, including three history events
  accessed_at: '2026-10-21T20:22:41Z'
  support: supports
  summary: ARO-derived magainin A has a neutral single-component peptide graph, two
    xrefs and a peptide-antibiotic parent/class. The definition asserts amphibian
    production and antimicrobial activity. No separate structured target, resistance,
    activity spectrum, producer, product or causal graph objects are present.
  snapshot_sha256: a87afe79402b57578bb6b325140fbc82a435b76c36b6da0abdfc832639fca522
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; curation/record_review_queue.tsv
  locator: Exact ARO row261, PubChem row86 and readiness row2752
  accessed_at: '2026-10-21T20:22:41Z'
  support: context_only
  summary: ARO owns the name, definition, citation and source concept; PubChem supplies
    the exact graph. Original 13 captured inputs were preserved and actual owner/context
    inputs expanded to 21 before detailed assessment. The maintained PubChem script
    is scripts/enrich_pubchem_structures.py.
  snapshot_sha256: 96890c0ef82f6601c146c02ec2b70c7425ef9204caeffbaa1f215d53ffbccd20
- evidence_id: search
  kind: search
  reference: /private/tmp/am-review-session/624-context-search.txt
  locator: Hidden- and ignored-inclusive local search
  accessed_at: '2026-10-21T20:22:41Z'
  support: context_only
  summary: The bounded search covered native identifiers, magainin names and the structure-key
    prefix in data/raw, curation, conf, scripts and reports, alongside preserved initial
    local hits. The imported natural-production sentence reproduces its ARO source.
  snapshot_sha256: 625573f1be49877e49cb57423e2be97efd61d20bf769f34dfd9e36457f5a99d1
  search_scope: rg --no-ignore --hidden -n -i magainin|ARO:3003567|PIMDIROPKFPSDI
    over data/raw, curation, conf, scripts and reports, plus initial local hits.
- evidence_id: adapter
  kind: search
  reference: /private/tmp/am-review-session/624-adapter-scope.json
  locator: Applicability determined before open-ended literature research
  accessed_at: '2026-10-21T20:22:41Z'
  support: context_only
  summary: The native record names no protein, gene or pathway claim. Amphibian innate
    immunity is broad producer context, so a protein/pathway adapter query is not
    applicable to this exact record. No adapter result is implied.
  snapshot_sha256: 0d5cc0b04fe241139f22986aea1d1fe38aff5855f914857d94f9ce0b9e4d5c19
  search_scope: Full native field inventory and definition checked for named protein/pathway
    claims before web follow-up.
- evidence_id: aro
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3003567
  locator: Current ARO3003567 term, definition, PMID and PubChem xref
  accessed_at: '2026-10-21T20:18:39.284181Z'
  support: partial
  summary: The current official term reproduces the native name, natural-production
    definition, PMID2285300 and CID16132424. Faithful propagation does not independently
    validate the incorrect producer attribution.
  snapshot_sha256: fd70f71682dab20e4cdad698964875ec46ae8183ebff5557b667741cebb97be8
- evidence_id: parent
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3000053
  locator: Current ARO3000053 definition
  accessed_at: '2026-10-21T20:18:39.284501Z'
  support: supports
  summary: The peptide-antibiotic parent is compatible with this peptide and the exact
    antibacterial experiment. Generic membrane language in the class definition is
    not treated as a demonstrated magainin A molecular target.
  snapshot_sha256: b6ab78fcd5c01625148a14ecb461eb0b963eaf49e1c5992b9b06ea601f8cb57c
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/16132424/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON
  locator: Asserted exact CID16132424 properties
  accessed_at: '2026-10-21T20:18:39.283097Z'
  support: supports
  summary: Current PubChem retains PIMDIROPKFPSDI-BXRJKVPUSA-N, neutral C117H187N31O27S
    and matching mass values. Its SMILES and InChI were independently parsed.
  snapshot_sha256: b767503da61e85467bb5e0df82f65dd9398603d16b689dcd5744e97119be79e3
- evidence_id: pubchem-sequence
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/16132424/JSON
  locator: Biologic line notation and depositor-supplied synonyms
  accessed_at: '2026-10-21T20:18:39.284040Z'
  support: supports
  summary: The structured sequence is H-betaAla-Ile-Gly-Lys-Phe-Leu-His-Ala-Ala-Lys-Lys-Phe-Ala-Lys-Ala-Phe-Val-Ala-Glu-Ile-Met-Asn-Ser-NH2.
    This authority annotation agrees with independently inspected primary sequence
    evidence; depositor names alone are not the proof of natural origin.
  snapshot_sha256: 7b12def0e0ef71eb24b6700710d1d30600c22303ccc0ea97ab59270c1ed7f6fd
- evidence_id: chemistry
  kind: validation
  reference: /private/tmp/am-review-session/624-authority-chemistry.json
  locator: Four native/authority encodings and one independently constructed sequence;
    residue-to-native atom map
  accessed_at: '2026-10-21T20:22:41Z'
  support: supports
  summary: Native SMILES/InChI and current PubChem SMILES/InChI agree. Building the
    inventor claim 5 sequence from L-amino-acid templates, replacing terminal Gly
    with beta-alanine and amidating the C terminus reproduces the native key and reciprocal
    chirality-aware graph matches. There are 23 assigned centres and no unassigned
    centres. The 2492.0 source weight is compatible with calculated 2492.04 at its
    reported precision. The source mint also reproduces.
  snapshot_sha256: f5f4531a43a983694c42eed464be041c4fa4db3bb0bf2dbfbfe980a50298f058
- evidence_id: adopted1990
  kind: primary_source
  reference: PMID:2285300; DOI:10.1128/AAC.34.9.1824; https://pmc.ncbi.nlm.nih.gov/articles/PMC171939/
  locator: All three original scan pages 1824–1826 read; sequence block, methods,
    results, references and Figure 1 caption
  accessed_at: '2026-10-21T20:20:30.883022Z'
  support: partial
  summary: This original synthesizes and assays analogs B, G and H. It distinguishes
    these from naturally isolated magainins 1/2 and does not supply an A experiment.
    Protozoal endpoints are morphology, motility and membrane leakage at 50–500 micrograms/mL,
    not bacterial MICs. Its discussion leaves the precise antiprotozoal mechanism
    unresolved. The adopted citation cannot support the native claim that amphibians
    produce exact A.
  snapshot_sha256: 5ccd1346bfff1e5ea1d5cf3336cac8fcdac637120f5e66f38d5a0af0acf4169e
- evidence_id: adopted1990-figure
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3953/171939/e5211ed7d174/aac00065-0227.png
  locator: Actual Figure 1 scan on p1825 and its full caption
  accessed_at: '2026-10-21T20:20:30.886937Z'
  support: context_only
  summary: The scanned images were opened, but panels are extremely dark and detailed
    morphology cannot be independently resolved. The caption attributes the experiments
    to B, not A. Caption statements are distinguished from visual confirmation of
    individual cell changes.
  snapshot_sha256: 7788ae01e9559f71a153d22d1dbd3739ac1a55c7f7e69391eaba7c2846d57d17
- evidence_id: adopted1990-end
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3953/171939/11e3ee60a5fc/aac00065-0228.png
  locator: Original p1826 discussion and references
  accessed_at: '2026-10-21T20:20:30.887650Z'
  support: context_only
  summary: The paper explicitly concludes in-vitro activity for B and G and calls
    for in-vivo work. Its references lead to the 1988 synthetic analog study. Nothing
    in this page assigns exact A to an amphibian producer or establishes a specific
    protein target.
  snapshot_sha256: c6de8efe500b20b4733fbece80900e1255c3a05618f1f74464cd8240b35ef14e
- evidence_id: patent-sequence
  kind: primary_source
  reference: https://patents.google.com/patent/US5221732A/en
  locator: Inventor original PDF p5, Table 1 and synthesis; claim 5 on p7; actual
    Table 1 image inspected
  accessed_at: '2026-10-21T20:21:03.126743Z'
  support: supports
  summary: The inventor source defines A as synthetic betaAla1/Ala8,13,18 magainin-2
    amide. Claim5 spells out the complete sequence. Solid-phase synthesis and chromatographic
    purification are described, with greater than 93% HPLC purity. These are positive
    identity and production data, not an argument from failure to find natural isolation.
  snapshot_sha256: b11506108b20c42700706e1f269707a7831df446edd3c478560c1cf37debd634
- evidence_id: patent-activity
  kind: primary_source
  reference: https://patentimages.storage.googleapis.com/21/09/ae/d05ea212075f40/US5221732.pdf
  locator: Original PDF p6, Table 3 columnA and adjacent assay methods; actual table
    inspected
  accessed_at: '2026-10-21T20:21:03.126743Z'
  support: partial
  summary: A has reported 100% growth-inhibition endpoints of 2.5,25,25,1,10,10,10
    micrograms/mL against E. coli 25922, K. pneumoniae 13883, P. aeruginosa 27853,
    S. agalactiae 12386, historical S. faecalis 29212 and S. aureus 29213/25923, respectively.
    The modified macrodilution assay uses trypticase soy broth, inocula 10^5 and10^6
    CFU/mL, 35 °C and 6–9 h OD600 readout. Paired50% endpoints are distinct. Counterion
    stoichiometry and assignment of each inoculum to a table row are not specified.
    These preparation-specific values are not clinical breakpoints or MBCs.
  snapshot_sha256: b11506108b20c42700706e1f269707a7831df446edd3c478560c1cf37debd634
- evidence_id: original1989
  kind: primary_source
  reference: PMID:2544449; DOI:10.1016/0014-5793(89)80627-1
  locator: Complete original abstract; full publisher PDF/HTML unavailable
  accessed_at: '2026-10-21T20:20:30.893866Z'
  support: partial
  summary: The original explicitly compares synthetic magainin 2 amide with analog
    A in E. coli growth and membrane-potential experiments, and in cytochrome-oxidase
    liposomes. It reports stronger growth inhibition by A but a much smaller difference
    in the model membrane system, with proteolysis suggested as an explanation. Exact
    strain, reagent form and full quantitative methods were not recovered; these are
    not inferred from the abstract.
  snapshot_sha256: 7eb080614c0abb58fdbe086c3e0f4577bcfcaf8a6220dce0645bf5412011d746
- evidence_id: lead-3410055
  kind: primary_source
  reference: PMID:3410055
  locator: Additional primary discovery lead; abstract depth only
  accessed_at: '2026-10-21T20:20:30.893866Z'
  support: context_only
  summary: The 1988 synthetic magainin-2 analog study reports enhanced antimicrobial
    activity in its complete abstract, but individual A/B tables were inaccessible.
  snapshot_sha256: 7eb080614c0abb58fdbe086c3e0f4577bcfcaf8a6220dce0645bf5412011d746
- evidence_id: lead-2365080
  kind: primary_source
  reference: PMID:2365080
  locator: Additional primary discovery lead; abstract depth only
  accessed_at: '2026-10-21T20:20:30.893866Z'
  support: context_only
  summary: The 1990 PKC paper explicitly defines B through Ala8,13,18 substitutions
    in magainin-2 amide; its kinase experiments concern B and are not transferred
    to A or treated as an antibacterial target.
  snapshot_sha256: 7eb080614c0abb58fdbe086c3e0f4577bcfcaf8a6220dce0645bf5412011d746
- evidence_id: lead-1708887
  kind: primary_source
  reference: PMID:1708887
  locator: Additional primary discovery lead; abstract depth only
  accessed_at: '2026-10-21T20:20:30.893866Z'
  support: context_only
  summary: The 1991 paper concerns cytolysis of transformed mammalian cells by magainin
    2 and synthetic analogs; its abstract does not resolve exact A-specific antibacterial
    measurements.
  snapshot_sha256: 7eb080614c0abb58fdbe086c3e0f4577bcfcaf8a6220dce0645bf5412011d746
- evidence_id: lead-3277183
  kind: primary_source
  reference: PMID:3277183
  locator: Additional primary discovery lead; abstract depth only
  accessed_at: '2026-10-21T20:20:30.893866Z'
  support: context_only
  summary: The 1988 paper compares synthetic natural-sequence magainins with isolated
    peptides; it does not establish natural production of the modified A sequence.
  snapshot_sha256: 7eb080614c0abb58fdbe086c3e0f4577bcfcaf8a6220dce0645bf5412011d746
- evidence_id: lead-3299384
  kind: primary_source
  reference: PMID:3299384
  locator: Additional primary discovery lead; abstract depth only
  accessed_at: '2026-10-21T20:20:30.893866Z'
  support: context_only
  summary: The 1987 isolation paper describes two natural23-residue peptides from
    Xenopus skin. Its complete abstract supports family context, not natural biosynthesis
    of the beta-alanine/Ala-substituted amidated A analog.
  snapshot_sha256: 7eb080614c0abb58fdbe086c3e0f4577bcfcaf8a6220dce0645bf5412011d746
- evidence_id: lead-2980783
  kind: primary_source
  reference: PMID:2980783
  locator: Additional primary discovery lead; abstract depth only
  accessed_at: '2026-10-21T20:20:30.893866Z'
  support: context_only
  summary: The 1988 omission-analog study supplies only a database-truncated abstract.
    Its different peptide series is contextual and no result is transferred to A.
  snapshot_sha256: 7eb080614c0abb58fdbe086c3e0f4577bcfcaf8a6220dce0645bf5412011d746
- evidence_id: access
  kind: search
  reference: /private/tmp/am-review-session/624-fetch2.json; /private/tmp/am-review-session/624-fetch4.json;
    /private/tmp/am-review-session/624-fetch5.json
  locator: Recorded free public retrieval attempts and bounded title screening
  accessed_at: '2026-10-21T20:22:41Z'
  support: context_only
  summary: EuropePMC fullTextXML returned500; PMC PDF routes returned HTML challenges,
    while all three original scan pages were available. The 1988/1989 Wiley original
    routes returned403. The broader search was polluted by family literature; the
    first 100 titles of the refined363-hit result were screened, with the exact adopted
    original, inventor patent and selected historical comparators followed. No exhaustive
    family bibliography is claimed.
  snapshot_sha256: dcf001b4ccd14836530c5d5c44f2a454be773fd6a9a55ccafb4f1f521b3e8847
  search_scope: Stored EuropePMC TITLE_ABS magainin A query, then magainin AND (beta-alanine
    OR magainin A OR magainin B),1987–1995; first100 refined titles and selected exact
    PMID/DOI routes. Not all363 results or all family originals were read.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact sequence, termini and stereochemistry
  outcome: supported
  summary: The complete native graph maps to a23-residue synthetic magainin A, with
    beta-alanine at position 1, alanine at 8/13/18 and C-terminal amide. Four native/current
    encodings and an independently assembled primary sequence agree, including all
    23 stereocentres. No salt or natural-producer equivalence is inferred.
  target_ids:
  - antibioticmech:aro-77a152a10f
  evidence_ids:
  - native
  - pubchem
  - pubchem-sequence
  - chemistry
  - patent-sequence
- assessment_id: grounding
  area: grounding
  topic: Asserted cross-references and peptide class
  outcome: supported
  summary: Both asserted xrefs resolve to the intended A concept/graph. The peptide-antibiotic
    parent is appropriate. There are no native synonyms, document or drug-level xrefs
    requiring additional dispositions.
  target_ids:
  - antibioticmech:aro-77a152a10f
  evidence_ids:
  - aro
  - parent
  - pubchem
  - chemistry
- assessment_id: production
  area: evidence
  topic: Synthetic analog versus amphibian family
  outcome: concern
  summary: The native definition substitutes a natural magainin-family origin for
    exact synthetic A. Positive inventor synthesis and sequence evidence, plus the
    original 1989 synthetic comparison, establish the distinction. Adopted PMID2285300
    assays B/G/H and does not support the A-specific production claim.
  target_ids:
  - antibioticmech:aro-77a152a10f
  evidence_ids:
  - native
  - patent-sequence
  - original1989
  - adopted1990
- assessment_id: activity
  area: evidence
  topic: Exact antibacterial eligibility and assay limits
  outcome: supported
  summary: The inventor table contains exact A antibacterial measurements and the
    1989 original abstract independently names A in E. coli growth experiments. Values
    remain bounded by the synthetic preparation and nonstandard short-incubation assay.
    B/G/H protozoal results, host PKC effects and natural magainin data are not transferred.
  target_ids:
  - antibioticmech:aro-77a152a10f
  evidence_ids:
  - patent-activity
  - original1989
  - adopted1990
  - lead-2365080
- assessment_id: mechanism
  area: evidence
  topic: No unasserted molecular target inferred
  outcome: unknown
  summary: The native has no molecular target or mechanism object. The 1989 abstract
    provides membrane-potential and proteolysis comparisons, not a compound-specific
    protein-binding mechanism. A model liposome experiment does not alone establish
    a bacterial causal chain.
  target_ids:
  - antibioticmech:aro-77a152a10f
  evidence_ids:
  - native
  - original1989
  - adapter
- assessment_id: completeness
  area: completeness
  topic: Optional structured fields and reading depth
  outcome: unknown
  summary: Absent optional activity, producer, resistance and causal graph objects
    are not defects. Exact source-supported enrichment could be curated separately.
    The one adopted citation was read in full scanned form; inaccessible1988/1989
    originals and a truncated comparator abstract remain explicitly bounded.
  target_ids:
  - antibioticmech:aro-77a152a10f
  evidence_ids:
  - native
  - adopted1990
  - access
- assessment_id: provenance
  area: provenance
  topic: Whole record, actual owners and history
  outcome: supported
  summary: Every native field and all three history events were read. Source rows
    and current authority comparisons establish the origin of the erroneous definition.
    Original 13 and expanded 21 hashes are unchanged; no native scientific status
    or history was modified.
  target_ids:
  - antibioticmech:aro-77a152a10f
  evidence_ids:
  - owners
  - search
  - native
  - aro
findings:
- finding_id: F1
  issue_key: magainin-a-synthetic-analog-misattributed-to-amphibian-production
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The definition assigns a synthetic magainin analog to amphibian production
  description: Exact magainin A is the beta-alanine1/Ala8,13,18, C-terminal-amide
    synthetic analog documented in the inventor sequence and synthesis. The native
    definition instead says amphibians produce it as innate immunity. Its cited1990
    paper tests B/G/H and distinguishes natural magainins from synthetic analogs;
    it does not establish natural production of A. Correct the definition and citation
    while retaining the coherent graph and supported antibacterial classification.
  target_ids:
  - antibioticmech:aro-77a152a10f
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - native
  - aro
  - chemistry
  - patent-sequence
  - original1989
  - adopted1990
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO definition and citation
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition and provenance owner
  rule_id: 'review-yaml-record: exact-compound producer and claim-level primary support'
  normalization_reason: Major false producer/definition attribution supported by positive
    original synthesis and sequence evidence. Exact chemical identity is coherent,
    so this is not a wrong-structure blocker.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-77a152a10f
  description: Correct the ARO-derived definition through maintained source handling
    and regenerate the record.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO definition and citation
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition and provenance owner
  generator: scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  acceptance_checks:
  - Describe A as a synthetic magainin-2 analog with its verified modifications; distinguish
    the natural amphibian family from the manufactured compound.
  - Attach exact-compound primary sequence/synthesis and antibacterial support, preserving
    the old ARO provenance without treating PMID2285300 as an A-specific experiment.
  - Retain the coherent native graph and PubChem xref; do not transfer B/G/H protozoal
    measurements, PKC effects or unspecified counterion details.
  - Regenerate and run focused and required shared validation checks.
limitations:
- The 1988 and1989 full originals were unavailable through attempted public publisher
  routes. Complete abstracts were read, and the inventor original patent independently
  supplied the exact sequence, synthesis and activity tables. The 1988 omission-series
  abstract is explicitly truncated.
- All three1990 scan pages and the actual Figure 1 scan were inspected, but the image
  panels are too dark for detailed independent morphology interpretation. Reported
  results and captions remain distinguished from visible image evidence.
- Patent endpoints are preparation- and protocol-specific. Counterion stoichiometry,
  per-row assignment of the two inoculum densities and clinical breakpoint relevance
  are unresolved; none is inferred.
- The bounded discovery reviewed the first 100 refined titles and selected exact sources,
  not every magainin-family publication.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Original 13 and expanded 21 input hashes remain unchanged; all edits were limited
  to review scratch artifacts.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
