# Hyperforin: coherent native structure with a stereochemically different PDB chemical cross-reference

- Review: 20261021T183953Z-hyperforin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T18:07:33Z
- Finished UTC: 2026-10-21T18:39:53Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact neutral native hyperforin graph, composition and systematic names agree with current ChEBI, KEGG and the molecular encodings in KNApSAcK, with primary synthesis support. However, asserted exact xref PDB CCD HYF encodes the C7 epimer in its descriptors and coordinate models. One major grounding correction is required. All ten adopted abstracts were read, with original synthesis full text and selected primary antibacterial and protonophore experiments examined beyond abstracts.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Assigned queue position 543; one exact native record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:5834 | data/antibiotics/antibacterial/hyperforin.yaml | generated | hyperforin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:5834 | Actual focused execution exited 0. Executed against 055; chemistry used the existing 019 RDKit interpreter, while schema/strict used 055. |
| Focused schema verification | passed | True | CHEBI:5834 | Actual focused execution exited 0. Executed against 055; chemistry used the existing 019 RDKit interpreter, while schema/strict used 055. |
| Focused strict verification | passed | True | CHEBI:5834 | Actual focused execution exited 0. Executed against 055; chemistry used the existing 019 RDKit interpreter, while schema/strict used 055. |
| Authoritative full QC | failed | True | CHEBI:5834 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:5834 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:5834 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:5834 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:5834 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:5834 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:5834 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:5834 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:5834 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Neutral natural-series hyperforin graph and names

identity: supported. Targets: CHEBI:5834.

Composition, charge, mass and four configured centres are coherent. Accurate CIP validates both systematic synonyms, and the adopted synthesis plus supplementary natural-product comparison supports the retained series. No wrong-native-identity conclusion follows from the erroneous CCD link.

### Exact chemical xrefs versus drug/document associations

grounding: concern. Targets: CHEBI:5834.

PDB CCD HYF is a confirmed C7 epimer across descriptors and both coordinate sets, so its exact xref is invalid for this graph. KEGG and KNApSAcK molecular encodings match; the latter’s printed key is separately inconsistent. DrugBank is drug-level and Wikipedia a document; inaccessible registry content is unresolved rather than falsely verified.

### Broader ring classes and unresolved sesquarterpenoid boundary

grounding: unknown. Targets: CHEBI:5834.

The cyclic terpene ketone and carbobicyclic classes fit the retained ring/ketone graph. CHEBI:51961 requires sesquarterpene derivation, which carbon count alone does not prove. The inspected synthesis describes a polyketide-derived acylphloroglucinol core and terpene side chains; its relationship to the asserted biosynthetic parent needs separate ontology/source adjudication. No confirmed additional correction is inferred.

### Antibacterial role and exact assay boundaries

evidence: supported. Targets: CHEBI:5834.

The inspected 2025 original supplies hyperforin-alone bacterial growth inhibition under specified conditions, including the exceptional LPS-deficient AB065 strain. It supports the qualitative role without generalizing combination synergy or host pharmacology to antibacterial mechanism.

### All adopted leads and optional biological representation

completeness: unknown. Targets: CHEBI:5834.

All ten adopted abstracts were read, including two recognized secondary reviews; the 2013 original was followed to full main and selected SI identity sections. Direct protonophore behavior has been studied outside bacterial cells, but no bacterial target is established by the inspected work. Missing optional targets, causal graphs and quantitative observations are not a required correction.

### Source-owned content and unchanged captures/history

provenance: supported. Targets: CHEBI:5834.

The complete source row, all native history events and maintained extraction/seeding ownership were checked. Original 13 and expanded 21 input hashes remain unchanged; the review does not promote SEEDED status.

## Findings

### F1: PDB CCD HYF encodes the C7 epimer rather than the native exact structure

major / open / confirmed; issue key: hyperforin-pdb-ccd-hyf-c7-epimer-xref.

Native xrefs[4] asserts exact chemical equivalence to HYF. Current HYF descriptors and independently reconstructed model/ideal coordinates give IWBJJCOKGLUQIZ-OJCNYLSASA-N, while native is IWBJJCOKGLUQIZ-HQKKAZOISA-N. Inverting only native atom 8 (systematic bicyclo C7S to R; CCD atom C33) reproduces HYF with reciprocal chirality-aware matches. Correct the maintained exact-link handling without replacing the supported native hyperforin graph or dismissing the separate human-PXR experiment as nonexistent.

## Recommended Actions And Acceptance Checks

### A1

Adjudicate the HYF exact xref in maintained ChEBI extraction/inventory handling and regenerate the native field.

- Retain the supported native composition and four configured centres; remove or appropriately qualify HYF as an exact chemical link unless a corrected upstream component is independently verified.
- Compare full stereo-aware graphs, including native atom 8/systematic C7 and CCD C33; do not use the shared first InChIKey block or name alone as equality.
- Do not conflate the exact xrefs rule with drug_xrefs, and do not replace native with the unasserted alternate PubChem tautomer automatically.
- Rerun native schema/strict, exact chemical comparison and required corpus/reference/history gates; demonstrate that re-seeding preserves the adjudication.

### A2

Optional mechanism or activity enrichment must preserve experimental material and system boundaries.

