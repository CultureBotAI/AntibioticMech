# Furanomycin: coherent natural stereochemistry with bounded activity and substrate evidence

- Review: 20261021T171448Z-furanomycin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T16:59:12Z
- Finished UTC: 2026-10-21T17:14:48Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native (2S,2′R,5′S) amino-acid structure agrees with current authorities and inspected primary synthesis/isolation drawings. No confirmed native defect was found. Original evidence distinguishes culture-filtrate inhibition from purified-fraction activity, and IleRS substrate charging from a simple enzyme-inhibitor mechanism. The proposed downstream toxicity mechanism and unresolved accession/full-text limits are retained. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 482; original thirteen hashes preserved within twenty-one captured inputs, with readiness and seven guidance/contract files appended.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:79390 | data/antibiotics/antibacterial/furanomycin.yaml | generated | furanomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:79390 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:79390 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:79390 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:79390 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:79390 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:79390 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:79390 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:79390 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:79390 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:79390 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:79390 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:79390 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact amino-acid graph and stereochemical names

identity: supported. Targets: CHEBI:79390.

Native alpha 2S/ring 2′R/ring 5′S agrees with the original 2000 final synthesis and 2013 Figure 5, current ChEBI and independent PubChem graph. The 2013 isolate assignment uses literature comparison rather than an independent optical/crystal absolute determination.

### Ontology and external-reference scope

grounding: unknown. Targets: CHEBI:79390.

Structural parents and antibacterial/antimicrobial roles are coherent. CAS has exact-key database corroboration, while direct CAS and Reaxys authority access remains unavailable. Wikipedia resolves as a document topic and is not primary scientific evidence.

### Purified material versus culture-filtrate measurements

evidence: supported. Targets: CHEBI:79390.

The 2013 study follows antibacterial activity through purification and reports final-fraction inhibition of D. dadantii 1447, supporting antibacterial eligibility. Its six-strain quantitative table and amino-acid reversal are culture-filtrate measurements. They cannot be recast as pure-compound MICs or species-wide sensitivity.

### IleRS substrate charging and proposed downstream toxicity

evidence: supported. Targets: CHEBI:79390.

Original 1990 experiments support enzyme binding, furanomycyl-tRNA formation, binding of charged tRNA to the tested EF-Tu complex, and authors’ evidence for incorporation in a cell-free protein assay. Furanomycin is an unnatural substrate in this chain; a simple IleRS-inhibition label loses crucial evidence. Protein dysfunction causing antibacterial toxicity is proposed, not experimentally closed here. No native mechanism assertion is contradicted.

### 2012 C. elegans citation

scope: supported. Targets: CHEBI:79390.

The original figure resolves why this source appears among adopted leads: furanomycin is listed as a contextual tRNA-synthetase-associated toxin. Its presence is not evidence that furanomycin was one of the plotted worm-aversion treatments or that its bacterial mechanism was directly studied there.

### Bounded source organism follow-up

evidence: supported. Targets: CHEBI:79390.

The 2013 original supports production by source-identified P. fluorescens SBW25. Its claims about earlier S. threomyceticus/ATCC 15795 production cite prior work; the inaccessible 1967 original is not represented as independently read. No native producer collection requires correction.

### No inferred resistance or clinical phenotype

scope: unknown. Targets: CHEBI:79390.

Filtrate-insensitive strains and amino-acid rescue do not establish a furanomycin resistance determinant, clinical breakpoint or clinical efficacy. No native resistance/clinical product assertion exists.

### All adopted leads and optional annotations

completeness: unknown. Targets: CHEBI:79390.

All five adopted leads were disposed at their recorded reading depths. Optional activity_spectrum, molecular_targets, producer or causal_graphs enrichment is possible with exact material/assay boundaries; absent optional collections are not required-schema defects.

### Maintained ownership and history

provenance: supported. Targets: CHEBI:79390.

The entire native/raw rows, source configuration/owners and all four history events were inspected. Twenty-one captured input hashes preserve the original thirteen, and SEEDED status remains unchanged.

### Deterministic molecular and native validation

schema: supported. Targets: CHEBI:79390.

Schema, strict, source mint and independent chemistry checks pass; these are distinguished from primary-source scientific assessment.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optional future curation can add the original substrate-to-incorporation evidence and bounded activity/producer context.

- Keep E. coli IleRS/tRNA distinct from T. thermophilus HB8 EF-Tu/EF-Ts. Verify any specific protein example against the original construct and reviewed authority rather than substituting an adapter hit.
- Preserve binding versus substrate charging, low-versus-high enzyme concentration, cell-free incorporation evidence and the proposed nature of protein dysfunction/toxicity. Do not flatten this chain into a generic IleRS-inhibition claim.
- Do not convert 2013 culture-filtrate zone areas or 10 mM amino-acid rescue into purified-compound MICs; preserve D. dadantii 1447 purified-fraction activity separately.
- Use claim-level citations and material-qualified observations; any native curation/status event requires separately authorized work and all required gates.

### A2

Optional access follow-up can resolve legacy authority and original source limits.

