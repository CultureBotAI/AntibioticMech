# Heptachlor: consistent generic structure, material-limited microbial evidence and a trade-name alias

- Review: 20261021T180919Z-heptachlor-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T17:48:34Z
- Finished UTC: 2026-10-21T18:09:19Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The stereo-unspecified heptachlor graph agrees across nine native and authority encodings. Historical original studies report bacterial and fungal effects, but reagent purity, indirect growth endpoints and technical-grade material limit exact-compound attribution. One minor name-typing correction is supported for Heptamul. No unsupported stereochemical replacement or clinical antimicrobial inference is proposed.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position 528; entire native record, original thirteen inputs preserved and actual ChEBI ownership confirmed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:34785 | data/antibiotics/antibacterial/heptachlor.yaml | generated | heptachlor |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:34785 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:34785 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:34785 | Actual focused execution exited 0. |
| Independent authority chemistry | passed | False | CHEBI:34785 | Nine native and authority encodings reproduce the full key, formula, charge and reciprocal graph match, with five unassigned stereocentres. |
| Authoritative full QC | failed | True | CHEBI:34785 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:34785 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:34785 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:34785 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:34785 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:34785 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:34785 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:34785 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:34785 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Generic heptachlor and chemical authority agreement

identity: supported. Targets: CHEBI:34785.

All checked exact xrefs and native encodings agree at the represented stereo-unspecified level. No specific enantiomer or technical formulation is asserted. Additional stereochemical resolution requires an explicitly chosen material scope.

### Antimicrobial classification and tested-material limits

evidence: unknown. Targets: CHEBI:34785.

Current database roles and historical microbial inhibition are compatible, but exact pure-material attribution remains limited:1968 uses77.2% material,1985 technical material, and1970 does not specify purity. No forced role deletion or exact pure-compound MIC is justified from these sources.

### Trade name within exact aliases

nomenclature: concern. Targets: CHEBI:34785.

Heptamul is explicitly a trade name in the WHO identity section and should be typed accordingly. Other name use, including Heptachlorane, is not overcorrected where generic and commercial usage overlap.

### Exact and document references

grounding: unknown. Targets: CHEBI:34785.

CAS, KEGG and PPDB are independently corroborated. Reaxys is source-attributed only; the Wikipedia link is relevant document context. No inaccessible-registry mismatch is invented.

### No target overpromotion

evidence: supported. Targets: CHEBI:34785.

The native makes no molecular-target assertion. Host mitochondrial results and indirect bacterial enzyme/respiration measurements are kept separate from binding evidence and insect chloride-channel context.

### Complete native/source/history review

provenance: supported. Targets: CHEBI:34785.

All original thirteen hashes are retained, the exact adopted source row was read, both adopted citations disposed, and four chronological source-history events are preserved. Optional microbial observations or causal graphs are not required just because literature exists.

## Findings

### F1: Heptamul is a trade name rather than an exact chemical-name synonym

minor / open / confirmed; issue key: heptachlor-heptamul-trade-name-type.

The native Heptamul synonym is typed EXACT_SYNONYM. WHO EHC38 section2.1 explicitly lists Heptamul as a common trade name. Preserve the useful alias but classify its commercial-name scope; do not infer product composition or one formulation from the generic chemical graph.

## Recommended Actions And Acceptance Checks

### A1

Preserve Heptamul with a trade-name type through the maintained synonym handling.

- Use BRAND_NAME for the Heptamul alias with the WHO identity source retained; avoid unsupported changes to dual-use Heptachlorane.
- Regenerate through the maintained owner and verify exact structure, provenance/history, schema/strict and required corpus gates.

### A2

If activity is later curated, retain the tested material and endpoint boundaries.