- For bacterial activity retain the named preparation, strain, CAMHB conditions, visible-growth endpoint, 18–20 h and printed mg/L units; do not generalize AB065 to all A.baumannii.
- For protonophore claims distinguish free acid from DCHA salt, protein-free membranes from mammalian cells and hypotheses about bacterial action from directly tested mechanisms.
- Resolve original 1999 table and 1983 absolute-configuration paper access before claiming those originals were fully adjudicated; do not import seven unrelated 2012 metabolite values.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/hyperforin.yaml; Entire native record, including definition, five synonyms, three parents, role, structure, six chemical xrefs, one drug xref, document link and four history events | supports | CHEBI:5834 is SEEDED, EXACT and ANTIBACTERIAL. It denotes neutral C35H52O4, key IWBJJCOKGLUQIZ-HQKKAZOISA-N, with four configured tetrahedral centres. No molecular target, resistance, quantitative activity_spectrum, causal graph or clinical-product claim is asserted. |
| owners | data/raw/chebi_antimicrobials.tsv#CHEBI:5834; Complete row 195, readiness row 1399 and exact curator/decision lookup | context_only | The complete ChEBI row supplies the identity, names, chemical links and ten adopted PMID leads. No exact curator or decision override was found. Original 13 captured inputs were preserved and expanded to 21 actual owner/context inputs before judgment. |
| search | /private/tmp/am-review-session/543-context-search.txt; Initial whole-tree and owner searches, plus bounded Europe PMC discovery | context_only | Identifier, label and slug searches included hidden and ignored files. Additional primary leads were selected for exact identity, antibacterial assays and mechanistic scope; the discovery response is not a claim that every returned paper was fully reviewed. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/5834/; Complete current CHEBI:5834 identity response | supports | Current ChEBI agrees with the native graph, formula, charge, names and source assertions, including the disputed PDB CCD link. Agreement identifies provenance but does not independently validate that link. |
| kegg | https://rest.kegg.jp/get/C07608/mol; C07608 molfile and accompanying entry | supports | The KEGG compound molfile reproduces the native full graph and key. |
| knapsack | https://www.knapsackfamily.com/knapsack_core/information.php?word=C00034542; C00034542 complete identity page; molecular encodings versus displayed key | supports | The page names hyperforin and supplies SMILES and InChI that reproduce the native graph. Its separately printed InChIKey IWBJJCOKGLUQIZ-GXUKJDDZNA-N conflicts with those encodings. This external display inconsistency is preserved; it does not establish a different compound when the supplied molecular graphs match. |
| mapping | /private/tmp/am-review-session/543-map.py; 019 RDKit 2026.03.5 executed against worktree 055; native and current authority graphs | supports | Native SMILES/InChI, current ChEBI, KEGG and KNApSAcK molecular encodings agree. Accurate rdCIPLabeler gives native systematic bicyclo positions 1R,5S,6R,7S at zero-based atoms 15,31,6,8. Legacy RDKit incorrectly labels bridgehead atom 15 S; this algorithm difference does not make the native chemical name wrong. Full numbered correspondence is retained. |
| ccd | https://files.rcsb.org/ligands/download/HYF.cif; HYF CIF descriptors, atom/bond table and model/ideal coordinates | refutes | HYF has the same constitution but configured descriptors encode IWBJJCOKGLUQIZ-OJCNYLSASA-N. The native C7 centre is S, whereas HYF atom C33 is R. CIF records model coordinates from 1M13; this is a chemical component accession, not a drug-level association. |
| single-inversion | /private/tmp/am-review-session/543-compare.py; Single-centre inversion and stereo-preserving tautomer comparison | refutes | Inverting only native atom 8, systematic bicyclo C7, gives the exact HYF full key and reciprocal chirality-aware graph matches. Separately, the unasserted PubChem name comparator has a different keto-enol representation but converges with native under tautomer normalization that retains sp3 stereo. That comparator is not a native bad xref. |
| ccd-coordinates | /private/tmp/am-review-session/543-cif-map.py; Independent graph construction from CIF bond table and stereo assignment from model and ideal coordinates | refutes | Both coordinate sets reproduce the HYF descriptor key and C33R. No native stereo was supplied to this reconstruction. This confirms an actual stereochemical difference, rather than a spelling, atom-order or CIP-label artifact; the original protein diffraction data were not re-refined. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/hyperforin/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,Charge/JSON; Additional unasserted name comparator | context_only | PubChem returns KGSZHKRKHXOAMG-HQKKAZOISA-N, an alternate keto-enol form with the retained tetrahedral configuration. This additional lookup is not asserted in native xrefs and is not treated as a record defect or automatic replacement. |
| term36130 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/36130/; Current CHEBI:36130 definition | supports | cyclic terpene ketone: An alicyclic ketone in which the carbocyclic ring structure forms part of a terpene skeleton. The native graph supports this broader ring/ketone classification. |
| term36785 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/36785/; Current CHEBI:36785 definition | supports | carbobicyclic compound: A bicyclic compound in which all the ring atoms are carbon. The native graph supports this broader ring/ketone classification. |
| term51961 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/51961/; Current CHEBI:51961 definition | supports | sesquarterpenoid: Any terpenoid derived from a sesquarterpene. The term includes compounds in which the C35 skeleton of the parent sesquarterpene has been rearranged or modified by the removal of one or more skeletal atoms (generally methyl groups). The source asserts this parent, but C35 composition alone does not establish sesquarterpene derivation. The inspected 2013 main instead describes a polyketide-derived acylphloroglucinol core with terpene-side-chain construction; this biosynthetic class boundary remains unresolved. |
| role | https://www.ebi.ac.uk/chebi/backend/api/public/compound/33282/; Current antibacterial-agent role; shared official snapshot | supports | The role denotes inhibition or killing of bacteria, without requiring a clinical indication, universal species spectrum or demonstrated molecular target. |
| pmid12578355 | PMID:12578355; DOI 10.1021/bi0268753; complete adopted abstract read | context_only | Original human pregnane X receptor co-crystal study at 2.1 Å; this is host drug-metabolism biology, not a bacterial target. RCSB1M13 is linked to this original, but its HYF chemical stereochemistry conflicts with native as independently checked. |
| pmid16973193 | PMID:16973193; DOI 10.1016/j.phytochem.2006.08.017; complete adopted abstract read | context_only | This is a secondary review of hyperforin distribution, biosynthesis and pharmacology, useful for discovery rather than primary mechanism proof. |
| pmid21947285 | PMID:21947285; DOI 10.3892/ijo.2011.1206; complete adopted abstract read | context_only | Original CLL/MEC1 leukemia experiments examine Noxa, apoptosis and proteasome-related effects. Host cancer-cell effects do not establish antibacterial mechanism. |
| pmid22226089 | PMID:22226089; DOI 10.1017/s146114571100188x; complete adopted abstract read | context_only | Original mouse cortex/neuron study concerns chronic hyperforin and TRPC6/CREB/TrkB-associated neurobiology, not bacterial activity. |
| pmid22924417 | PMID:22924417; DOI 10.2174/156800913804486601; complete adopted abstract read | context_only | Secondary review of antileukemic mechanisms; it is not relabeled as primary evidence. |
| pmid23149561 | PMID:23149561; DOI 10.1038/jcbfm.2012.164; complete adopted abstract read | context_only | Original rat cerebral ischemia/neuroprotection study evaluates TRPC6 degradation. Host protection is not bacterial target evidence. |
| pmid23270309 | PMID:23270309; DOI 10.1021/ja312150d; complete adopted abstract read | context_only | Original enantioselective total synthesis, followed to the full accepted manuscript and selected supplementary identity pages below. |
| pmid23811220 | PMID:23811220; DOI 10.1016/j.ejpb.2013.06.016; complete adopted abstract read | context_only | Original 11-volunteer skin study uses a hyperforin-rich cream and placebo to examine radical formation and skin lipids. Formulated extract and human endpoints are not pure-compound antibacterial assays. |
| pmid24033566 | PMID:24033566; DOI 10.1111/cpr.12060; complete adopted abstract read | context_only | Original mouse embryonic stem-cell/fibroblast differentiation and toxicity study; it establishes neither bacterial mechanism nor general safety. |
| pmid24121871 | PMID:24121871; DOI 10.1007/s00592-013-0518-2; complete adopted abstract read | context_only | Original rat/human islet study distinguishes Hypericum extract and hyperforin in cytokine protection. These host endpoints do not support antibacterial targets. |
| primary2013 | https://dash.harvard.edu/server/api/core/bitstreams/7312037d-1e72-6bd4-e053-0100007fdf3b/content; Full accepted manuscript scientific text; actual Schemes 1 and 3 viewed | supports | The original reports an 18-step enantioselective synthesis of natural hyperforin and distinguishes prior ent-hyperforin synthesis. It identifies the natural source as Hypericum perforatum and provides exact structure drawings. This is an author-repository accepted version, not falsely labeled the final typeset version. Its introductory TRPC6 account is not adopted as an antibacterial target. |
| primary2013-si | https://ndownloader.figshare.com/files/4094722; Selected SI S24–S30 identity, conversion and comparison sections; actual S26/S28 structure pages viewed | supports | S24 names O-methylhyperforin 21 with 7S configuration; S26 demethylates 21 to hyperforin 1 without altering that carbon. The isolated synthetic product is 40.0 mg and has [α]D23 +39.5 (c3.02,EtOH), compared by the authors with historical natural +41 (18°C,c5,EtOH). S29–S30 compare proton/carbon data with published natural and synthetic ent material. S28 explicitly discusses water/concentration-dependent keto-enol behavior. This supports the natural-series identity, without claiming rotation alone proves absolute configuration or independently reassigning raw spectra. |
| primary2025 | PMID:41222309; DOI:10.1128/aac.01007-25; Selected exact-material Methods, MIC Table 1, associated results and mechanistic discussion | supports | The original uses hyperforin from Henan Chemical Co., CAS11079-53-1, dissolved in methanol; no lot-specific purity or independent stereochemical analysis is stated in the inspected methods. Broth microdilution uses CAMHB, approximately 0.5 McFarland suspension,100µL suspension plus100µL drug and 37°C for18–20h, with visible-growth MIC. The final viable inoculum was not independently established. |
| primary2025-activity | PMID:41222309; Table 1 exact hyperforin-alone column and A.baumannii FADDI-AB065 discussion | supports | The original reports hyperforin MIC 0.25 mg/L against the authors’ LPS-deficient FADDI-AB065, whereas most panel isolates are &gt;128 mg/L and some other isolates have finite higher values. This supports a bounded antibacterial role, not species-wide potency. The AB065 combination FICI is 2.0, not synergy. Combination permeability/ROS observations do not establish hyperforin binding to peptidoglycan or a particular intracellular target. |
| primary2025-limits | PMID:41222309; Source discrepancies and experiment boundaries in selected main | context_only | The article uses both &lt;0.5 and ≤0.5 synergy cutoffs and its prose ATCC 13883 FICI differs from Table 1. Censored hyperforin MICs are substituted for some calculations. No numerical combination, time-kill or biofilm result is imported into native activity_spectrum; figures and supplementary experiments were not independently inspected. These limits do not erase the exact monotherapy Table 1 result. |
| primary2014 | PMID:25511254; DOI:10.1038/srep07500; Selected original Results, Chemicals, electrophysiology and lipid-bilayer Methods; figure captions | context_only | The original compares hyperforin-DCHA salt with free acid in methanol and demonstrates TRPC6-independent proton currents in mammalian cells and protein-free lipid bilayers. The inspected results include free-acid microglial experiments, while other experiments use salt preparations. This is direct biophysical protonophore evidence in the tested systems, not a directly demonstrated bacterial molecular target; its antibiotic-mechanism extension is explicitly discussed as a possibility. No figure-derived numerical endpoint is asserted from unread images. |
| excluded2012 | PMID:22170780; Selected complete isolation/methods and compound scope in PMC3339047 | context_only | The paper tests seven metabolites from H.densiflorum,H.ellipticum,H.prolificum and H.punctatum. Its discussion references hyperforin, but those compounds and their pooled MIC ranges are not treated as exact hyperforin assays. |
| historical1999 | PMID:10382704; DOI:10.1016/S0140-6736(99)00214-7; Original metadata/title only; no indexed abstract and publisher full text 403 | context_only | The title is a relevant original antibacterial lead, but the experimental table/material details were not accessed. PMID 10475223 is a later comment, not a substitute assay source. No historical MIC is inferred from review quotations or title alone. |
| access | /private/tmp/am-review-session/543-fetch1.json; Recorded public retrieval attempts and successful alternatives in 543-fetch1 through 543-fetch8 | context_only | HMDB returned 403, CAS 401 and DrugBank 403; Reaxys free primary registry content remained unavailable. DrugBank is a drug-level association, not exact-structure equivalence. Original 1983 archive requests failed; direct ACS main/SI routes were 403 and Harvard download routes 429, but the legitimate Harvard repository API and verified ACS Figshare file supplied the 2013 originals. Wikipedia resolves as a document reference only. |
| adapter | /private/tmp/am-review-session/543-adapter-scope.json; Native applicability assessed before open-ended literature follow-up | context_only | No native gene, protein, regulator, pathway or transcriptomic assertion requires a structured query. The producer plant is not a covered bacterial expression dataset; later host-mechanism discovery does not become a native assertion. |

