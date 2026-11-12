# Hexadecan-2-ol: coherent secondary alcohol with bounded antibacterial evidence

- Review: 20261021T181616Z-hexadecan-2-ol-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T18:00:54Z
- Finished UTC: 2026-10-21T18:16:16Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The neutral C16 secondary-alcohol graph, four synonyms and broader classes agree with current authorities. Its single stereocentre is unassigned, which does not assert a racemate. All seven adopted references were resolved at their actual reading depths. Exact antibacterial support includes an inspected patent experiment and a separately qualified ChEMBL extraction of the inaccessible antiacne paper. No required native correction was established. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Assigned queue position 531; one exact native record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:185029 | data/antibiotics/antibacterial/hexadecan-2-ol.yaml | generated | hexadecan-2-ol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:185029 | Actual focused execution exited 0. Executed against worktree 054; chemistry used existing 019 RDKit and native validators used 054. |
| Focused schema verification | passed | True | CHEBI:185029 | Actual focused execution exited 0. Executed against worktree 054; chemistry used existing 019 RDKit and native validators used 054. |
| Focused strict verification | passed | True | CHEBI:185029 | Actual focused execution exited 0. Executed against worktree 054; chemistry used existing 019 RDKit and native validators used 054. |
| Authoritative full QC | failed | True | CHEBI:185029 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:185029 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:185029 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:185029 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:185029 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:185029 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:185029 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:185029 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:185029 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact positional alcohol and unspecified stereochemistry

identity: supported. Targets: CHEBI:185029.

The neutral secondary-alcohol constitution, four names, formula and masses agree with authorities. The single unassigned centre is a partially specified graph, not evidence of a racemate or an automatically wrong exact identifier. No source-specific enantiomer is silently substituted.

### Chemical xrefs and broader terms

grounding: supported. Targets: CHEBI:185029.

CHEBI:185029 and ChemSpider 77368 resolve to the exact graph. Secondary fatty alcohol and hexadecanol are compatible broader classes. CAS and Reaxys have corroborating identifier associations but independent registry access remains limited, without evidence of a wrong xref.

### Qualitative antibacterial role and experimental depth

evidence: supported. Targets: CHEBI:185029.

The inspected patent reports an exact positional-isomer antibacterial experiment, and the adopted antiacne publication has an exact graph-mapped ChEMBL MIC extraction. Together these support retaining the qualitative role while the original antiacne assay remains unverified. No quantitative native MIC, membrane target, clinical indication or broad-spectrum assertion is present.

### All seven adopted leads and optional biological fields

completeness: unknown. Targets: CHEBI:185029.

All seven original abstracts were read, plus selected 1998 metabolic sections and exact patent experiment/figures. Catabolism, interface physics and host-cell apoptosis do not establish antibacterial mechanism. Original antiacne table access and material scope remain unresolved; absent optional targets, resistance, producer and activity_spectrum fields are not native defects.

### Source ownership, history and read-only assessment

provenance: supported. Targets: CHEBI:185029.

The entire native record, exact source row and three chronological seed/reseed events were read. Original 13 and expanded 21 input hashes remain unchanged. ChEBI extraction/seeding owns generated content; no curator ownership or status promotion was invented.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optional follow-up: inspect the original antiacne experiment before adding detailed activity or mechanism.