- Do not convert technical or77.2% material into pure exact-compound MIC evidence.
- Distinguish nitrite-depletion growth proxy, viable-count killing, dry-weight inhibition, toxin production and substrate utilization; retain organism, medium and assay duration.
- Resolve reagent purity and chosen stereochemical scope before adding exact-material claims; do not transfer host or insect mechanisms into bacterial binding targets.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/heptachlor.yaml; Entire YAML: definition, seven aliases, parent, both roles, chemistry, all four exact xrefs, document link, source concept and four history events. | supports | The EXACT/SEEDED entry is neutral C10H5Cl7, FRCCEHPWNOQAEU-UHFFFAOYSA-N, without assigned stereochemistry. It denotes the generic chemical rather than a named enantiomer or a technical pesticide formulation. There is no molecular target, microbial observation, resistance route, causal graph, clinical claim or producer object. |
| owners | data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Complete exact source row and applicable role/synonym projection; 528-source-rows.json. | supports | The adopted ChEBI row reproduces the native definition, seven names, chemical data, xrefs and two literature leads. Both antibacterial and antifungal roles are retained; configured priority selects ANTIBACTERIAL. No matching curator or decisions row was present in the inspected inventories. Source-concept minting is provenance, not an alternate exact identity. |
| authority | CHEBI:34785; PubChem:3589; kegg.compound:C14185; ppdb:378; cas:76-44-8; Current ChEBI/PubChem graphs, KEGG molfile/text, PPDB structural identifiers and NIST standard InChI; nine encodings independently parsed. | supports | All nine encodings match the native full key, formula, neutral charge and stereo-unspecified graph. Five potential stereocentres remain unassigned consistently. KEGG and PPDB expressly associate CAS76-44-8; NIST independently corroborates it. Average-mass differences reflect provider precision. Heptachlor epoxide and chlordane are distinct compounds and were not substituted. |
| classes | CHEBI:23457; CHEBI:33282; CHEBI:35718; Current parent and role definitions/outgoing relationships. | supports | The parent is a broader cyclodiene organochlorine insecticide class derived from hexachlorocyclopentadiene, compatible with the bridged chlorinated graph. The roles concern suppressing bacterial or fungal growth; they do not assert a licensed antimicrobial treatment. Current ChEBI still assigns both. Its additional insect chloride-channel role is not imported as a bacterial target. |
| xref | reaxys:2058523; wikipedia.en:Heptachlor; Current ChEBI attribution and fetched native Wikipedia destination; underlying Reaxys graph not inspected. | partial | The document link resolves to heptachlor context. Reaxys2058523 is retained by the current source authority, but proprietary registry identity was not independently resolved. No positive mismatch is established; source attribution is not counted as direct registry verification. |
| names | https://www.inchem.org/documents/ehc/ehc/ehc38.htm; WHO Environmental Health Criteria38 (1984), section2.1 Identity and section2.2.1 physical properties. | supports | WHO explicitly lists Heptamul among common trade names, while distinguishing pure crystalline heptachlor from technical material. The native types Heptamul as EXACT_SYNONYM. Heptachlorane also appears in trade-name lists but is independently used as a general chemical name by KEGG; its potentially dual use is not classified as a confirmed defect. |
| stereo | PMID:14753706; DOI:10.1016/j.chroma.2003.10.026; Complete original indexed abstract; main chromatographic methods and raw separation data not obtained. | partial | The 2004 original separates individual heptachlor enantiomers on CHIRALCEL OD, distinguishing them from heptachlor-epoxide enantiomers. This establishes that generic heptachlor naming does not identify one absolute configuration. The native and accessible authorities consistently leave stereochemistry unassigned; neither a particular enantiomer nor technical-mixture composition is inferred from that representation. |
| adopted | PMID:24177859; PMID:24577234; Both complete adopted indexed abstracts and metadata. | supports | 24177859 quantifies organochlorine contaminants in108 East Lake water samples; heptachlor occurrence and environmental risk do not constitute antimicrobial assays. 24577234 studies SH-SY5Y cells and injected mice, not bacterial or fungal inhibition. Neither adopted source directly establishes either microbial role. |
| host | PMID:24577234; DOI:10.1038/emm.2014.12; PMC3944446; Complete abstract, selected introduction, reagent and injection Methods, and selected Results/Discussion; images not independently analyzed. | context_only | Supelco heptachlor was used in mammalian cell and mouse experiments. The report associates treatment with mitochondria-mediated neuronal injury and Parkinsonism-like behavior. These host toxicity observations are not direct bacterial-target evidence, natural production, or clinical antimicrobial activity; detailed host numerical results are not imported. |
| bacterial1968 | PMID:4872999; DOI:10.1128/am.16.5.799-800.1968; PMC547523; Both original scanned pages799–800 read visually in full, including Figures1–2 and all methods. | partial | Collins and Langlois used77.2% heptachlor, with nominal50/100 ppm tests in trypticase soy broth or reconstituted skim milk and alcohol controls. S.aureus showed killing in broth at37 degrees C; E.coli and P.fluorescens did not show a heptachlor growth effect, and the skim-milk tests did not show inhibition. Colony counts were followed through7 days. The mixed-purity reagent and medium dependence prevent treating this as an exact pure-heptachlor universal MIC. |
| bacterial1968-results | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3808/547523/b9170227a26b/applmicro00241-0134.png; Actual second scanned page800, full Results/Conclusion. | partial | The original explicitly separates the S.aureus heptachlor result from DDT effects on P.fluorescens and from negative skim-milk conditions. The review does not transfer DDT growth effects or regard all pesticides as equivalent. |
| bacterial1970 | PMID:4314375; DOI:10.1128/am.19.2.214-219.1970; PMC376654; All six original page scans214–219 read visually, including all three tables, figure, Methods and Discussion. | partial | Nitrobacter agilis ATCC14123 was grown in defined inorganic medium at30 degrees C with shaking and acetone vehicle controls. Table1 reports complete prevention of nitrite depletion at10 micrograms/mL heptachlor through9 days;5 micrograms/mL delayed depletion. Nitrite disappearance was used as the growth proxy, rather than viable counts or a standard MIC endpoint. Reagent purity and stereochemical composition are not specified in the inspected main. Cell-suspension and cell-free effects occur at much higher concentrations; the authors explicitly caution that those oxidation effects probably do not explain growth inhibition. No Kd, purified-protein binding target or exclusive antibacterial mechanism is established. |
| bacterial1970-discussion | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/15ff/376654/3f51137386f9/applmicro00100-0036.png; Original page218, Table3 and Discussion; other page hashes in053-root-fetch6.json. | context_only | The authors discuss solubility limits, potential binding of protein in extracts and adsorption by insoluble pesticide particles. Heptachlor suppresses cell-free nitrite oxidation more than whole-cell oxidation, but the disparity between growth and oxidation concentrations precludes a simple direct-target inference. |
| fungal1985 | DOI:10.1094/Phyto-75-553; https://www.apsnet.org/publications/phytopathology/backissues/Documents/1985Articles/Phyto75n05_553.pdf; All four original scanned pages553–556 read visually, including Tables1–3 and complete Methods/Results/Discussion. | partial | Draughon and Churchville tested technical-grade heptachlor supplied by Chevron against Fusarium roseum var.graminearum NRRL3376. In potato-dextrose broth at21 degrees C for3 weeks, dry mycelial mass was reduced41,46 and49 percent at10,50 and100 ppm active-ingredient dosing, respectively (Table2). This is partial growth inhibition, not complete MIC or killing. Zearalenone on corn was a separate endpoint and the field treatments used other pesticides. Technical material and unreported detailed composition limit attribution to the exact graph. |
| negative-context | PMID:2518692; Smith et al.1976, Developments in Industrial Microbiology17:331–336; https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=9100UKCN.TXT; 1989 complete original indexed abstract; selected1976 original abstract, Methods, Results and Tables2–4 from public EPA reprint text via web provider. | context_only | The1989 rumen fermentation study found no heptachlor suppression of dry-matter disappearance under its conditions, unlike pentachlorophenol. The1976 fungal study used99.8% reference material in hexadecane and found no apparent suppression of utilization by the studied Candida preparations, with some stimulation in one condition. These condition-specific results neither erase the positive historical observations nor prove universal inactivity. The1976 direct download returned a redirect shell, so no downloaded-full-paper claim is made. |
| search | 528-local-hits.txt; 528-microbial-search.json; 053-root-fetch1.json through053-root-fetch6.json; Ignored- and hidden-inclusive initial local search, all adopted leads, targeted microbial discovery and ordinary free-authority/full-text retrieval. | context_only | The broader heptachlor query returned1536 hits and only the first1000 were captured; the targeted microbial query returned64. Titles were screened and selected exact-compound originals pursued. This is bounded discovery, not exhaustive absence evidence. Failed XML, PDF and challenge routes are retained separately from the successfully inspected page scans and publisher PDF. |