## Limits And Additional Notes

- All ten adopted abstracts were read. Beyond abstracts, the 2013 accepted manuscript and selected SI identity/conversion/comparison pages were inspected; the other adopted host-pharmacology papers were not exhaustively audited at full experimental depth.
- CHEBI:51961 sesquarterpenoid remains an unresolved biosynthetic classification boundary. The retained C35 composition is not treated as proof of seven-isoprene-unit ancestry; direct biosynthesis and the ontology scope require separate adjudication.
- The 1983 original absolute-configuration paper and 1999 antibacterial experimental table were inaccessible through the attempted free routes. The 2013 synthesis and current authority comparisons supply independent bounded identity support; no claim of raw diffraction or raw NMR reanalysis is made.
- The 2025 original was read selectively for exact reagent, MIC Table 1, associated results and mechanism scope. Figures and supplementary assays were not independently viewed, reagent purity/stereo was not remeasured, and source FICI discrepancies preclude unqualified quantitative transfer.
- HMDB 403, CAS 401, DrugBank 403 and unavailable independent Reaxys content limit registry verification. KNApSAcK’s displayed key conflicts with its matching molecular encodings. The HYF coordinate check concerns the deposited model, not a new protein crystallographic refinement.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All original 13 and expanded 21 local input hashes were rechecked unchanged before draft writing. No native/source/history/progress/saved-bundle/Git writes occurred.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T183953Z-hyperforin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Hyperforin: coherent native structure with a stereochemically different PDB
  chemical cross-reference'