- Retrieve and inspect the exact 2-hexadecanol row, preparation, medium, inoculum and endpoint in PMID:8158169; preserve the current ChEMBL value as database evidence until then.
- Do not import plant-extract, positional-isomer, apoptosis or catabolic-substrate results as direct exact-compound antibacterial mechanism.
- Preserve unspecified stereo unless the tested material is independently characterized; patent disc measurements and coating/larval outcomes must not become MICs or clinical efficacy.
- Resolve free CAS/Reaxys exact registry access before claiming every xref independently verified; no correction is required merely because access is unavailable.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/hexadecan-2-ol.yaml; Entire native record: definition, all four synonyms, two parents, role, chemistry, three xrefs and history | supports | The SEEDED exact record denotes neutral hexadecan-2-ol, C16H34O, key FVDRFBGMOWJEOR-UHFFFAOYSA-N. One tetrahedral centre is unspecified. It contains no primary target, resistance, activity_spectrum, producer, causal graph or clinical-product assertion. |
| owners | data/raw/chebi_antimicrobials.tsv#CHEBI:185029; Adopted ChEBI row 2846, readiness row 1377 and exact curator/decision search | context_only | The adopted row supplies the complete native content and seven PMID leads. All original 13 hashes were preserved and expanded to 21 context/owner inputs. No exact curator or decision override was found. |
| search | /private/tmp/am-review-session/531-context-search.txt; Original whole-tree capture and exact owner follow-up | context_only | Identifier, label and slug searches included hidden and gitignored content; no absence assertion relies on default ignored-file exclusion. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/185029/; CHEBI:185029 current definition, graph, synonyms and accessions | supports | Current ChEBI reproduces the native exact secondary-alcohol graph and names. The C-2 alcohol is distinct from hexadecan-1-ol and other positional isomers. Neither native nor current graph specifies absolute configuration or enantiomeric composition. |
| chemspider | https://www.chemspider.com/Chemical-Structure.77368.html; ChemSpider 77368 embedded current structure data; decoded531-chemspider-fields.json | supports | The current ChemSpider page directly supplies the matching SMILES and Standard InChI/key. Its listed CAS 14852-31-4 and database identifier 1748421 corroborate source associations, but do not substitute for independent access to the CAS/Reaxys registry records. |
| mapping | /private/tmp/am-review-session/531-map.py; 019 RDKit2026.03.5, cwd054; seven native/authority encodings | supports | Native, ChEBI and ChemSpider SMILES/InChI and additional PubChem InChI all agree at complete key, formula, charge and reciprocal graph match. There is one unassigned secondary-alcohol centre. Formula, masses, mint and encoding checks pass. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/hexadecan-2-ol/property/MolecularFormula,MolecularWeight,MonoisotopicMass,InChI,InChIKey,IUPACName,CanonicalSMILES,IsomericSMILES/JSON; CID85779 additional official structure comparison | context_only | The current name lookup agrees with the native graph. PubChem is used only as an additional comparator, not represented as a native asserted xref. |
| term167095 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/167095/; CHEBI:167095 current definition | supports | Resolved secondary fatty alcohol: A fatty alcohol consisting of a chain of 3 to greater than 27 carbon atoms in which a hydroxy group is attached to a saturated carbon atom different from the terminal carbons. Secondary fatty alcohols may be saturated or unsaturated and may be branched or unbranched. The native chain and C-2 OH satisfy this broader class. |
| term197387 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/197387/; CHEBI:197387 current definition | supports | Resolved hexadecanol: A fatty alcohol consisting of a hydroxy function at any position of an unbranched saturated chain of sixteen carbon atoms. The native chain and C-2 OH satisfy this broader class. |
| role | https://www.ebi.ac.uk/chebi/backend/api/public/compound/33282/; CHEBI:33282 current antibacterial-agent role, shared official snapshot | supports | The qualitative role concerns killing or slowing bacterial growth. It does not require a particular potency threshold, clinical use or demonstrated molecular target. |
| registry-limits | https://commonchemistry.cas.org/api/detail?cas_rn=14852-31-4; CAS 14852-31-4 API access and Reaxys1748421 boundary | context_only | The CAS detail API returned 401. Reaxys exact registry content was not independently accessible through the free routes; matching external authority identifiers are corroboration only. No contradictory identity was established. |
| pmid11538137 | PMID:11538137; DOI10.1016/0273-1177(92)90171-s; original abstract read | context_only | The original photochemistry abstract describes PAH-mediated hexadecane oxidation and formation of long-chain amphiphiles including 2-hexadecanol. It is a prebiotic model, not an antibacterial experiment or biological producer assertion. |
| pmid16952239 | PMID:16952239; DOI10.1021/la060816z; original abstract read | context_only | The original compares 1-,2-,3- and 4-hexadecanol at an air/water interface by surface pressure and vibrational spectroscopy. Packing and conformational order are physical measurements; they do not demonstrate antibacterial membrane disruption. |
| pmid32222494 | PMID:32222494; DOI10.1016/j.ejphar.2020.173075; original abstract read | context_only | The original isolates and characterizes2-hexadecanol from Virgularia gustaviana material and studies human HeLa/MDA-MB-231 cytotoxicity and apoptosis markers. These host-cell endpoints do not establish antibacterial target or potency. |
| pmid4840837 | PMID:4840837; DOI10.1042/bj1380053; original abstract read | context_only | The original abstract identifies hexadecan-2-ol plus secondary alkyl sulfates as combined inducers of Pseudomonas C12B S3 alkylsulfatase. The alcohol is an inducer in a mixture, not a demonstrated inhibitor of that enzyme or antibacterial target. |
| pmid5785950 | PMID:5785950; DOI10.1128/am.17.5.676-681.1969; original abstract read | context_only | The original abstract reports secondary-alcohol intermediates in Arthrobacter hexadecane oxidation and conversion of 2-hexadecanol to ketones by resting cells. Substrate transformation or failure to grow on a sole substrate is not antimicrobial inhibition. |
| pmid8158169 | PMID:8158169; DOI10.1021/np50103a002; original abstract read | context_only | The original antiacne abstract reports plant metabolites and a long-chain alcohol series against Propionibacterium acnes, but does not name each alcohol or expose its table. The exact 2-hexadecanol result is visible in a separate database extraction, not independently verified in original full text. |
| pmid9647833 | PMID:9647833; DOI10.1128/aem.64.7.2578-2584.1998; original abstract read | context_only | The original abstract identifies1- and2-hexadecanol as Rhodococcus sp. Q15 metabolic intermediates and studies their utilization. This supports chemical/metabolic context, not an antibacterial target. |
| primary1998 | PMID:9647833; Original full-main selected Methods and catabolic-pathway Results | context_only | The primary text confirms2-hexadecanol by retention time/mass-spectrum comparison with authentic standards. Its utilization experiment supplies 100 ppm as sole carbon source and measures respiration at 24 °C. This does not test bactericidal action or an inhibitory MIC. The remaining paper was not read exhaustively. |
| chembl-activity | https://www.ebi.ac.uk/chembl/api/data/activity.json?molecule_chembl_id=CHEMBL446956&amp;limit=100; Exact activity 2438985; molecule CHEMBL446956 and assay CHEMBL1006951 | context_only | The current database ties the exact unspecified-stereo graph to MIC 0.78 µg/mL against P. acnes ATCC 11827 after two days by broth dilution. This is explicitly a database transcription and not newly inspected original-table evidence. Its organism target is non-molecular; it is not a protein-binding assay. |
| chembl-document | https://www.ebi.ac.uk/chembl/api/data/document/CHEMBL1149024.json; CHEMBL1149024 exact publication mapping | context_only | The activity document resolves to adopted PMID:8158169, DOI10.1021/np50103a002, J.Nat.Prod.57:9–17(1994). The public publisher PDF route returned 403 and the publisher page required paid access. The review did not obtain or claim to read the original table. |
| chembl-assay | https://www.ebi.ac.uk/chembl/api/data/assay/CHEMBL1006951.json; CHEMBL1006951 original extraction description | context_only | The database names ATCC 11827 and the two-day broth-dilution endpoint. It does not expose enough original medium, inoculum, material characterization or controls to construct a fully primary-verified native observation. |
| patent | https://patents.google.com/patent/KR20130027376A/en; KR20130027376A; selected description, Experiment 1 paragraphs 0063–0066 and Table 1 | supports | The primary patent disclosure separately tests eight positional hexadecanols, including named2-hexadecanol, dissolved in methanol and applied to paper discs. It specifies unnamed marine bacteria, M1 medium,25 °C and7 h. The2-isomer row reports 3,2.4,1 and0.5 mm at 10,1,0.1 and0.01 ppm, with a zero control row. The geometry of the reported inhibition measurement, strain, inoculum, reagent purity and enantiomeric composition are not sufficiently specified for quantitative transfer. This is a patent experiment, not a peer-reviewed MIC study. |
| patent-structure | https://patentimages.storage.googleapis.com/12/36/52/1e59ef995ca024/KR20130027376A.pdf; Actual original Korean PDF p8, formula 2, and p10 Table 1 inspected | supports | Formula 2 depicts the C16 chain with an OH at C-2 and no stereochemical wedge, independently distinguishing the exact positional isomer. The actual p10 table confirms the separate 2-hexadecanol row and reported units. Patent prose proposing membrane disturbance is not accompanied by a direct mechanistic assay in these inspected sections. |
| adapter | /private/tmp/am-review-session/531-adapter-scope.json; Native applicability assessed before open-web follow-up | context_only | The native record names no gene, protein, pathway or expression module. No expression query was applicable; biochemical genes discovered in unrelated catabolism sources do not become native targets. |