- Inspect exact CAS and Reaxys structures when public authority access permits; no identifier removal is justified merely by 401/403.
- Obtain the 1967 original if its historical producer/assay details are to be curated. The 2012 figure’s contextual listing is not a furanomycin experiment and does not replace the 1990 original.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/furanomycin.yaml; Entire native record and all four seed/reseed events | supports | CHEBI:79390 is a SEEDED, EXACT antibacterial amino acid with neutral C7H11NO3, three defined centres, five exact synonyms, two structural parents and antimicrobial/antibacterial roles. Its native exact xrefs are CAS 18455-25-9 and Reaxys 5254308; Wikipedia is a document link. No target, mode, causal graph, activity observation, resistance determinant, producer collection, FDA assertion or dataset is present. |
| owner | data/raw/chebi_antimicrobials.tsv; curation/record_review_queue.tsv; Entire exact ChEBI raw row 2036 and readiness row 1283 | supports | The source row reproduces the native structure/definition/synonyms/roles and adopts five PMID leads. The maintained source, extraction/seeding ownership and readiness context were inspected before detailed judgment. No curator or decision override was found by complete exact-row inspection. |
| search | 482-local-hits.txt; Initial hidden/ignored-inclusive worktree search and exact maintained TSV inspection | context_only | The initial search covered hidden and ignored worktree files except .git and .venv. Actual source/readiness rows were read; historical research ledgers and rendered pages were only discovery leads. Complete curator and decision TSV inspection found no exact target override. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/79390/; Current CHEBI:79390 identity, definition, structure, synonyms, relations and citations | supports | Current ChEBI retains the native (2S,2′R,5′S) structure, key PNOKUGWGMLEAPE-JKUQZMGJSA-N and neutral formula. The stated amino-acid/dihydrofuran definition and exact names align with that graph. |
| chemistry | 482-chemistry.json; RDKit 2026.03.5 using the 019 interpreter against 049 cwd | supports | Independent SMILES/InChI parsing reproduces native formula, charge, one fragment, both masses and key. Atom 1 is the S amino-acid alpha centre, atom 0 is ring 2′R and atom 8 is ring 5′S in the SMILES atom map. The source mint reproduces antibioticmech:chebi-bc629452ae. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/furanomycin/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON; Name query CID 73423 property response | supports | Current PubChem name resolution independently agrees with the complete native structure and stereochemical key. It is an auxiliary authority lookup, not an additional asserted native xref. |
| cas | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/18455-25-9/property/InChI,InChIKey/JSON; CAS 18455-25-9 name lookup in PubChem | context_only | The exact CAS string resolves to CID 73423 and the same stereochemical key. This corroborates the association at database tier; direct Common Chemistry authority access returned 401, so that registration was not independently inspected. |
| mapping | 481482-xref-check.json; Independent native versus PubChem graph comparison | supports | The three assigned native centres are R,S,S at zero-based atoms 0,1,8, respectively; these map to ring 2′R, alpha 2S and ring 5′S. PubChem agrees exactly. Neutral representation does not assert the predominant solution protonation state at every pH. |
| term-51659 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/51659/; CHEBI:51659 current label and definition | supports | The retained term resolves to dihydrofuran; its structural or activity scope is coherent with the native graph and inspected original evidence. No unsupported parent/role correction is inferred from absent optional annotations. |
| term-83822 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/83822/; CHEBI:83822 current label and definition | supports | The retained term resolves to non-proteinogenic L-alpha-amino acid; its structural or activity scope is coherent with the native graph and inspected original evidence. No unsupported parent/role correction is inferred from absent optional annotations. |
| term-33281 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/33281/; CHEBI:33281 current label and definition | supports | The retained term resolves to antimicrobial agent; its structural or activity scope is coherent with the native graph and inspected original evidence. No unsupported parent/role correction is inferred from absent optional annotations. |
| term-33282 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/33282/; CHEBI:33282 current label and definition | supports | The retained term resolves to antibacterial agent; its structural or activity scope is coherent with the native graph and inspected original evidence. No unsupported parent/role correction is inferred from absent optional annotations. |
| wikipedia | https://en.wikipedia.org/wiki/Furanomycin; Resolved Furanomycin topic page | context_only | The asserted document link resolves to the intended compound topic. It is not used as primary evidence for stereochemistry, producer taxonomy, activity or mechanism. |
| adopted | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A%2810814415%20OR%202182633%20OR%2022500807%20OR%2023688329%20OR%204861779%29%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=100; All five adopted PMID leads; complete available abstracts and bibliographic metadata | supports | PMID 4861779 is the 1967 original antibiotic report, DOI 10.1021/jm00318a035; metadata resolves but no abstract/full text was accessible. PMID 10814415, DOI 10.1021/ol005569j, reports asymmetric (+)-furanomycin synthesis, with original SI inspected below. PMID 2182633, DOI 10.1016/S0021-9258(19)39239-7, is the 1990 IleRS charging/incorporation study, whose original public text was read. PMID 23688329, DOI 10.1186/1471-2180-13-111, is the 2013 SBW25 isolation/activity study, read in full main XML. PMID 22500807, DOI 10.1016/j.cell.2012.02.050, concerns C. elegans surveillance/aversion; actual Figure 2A provides only contextual furanomycin listing. |
| synthesis | https://ndownloader.figshare.com/files/5827437; Original DOI 10.1021/ol005569j SI experimental procedures; final compound 1 p3 drawing actually viewed | supports | The asymmetric synthesis isolates the amino acid after TFA deprotection, basic ion-exchange work-up and crystallization. Final compound 1 has the same stereochemical drawing as native, and optical rotation +139 (c 1, H2O), compared with original 1967 and corrected 1980 literature values. The procedure supplies identity evidence, not an antibacterial assay. The final graph has no retained TFA counterion; the MS [M+H]+ is an analytical ion. |
| isolation | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3662646/fullTextXML; Full 2013 original main text; purification/identification, Figure 5, Tables 1–2 and methods | supports | The authors isolate 3.7 mg from material corresponding to approximately 600 mL of P. fluorescens SBW25 culture filtrate. HRESIMS and NMR identify C7H11NO3; the main text assigns (2S,2′R,5′S) by comparison with literature and synthetic diastereomers. Glycerol contamination prevents an accurate optical rotation, so this is not an independent optical absolute-hand determination. A final purified-fraction aliquot inhibits D. dadantii 1447. Table 2, however, measures culture-filtrate inhibition-zone areas, not pure-compound MICs. The filtrate panel has six sensitive strains: B. megaterium K2; D. dadantii X179/1447; E. amylovora 153; and P. syringae maculicola M4/tomato DC3000. |
| structure-figure | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/9c1a/3662646/41202c06a991/1471-2180-13-111-5.jpg; Actual Figure 5 molecular drawing | supports | The primary drawing is consistent with the native alpha 2S/ring 2′R/ring 5′S graph and the independently inspected 2000 final synthesis drawing. Its agreement is not treated as a direct crystal determination or proof that achiral NMR alone distinguishes enantiomers. |
| activity-method | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3662646/fullTextXML; 2013 Methods: culture filtrate production and agar diffusion; Results amino-acid reversal | supports | Seven-day cultures provide sterile filtrate. Indicator strains are grown in LB, adjusted to OD600 0.2 (E. coli 0.8), and 300 µL spread on 925 Minimal Medium plates. A 300 µL filtrate aliquot enters the central well; incubation is 48 h at 28°C, with triplicates and repeat experiments for sensitive strains. D. dadantii 1447 inhibition is reversed by 10 mM isoleucine, leucine or valine, but not glutamine/alanine; serine gives ambiguous reduced-density zones excluded from statistics. These are filtrate rescue experiments, not proof of a unique purified-compound target or a clinical breakpoint. |
| enzyme-method | https://www.researchgate.net/publication/20972689_Nonprotein_amino_acid_furanomycin_unlike_isoleucine_in_chemical_structure_is_charged_to_isoleucine_tRNA_by_isoleucyl-tRNA_synthetase_and_incorporated_into_protein; Original 1990 public author-copy text p 6931; Materials and binding/NMR methods | supports | The actual original source text identifies furanomycin supplied by Shionogi, E. coli IleRS and tRNAIle, and separately T. thermophilus HB8 EF-Tu/EF-Ts. The latter proteins must not be relabelled E. coli. Ligand binding is measured by TNS fluorescence at 37°C, pH 7.0; transferred-NOE NMR examines bound conformation. This is inspected original text delivered by a public author-copy page; direct publisher PDFs returned 403. |
| charging | https://doi.org/10.1016/S0021-9258(19)39239-7; Original 1990 text pp 6932–6933; aminoacylation methods and results surrounding Figures 6–7 | supports | Furanomycin binds IleRS with reported Kd 0.031 mM versus 0.010 mM for isoleucine. The authors use a back-titration/acetylation assay because labelled furanomycin is unavailable. At low IleRS concentration, furanomycyl-tRNA formation is slower than isoleucyl-tRNA; at higher enzyme concentration, charging is comparably efficient. These are substrate recognition and charging results, not a generic inhibition IC50 or measured bacterial MIC. |
| incorporation | https://doi.org/10.1016/S0021-9258(19)39239-7; Original 1990 text pp 6934–6935; ternary complex, Figure 8 description and Discussion | supports | Furanomycyl-tRNA binds the tested EF-Tu.GTP complex with affinity similar to isoleucyl-tRNA. An E. coli S30/pAT153 cell-free reaction lacking isoleucine regains a beta-lactamase-precursor band when 10 mM furanomycin is supplied; the authors interpret the control/NMR-purity evidence as incorporation in place of isoleucine. This is not residue-resolved mass spectrometry. The Discussion proposes that bulky substituted residues disturb protein conformation/function and cause toxicity; that downstream mechanism is a hypothesis, not directly measured in this experiment. No whole-cell kill kinetics or resistance mechanism is established. |
| host-study | https://pmc.ncbi.nlm.nih.gov/articles/PMC3613046/?pdf=1; Original 2012 abstract, relevant Results/Methods and Figure 2 caption | context_only | The inspected experiment concerns C. elegans aversion and immune/detoxification responses to disruption of core host processes. The actual tested drugs in the main aversion experiment are other compounds. It supplies no direct furanomycin bacterial potency or furanomycin-specific worm endpoint in the inspected main text. |
| host-figure | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/f8bf/3613046/0d3da176f8e3/nihms366225f2.jpg; Actual 2012 Figure 2A–C viewed | context_only | Furanomycin appears in panel A among examples associated with tRNA synthetases, with a prokaryote/eukaryote cross-specificity footnote. Panels B/C test zeocin, antimycin A, tunicamycin, bortezomib, geneticin, paraquat and concanamycin A; furanomycin is not among those plotted drugs. This contextual list cannot substitute for the 1990 specific substrate/charging experiments. |
| adapter | kg-microbe-sources imodulondb search --organism e_coli --dataset precise1k --query ileS; iModulonDB e_coli/precise1k search ileS after covered-dataset catalog | context_only | Before open mechanistic follow-up, the successful adapter read returned e_coli/precise1k/b0026 ileS, isoleucine--tRNA ligase, and zero iModulons. The first sandbox attempt failed DNS; a public read succeeded. This annotation does not identify the exact original 1990 construct or independently prove binding, charging or toxicity. |
| access | 481482-fetch6.json; Recorded public retrieval successes and failures | context_only | The original 1967 ACS page returned 403; its metadata alone was inspected. Direct 1990 JBC routes returned 403, but public author-copy original text was available. The 2000 main paper was read at abstract depth, with final experimental SI and drawing independently inspected. 2012 full XML returned 500; its PMC HTML and Figure 2 were readable. Supplementary PDF retrieval returned a download challenge and EuropePMC supplementary route explicitly said the article was not open access. Common Chemistry returned 401 and Reaxys 5254308 returned 403. |
| gates | 482-focused-results.json; Actual chemistry/schema/strict results | supports | All focused executions exited 0. Native validators used 049 own environment; RDKit used 019 interpreter with 049 cwd. Exact source-id mint and all internal chemical representations agree. |