started_at: '2026-10-21T18:07:33Z'
finished_at: '2026-10-21T18:39:53Z'
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
summary: The exact neutral native hyperforin graph, composition and systematic names
  agree with current ChEBI, KEGG and the molecular encodings in KNApSAcK, with primary
  synthesis support. However, asserted exact xref PDB CCD HYF encodes the C7 epimer
  in its descriptors and coordinate models. One major grounding correction is required.
  All ten adopted abstracts were read, with original synthesis full text and selected
  primary antibacterial and protonophore experiments examined beyond abstracts.
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
  - path: data/antibiotics/antibacterial/hyperforin.yaml
    sha256: 665909ebe862219ffa629c44ab3c79d031251696993d20f72060ca8ca9c3ac61
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
- target_id: CHEBI:5834
  path: data/antibiotics/antibacterial/hyperforin.yaml
  label: hyperforin
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
  selection: Assigned queue position 543; one exact native record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:5834
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0. Executed against 055; chemistry used
    the existing 019 RDKit interpreter, while schema/strict used 055.
  target_ids:
  - CHEBI:5834
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    543
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Executed against 055; chemistry used
    the existing 019 RDKit interpreter, while schema/strict used 055.
  target_ids:
  - CHEBI:5834
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/hyperforin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Executed against 055; chemistry used
    the existing 019 RDKit interpreter, while schema/strict used 055.
  target_ids:
  - CHEBI:5834
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/hyperforin.yaml --out /private/tmp/am-review-session/543-strict.tsv
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
  - CHEBI:5834
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
  - CHEBI:5834
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
  - CHEBI:5834
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
  - CHEBI:5834
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
  - CHEBI:5834
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
  - CHEBI:5834
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
  - CHEBI:5834
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
  - CHEBI:5834
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
  - CHEBI:5834
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/hyperforin.yaml
  locator: Entire native record, including definition, five synonyms, three parents,
    role, structure, six chemical xrefs, one drug xref, document link and four history
    events
  accessed_at: '2026-10-21T18:31:27Z'
  support: supports
  summary: CHEBI:5834 is SEEDED, EXACT and ANTIBACTERIAL. It denotes neutral C35H52O4,
    key IWBJJCOKGLUQIZ-HQKKAZOISA-N, with four configured tetrahedral centres. No
    molecular target, resistance, quantitative activity_spectrum, causal graph or
    clinical-product claim is asserted.
  snapshot_sha256: 665909ebe862219ffa629c44ab3c79d031251696993d20f72060ca8ca9c3ac61
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv#CHEBI:5834
  locator: Complete row 195, readiness row 1399 and exact curator/decision lookup
  accessed_at: '2026-10-21T18:31:27Z'
  support: context_only
  summary: The complete ChEBI row supplies the identity, names, chemical links and
    ten adopted PMID leads. No exact curator or decision override was found. Original
    13 captured inputs were preserved and expanded to 21 actual owner/context inputs
    before judgment.
  snapshot_sha256: 4fed0ea146d87575fd00429f362523ac587d386c4ed56ade3021729694955404
- evidence_id: search
  kind: search
  reference: /private/tmp/am-review-session/543-context-search.txt
  locator: Initial whole-tree and owner searches, plus bounded Europe PMC discovery
  accessed_at: '2026-10-21T18:31:27Z'
  support: context_only
  summary: Identifier, label and slug searches included hidden and ignored files.
    Additional primary leads were selected for exact identity, antibacterial assays
    and mechanistic scope; the discovery response is not a claim that every returned
    paper was fully reviewed.
  snapshot_sha256: 73789106e6d0c699d46e0783d512c8c2282c10a224b2719563460e0d27667c8b
  search_scope: Worktree 055 initial543-local-hits.txt and rg --no-ignore --hidden
    owner follow-up; exact hyperforin public Europe PMC query recorded in543-fetch
    manifests.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/5834/
  locator: Complete current CHEBI:5834 identity response
  accessed_at: '2026-10-21T18:22:18.647878Z'
  support: supports
  summary: Current ChEBI agrees with the native graph, formula, charge, names and
    source assertions, including the disputed PDB CCD link. Agreement identifies provenance
    but does not independently validate that link.
  snapshot_sha256: 5381e54c1ab98634d2947f7bd88f3e1767b8d13064cc9c0b7f7b41474392bea2
- evidence_id: kegg
  kind: authority
  reference: https://rest.kegg.jp/get/C07608/mol
  locator: C07608 molfile and accompanying entry
  accessed_at: '2026-10-21T18:22:19.191081Z'
  support: supports
  summary: The KEGG compound molfile reproduces the native full graph and key.
  snapshot_sha256: 723c1f7519d65c560fd64c063f77312be3f2520fb30d12fcf0bd38cc579f6c49
- evidence_id: knapsack
  kind: authority
  reference: https://www.knapsackfamily.com/knapsack_core/information.php?word=C00034542
  locator: C00034542 complete identity page; molecular encodings versus displayed
    key
  accessed_at: '2026-10-21T18:22:19.908119Z'
  support: supports
  summary: The page names hyperforin and supplies SMILES and InChI that reproduce
    the native graph. Its separately printed InChIKey IWBJJCOKGLUQIZ-GXUKJDDZNA-N
    conflicts with those encodings. This external display inconsistency is preserved;
    it does not establish a different compound when the supplied molecular graphs
    match.
  snapshot_sha256: 1660a319fcbb5820776f820f9af7065a2f5aa24e6da16ee0d7c6e6110646411f
- evidence_id: mapping
  kind: validation
  reference: /private/tmp/am-review-session/543-map.py
  locator: 019 RDKit 2026.03.5 executed against worktree 055; native and current authority
    graphs
  accessed_at: '2026-10-21T18:31:27Z'
  support: supports
  summary: Native SMILES/InChI, current ChEBI, KEGG and KNApSAcK molecular encodings
    agree. Accurate rdCIPLabeler gives native systematic bicyclo positions 1R,5S,6R,7S
    at zero-based atoms 15,31,6,8. Legacy RDKit incorrectly labels bridgehead atom
    15 S; this algorithm difference does not make the native chemical name wrong.
    Full numbered correspondence is retained.
  snapshot_sha256: d5bf515f8ed7ef5fc14f1d736f326134986d8508ab68df762e277a211d0dc2e4