## Limits And Additional Notes

- Required shared full-corpus gates are incorporated separately by root before finalization; actual focused checks are recorded here.
- All seven adopted abstracts were read. The 1994 antiacne main/table could not be retrieved through the attempted free route; the exact 0.78 µg/mL result is a ChEMBL transcription only. The other adopted papers remain abstract-depth except selected 1998 metabolic sections. Retrieved 1974/1969 PMC pages did not receive full scan-by-scan review.
- The Korean primary patent was inspected selectively through its original formula/table pages and publicly supplied English translation. Its marine bacterial strain, precise disc measurement definition, material purity and enantiomeric composition remain unresolved. No mechanism or quantitative assay observation was added.
- CAS detail API returned 401; independent Reaxys registry content remained unavailable. ChEBI/ChemSpider identifier agreement does not erase these access limitations.
- No raw spectral data were reanalyzed, and the unspecified tetrahedral centre was not resolved experimentally.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 13 original hashes and all 21 expanded hashes were rechecked unchanged before draft writing. No native/source/history/progress/saved-bundle/Git edits were made.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T181616Z-hexadecan-2-ol-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Hexadecan-2-ol: coherent secondary alcohol with bounded antibacterial evidence'
started_at: '2026-10-21T18:00:54Z'
finished_at: '2026-10-21T18:16:16Z'
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
summary: The neutral C16 secondary-alcohol graph, four synonyms and broader classes
  agree with current authorities. Its single stereocentre is unassigned, which does
  not assert a racemate. All seven adopted references were resolved at their actual
  reading depths. Exact antibacterial support includes an inspected patent experiment
  and a separately qualified ChEMBL extraction of the inaccessible antiacne paper.
  No required native correction was established. Scientific assessment retains the
  stated evidence limits; full verification is blocked by the shared native-library
  failure.
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
  - path: data/antibiotics/antibacterial/hexadecan-2-ol.yaml
    sha256: 18504674ccb7a6edb9252898f16f8e7d3af896995104c3d93c66166c73d49b78
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
  - path: curation/record_review_queue.tsv
    sha256: 3828a5120b892ee0ee0b776affc6c3e4f1f1a3355ec4edd30e6005762de00e70
    role: context
  - path: CLAUDE.md
    sha256: 36fb92f8919481cfbf3f17ddde4a1e244c81f76c64396dbbac910c4815fb9f16
    role: context
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
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
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
targets:
- target_id: CHEBI:185029
  path: data/antibiotics/antibacterial/hexadecan-2-ol.yaml
  label: hexadecan-2-ol
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
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Assigned queue position 531; one exact native record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:185029
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0. Executed against worktree 054; chemistry
    used existing 019 RDKit and native validators used 054.
  target_ids:
  - CHEBI:185029
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    531
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Executed against worktree 054; chemistry
    used existing 019 RDKit and native validators used 054.
  target_ids:
  - CHEBI:185029
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/hexadecan-2-ol.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Executed against worktree 054; chemistry
    used existing 019 RDKit and native validators used 054.
  target_ids:
  - CHEBI:185029
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/hexadecan-2-ol.yaml --out /private/tmp/am-review-session/531-strict.tsv
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
  - CHEBI:185029
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
  - CHEBI:185029
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
  - CHEBI:185029
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
  - CHEBI:185029
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
  - CHEBI:185029
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
  - CHEBI:185029
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
  - CHEBI:185029
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
  - CHEBI:185029
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
  - CHEBI:185029
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/hexadecan-2-ol.yaml
  locator: 'Entire native record: definition, all four synonyms, two parents, role,
    chemistry, three xrefs and history'
  accessed_at: '2026-10-21T18:12:19Z'
  support: supports
  summary: The SEEDED exact record denotes neutral hexadecan-2-ol, C16H34O, key FVDRFBGMOWJEOR-UHFFFAOYSA-N.
    One tetrahedral centre is unspecified. It contains no primary target, resistance,
    activity_spectrum, producer, causal graph or clinical-product assertion.
  snapshot_sha256: 18504674ccb7a6edb9252898f16f8e7d3af896995104c3d93c66166c73d49b78
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv#CHEBI:185029
  locator: Adopted ChEBI row 2846, readiness row 1377 and exact curator/decision search
  accessed_at: '2026-10-21T18:12:19Z'
  support: context_only
  summary: The adopted row supplies the complete native content and seven PMID leads.
    All original 13 hashes were preserved and expanded to 21 context/owner inputs.
    No exact curator or decision override was found.
  snapshot_sha256: edbb05f7dcac0944310702969f651c93e38e3dab65a61e1b72e58525256adc2a