## Limits And Additional Notes

- Root attaches shared required corpus/QC/contract regression checks for the unchanged base; this draft records actual focused checks only.
- The 2013 main XML was read in full, including exact methods and table scope, and Figure 5 was visually inspected. NMR spectra were not independently reprocessed. The paper explicitly could not measure accurate optical rotation because of glycerol contamination.
- The 2000 original abstract and three-page experimental SI were read; final compound 1 drawing was visually inspected. The main article and all raw supplementary spectra were not fully audited. The 1967 original remains metadata-only after publisher 403.
- The 1990 original text was inspected through a public author-copy transcription because publisher PDFs returned 403. Methods, results and relevant figure descriptions were read; original plot pixels and raw spectra were not inspected, so no new graphical measurement or reanalysis is claimed.
- The 2012 original HTML relevant sections and actual Figure 2 were inspected. Supplementary files were inaccessible through a PMC download challenge and non-open-access EuropePMC response. No furanomycin-specific uninspected supplementary assay is inferred.
- CAS 18455-25-9 has exact-key PubChem corroboration, but the authoritative registration and Reaxys 5254308 remain unverified after 401/403.
- The source-supported activity observations do not establish clinical efficacy, species-wide spectrum, a pure-compound MIC table for the 2013 strains, or an experimentally complete whole-cell toxicity chain.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native or maintained file was edited. All twenty-one input hashes and original thirteen capture entries were rechecked; optional links/tags/notes are specific to furanomycin.
- Source manifests retain actual URLs, UTC access times, hashes and failed responses. No module-level evidence was inferred from the adapter’s zero iModulon result.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T171448Z-furanomycin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Furanomycin: coherent natural stereochemistry with bounded activity and substrate
  evidence'