- evidence_id: ccd
  kind: authority
  reference: https://files.rcsb.org/ligands/download/HYF.cif
  locator: HYF CIF descriptors, atom/bond table and model/ideal coordinates
  accessed_at: '2026-10-21T18:22:19.716871Z'
  support: refutes
  summary: HYF has the same constitution but configured descriptors encode IWBJJCOKGLUQIZ-OJCNYLSASA-N.
    The native C7 centre is S, whereas HYF atom C33 is R. CIF records model coordinates
    from 1M13; this is a chemical component accession, not a drug-level association.
  snapshot_sha256: 95b70bc0a2fad60e48068d1b8ffe62905bdc2e6448421c49dda96954eec020f1
- evidence_id: single-inversion
  kind: validation
  reference: /private/tmp/am-review-session/543-compare.py
  locator: Single-centre inversion and stereo-preserving tautomer comparison
  accessed_at: '2026-10-21T18:31:27Z'
  support: refutes
  summary: Inverting only native atom 8, systematic bicyclo C7, gives the exact HYF
    full key and reciprocal chirality-aware graph matches. Separately, the unasserted
    PubChem name comparator has a different keto-enol representation but converges
    with native under tautomer normalization that retains sp3 stereo. That comparator
    is not a native bad xref.
  snapshot_sha256: 397c99b7ee0a43bbabc191c147a0c9b949d0b1e32153bd488c815bc72a26a996
- evidence_id: ccd-coordinates
  kind: validation
  reference: /private/tmp/am-review-session/543-cif-map.py
  locator: Independent graph construction from CIF bond table and stereo assignment
    from model and ideal coordinates
  accessed_at: '2026-10-21T18:31:27Z'
  support: refutes
  summary: Both coordinate sets reproduce the HYF descriptor key and C33R. No native
    stereo was supplied to this reconstruction. This confirms an actual stereochemical
    difference, rather than a spelling, atom-order or CIP-label artifact; the original
    protein diffraction data were not re-refined.
  snapshot_sha256: e8b446616b8e92767dd109e1b17288b29e07ae79e64bc66dbfc91e3ca5a43c97
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/hyperforin/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,Charge/JSON
  locator: Additional unasserted name comparator
  accessed_at: '2026-10-21T18:22:18.651203Z'
  support: context_only
  summary: PubChem returns KGSZHKRKHXOAMG-HQKKAZOISA-N, an alternate keto-enol form
    with the retained tetrahedral configuration. This additional lookup is not asserted
    in native xrefs and is not treated as a record defect or automatic replacement.
  snapshot_sha256: 936264acdb1b5459e07d6206575abfab04eb837931b04dcc16a436d33ded2676
- evidence_id: term36130
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/36130/
  locator: Current CHEBI:36130 definition
  accessed_at: '2026-10-21T18:22:20.610900Z'
  support: supports
  summary: 'cyclic terpene ketone: An alicyclic ketone in which the carbocyclic ring
    structure forms part of a terpene skeleton. The native graph supports this broader
    ring/ketone classification.'
  snapshot_sha256: 8425f9cca308f59663be473c630dca3a332b3d0c8ebec0656fdc999fa4ece838
- evidence_id: term36785
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/36785/
  locator: Current CHEBI:36785 definition
  accessed_at: '2026-10-21T18:22:21.415356Z'
  support: supports
  summary: 'carbobicyclic compound: A bicyclic compound in which all the ring atoms
    are carbon. The native graph supports this broader ring/ketone classification.'
  snapshot_sha256: 050994a37e7b70fc7ca09e42105d15e9228061408620d4ddb077b689a4e29cca
- evidence_id: term51961
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/51961/
  locator: Current CHEBI:51961 definition
  accessed_at: '2026-10-21T18:22:22.182972Z'
  support: supports
  summary: 'sesquarterpenoid: Any terpenoid derived from a sesquarterpene. The term
    includes compounds in which the C35 skeleton of the parent sesquarterpene has
    been rearranged or modified by the removal of one or more skeletal atoms (generally
    methyl groups). The source asserts this parent, but C35 composition alone does
    not establish sesquarterpene derivation. The inspected 2013 main instead describes
    a polyketide-derived acylphloroglucinol core with terpene-side-chain construction;
    this biosynthetic class boundary remains unresolved.'
  snapshot_sha256: 46a03de8293f0348d1276ebdea9a5697d92811eacf1c8fb75b424991f3161930
- evidence_id: role
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/33282/
  locator: Current antibacterial-agent role; shared official snapshot
  accessed_at: '2026-10-21T18:31:27Z'
  support: supports
  summary: The role denotes inhibition or killing of bacteria, without requiring a
    clinical indication, universal species spectrum or demonstrated molecular target.
  snapshot_sha256: 20d92ce7e00c204b1753184671c043160821d692438278344335446aadcd5082
- evidence_id: pmid12578355
  kind: primary_source
  reference: PMID:12578355
  locator: DOI 10.1021/bi0268753; complete adopted abstract read
  accessed_at: '2026-10-21T18:22:18.650260Z'
  support: context_only
  summary: Original human pregnane X receptor co-crystal study at 2.1 Å; this is host
    drug-metabolism biology, not a bacterial target. RCSB1M13 is linked to this original,
    but its HYF chemical stereochemistry conflicts with native as independently checked.
  snapshot_sha256: 8265e6d4d9c64c53daf66022d11add7456645ec63e9159756af9387110de3424
- evidence_id: pmid16973193
  kind: database
  reference: PMID:16973193
  locator: DOI 10.1016/j.phytochem.2006.08.017; complete adopted abstract read
  accessed_at: '2026-10-21T18:22:18.650260Z'
  support: context_only
  summary: This is a secondary review of hyperforin distribution, biosynthesis and
    pharmacology, useful for discovery rather than primary mechanism proof.
  snapshot_sha256: 8265e6d4d9c64c53daf66022d11add7456645ec63e9159756af9387110de3424
- evidence_id: pmid21947285
  kind: primary_source
  reference: PMID:21947285
  locator: DOI 10.3892/ijo.2011.1206; complete adopted abstract read
  accessed_at: '2026-10-21T18:22:18.650260Z'
  support: context_only
  summary: Original CLL/MEC1 leukemia experiments examine Noxa, apoptosis and proteasome-related
    effects. Host cancer-cell effects do not establish antibacterial mechanism.
  snapshot_sha256: 8265e6d4d9c64c53daf66022d11add7456645ec63e9159756af9387110de3424