- evidence_id: search
  kind: search
  reference: /private/tmp/am-review-session/531-context-search.txt
  locator: Original whole-tree capture and exact owner follow-up
  accessed_at: '2026-10-21T18:12:19Z'
  support: context_only
  summary: Identifier, label and slug searches included hidden and gitignored content;
    no absence assertion relies on default ignored-file exclusion.
  snapshot_sha256: 556c7bf817a60aa149629deab91d5fcd4a3aa58fe3e955e1d0ad92fd7931390b
  search_scope: Isolated054; initial531-local-hits.txt plus rg --no-ignore --hidden
    across curation/conf/scripts/data/raw.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/185029/
  locator: CHEBI:185029 current definition, graph, synonyms and accessions
  accessed_at: '2026-10-21T18:09:41.655890Z'
  support: supports
  summary: Current ChEBI reproduces the native exact secondary-alcohol graph and names.
    The C-2 alcohol is distinct from hexadecan-1-ol and other positional isomers.
    Neither native nor current graph specifies absolute configuration or enantiomeric
    composition.
  snapshot_sha256: 38cb33743d29acc7a5f3713e5894c7a8f908eccd1b0489145e65fad23a90a242
- evidence_id: chemspider
  kind: authority
  reference: https://www.chemspider.com/Chemical-Structure.77368.html
  locator: ChemSpider 77368 embedded current structure data; decoded531-chemspider-fields.json
  accessed_at: '2026-10-21T18:09:41.657965Z'
  support: supports
  summary: The current ChemSpider page directly supplies the matching SMILES and Standard
    InChI/key. Its listed CAS 14852-31-4 and database identifier 1748421 corroborate
    source associations, but do not substitute for independent access to the CAS/Reaxys
    registry records.
  snapshot_sha256: 1990dfc8e5dc46c5278438fdc9e682041656a642154cfc18704b65320753a79e