started_at: '2026-10-21T16:59:12Z'
finished_at: '2026-10-21T17:14:48Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
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
summary: The native (2S,2′R,5′S) amino-acid structure agrees with current authorities
  and inspected primary synthesis/isolation drawings. No confirmed native defect was
  found. Original evidence distinguishes culture-filtrate inhibition from purified-fraction
  activity, and IleRS substrate charging from a simple enzyme-inhibitor mechanism.
  The proposed downstream toxicity mechanism and unresolved accession/full-text limits
  are retained. Scientific assessment retains the stated evidence limits; full verification
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
  - path: data/antibiotics/antibacterial/furanomycin.yaml
    sha256: 1adf925481beaff7dc5fcee7fc686e1a51285ec7692eade9256c94aa75ce1308
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
- target_id: CHEBI:79390
  path: data/antibiotics/antibacterial/furanomycin.yaml
  label: furanomycin
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
  selection: Queue position 482; original thirteen hashes preserved within twenty-one
    captured inputs, with readiness and seven guidance/contract files appended.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:79390
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:79390
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    482
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:79390
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/furanomycin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:79390
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/furanomycin.yaml --out /private/tmp/am-review-session/482-strict.tsv
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
  - CHEBI:79390
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
  - CHEBI:79390
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
  - CHEBI:79390
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
  - CHEBI:79390
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
  - CHEBI:79390
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
  - CHEBI:79390
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
  - CHEBI:79390
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
  - CHEBI:79390
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
  - CHEBI:79390
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/furanomycin.yaml
  locator: Entire native record and all four seed/reseed events
  accessed_at: '2026-10-21T17:13:24Z'
  support: supports
  summary: CHEBI:79390 is a SEEDED, EXACT antibacterial amino acid with neutral C7H11NO3,
    three defined centres, five exact synonyms, two structural parents and antimicrobial/antibacterial
    roles. Its native exact xrefs are CAS 18455-25-9 and Reaxys 5254308; Wikipedia
    is a document link. No target, mode, causal graph, activity observation, resistance
    determinant, producer collection, FDA assertion or dataset is present.
  snapshot_sha256: 881f755954d1b1b5bbbdea1c93f51bd0197414049e373f5b4f0db661bd17cc3e
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; curation/record_review_queue.tsv
  locator: Entire exact ChEBI raw row 2036 and readiness row 1283
  accessed_at: '2026-10-21T17:13:24Z'
  support: supports
  summary: The source row reproduces the native structure/definition/synonyms/roles
    and adopts five PMID leads. The maintained source, extraction/seeding ownership
    and readiness context were inspected before detailed judgment. No curator or decision
    override was found by complete exact-row inspection.
  snapshot_sha256: 0a1359f443c350a8c43544c5f2382cf03c0b3962088e0f343d0bcf4f8a24c5b7
- evidence_id: search
  kind: search
  reference: 482-local-hits.txt
  locator: Initial hidden/ignored-inclusive worktree search and exact maintained TSV
    inspection
  accessed_at: '2026-10-21T17:13:24Z'
  support: context_only
  summary: The initial search covered hidden and ignored worktree files except .git
    and .venv. Actual source/readiness rows were read; historical research ledgers
    and rendered pages were only discovery leads. Complete curator and decision TSV
    inspection found no exact target override.
  search_scope: rg --no-ignore --hidden target search across the 049 worktree excluding
    .git and .venv; complete maintained TSV exact-row inspection in 481482-context.py.
  snapshot_sha256: 0b8c247143013432099e161498788ab6c3ab1fff2ca694065c960954c608d816
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/79390/
  locator: Current CHEBI:79390 identity, definition, structure, synonyms, relations
    and citations
  accessed_at: '2026-10-21T17:03:11.156658Z'
  support: supports
  summary: Current ChEBI retains the native (2S,2′R,5′S) structure, key PNOKUGWGMLEAPE-JKUQZMGJSA-N
    and neutral formula. The stated amino-acid/dihydrofuran definition and exact names
    align with that graph.
  snapshot_sha256: f57708f73c66dacee77ab43e598655f29cbb29e92bcba63d90fcc6e040756c02
- evidence_id: chemistry
  kind: validation
  reference: 482-chemistry.json
  locator: RDKit 2026.03.5 using the 019 interpreter against 049 cwd
  accessed_at: '2026-10-21T17:13:24Z'
  support: supports
  summary: Independent SMILES/InChI parsing reproduces native formula, charge, one
    fragment, both masses and key. Atom 1 is the S amino-acid alpha centre, atom 0
    is ring 2′R and atom 8 is ring 5′S in the SMILES atom map. The source mint reproduces
    antibioticmech:chebi-bc629452ae.
  snapshot_sha256: 6318fb081fbcd31711e3ce29424c28d16ec8e6d027ce44b3b564f4d75ffd2eb7
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/furanomycin/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON
  locator: Name query CID 73423 property response
  accessed_at: '2026-10-21T17:03:11.361336Z'
  support: supports
  summary: Current PubChem name resolution independently agrees with the complete
    native structure and stereochemical key. It is an auxiliary authority lookup,
    not an additional asserted native xref.
  snapshot_sha256: 9aef06e15cd34c9284b3d5c748826d16a5b471d321034cbc46b33e555e70feec