- evidence_id: pmid22226089
  kind: primary_source
  reference: PMID:22226089
  locator: DOI 10.1017/s146114571100188x; complete adopted abstract read
  accessed_at: '2026-10-21T18:22:18.650260Z'
  support: context_only
  summary: Original mouse cortex/neuron study concerns chronic hyperforin and TRPC6/CREB/TrkB-associated
    neurobiology, not bacterial activity.
  snapshot_sha256: 8265e6d4d9c64c53daf66022d11add7456645ec63e9159756af9387110de3424
- evidence_id: pmid22924417
  kind: database
  reference: PMID:22924417
  locator: DOI 10.2174/156800913804486601; complete adopted abstract read
  accessed_at: '2026-10-21T18:22:18.650260Z'
  support: context_only
  summary: Secondary review of antileukemic mechanisms; it is not relabeled as primary
    evidence.
  snapshot_sha256: 8265e6d4d9c64c53daf66022d11add7456645ec63e9159756af9387110de3424
- evidence_id: pmid23149561
  kind: primary_source
  reference: PMID:23149561
  locator: DOI 10.1038/jcbfm.2012.164; complete adopted abstract read
  accessed_at: '2026-10-21T18:22:18.650260Z'
  support: context_only
  summary: Original rat cerebral ischemia/neuroprotection study evaluates TRPC6 degradation.
    Host protection is not bacterial target evidence.
  snapshot_sha256: 8265e6d4d9c64c53daf66022d11add7456645ec63e9159756af9387110de3424
- evidence_id: pmid23270309
  kind: primary_source
  reference: PMID:23270309
  locator: DOI 10.1021/ja312150d; complete adopted abstract read
  accessed_at: '2026-10-21T18:22:18.650260Z'
  support: context_only
  summary: Original enantioselective total synthesis, followed to the full accepted
    manuscript and selected supplementary identity pages below.
  snapshot_sha256: 8265e6d4d9c64c53daf66022d11add7456645ec63e9159756af9387110de3424
- evidence_id: pmid23811220
  kind: primary_source
  reference: PMID:23811220
  locator: DOI 10.1016/j.ejpb.2013.06.016; complete adopted abstract read
  accessed_at: '2026-10-21T18:22:18.650260Z'
  support: context_only
  summary: Original 11-volunteer skin study uses a hyperforin-rich cream and placebo
    to examine radical formation and skin lipids. Formulated extract and human endpoints
    are not pure-compound antibacterial assays.
  snapshot_sha256: 8265e6d4d9c64c53daf66022d11add7456645ec63e9159756af9387110de3424
- evidence_id: pmid24033566
  kind: primary_source
  reference: PMID:24033566
  locator: DOI 10.1111/cpr.12060; complete adopted abstract read
  accessed_at: '2026-10-21T18:22:18.650260Z'
  support: context_only
  summary: Original mouse embryonic stem-cell/fibroblast differentiation and toxicity
    study; it establishes neither bacterial mechanism nor general safety.
  snapshot_sha256: 8265e6d4d9c64c53daf66022d11add7456645ec63e9159756af9387110de3424
- evidence_id: pmid24121871
  kind: primary_source
  reference: PMID:24121871
  locator: DOI 10.1007/s00592-013-0518-2; complete adopted abstract read
  accessed_at: '2026-10-21T18:22:18.650260Z'
  support: context_only
  summary: Original rat/human islet study distinguishes Hypericum extract and hyperforin
    in cytokine protection. These host endpoints do not support antibacterial targets.
  snapshot_sha256: 8265e6d4d9c64c53daf66022d11add7456645ec63e9159756af9387110de3424
- evidence_id: primary2013
  kind: primary_source
  reference: https://dash.harvard.edu/server/api/core/bitstreams/7312037d-1e72-6bd4-e053-0100007fdf3b/content
  locator: Full accepted manuscript scientific text; actual Schemes 1 and 3 viewed
  accessed_at: '2026-10-21T18:26:20.952357Z'
  support: supports
  summary: The original reports an 18-step enantioselective synthesis of natural hyperforin
    and distinguishes prior ent-hyperforin synthesis. It identifies the natural source
    as Hypericum perforatum and provides exact structure drawings. This is an author-repository
    accepted version, not falsely labeled the final typeset version. Its introductory
    TRPC6 account is not adopted as an antibacterial target.
  snapshot_sha256: e212f31a095dd9c11621d87d2d0253077458233f161217c99ddd331a3ca941de
- evidence_id: primary2013-si
  kind: primary_source
  reference: https://ndownloader.figshare.com/files/4094722
  locator: Selected SI S24–S30 identity, conversion and comparison sections; actual
    S26/S28 structure pages viewed
  accessed_at: '2026-10-21T18:27:02.293945Z'
  support: supports
  summary: S24 names O-methylhyperforin 21 with 7S configuration; S26 demethylates
    21 to hyperforin 1 without altering that carbon. The isolated synthetic product
    is 40.0 mg and has [α]D23 +39.5 (c3.02,EtOH), compared by the authors with historical
    natural +41 (18°C,c5,EtOH). S29–S30 compare proton/carbon data with published
    natural and synthetic ent material. S28 explicitly discusses water/concentration-dependent
    keto-enol behavior. This supports the natural-series identity, without claiming
    rotation alone proves absolute configuration or independently reassigning raw
    spectra.
  snapshot_sha256: c69e25927964e24ebef6e888bb47748043d4ea2260634fa62469cfae32e548d9
- evidence_id: primary2025
  kind: primary_source
  reference: PMID:41222309; DOI:10.1128/aac.01007-25
  locator: Selected exact-material Methods, MIC Table 1, associated results and mechanistic
    discussion
  accessed_at: '2026-10-21T18:23:05.438399Z'
  support: supports
  summary: The original uses hyperforin from Henan Chemical Co., CAS11079-53-1, dissolved
    in methanol; no lot-specific purity or independent stereochemical analysis is
    stated in the inspected methods. Broth microdilution uses CAMHB, approximately
    0.5 McFarland suspension,100µL suspension plus100µL drug and 37°C for18–20h, with
    visible-growth MIC. The final viable inoculum was not independently established.
  snapshot_sha256: 1e2d827a13958889daaa1226c97948d6231bc3d74fa98660d02a6b9ba61fc7f4