- evidence_id: mapping
  kind: validation
  reference: /private/tmp/am-review-session/531-map.py
  locator: 019 RDKit2026.03.5, cwd054; seven native/authority encodings
  accessed_at: '2026-10-21T18:12:19Z'
  support: supports
  summary: Native, ChEBI and ChemSpider SMILES/InChI and additional PubChem InChI
    all agree at complete key, formula, charge and reciprocal graph match. There is
    one unassigned secondary-alcohol centre. Formula, masses, mint and encoding checks
    pass.
  snapshot_sha256: dcb069c00562011d1d7a582118c97e8f197074334dc6b63ef4107ae2b202eb9b
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/hexadecan-2-ol/property/MolecularFormula,MolecularWeight,MonoisotopicMass,InChI,InChIKey,IUPACName,CanonicalSMILES,IsomericSMILES/JSON
  locator: CID85779 additional official structure comparison
  accessed_at: '2026-10-21T18:09:42.597747Z'
  support: context_only
  summary: The current name lookup agrees with the native graph. PubChem is used only
    as an additional comparator, not represented as a native asserted xref.
  snapshot_sha256: e0ccc38cc986ad518edba4a71c2716a41ba5c08ec0ba28a6dfa0ad1d33453a34
- evidence_id: term167095
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/167095/
  locator: CHEBI:167095 current definition
  accessed_at: '2026-10-21T18:09:41.852740Z'
  support: supports
  summary: 'Resolved secondary fatty alcohol: A fatty alcohol consisting of a chain
    of 3 to greater than 27 carbon atoms in which a hydroxy group is attached to a
    saturated carbon atom different from the terminal carbons. Secondary fatty alcohols
    may be saturated or unsaturated and may be branched or unbranched. The native
    chain and C-2 OH satisfy this broader class.'
  snapshot_sha256: fdc0c393e89d177e40d8e2e689f942c1d9425ab8b30bb9cb7c1419b54d7dfedd
- evidence_id: term197387
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/197387/
  locator: CHEBI:197387 current definition
  accessed_at: '2026-10-21T18:09:42.432684Z'
  support: supports
  summary: 'Resolved hexadecanol: A fatty alcohol consisting of a hydroxy function
    at any position of an unbranched saturated chain of sixteen carbon atoms. The
    native chain and C-2 OH satisfy this broader class.'
  snapshot_sha256: e1c8c361b2d879b725ffb3ab1e0e0ee98cf88d93675969f210bd8723ae39fca8
- evidence_id: role
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/33282/
  locator: CHEBI:33282 current antibacterial-agent role, shared official snapshot
  accessed_at: '2026-10-21T18:12:19Z'
  support: supports
  summary: The qualitative role concerns killing or slowing bacterial growth. It does
    not require a particular potency threshold, clinical use or demonstrated molecular
    target.
  snapshot_sha256: 20d92ce7e00c204b1753184671c043160821d692438278344335446aadcd5082
- evidence_id: registry-limits
  kind: authority
  reference: https://commonchemistry.cas.org/api/detail?cas_rn=14852-31-4
  locator: CAS 14852-31-4 API access and Reaxys1748421 boundary
  accessed_at: '2026-10-21T18:09:41.661296Z'
  support: context_only
  summary: The CAS detail API returned 401. Reaxys exact registry content was not
    independently accessible through the free routes; matching external authority
    identifiers are corroboration only. No contradictory identity was established.
  snapshot_sha256: 3e7db788e384631f8a9f299d1797e6f8af6d16d643a1c91f9e83ae15212de45c
- evidence_id: pmid11538137
  kind: primary_source
  reference: PMID:11538137
  locator: DOI10.1016/0273-1177(92)90171-s; original abstract read
  accessed_at: '2026-10-21T18:09:41.657471Z'
  support: context_only
  summary: The original photochemistry abstract describes PAH-mediated hexadecane
    oxidation and formation of long-chain amphiphiles including 2-hexadecanol. It
    is a prebiotic model, not an antibacterial experiment or biological producer assertion.
  snapshot_sha256: ed22255c17ad6dd5d09a184a842b2b84ff0d28771b067be889ccc7a1e81f5520