- evidence_id: cas
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/18455-25-9/property/InChI,InChIKey/JSON
  locator: CAS 18455-25-9 name lookup in PubChem
  accessed_at: '2026-10-21T17:08:43.883055Z'
  support: context_only
  summary: The exact CAS string resolves to CID 73423 and the same stereochemical
    key. This corroborates the association at database tier; direct Common Chemistry
    authority access returned 401, so that registration was not independently inspected.
  snapshot_sha256: 388172e8b73e067685010a984f9e685237a6bceac1315c97444f2c8231bc2c2b
- evidence_id: mapping
  kind: validation
  reference: 481482-xref-check.json
  locator: Independent native versus PubChem graph comparison
  accessed_at: '2026-10-21T17:13:24Z'
  support: supports
  summary: The three assigned native centres are R,S,S at zero-based atoms 0,1,8,
    respectively; these map to ring 2′R, alpha 2S and ring 5′S. PubChem agrees exactly.
    Neutral representation does not assert the predominant solution protonation state
    at every pH.
  snapshot_sha256: 93d7e8c8cd70dba30f52290b24c9cddb59d03e90749a677a4fd5d49f779735e0
- evidence_id: term-51659
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/51659/
  locator: CHEBI:51659 current label and definition
  accessed_at: '2026-10-21T17:03:11.875130Z'
  support: supports
  summary: The retained term resolves to dihydrofuran; its structural or activity
    scope is coherent with the native graph and inspected original evidence. No unsupported
    parent/role correction is inferred from absent optional annotations.
  snapshot_sha256: 371e936688e872c5828902e5dd9f7b8806156a6fcdc18c9d4e9c9b6fd65e3fbb
- evidence_id: term-83822
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/83822/
  locator: CHEBI:83822 current label and definition
  accessed_at: '2026-10-21T17:03:12.281678Z'
  support: supports
  summary: The retained term resolves to non-proteinogenic L-alpha-amino acid; its
    structural or activity scope is coherent with the native graph and inspected original
    evidence. No unsupported parent/role correction is inferred from absent optional
    annotations.
  snapshot_sha256: 0d7cb2a0e0ce77fabb65bd4eef1788a86bc619e61414ace1fb4178d86fb45783
- evidence_id: term-33281
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/33281/
  locator: CHEBI:33281 current label and definition
  accessed_at: '2026-10-21T17:03:12.283961Z'
  support: supports
  summary: The retained term resolves to antimicrobial agent; its structural or activity
    scope is coherent with the native graph and inspected original evidence. No unsupported
    parent/role correction is inferred from absent optional annotations.
  snapshot_sha256: 0f66df822d1a825c02531f80cc0fcc12783ac72a0c2f0482a9d9018db0dba9e1
- evidence_id: term-33282
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/33282/
  locator: CHEBI:33282 current label and definition
  accessed_at: '2026-10-21T17:03:12.368473Z'
  support: supports
  summary: The retained term resolves to antibacterial agent; its structural or activity
    scope is coherent with the native graph and inspected original evidence. No unsupported
    parent/role correction is inferred from absent optional annotations.
  snapshot_sha256: 20d92ce7e00c204b1753184671c043160821d692438278344335446aadcd5082
- evidence_id: wikipedia
  kind: database
  reference: https://en.wikipedia.org/wiki/Furanomycin
  locator: Resolved Furanomycin topic page
  accessed_at: '2026-10-21T17:03:13.955452Z'
  support: context_only
  summary: The asserted document link resolves to the intended compound topic. It
    is not used as primary evidence for stereochemistry, producer taxonomy, activity
    or mechanism.
  snapshot_sha256: fed5333d776e49718e0e47ae0522970ce811f5453925ff4da3f72837f728eb9e
- evidence_id: adopted
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A%2810814415%20OR%202182633%20OR%2022500807%20OR%2023688329%20OR%204861779%29%20AND%20SRC%3AMED&format=json&resultType=core&pageSize=100
  locator: All five adopted PMID leads; complete available abstracts and bibliographic
    metadata
  accessed_at: '2026-10-21T17:03:11.465460Z'
  support: supports
  summary: PMID 4861779 is the 1967 original antibiotic report, DOI 10.1021/jm00318a035;
    metadata resolves but no abstract/full text was accessible. PMID 10814415, DOI
    10.1021/ol005569j, reports asymmetric (+)-furanomycin synthesis, with original
    SI inspected below. PMID 2182633, DOI 10.1016/S0021-9258(19)39239-7, is the 1990
    IleRS charging/incorporation study, whose original public text was read. PMID
    23688329, DOI 10.1186/1471-2180-13-111, is the 2013 SBW25 isolation/activity study,
    read in full main XML. PMID 22500807, DOI 10.1016/j.cell.2012.02.050, concerns
    C. elegans surveillance/aversion; actual Figure 2A provides only contextual furanomycin
    listing.
  snapshot_sha256: c145b5d13ea19d28557dfb80fe9a2db553691b4e0e9a400dd07b89a09008e2e9
- evidence_id: synthesis
  kind: primary_source
  reference: https://ndownloader.figshare.com/files/5827437
  locator: Original DOI 10.1021/ol005569j SI experimental procedures; final compound
    1 p3 drawing actually viewed
  accessed_at: '2026-10-21T17:08:43.874388Z'
  support: supports
  summary: The asymmetric synthesis isolates the amino acid after TFA deprotection,
    basic ion-exchange work-up and crystallization. Final compound 1 has the same
    stereochemical drawing as native, and optical rotation +139 (c 1, H2O), compared
    with original 1967 and corrected 1980 literature values. The procedure supplies
    identity evidence, not an antibacterial assay. The final graph has no retained
    TFA counterion; the MS [M+H]+ is an analytical ion.
  snapshot_sha256: 2b6cf1c33fc35bc07338cecfd0b238a10df11ac422cf15aba902619c182ba53f