- evidence_id: primary2025-activity
  kind: primary_source
  reference: PMID:41222309
  locator: Table 1 exact hyperforin-alone column and A.baumannii FADDI-AB065 discussion
  accessed_at: '2026-10-21T18:23:05.438399Z'
  support: supports
  summary: The original reports hyperforin MIC 0.25 mg/L against the authors’ LPS-deficient
    FADDI-AB065, whereas most panel isolates are >128 mg/L and some other isolates
    have finite higher values. This supports a bounded antibacterial role, not species-wide
    potency. The AB065 combination FICI is 2.0, not synergy. Combination permeability/ROS
    observations do not establish hyperforin binding to peptidoglycan or a particular
    intracellular target.
  snapshot_sha256: 1e2d827a13958889daaa1226c97948d6231bc3d74fa98660d02a6b9ba61fc7f4
- evidence_id: primary2025-limits
  kind: primary_source
  reference: PMID:41222309
  locator: Source discrepancies and experiment boundaries in selected main
  accessed_at: '2026-10-21T18:23:05.438399Z'
  support: context_only
  summary: The article uses both <0.5 and ≤0.5 synergy cutoffs and its prose ATCC
    13883 FICI differs from Table 1. Censored hyperforin MICs are substituted for
    some calculations. No numerical combination, time-kill or biofilm result is imported
    into native activity_spectrum; figures and supplementary experiments were not
    independently inspected. These limits do not erase the exact monotherapy Table
    1 result.
  snapshot_sha256: 1e2d827a13958889daaa1226c97948d6231bc3d74fa98660d02a6b9ba61fc7f4
- evidence_id: primary2014
  kind: primary_source
  reference: PMID:25511254; DOI:10.1038/srep07500
  locator: Selected original Results, Chemicals, electrophysiology and lipid-bilayer
    Methods; figure captions
  accessed_at: '2026-10-21T18:23:05.435298Z'
  support: context_only
  summary: The original compares hyperforin-DCHA salt with free acid in methanol and
    demonstrates TRPC6-independent proton currents in mammalian cells and protein-free
    lipid bilayers. The inspected results include free-acid microglial experiments,
    while other experiments use salt preparations. This is direct biophysical protonophore
    evidence in the tested systems, not a directly demonstrated bacterial molecular
    target; its antibiotic-mechanism extension is explicitly discussed as a possibility.
    No figure-derived numerical endpoint is asserted from unread images.
  snapshot_sha256: 67912924a439d23e9163ce34a2802cc67bd27ae4c226ee5f9524dc92a5d23abb
- evidence_id: excluded2012
  kind: primary_source
  reference: PMID:22170780
  locator: Selected complete isolation/methods and compound scope in PMC3339047
  accessed_at: '2026-10-21T18:24:07.808577Z'
  support: context_only
  summary: The paper tests seven metabolites from H.densiflorum,H.ellipticum,H.prolificum
    and H.punctatum. Its discussion references hyperforin, but those compounds and
    their pooled MIC ranges are not treated as exact hyperforin assays.
  snapshot_sha256: d3592875119cd1151578d42f7e581a9df69d8107595ed65692f3daf167a8729c
- evidence_id: historical1999
  kind: database
  reference: PMID:10382704; DOI:10.1016/S0140-6736(99)00214-7
  locator: Original metadata/title only; no indexed abstract and publisher full text
    403
  accessed_at: '2026-10-21T18:23:05.443633Z'
  support: context_only
  summary: The title is a relevant original antibacterial lead, but the experimental
    table/material details were not accessed. PMID 10475223 is a later comment, not
    a substitute assay source. No historical MIC is inferred from review quotations
    or title alone.
  snapshot_sha256: 2b103eabd3033142e30d33ddf93bb6f987f4156a1186fbd16b088a844086356f
- evidence_id: access
  kind: validation
  reference: /private/tmp/am-review-session/543-fetch1.json
  locator: Recorded public retrieval attempts and successful alternatives in 543-fetch1
    through 543-fetch8
  accessed_at: '2026-10-21T18:31:27Z'
  support: context_only
  summary: HMDB returned 403, CAS 401 and DrugBank 403; Reaxys free primary registry
    content remained unavailable. DrugBank is a drug-level association, not exact-structure
    equivalence. Original 1983 archive requests failed; direct ACS main/SI routes
    were 403 and Harvard download routes 429, but the legitimate Harvard repository
    API and verified ACS Figshare file supplied the 2013 originals. Wikipedia resolves
    as a document reference only.
  snapshot_sha256: 0e42c15157de801c66d50c613d5c6a86299c126ed8e43c323ee337deb6cf117d
- evidence_id: adapter
  kind: search
  reference: /private/tmp/am-review-session/543-adapter-scope.json
  locator: Native applicability assessed before open-ended literature follow-up
  accessed_at: '2026-10-21T18:31:27Z'
  support: context_only
  summary: No native gene, protein, regulator, pathway or transcriptomic assertion
    requires a structured query. The producer plant is not a covered bacterial expression
    dataset; later host-mechanism discovery does not become a native assertion.
  snapshot_sha256: d4b47cf8dc65d3b333e1ad77867a652df96677d55723f37183fdb3e1726f7b7d
  search_scope: Entire native 543 plus preserved official shared adapter catalog 456460-adapter-catalog.txt;
    applicability recorded before web retrieval.
assessments:
- assessment_id: identity
  area: identity
  topic: Neutral natural-series hyperforin graph and names
  outcome: supported
  summary: Composition, charge, mass and four configured centres are coherent. Accurate
    CIP validates both systematic synonyms, and the adopted synthesis plus supplementary
    natural-product comparison supports the retained series. No wrong-native-identity
    conclusion follows from the erroneous CCD link.
  target_ids:
  - CHEBI:5834
  evidence_ids:
  - native
  - chebi
  - mapping
  - primary2013
  - primary2013-si
- assessment_id: grounding
  area: grounding
  topic: Exact chemical xrefs versus drug/document associations
  outcome: concern
  summary: PDB CCD HYF is a confirmed C7 epimer across descriptors and both coordinate
    sets, so its exact xref is invalid for this graph. KEGG and KNApSAcK molecular
    encodings match; the latter’s printed key is separately inconsistent. DrugBank
    is drug-level and Wikipedia a document; inaccessible registry content is unresolved
    rather than falsely verified.
  target_ids:
  - CHEBI:5834
  evidence_ids:
  - ccd
  - single-inversion
  - ccd-coordinates
  - kegg
  - knapsack
  - pubchem
  - access