- evidence_id: pmid16952239
  kind: primary_source
  reference: PMID:16952239
  locator: DOI10.1021/la060816z; original abstract read
  accessed_at: '2026-10-21T18:09:41.657471Z'
  support: context_only
  summary: The original compares 1-,2-,3- and 4-hexadecanol at an air/water interface
    by surface pressure and vibrational spectroscopy. Packing and conformational order
    are physical measurements; they do not demonstrate antibacterial membrane disruption.
  snapshot_sha256: ed22255c17ad6dd5d09a184a842b2b84ff0d28771b067be889ccc7a1e81f5520
- evidence_id: pmid32222494
  kind: primary_source
  reference: PMID:32222494
  locator: DOI10.1016/j.ejphar.2020.173075; original abstract read
  accessed_at: '2026-10-21T18:09:41.657471Z'
  support: context_only
  summary: The original isolates and characterizes2-hexadecanol from Virgularia gustaviana
    material and studies human HeLa/MDA-MB-231 cytotoxicity and apoptosis markers.
    These host-cell endpoints do not establish antibacterial target or potency.
  snapshot_sha256: ed22255c17ad6dd5d09a184a842b2b84ff0d28771b067be889ccc7a1e81f5520
- evidence_id: pmid4840837
  kind: primary_source
  reference: PMID:4840837
  locator: DOI10.1042/bj1380053; original abstract read
  accessed_at: '2026-10-21T18:09:41.657471Z'
  support: context_only
  summary: The original abstract identifies hexadecan-2-ol plus secondary alkyl sulfates
    as combined inducers of Pseudomonas C12B S3 alkylsulfatase. The alcohol is an
    inducer in a mixture, not a demonstrated inhibitor of that enzyme or antibacterial
    target.
  snapshot_sha256: ed22255c17ad6dd5d09a184a842b2b84ff0d28771b067be889ccc7a1e81f5520
- evidence_id: pmid5785950
  kind: primary_source
  reference: PMID:5785950
  locator: DOI10.1128/am.17.5.676-681.1969; original abstract read
  accessed_at: '2026-10-21T18:09:41.657471Z'
  support: context_only
  summary: The original abstract reports secondary-alcohol intermediates in Arthrobacter
    hexadecane oxidation and conversion of 2-hexadecanol to ketones by resting cells.
    Substrate transformation or failure to grow on a sole substrate is not antimicrobial
    inhibition.
  snapshot_sha256: ed22255c17ad6dd5d09a184a842b2b84ff0d28771b067be889ccc7a1e81f5520
- evidence_id: pmid8158169
  kind: primary_source
  reference: PMID:8158169
  locator: DOI10.1021/np50103a002; original abstract read
  accessed_at: '2026-10-21T18:09:41.657471Z'
  support: context_only
  summary: The original antiacne abstract reports plant metabolites and a long-chain
    alcohol series against Propionibacterium acnes, but does not name each alcohol
    or expose its table. The exact 2-hexadecanol result is visible in a separate database
    extraction, not independently verified in original full text.
  snapshot_sha256: ed22255c17ad6dd5d09a184a842b2b84ff0d28771b067be889ccc7a1e81f5520
- evidence_id: pmid9647833
  kind: primary_source
  reference: PMID:9647833
  locator: DOI10.1128/aem.64.7.2578-2584.1998; original abstract read
  accessed_at: '2026-10-21T18:09:41.657471Z'
  support: context_only
  summary: The original abstract identifies1- and2-hexadecanol as Rhodococcus sp.
    Q15 metabolic intermediates and studies their utilization. This supports chemical/metabolic
    context, not an antibacterial target.
  snapshot_sha256: ed22255c17ad6dd5d09a184a842b2b84ff0d28771b067be889ccc7a1e81f5520
- evidence_id: primary1998
  kind: primary_source
  reference: PMID:9647833
  locator: Original full-main selected Methods and catabolic-pathway Results
  accessed_at: '2026-10-21T18:10:32.921477Z'
  support: context_only
  summary: The primary text confirms2-hexadecanol by retention time/mass-spectrum
    comparison with authentic standards. Its utilization experiment supplies 100 ppm
    as sole carbon source and measures respiration at 24 °C. This does not test bactericidal
    action or an inhibitory MIC. The remaining paper was not read exhaustively.
  snapshot_sha256: 3ca25fc7d90067018f9e1665ad47420469555e5578884db9cc9c5324e84e37c0