- evidence_id: isolation
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3662646/fullTextXML
  locator: Full 2013 original main text; purification/identification, Figure 5, Tables
    1–2 and methods
  accessed_at: '2026-10-21T17:04:21.326217Z'
  support: supports
  summary: 'The authors isolate 3.7 mg from material corresponding to approximately
    600 mL of P. fluorescens SBW25 culture filtrate. HRESIMS and NMR identify C7H11NO3;
    the main text assigns (2S,2′R,5′S) by comparison with literature and synthetic
    diastereomers. Glycerol contamination prevents an accurate optical rotation, so
    this is not an independent optical absolute-hand determination. A final purified-fraction
    aliquot inhibits D. dadantii 1447. Table 2, however, measures culture-filtrate
    inhibition-zone areas, not pure-compound MICs. The filtrate panel has six sensitive
    strains: B. megaterium K2; D. dadantii X179/1447; E. amylovora 153; and P. syringae
    maculicola M4/tomato DC3000.'
  snapshot_sha256: ad4ba0d8bb2ae185f9be8a6e56e2055db6e876eb0db52dae4693083025d8909b
- evidence_id: structure-figure
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/9c1a/3662646/41202c06a991/1471-2180-13-111-5.jpg
  locator: Actual Figure 5 molecular drawing
  accessed_at: '2026-10-21T17:07:52.092702Z'
  support: supports
  summary: The primary drawing is consistent with the native alpha 2S/ring 2′R/ring
    5′S graph and the independently inspected 2000 final synthesis drawing. Its agreement
    is not treated as a direct crystal determination or proof that achiral NMR alone
    distinguishes enantiomers.
  snapshot_sha256: 51b26efc69ff989d82b8bd68cb8a3f9a577b28e95cf215134b5ed6bad13a4401
- evidence_id: activity-method
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3662646/fullTextXML
  locator: '2013 Methods: culture filtrate production and agar diffusion; Results
    amino-acid reversal'
  accessed_at: '2026-10-21T17:04:21.326217Z'
  support: supports
  summary: Seven-day cultures provide sterile filtrate. Indicator strains are grown
    in LB, adjusted to OD600 0.2 (E. coli 0.8), and 300 µL spread on 925 Minimal Medium
    plates. A 300 µL filtrate aliquot enters the central well; incubation is 48 h
    at 28°C, with triplicates and repeat experiments for sensitive strains. D. dadantii
    1447 inhibition is reversed by 10 mM isoleucine, leucine or valine, but not glutamine/alanine;
    serine gives ambiguous reduced-density zones excluded from statistics. These are
    filtrate rescue experiments, not proof of a unique purified-compound target or
    a clinical breakpoint.
  snapshot_sha256: ad4ba0d8bb2ae185f9be8a6e56e2055db6e876eb0db52dae4693083025d8909b
- evidence_id: enzyme-method
  kind: primary_source
  reference: https://www.researchgate.net/publication/20972689_Nonprotein_amino_acid_furanomycin_unlike_isoleucine_in_chemical_structure_is_charged_to_isoleucine_tRNA_by_isoleucyl-tRNA_synthetase_and_incorporated_into_protein
  locator: Original 1990 public author-copy text p 6931; Materials and binding/NMR
    methods
  accessed_at: '2026-10-21T17:13:24Z'
  support: supports
  summary: The actual original source text identifies furanomycin supplied by Shionogi,
    E. coli IleRS and tRNAIle, and separately T. thermophilus HB8 EF-Tu/EF-Ts. The
    latter proteins must not be relabelled E. coli. Ligand binding is measured by
    TNS fluorescence at 37°C, pH 7.0; transferred-NOE NMR examines bound conformation.
    This is inspected original text delivered by a public author-copy page; direct
    publisher PDFs returned 403.
  snapshot_sha256: 1df8744286389a9375c1092fa4cb3dcabd2c24854dddef3badc296c1028438d3
- evidence_id: charging
  kind: primary_source
  reference: https://doi.org/10.1016/S0021-9258(19)39239-7
  locator: Original 1990 text pp 6932–6933; aminoacylation methods and results surrounding
    Figures 6–7
  accessed_at: '2026-10-21T17:13:24Z'
  support: supports
  summary: Furanomycin binds IleRS with reported Kd 0.031 mM versus 0.010 mM for isoleucine.
    The authors use a back-titration/acetylation assay because labelled furanomycin
    is unavailable. At low IleRS concentration, furanomycyl-tRNA formation is slower
    than isoleucyl-tRNA; at higher enzyme concentration, charging is comparably efficient.
    These are substrate recognition and charging results, not a generic inhibition
    IC50 or measured bacterial MIC.
  snapshot_sha256: f819cc9e1023752f9c4a98c8f4206fd9e714663e2847fd1fbb3749363505cf69
- evidence_id: incorporation
  kind: primary_source
  reference: https://doi.org/10.1016/S0021-9258(19)39239-7
  locator: Original 1990 text pp 6934–6935; ternary complex, Figure 8 description
    and Discussion
  accessed_at: '2026-10-21T17:13:24Z'
  support: supports
  summary: Furanomycyl-tRNA binds the tested EF-Tu.GTP complex with affinity similar
    to isoleucyl-tRNA. An E. coli S30/pAT153 cell-free reaction lacking isoleucine
    regains a beta-lactamase-precursor band when 10 mM furanomycin is supplied; the
    authors interpret the control/NMR-purity evidence as incorporation in place of
    isoleucine. This is not residue-resolved mass spectrometry. The Discussion proposes
    that bulky substituted residues disturb protein conformation/function and cause
    toxicity; that downstream mechanism is a hypothesis, not directly measured in
    this experiment. No whole-cell kill kinetics or resistance mechanism is established.
  snapshot_sha256: da36b050331d36bf83858707dd18f1f4d3d16ae64ab5b5501879996d5391f7f2