## Limits And Additional Notes

- Full original1968,1970 and1985 papers were visually read at all pages. Original spectra and supplier certificates were not available;1968 and1985 explicitly use impure/technical material, while1970 main does not state chemical purity.
- Both adopted complete abstracts were read. The2014 mouse paper was inspected only at the selected-main depth stated above, without raw image analysis; the lake-contamination paper remained abstract-depth.
- The2004 enantiomer-separation and1989 rumen studies remained complete-abstract depth. The1976 fungal reprint was read only at the stated selected-text depth through the web provider; tables and page images were not independently downloaded.
- The generic authoritative graph leaves five potential stereocentres unassigned. This review does not claim one enantiomer, an exhaustive stereochemical-isomer inventory, or the composition of a technical product.
- Reaxys2058523 underlying registration was not independently inspected. A public registry access gap does not establish an incorrect xref.
- Searches were bounded. The broad1536-hit result was truncated to1000 records; no claim of exhaustive microbial or regulatory literature coverage is made.
- The native has no populated bacterial protein/pathway assertion; broad activity discovery did not trigger a structured target-dataset lookup. Shared required corpus gates and the known SciPy platform failure are incorporated separately by the finalizer.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- The original source and native record remain unchanged; this is a scientific review with one bounded alias finding.
- Successful scan/PDF retrievals are explicitly distinguished from HTTP200 challenge shells, failed XML routes and the inaccessible IARC page. The actual publisher1985 PDF was retrieved via its lower-case .pdf URL and rendered locally.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T180919Z-heptachlor-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Heptachlor: consistent generic structure, material-limited microbial evidence
  and a trade-name alias'