- assessment_id: classification
  area: grounding
  topic: Broader ring classes and unresolved sesquarterpenoid boundary
  outcome: unknown
  summary: The cyclic terpene ketone and carbobicyclic classes fit the retained ring/ketone
    graph. CHEBI:51961 requires sesquarterpene derivation, which carbon count alone
    does not prove. The inspected synthesis describes a polyketide-derived acylphloroglucinol
    core and terpene side chains; its relationship to the asserted biosynthetic parent
    needs separate ontology/source adjudication. No confirmed additional correction
    is inferred.
  target_ids:
  - CHEBI:5834
  evidence_ids:
  - native
  - term36130
  - term36785
  - term51961
  - primary2013
- assessment_id: activity
  area: evidence
  topic: Antibacterial role and exact assay boundaries
  outcome: supported
  summary: The inspected 2025 original supplies hyperforin-alone bacterial growth
    inhibition under specified conditions, including the exceptional LPS-deficient
    AB065 strain. It supports the qualitative role without generalizing combination
    synergy or host pharmacology to antibacterial mechanism.
  target_ids:
  - CHEBI:5834
  evidence_ids:
  - role
  - primary2025
  - primary2025-activity
  - primary2025-limits
- assessment_id: completeness
  area: completeness
  topic: All adopted leads and optional biological representation
  outcome: unknown
  summary: All ten adopted abstracts were read, including two recognized secondary
    reviews; the 2013 original was followed to full main and selected SI identity
    sections. Direct protonophore behavior has been studied outside bacterial cells,
    but no bacterial target is established by the inspected work. Missing optional
    targets, causal graphs and quantitative observations are not a required correction.
  target_ids:
  - CHEBI:5834
  evidence_ids:
  - pmid12578355
  - pmid16973193
  - pmid21947285
  - pmid22226089
  - pmid22924417
  - pmid23149561
  - pmid23270309
  - pmid23811220
  - pmid24033566
  - pmid24121871
  - primary2014
  - excluded2012
  - historical1999
  - adapter
- assessment_id: provenance
  area: provenance
  topic: Source-owned content and unchanged captures/history
  outcome: supported
  summary: The complete source row, all native history events and maintained extraction/seeding
    ownership were checked. Original 13 and expanded 21 input hashes remain unchanged;
    the review does not promote SEEDED status.
  target_ids:
  - CHEBI:5834
  evidence_ids:
  - native
  - owners
  - search
findings:
- finding_id: F1
  issue_key: hyperforin-pdb-ccd-hyf-c7-epimer-xref
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: PDB CCD HYF encodes the C7 epimer rather than the native exact structure
  description: Native xrefs[4] asserts exact chemical equivalence to HYF. Current
    HYF descriptors and independently reconstructed model/ideal coordinates give IWBJJCOKGLUQIZ-OJCNYLSASA-N,
    while native is IWBJJCOKGLUQIZ-HQKKAZOISA-N. Inverting only native atom 8 (systematic
    bicyclo C7S to R; CCD atom C33) reproduces HYF with reciprocal chirality-aware
    matches. Correct the maintained exact-link handling without replacing the supported
    native hyperforin graph or dismissing the separate human-PXR experiment as nonexistent.
  target_ids:
  - CHEBI:5834
  field_paths:
  - xrefs[4]
  evidence_ids:
  - native
  - owners
  - ccd
  - mapping
  - single-inversion
  - ccd-coordinates
  - primary2013-si
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Actual imported ChEBI chemical-xref inventory
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI extraction and exact-xref adjudication
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated chemical-xref field owner
  rule_id: review-checklist:Equivalence
  native_severity: major
  normalization_reason: The retained native identity is supported, but one asserted
    exact cross-reference denotes a different stereoisomer; this is a major grounding
    error rather than a blocker in the native molecular graph.
actions:
- action_id: A1
  description: Adjudicate the HYF exact xref in maintained ChEBI extraction/inventory
    handling and regenerate the native field.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:5834
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Actual imported ChEBI chemical-xref inventory
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI extraction and exact-xref adjudication
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated chemical-xref field owner
  generator: scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  acceptance_checks:
  - Retain the supported native composition and four configured centres; remove or
    appropriately qualify HYF as an exact chemical link unless a corrected upstream
    component is independently verified.
  - Compare full stereo-aware graphs, including native atom 8/systematic C7 and CCD
    C33; do not use the shared first InChIKey block or name alone as equality.
  - Do not conflate the exact xrefs rule with drug_xrefs, and do not replace native
    with the unasserted alternate PubChem tautomer automatically.
  - Rerun native schema/strict, exact chemical comparison and required corpus/reference/history
    gates; demonstrate that re-seeding preserves the adjudication.
- action_id: A2
  description: Optional mechanism or activity enrichment must preserve experimental
    material and system boundaries.
  finding_ids: []
  target_ids:
  - CHEBI:5834
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/hyperforin.yaml
    role: Future validated curator-owned primary literature annotations
  acceptance_checks:
  - For bacterial activity retain the named preparation, strain, CAMHB conditions,
    visible-growth endpoint, 18–20 h and printed mg/L units; do not generalize AB065
    to all A.baumannii.
  - For protonophore claims distinguish free acid from DCHA salt, protein-free membranes
    from mammalian cells and hypotheses about bacterial action from directly tested
    mechanisms.
  - Resolve original 1999 table and 1983 absolute-configuration paper access before
    claiming those originals were fully adjudicated; do not import seven unrelated
    2012 metabolite values.
limitations:
- All ten adopted abstracts were read. Beyond abstracts, the 2013 accepted manuscript
  and selected SI identity/conversion/comparison pages were inspected; the other adopted
  host-pharmacology papers were not exhaustively audited at full experimental depth.
- CHEBI:51961 sesquarterpenoid remains an unresolved biosynthetic classification boundary.
  The retained C35 composition is not treated as proof of seven-isoprene-unit ancestry;
  direct biosynthesis and the ontology scope require separate adjudication.
- The 1983 original absolute-configuration paper and 1999 antibacterial experimental
  table were inaccessible through the attempted free routes. The 2013 synthesis and
  current authority comparisons supply independent bounded identity support; no claim
  of raw diffraction or raw NMR reanalysis is made.
- The 2025 original was read selectively for exact reagent, MIC Table 1, associated
  results and mechanism scope. Figures and supplementary assays were not independently
  viewed, reagent purity/stereo was not remeasured, and source FICI discrepancies
  preclude unqualified quantitative transfer.
- HMDB 403, CAS 401, DrugBank 403 and unavailable independent Reaxys content limit
  registry verification. KNApSAcK’s displayed key conflicts with its matching molecular
  encodings. The HYF coordinate check concerns the deposited model, not a new protein
  crystallographic refinement.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All original 13 and expanded 21 local input hashes were rechecked unchanged before
  draft writing. No native/source/history/progress/saved-bundle/Git writes occurred.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