- evidence_id: host-study
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3613046/?pdf=1
  locator: Original 2012 abstract, relevant Results/Methods and Figure 2 caption
  accessed_at: '2026-10-21T17:06:50.227280Z'
  support: context_only
  summary: The inspected experiment concerns C. elegans aversion and immune/detoxification
    responses to disruption of core host processes. The actual tested drugs in the
    main aversion experiment are other compounds. It supplies no direct furanomycin
    bacterial potency or furanomycin-specific worm endpoint in the inspected main
    text.
  snapshot_sha256: 01be7336f53cdd84b3dc13391633cbbc39c94e1dbcb60a3c3e6cd533c3b21833
- evidence_id: host-figure
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/f8bf/3613046/0d3da176f8e3/nihms366225f2.jpg
  locator: Actual 2012 Figure 2A–C viewed
  accessed_at: '2026-10-21T17:10:40.157037Z'
  support: context_only
  summary: Furanomycin appears in panel A among examples associated with tRNA synthetases,
    with a prokaryote/eukaryote cross-specificity footnote. Panels B/C test zeocin,
    antimycin A, tunicamycin, bortezomib, geneticin, paraquat and concanamycin A;
    furanomycin is not among those plotted drugs. This contextual list cannot substitute
    for the 1990 specific substrate/charging experiments.
  snapshot_sha256: e7628559f76c1c670460f5f0cc6e39d66e286328ccaf8cf3409dc10db4db506a
- evidence_id: adapter
  kind: database
  reference: kg-microbe-sources imodulondb search --organism e_coli --dataset precise1k
    --query ileS
  locator: iModulonDB e_coli/precise1k search ileS after covered-dataset catalog
  accessed_at: '2026-10-21T17:13:24Z'
  support: context_only
  summary: Before open mechanistic follow-up, the successful adapter read returned
    e_coli/precise1k/b0026 ileS, isoleucine--tRNA ligase, and zero iModulons. The
    first sandbox attempt failed DNS; a public read succeeded. This annotation does
    not identify the exact original 1990 construct or independently prove binding,
    charging or toxicity.
  snapshot_sha256: af59bc73d5fc052e972256ac220e54f8eda218e1045bbfd3e3ff56945c28ad5a
- evidence_id: access
  kind: search
  reference: 481482-fetch6.json
  locator: Recorded public retrieval successes and failures
  accessed_at: '2026-10-21T17:13:24Z'
  support: context_only
  summary: The original 1967 ACS page returned 403; its metadata alone was inspected.
    Direct 1990 JBC routes returned 403, but public author-copy original text was
    available. The 2000 main paper was read at abstract depth, with final experimental
    SI and drawing independently inspected. 2012 full XML returned 500; its PMC HTML
    and Figure 2 were readable. Supplementary PDF retrieval returned a download challenge
    and EuropePMC supplementary route explicitly said the article was not open access.
    Common Chemistry returned 401 and Reaxys 5254308 returned 403.
  search_scope: Free EPMC, PMC/CDN, publisher, author-copy, Figshare, ChEBI, CAS,
    Reaxys and PubChem retrievals; actual URLs/timestamps/statuses/hashes in 481482-fetch1.json
    through 481482-fetch6.json and 482-fetch7.json. No subscriber or paid access.
  snapshot_sha256: 686469a17600bfe845c137a01c4f5b291d0f71ac4db3467ee13b6fa3c96b6dbc
- evidence_id: gates
  kind: validation
  reference: 482-focused-results.json
  locator: Actual chemistry/schema/strict results
  accessed_at: '2026-10-21T17:13:24Z'
  support: supports
  summary: All focused executions exited 0. Native validators used 049 own environment;
    RDKit used 019 interpreter with 049 cwd. Exact source-id mint and all internal
    chemical representations agree.
  snapshot_sha256: 13bc19b3ef79e16cd9fa8889437e9e5ccd3d508e15b44345b0c8fcf9b2a44545
assessments:
- assessment_id: identity
  area: identity
  topic: Exact amino-acid graph and stereochemical names
  outcome: supported
  summary: Native alpha 2S/ring 2′R/ring 5′S agrees with the original 2000 final synthesis
    and 2013 Figure 5, current ChEBI and independent PubChem graph. The 2013 isolate
    assignment uses literature comparison rather than an independent optical/crystal
    absolute determination.
  target_ids:
  - CHEBI:79390
  evidence_ids:
  - native
  - chebi
  - chemistry
  - mapping
  - synthesis
  - isolation
  - structure-figure
- assessment_id: grounding
  area: grounding
  topic: Ontology and external-reference scope
  outcome: unknown
  summary: Structural parents and antibacterial/antimicrobial roles are coherent.
    CAS has exact-key database corroboration, while direct CAS and Reaxys authority
    access remains unavailable. Wikipedia resolves as a document topic and is not
    primary scientific evidence.
  target_ids:
  - CHEBI:79390
  evidence_ids:
  - term-51659
  - term-83822
  - term-33281
  - term-33282
  - cas
  - pubchem
  - wikipedia
  - access
- assessment_id: activity
  area: evidence
  topic: Purified material versus culture-filtrate measurements
  outcome: supported
  summary: The 2013 study follows antibacterial activity through purification and
    reports final-fraction inhibition of D. dadantii 1447, supporting antibacterial
    eligibility. Its six-strain quantitative table and amino-acid reversal are culture-filtrate
    measurements. They cannot be recast as pure-compound MICs or species-wide sensitivity.
  target_ids:
  - CHEBI:79390
  evidence_ids:
  - isolation
  - activity-method
  - adopted
- assessment_id: mechanism
  area: evidence
  topic: IleRS substrate charging and proposed downstream toxicity
  outcome: supported
  summary: Original 1990 experiments support enzyme binding, furanomycyl-tRNA formation,
    binding of charged tRNA to the tested EF-Tu complex, and authors’ evidence for
    incorporation in a cell-free protein assay. Furanomycin is an unnatural substrate
    in this chain; a simple IleRS-inhibition label loses crucial evidence. Protein
    dysfunction causing antibacterial toxicity is proposed, not experimentally closed
    here. No native mechanism assertion is contradicted.
  target_ids:
  - CHEBI:79390
  evidence_ids:
  - enzyme-method
  - charging
  - incorporation
  - adapter