started_at: '2026-10-21T17:48:34Z'
finished_at: '2026-10-21T18:09:19Z'
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
summary: The stereo-unspecified heptachlor graph agrees across nine native and authority
  encodings. Historical original studies report bacterial and fungal effects, but
  reagent purity, indirect growth endpoints and technical-grade material limit exact-compound
  attribution. One minor name-typing correction is supported for Heptamul. No unsupported
  stereochemical replacement or clinical antimicrobial inference is proposed.
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
  - path: data/antibiotics/antibacterial/heptachlor.yaml
    sha256: 1f9a9d3b29e59b55b2af947cf886a5320fe6dd6eb028d44e3b2534a061f22687
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
- target_id: CHEBI:34785
  path: data/antibiotics/antibacterial/heptachlor.yaml
  label: heptachlor
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, aliases, roles and publication leads
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Role priority and synonym mapping
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
  selection: Initially uncovered queue position 528; entire native record, original
    thirteen inputs preserved and actual ChEBI ownership confirmed.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:34785
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:34785
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    528
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:34785
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/heptachlor.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:34785
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/heptachlor.yaml --out /private/tmp/am-review-session/528-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: authority
  name: Independent authority chemistry
  status: passed
  required: false
  summary: Nine native and authority encodings reproduce the full key, formula, charge
    and reciprocal graph match, with five unassigned stereocentres.
  target_ids:
  - CHEBI:34785
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/528-authorities.py
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
  - CHEBI:34785
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
  - CHEBI:34785
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
  - CHEBI:34785
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
  - CHEBI:34785
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
  - CHEBI:34785
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
  - CHEBI:34785
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
  - CHEBI:34785
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
  - CHEBI:34785
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
  - CHEBI:34785
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/heptachlor.yaml
  locator: 'Entire YAML: definition, seven aliases, parent, both roles, chemistry,
    all four exact xrefs, document link, source concept and four history events.'
  accessed_at: '2026-10-21T18:00:01Z'
  support: supports
  summary: The EXACT/SEEDED entry is neutral C10H5Cl7, FRCCEHPWNOQAEU-UHFFFAOYSA-N,
    without assigned stereochemistry. It denotes the generic chemical rather than
    a named enantiomer or a technical pesticide formulation. There is no molecular
    target, microbial observation, resistance route, causal graph, clinical claim
    or producer object.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: Complete exact source row and applicable role/synonym projection; 528-source-rows.json.
  accessed_at: '2026-10-21T18:00:01Z'
  support: supports
  summary: The adopted ChEBI row reproduces the native definition, seven names, chemical
    data, xrefs and two literature leads. Both antibacterial and antifungal roles
    are retained; configured priority selects ANTIBACTERIAL. No matching curator or
    decisions row was present in the inspected inventories. Source-concept minting
    is provenance, not an alternate exact identity.
  snapshot_sha256: d35d9e481b3005f69238c62f6c986e7787f4d9ef5beab063e292a447cc8476c3