- evidence_id: chembl-activity
  kind: database
  reference: https://www.ebi.ac.uk/chembl/api/data/activity.json?molecule_chembl_id=CHEMBL446956&limit=100
  locator: Exact activity 2438985; molecule CHEMBL446956 and assay CHEMBL1006951
  accessed_at: '2026-10-21T18:10:06.594323Z'
  support: context_only
  summary: The current database ties the exact unspecified-stereo graph to MIC 0.78
    µg/mL against P. acnes ATCC 11827 after two days by broth dilution. This is explicitly
    a database transcription and not newly inspected original-table evidence. Its
    organism target is non-molecular; it is not a protein-binding assay.
  snapshot_sha256: e71b0f7c5aa902ffd214e103e883282f5d44df5acb92927deb1d3c2ce1e7e413
- evidence_id: chembl-document
  kind: database
  reference: https://www.ebi.ac.uk/chembl/api/data/document/CHEMBL1149024.json
  locator: CHEMBL1149024 exact publication mapping
  accessed_at: '2026-10-21T18:10:32.683532Z'
  support: context_only
  summary: The activity document resolves to adopted PMID:8158169, DOI10.1021/np50103a002,
    J.Nat.Prod.57:9–17(1994). The public publisher PDF route returned 403 and the
    publisher page required paid access. The review did not obtain or claim to read
    the original table.
  snapshot_sha256: 458ee93fad530a65b3a7041593af352b0f0a93709a6ed4c048af25071121b6a0
- evidence_id: chembl-assay
  kind: database
  reference: https://www.ebi.ac.uk/chembl/api/data/assay/CHEMBL1006951.json
  locator: CHEMBL1006951 original extraction description
  accessed_at: '2026-10-21T18:10:32.683739Z'
  support: context_only
  summary: The database names ATCC 11827 and the two-day broth-dilution endpoint.
    It does not expose enough original medium, inoculum, material characterization
    or controls to construct a fully primary-verified native observation.
  snapshot_sha256: 764fe25264b03cbca43775b92ef7d339162cea7140850d38d2114c68445e65b2
- evidence_id: patent
  kind: primary_source
  reference: https://patents.google.com/patent/KR20130027376A/en
  locator: KR20130027376A; selected description, Experiment 1 paragraphs 0063–0066
    and Table 1
  accessed_at: '2026-10-21T18:10:06.252068Z'
  support: supports
  summary: The primary patent disclosure separately tests eight positional hexadecanols,
    including named2-hexadecanol, dissolved in methanol and applied to paper discs.
    It specifies unnamed marine bacteria, M1 medium,25 °C and7 h. The2-isomer row
    reports 3,2.4,1 and0.5 mm at 10,1,0.1 and0.01 ppm, with a zero control row. The
    geometry of the reported inhibition measurement, strain, inoculum, reagent purity
    and enantiomeric composition are not sufficiently specified for quantitative transfer.
    This is a patent experiment, not a peer-reviewed MIC study.
  snapshot_sha256: c5787e5aad7acac52a793cca69d1b6d5af079b525760e8bfaaa6b4ec8d9b0f1b
- evidence_id: patent-structure
  kind: primary_source
  reference: https://patentimages.storage.googleapis.com/12/36/52/1e59ef995ca024/KR20130027376A.pdf
  locator: Actual original Korean PDF p8, formula 2, and p10 Table 1 inspected
  accessed_at: '2026-10-21T18:10:32.683826Z'
  support: supports
  summary: Formula 2 depicts the C16 chain with an OH at C-2 and no stereochemical
    wedge, independently distinguishing the exact positional isomer. The actual p10
    table confirms the separate 2-hexadecanol row and reported units. Patent prose
    proposing membrane disturbance is not accompanied by a direct mechanistic assay
    in these inspected sections.
  snapshot_sha256: 62aec5f572a5bcd738fdd3b8e302bf486b9c541ad72d8e7c563d7aab322018b3
- evidence_id: adapter
  kind: search
  reference: /private/tmp/am-review-session/531-adapter-scope.json
  locator: Native applicability assessed before open-web follow-up
  accessed_at: '2026-10-21T18:12:19Z'
  support: context_only
  summary: The native record names no gene, protein, pathway or expression module.
    No expression query was applicable; biochemical genes discovered in unrelated
    catabolism sources do not become native targets.
  snapshot_sha256: 6aafd356446cdecad1e6cb02587b42090525c7a90a592478c213a7a7c5b017d0
  search_scope: Entire native531 and preserved catalog456460-adapter-catalog.txt;
    no applicable native protein/gene claim.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact positional alcohol and unspecified stereochemistry
  outcome: supported
  summary: The neutral secondary-alcohol constitution, four names, formula and masses
    agree with authorities. The single unassigned centre is a partially specified
    graph, not evidence of a racemate or an automatically wrong exact identifier.
    No source-specific enantiomer is silently substituted.
  target_ids:
  - CHEBI:185029
  evidence_ids:
  - native
  - chebi
  - chemspider
  - mapping
  - patent-structure