- assessment_id: host
  area: scope
  topic: 2012 C. elegans citation
  outcome: supported
  summary: 'The original figure resolves why this source appears among adopted leads:
    furanomycin is listed as a contextual tRNA-synthetase-associated toxin. Its presence
    is not evidence that furanomycin was one of the plotted worm-aversion treatments
    or that its bacterial mechanism was directly studied there.'
  target_ids:
  - CHEBI:79390
  evidence_ids:
  - host-study
  - host-figure
  - adopted
- assessment_id: producer
  area: evidence
  topic: Bounded source organism follow-up
  outcome: supported
  summary: The 2013 original supports production by source-identified P. fluorescens
    SBW25. Its claims about earlier S. threomyceticus/ATCC 15795 production cite prior
    work; the inaccessible 1967 original is not represented as independently read.
    No native producer collection requires correction.
  target_ids:
  - CHEBI:79390
  evidence_ids:
  - isolation
  - adopted
  - access
- assessment_id: resistance
  area: scope
  topic: No inferred resistance or clinical phenotype
  outcome: unknown
  summary: Filtrate-insensitive strains and amino-acid rescue do not establish a furanomycin
    resistance determinant, clinical breakpoint or clinical efficacy. No native resistance/clinical
    product assertion exists.
  target_ids:
  - CHEBI:79390
  evidence_ids:
  - native
  - activity-method
  - incorporation
- assessment_id: completeness
  area: completeness
  topic: All adopted leads and optional annotations
  outcome: unknown
  summary: All five adopted leads were disposed at their recorded reading depths.
    Optional activity_spectrum, molecular_targets, producer or causal_graphs enrichment
    is possible with exact material/assay boundaries; absent optional collections
    are not required-schema defects.
  target_ids:
  - CHEBI:79390
  evidence_ids:
  - native
  - adopted
  - access
  - isolation
  - incorporation
- assessment_id: provenance
  area: provenance
  topic: Maintained ownership and history
  outcome: supported
  summary: The entire native/raw rows, source configuration/owners and all four history
    events were inspected. Twenty-one captured input hashes preserve the original
    thirteen, and SEEDED status remains unchanged.
  target_ids:
  - CHEBI:79390
  evidence_ids:
  - native
  - owner
  - search
  - gates
- assessment_id: validation
  area: schema
  topic: Deterministic molecular and native validation
  outcome: supported
  summary: Schema, strict, source mint and independent chemistry checks pass; these
    are distinguished from primary-source scientific assessment.
  target_ids:
  - CHEBI:79390
  evidence_ids:
  - gates
  - chemistry
  - mapping
findings: []
actions:
- action_id: A1
  description: Optional future curation can add the original substrate-to-incorporation
    evidence and bounded activity/producer context.
  finding_ids: []
  target_ids:
  - CHEBI:79390
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/furanomycin.yaml
    role: Future curator-owned molecular_targets, activity_spectrum, producer and
      causal_graphs annotations
  acceptance_checks:
  - Keep E. coli IleRS/tRNA distinct from T. thermophilus HB8 EF-Tu/EF-Ts. Verify
    any specific protein example against the original construct and reviewed authority
    rather than substituting an adapter hit.
  - Preserve binding versus substrate charging, low-versus-high enzyme concentration,
    cell-free incorporation evidence and the proposed nature of protein dysfunction/toxicity.
    Do not flatten this chain into a generic IleRS-inhibition claim.
  - Do not convert 2013 culture-filtrate zone areas or 10 mM amino-acid rescue into
    purified-compound MICs; preserve D. dadantii 1447 purified-fraction activity separately.
  - Use claim-level citations and material-qualified observations; any native curation/status
    event requires separately authorized work and all required gates.
- action_id: A2
  description: Optional access follow-up can resolve legacy authority and original
    source limits.
  finding_ids: []
  target_ids:
  - CHEBI:79390
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted external identifiers and literature leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI source extraction
  acceptance_checks:
  - Inspect exact CAS and Reaxys structures when public authority access permits;
    no identifier removal is justified merely by 401/403.
  - Obtain the 1967 original if its historical producer/assay details are to be curated.
    The 2012 figure’s contextual listing is not a furanomycin experiment and does
    not replace the 1990 original.
limitations:
- Root attaches shared required corpus/QC/contract regression checks for the unchanged
  base; this draft records actual focused checks only.
- The 2013 main XML was read in full, including exact methods and table scope, and
  Figure 5 was visually inspected. NMR spectra were not independently reprocessed.
  The paper explicitly could not measure accurate optical rotation because of glycerol
  contamination.
- The 2000 original abstract and three-page experimental SI were read; final compound
  1 drawing was visually inspected. The main article and all raw supplementary spectra
  were not fully audited. The 1967 original remains metadata-only after publisher
  403.
- The 1990 original text was inspected through a public author-copy transcription
  because publisher PDFs returned 403. Methods, results and relevant figure descriptions
  were read; original plot pixels and raw spectra were not inspected, so no new graphical
  measurement or reanalysis is claimed.
- The 2012 original HTML relevant sections and actual Figure 2 were inspected. Supplementary
  files were inaccessible through a PMC download challenge and non-open-access EuropePMC
  response. No furanomycin-specific uninspected supplementary assay is inferred.
- CAS 18455-25-9 has exact-key PubChem corroboration, but the authoritative registration
  and Reaxys 5254308 remain unverified after 401/403.
- The source-supported activity observations do not establish clinical efficacy, species-wide
  spectrum, a pure-compound MIC table for the 2013 strains, or an experimentally complete
  whole-cell toxicity chain.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native or maintained file was edited. All twenty-one input hashes and original
  thirteen capture entries were rechecked; optional links/tags/notes are specific
  to furanomycin.
- Source manifests retain actual URLs, UTC access times, hashes and failed responses.
  No module-level evidence was inferred from the adapter’s zero iModulon result.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://doi.org/10.1186/1471-2180-13-111
- https://doi.org/10.1016/S0021-9258(19)39239-7
- https://doi.org/10.1021/ol005569j
tags:
- furanomycin
- amino-acid-substrate
- material-scope
```