- evidence_id: authority
  kind: authority
  reference: CHEBI:34785; PubChem:3589; kegg.compound:C14185; ppdb:378; cas:76-44-8
  locator: Current ChEBI/PubChem graphs, KEGG molfile/text, PPDB structural identifiers
    and NIST standard InChI; nine encodings independently parsed.
  accessed_at: '2026-10-21T18:00:01Z'
  support: supports
  summary: All nine encodings match the native full key, formula, neutral charge and
    stereo-unspecified graph. Five potential stereocentres remain unassigned consistently.
    KEGG and PPDB expressly associate CAS76-44-8; NIST independently corroborates
    it. Average-mass differences reflect provider precision. Heptachlor epoxide and
    chlordane are distinct compounds and were not substituted.
  snapshot_sha256: dbccc50835393ed4c8e4757246601fc4c123620770176afaef462fcb5a121bde
- evidence_id: classes
  kind: authority
  reference: CHEBI:23457; CHEBI:33282; CHEBI:35718
  locator: Current parent and role definitions/outgoing relationships.
  accessed_at: '2026-10-21T18:00:01Z'
  support: supports
  summary: The parent is a broader cyclodiene organochlorine insecticide class derived
    from hexachlorocyclopentadiene, compatible with the bridged chlorinated graph.
    The roles concern suppressing bacterial or fungal growth; they do not assert a
    licensed antimicrobial treatment. Current ChEBI still assigns both. Its additional
    insect chloride-channel role is not imported as a bacterial target.
  snapshot_sha256: 996e392dbeb18880fec891455a5eaffb6ac882ea6ab50d30565d49e76048238e
- evidence_id: xref
  kind: database
  reference: reaxys:2058523; wikipedia.en:Heptachlor
  locator: Current ChEBI attribution and fetched native Wikipedia destination; underlying
    Reaxys graph not inspected.
  accessed_at: '2026-10-21T18:00:01Z'
  support: partial
  summary: The document link resolves to heptachlor context. Reaxys2058523 is retained
    by the current source authority, but proprietary registry identity was not independently
    resolved. No positive mismatch is established; source attribution is not counted
    as direct registry verification.
  snapshot_sha256: 996e392dbeb18880fec891455a5eaffb6ac882ea6ab50d30565d49e76048238e
- evidence_id: names
  kind: authority
  reference: https://www.inchem.org/documents/ehc/ehc/ehc38.htm
  locator: WHO Environmental Health Criteria38 (1984), section2.1 Identity and section2.2.1
    physical properties.
  accessed_at: '2026-10-21T18:00:01Z'
  support: supports
  summary: WHO explicitly lists Heptamul among common trade names, while distinguishing
    pure crystalline heptachlor from technical material. The native types Heptamul
    as EXACT_SYNONYM. Heptachlorane also appears in trade-name lists but is independently
    used as a general chemical name by KEGG; its potentially dual use is not classified
    as a confirmed defect.
  snapshot_sha256: 21cf42c1bad087d3d5527e277ffa19b18742b395a39e3937fc0f92f9c1b934f8
- evidence_id: stereo
  kind: primary_source
  reference: PMID:14753706; DOI:10.1016/j.chroma.2003.10.026
  locator: Complete original indexed abstract; main chromatographic methods and raw
    separation data not obtained.
  accessed_at: '2026-10-21T18:00:01Z'
  support: partial
  summary: The 2004 original separates individual heptachlor enantiomers on CHIRALCEL
    OD, distinguishing them from heptachlor-epoxide enantiomers. This establishes
    that generic heptachlor naming does not identify one absolute configuration. The
    native and accessible authorities consistently leave stereochemistry unassigned;
    neither a particular enantiomer nor technical-mixture composition is inferred
    from that representation.
  snapshot_sha256: a8be4a42201856bf4d327e6e59965ea25b96e3e39cf9becb6d64b72864828001
- evidence_id: adopted
  kind: database
  reference: PMID:24177859; PMID:24577234
  locator: Both complete adopted indexed abstracts and metadata.
  accessed_at: '2026-10-21T18:00:01Z'
  support: supports
  summary: 24177859 quantifies organochlorine contaminants in108 East Lake water samples;
    heptachlor occurrence and environmental risk do not constitute antimicrobial assays.
    24577234 studies SH-SY5Y cells and injected mice, not bacterial or fungal inhibition.
    Neither adopted source directly establishes either microbial role.
  snapshot_sha256: 5ab178f8b9297bb744e293f402a60b4caa55623237940ef85df429e9df072656