- assessment_id: grounding
  area: grounding
  topic: Chemical xrefs and broader terms
  outcome: supported
  summary: CHEBI:185029 and ChemSpider 77368 resolve to the exact graph. Secondary
    fatty alcohol and hexadecanol are compatible broader classes. CAS and Reaxys have
    corroborating identifier associations but independent registry access remains
    limited, without evidence of a wrong xref.
  target_ids:
  - CHEBI:185029
  evidence_ids:
  - chebi
  - chemspider
  - mapping
  - term167095
  - term197387
  - registry-limits
- assessment_id: activity
  area: evidence
  topic: Qualitative antibacterial role and experimental depth
  outcome: supported
  summary: The inspected patent reports an exact positional-isomer antibacterial experiment,
    and the adopted antiacne publication has an exact graph-mapped ChEMBL MIC extraction.
    Together these support retaining the qualitative role while the original antiacne
    assay remains unverified. No quantitative native MIC, membrane target, clinical
    indication or broad-spectrum assertion is present.
  target_ids:
  - CHEBI:185029
  evidence_ids:
  - role
  - patent
  - patent-structure
  - pmid8158169
  - chembl-activity
  - chembl-document
- assessment_id: completeness
  area: completeness
  topic: All seven adopted leads and optional biological fields
  outcome: unknown
  summary: All seven original abstracts were read, plus selected 1998 metabolic sections
    and exact patent experiment/figures. Catabolism, interface physics and host-cell
    apoptosis do not establish antibacterial mechanism. Original antiacne table access
    and material scope remain unresolved; absent optional targets, resistance, producer
    and activity_spectrum fields are not native defects.
  target_ids:
  - CHEBI:185029
  evidence_ids:
  - owners
  - pmid11538137
  - pmid16952239
  - pmid32222494
  - pmid4840837
  - pmid5785950
  - pmid8158169
  - pmid9647833
  - primary1998
  - chembl-assay
- assessment_id: provenance
  area: provenance
  topic: Source ownership, history and read-only assessment
  outcome: supported
  summary: The entire native record, exact source row and three chronological seed/reseed
    events were read. Original 13 and expanded 21 input hashes remain unchanged. ChEBI
    extraction/seeding owns generated content; no curator ownership or status promotion
    was invented.
  target_ids:
  - CHEBI:185029
  evidence_ids:
  - native
  - owners
  - search
findings: []
actions:
- action_id: A1
  description: 'Optional follow-up: inspect the original antiacne experiment before
    adding detailed activity or mechanism.'
  finding_ids: []
  target_ids:
  - CHEBI:185029
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/hexadecan-2-ol.yaml
    role: Future validated curator-owned literature annotation
  acceptance_checks:
  - Retrieve and inspect the exact 2-hexadecanol row, preparation, medium, inoculum
    and endpoint in PMID:8158169; preserve the current ChEMBL value as database evidence
    until then.
  - Do not import plant-extract, positional-isomer, apoptosis or catabolic-substrate
    results as direct exact-compound antibacterial mechanism.
  - Preserve unspecified stereo unless the tested material is independently characterized;
    patent disc measurements and coating/larval outcomes must not become MICs or clinical
    efficacy.
  - Resolve free CAS/Reaxys exact registry access before claiming every xref independently
    verified; no correction is required merely because access is unavailable.
limitations:
- Required shared full-corpus gates are incorporated separately by root before finalization;
  actual focused checks are recorded here.
- All seven adopted abstracts were read. The 1994 antiacne main/table could not be
  retrieved through the attempted free route; the exact 0.78 µg/mL result is a ChEMBL
  transcription only. The other adopted papers remain abstract-depth except selected
  1998 metabolic sections. Retrieved 1974/1969 PMC pages did not receive full scan-by-scan
  review.
- The Korean primary patent was inspected selectively through its original formula/table
  pages and publicly supplied English translation. Its marine bacterial strain, precise
  disc measurement definition, material purity and enantiomeric composition remain
  unresolved. No mechanism or quantitative assay observation was added.
- CAS detail API returned 401; independent Reaxys registry content remained unavailable.
  ChEBI/ChemSpider identifier agreement does not erase these access limitations.
- No raw spectral data were reanalyzed, and the unspecified tetrahedral centre was
  not resolved experimentally.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 13 original hashes and all 21 expanded hashes were rechecked unchanged before
  draft writing. No native/source/history/progress/saved-bundle/Git edits were made.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