- evidence_id: host
  kind: primary_source
  reference: PMID:24577234; DOI:10.1038/emm.2014.12; PMC3944446
  locator: Complete abstract, selected introduction, reagent and injection Methods,
    and selected Results/Discussion; images not independently analyzed.
  accessed_at: '2026-10-21T18:00:01Z'
  support: context_only
  summary: Supelco heptachlor was used in mammalian cell and mouse experiments. The
    report associates treatment with mitochondria-mediated neuronal injury and Parkinsonism-like
    behavior. These host toxicity observations are not direct bacterial-target evidence,
    natural production, or clinical antimicrobial activity; detailed host numerical
    results are not imported.
  snapshot_sha256: 81e655f926ea23efb43c19eab9fcc50258ba7b152bc246c5658930726eb62dec
- evidence_id: bacterial1968
  kind: primary_source
  reference: PMID:4872999; DOI:10.1128/am.16.5.799-800.1968; PMC547523
  locator: Both original scanned pages799–800 read visually in full, including Figures1–2
    and all methods.
  accessed_at: '2026-10-21T18:00:01Z'
  support: partial
  summary: Collins and Langlois used77.2% heptachlor, with nominal50/100 ppm tests
    in trypticase soy broth or reconstituted skim milk and alcohol controls. S.aureus
    showed killing in broth at37 degrees C; E.coli and P.fluorescens did not show
    a heptachlor growth effect, and the skim-milk tests did not show inhibition. Colony
    counts were followed through7 days. The mixed-purity reagent and medium dependence
    prevent treating this as an exact pure-heptachlor universal MIC.
  snapshot_sha256: fd610a7991d4f6efeb63b6ae5cdeac4766a21a0bd6f9cfebf42be495754df256
- evidence_id: bacterial1968-results
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3808/547523/b9170227a26b/applmicro00241-0134.png
  locator: Actual second scanned page800, full Results/Conclusion.
  accessed_at: '2026-10-21T18:00:01Z'
  support: partial
  summary: The original explicitly separates the S.aureus heptachlor result from DDT
    effects on P.fluorescens and from negative skim-milk conditions. The review does
    not transfer DDT growth effects or regard all pesticides as equivalent.
  snapshot_sha256: a7007a98335a10269b551e9a40fdddff5d4814e8e9b0aa98c8fc18cf9adcb4cf
- evidence_id: bacterial1970
  kind: primary_source
  reference: PMID:4314375; DOI:10.1128/am.19.2.214-219.1970; PMC376654
  locator: All six original page scans214–219 read visually, including all three tables,
    figure, Methods and Discussion.
  accessed_at: '2026-10-21T18:00:01Z'
  support: partial
  summary: Nitrobacter agilis ATCC14123 was grown in defined inorganic medium at30
    degrees C with shaking and acetone vehicle controls. Table1 reports complete prevention
    of nitrite depletion at10 micrograms/mL heptachlor through9 days;5 micrograms/mL
    delayed depletion. Nitrite disappearance was used as the growth proxy, rather
    than viable counts or a standard MIC endpoint. Reagent purity and stereochemical
    composition are not specified in the inspected main. Cell-suspension and cell-free
    effects occur at much higher concentrations; the authors explicitly caution that
    those oxidation effects probably do not explain growth inhibition. No Kd, purified-protein
    binding target or exclusive antibacterial mechanism is established.
  snapshot_sha256: ac92714b3f2d8153ea1cdd12392d636e8e1d46777a99b70ab217bb7f27ad36ec
- evidence_id: bacterial1970-discussion
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/15ff/376654/3f51137386f9/applmicro00100-0036.png
  locator: Original page218, Table3 and Discussion; other page hashes in053-root-fetch6.json.
  accessed_at: '2026-10-21T18:00:01Z'
  support: context_only
  summary: The authors discuss solubility limits, potential binding of protein in
    extracts and adsorption by insoluble pesticide particles. Heptachlor suppresses
    cell-free nitrite oxidation more than whole-cell oxidation, but the disparity
    between growth and oxidation concentrations precludes a simple direct-target inference.
  snapshot_sha256: 057e58cb77e634ffb2ed0f3de69a94ee6b9e4e8b533ec6bfd749db5686eea9e0
- evidence_id: fungal1985
  kind: primary_source
  reference: DOI:10.1094/Phyto-75-553; https://www.apsnet.org/publications/phytopathology/backissues/Documents/1985Articles/Phyto75n05_553.pdf
  locator: All four original scanned pages553–556 read visually, including Tables1–3
    and complete Methods/Results/Discussion.
  accessed_at: '2026-10-21T18:00:01Z'
  support: partial
  summary: Draughon and Churchville tested technical-grade heptachlor supplied by
    Chevron against Fusarium roseum var.graminearum NRRL3376. In potato-dextrose broth
    at21 degrees C for3 weeks, dry mycelial mass was reduced41,46 and49 percent at10,50
    and100 ppm active-ingredient dosing, respectively (Table2). This is partial growth
    inhibition, not complete MIC or killing. Zearalenone on corn was a separate endpoint
    and the field treatments used other pesticides. Technical material and unreported
    detailed composition limit attribution to the exact graph.
  snapshot_sha256: b3a1a9c023ced3e36a307a65e1056585f04b5679f062202c38bbf16c4ea29e47
- evidence_id: negative-context
  kind: primary_source
  reference: PMID:2518692; Smith et al.1976, Developments in Industrial Microbiology17:331–336;
    https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=9100UKCN.TXT
  locator: 1989 complete original indexed abstract; selected1976 original abstract,
    Methods, Results and Tables2–4 from public EPA reprint text via web provider.
  accessed_at: '2026-10-21T18:00:01Z'
  support: context_only
  summary: The1989 rumen fermentation study found no heptachlor suppression of dry-matter
    disappearance under its conditions, unlike pentachlorophenol. The1976 fungal study
    used99.8% reference material in hexadecane and found no apparent suppression of
    utilization by the studied Candida preparations, with some stimulation in one
    condition. These condition-specific results neither erase the positive historical
    observations nor prove universal inactivity. The1976 direct download returned
    a redirect shell, so no downloaded-full-paper claim is made.
  snapshot_sha256: a8be4a42201856bf4d327e6e59965ea25b96e3e39cf9becb6d64b72864828001
- evidence_id: search
  kind: search
  reference: 528-local-hits.txt; 528-microbial-search.json; 053-root-fetch1.json through053-root-fetch6.json
  locator: Ignored- and hidden-inclusive initial local search, all adopted leads,
    targeted microbial discovery and ordinary free-authority/full-text retrieval.
  accessed_at: '2026-10-21T18:00:01Z'
  support: context_only
  summary: The broader heptachlor query returned1536 hits and only the first1000 were
    captured; the targeted microbial query returned64. Titles were screened and selected
    exact-compound originals pursued. This is bounded discovery, not exhaustive absence
    evidence. Failed XML, PDF and challenge routes are retained separately from the
    successfully inspected page scans and publisher PDF.
  search_scope: 2026-10-21; isolated worktree053 including ignored/hidden local files;
    exact heptachlor name, identifiers, two adopted PMIDs, targeted microbial and
    stereochemical searches.
  snapshot_sha256: f02110ff2f830d540a4c6e242e95ebc69f6ad7f404531c5c3e0d33fde10ce0f7
assessments:
- assessment_id: identity
  area: identity
  topic: Generic heptachlor and chemical authority agreement
  outcome: supported
  summary: All checked exact xrefs and native encodings agree at the represented stereo-unspecified
    level. No specific enantiomer or technical formulation is asserted. Additional
    stereochemical resolution requires an explicitly chosen material scope.
  target_ids:
  - CHEBI:34785
  evidence_ids:
  - native
  - authority
  - stereo
- assessment_id: roles
  area: evidence
  topic: Antimicrobial classification and tested-material limits
  outcome: unknown
  summary: Current database roles and historical microbial inhibition are compatible,
    but exact pure-material attribution remains limited:1968 uses77.2% material,1985
    technical material, and1970 does not specify purity. No forced role deletion or
    exact pure-compound MIC is justified from these sources.
  target_ids:
  - CHEBI:34785
  evidence_ids:
  - classes
  - adopted
  - bacterial1968
  - bacterial1970
  - fungal1985
  - negative-context
- assessment_id: nomenclature
  area: nomenclature
  topic: Trade name within exact aliases
  outcome: concern
  summary: Heptamul is explicitly a trade name in the WHO identity section and should
    be typed accordingly. Other name use, including Heptachlorane, is not overcorrected
    where generic and commercial usage overlap.
  target_ids:
  - CHEBI:34785
  evidence_ids:
  - native
  - names
  - authority
- assessment_id: xref
  area: grounding
  topic: Exact and document references
  outcome: unknown
  summary: CAS, KEGG and PPDB are independently corroborated. Reaxys is source-attributed
    only; the Wikipedia link is relevant document context. No inaccessible-registry
    mismatch is invented.
  target_ids:
  - CHEBI:34785
  evidence_ids:
  - authority
  - xref
- assessment_id: mechanism
  area: evidence
  topic: No target overpromotion
  outcome: supported
  summary: The native makes no molecular-target assertion. Host mitochondrial results
    and indirect bacterial enzyme/respiration measurements are kept separate from
    binding evidence and insect chloride-channel context.
  target_ids:
  - CHEBI:34785
  evidence_ids:
  - native
  - host
  - bacterial1970
  - bacterial1970-discussion
- assessment_id: provenance
  area: provenance
  topic: Complete native/source/history review
  outcome: supported
  summary: All original thirteen hashes are retained, the exact adopted source row
    was read, both adopted citations disposed, and four chronological source-history
    events are preserved. Optional microbial observations or causal graphs are not
    required just because literature exists.
  target_ids:
  - CHEBI:34785
  evidence_ids:
  - native
  - owners
  - adopted
  - search
findings:
- finding_id: F1
  issue_key: heptachlor-heptamul-trade-name-type
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: Heptamul is a trade name rather than an exact chemical-name synonym
  description: The native Heptamul synonym is typed EXACT_SYNONYM. WHO EHC38 section2.1
    explicitly lists Heptamul as a common trade name. Preserve the useful alias but
    classify its commercial-name scope; do not infer product composition or one formulation
    from the generic chemical graph.
  target_ids:
  - CHEBI:34785
  field_paths:
  - synonyms[6].synonym_type
  evidence_ids:
  - native
  - names
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, aliases, roles and publication leads
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Role priority and synonym mapping
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  rule_id: review-yaml-record:Workflow:nomenclature
  native_severity: minor
  normalization_reason: An alias typing defect changes naming scope without changing
    the represented chemical structure.
actions:
- action_id: A1
  description: Preserve Heptamul with a trade-name type through the maintained synonym
    handling.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:34785
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, aliases, roles and publication leads
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Role priority and synonym mapping
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Use BRAND_NAME for the Heptamul alias with the WHO identity source retained; avoid
    unsupported changes to dual-use Heptachlorane.
  - Regenerate through the maintained owner and verify exact structure, provenance/history,
    schema/strict and required corpus gates.
- action_id: A2
  description: If activity is later curated, retain the tested material and endpoint
    boundaries.
  finding_ids: []
  target_ids:
  - CHEBI:34785
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/heptachlor.yaml
    role: Optional validated curator-owned evidence annotations
  acceptance_checks:
  - Do not convert technical or77.2% material into pure exact-compound MIC evidence.
  - Distinguish nitrite-depletion growth proxy, viable-count killing, dry-weight inhibition,
    toxin production and substrate utilization; retain organism, medium and assay
    duration.
  - Resolve reagent purity and chosen stereochemical scope before adding exact-material
    claims; do not transfer host or insect mechanisms into bacterial binding targets.
limitations:
- Full original1968,1970 and1985 papers were visually read at all pages. Original
  spectra and supplier certificates were not available;1968 and1985 explicitly use
  impure/technical material, while1970 main does not state chemical purity.
- Both adopted complete abstracts were read. The2014 mouse paper was inspected only
  at the selected-main depth stated above, without raw image analysis; the lake-contamination
  paper remained abstract-depth.
- The2004 enantiomer-separation and1989 rumen studies remained complete-abstract depth.
  The1976 fungal reprint was read only at the stated selected-text depth through the
  web provider; tables and page images were not independently downloaded.
- The generic authoritative graph leaves five potential stereocentres unassigned.
  This review does not claim one enantiomer, an exhaustive stereochemical-isomer inventory,
  or the composition of a technical product.
- Reaxys2058523 underlying registration was not independently inspected. A public
  registry access gap does not establish an incorrect xref.
- Searches were bounded. The broad1536-hit result was truncated to1000 records; no
  claim of exhaustive microbial or regulatory literature coverage is made.
- The native has no populated bacterial protein/pathway assertion; broad activity
  discovery did not trigger a structured target-dataset lookup. Shared required corpus
  gates and the known SciPy platform failure are incorporated separately by the finalizer.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- The original source and native record remain unchanged; this is a scientific review
  with one bounded alias finding.
- Successful scan/PDF retrievals are explicitly distinguished from HTTP200 challenge
  shells, failed XML routes and the inaccessible IARC page. The actual publisher1985
  PDF was retrieved via its lower-case .pdf URL and rendered locally.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
