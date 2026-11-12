# Iboxamycin: supported exact structure and ribosomal action with minor inherited spelling errors

- Review: 20261021T184510Z-iboxamycin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T18:07:36Z
- Finished UTC: 2026-10-21T18:45:10Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native neutral iboxamycin graph agrees with current PubChem and the ligand deposited with the original ribosome structure. Primary synthetic, antibacterial and structural work supports the definition, while later experiments explain the five database-qualified target-protection relations. Two inherited spelling errors require a minor source correction. Resistance effects are host- and context-dependent; the definition does not assert universal activity against every resistant strain.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 546; one whole exact record. The original thirteen captured hashes remain intact, with four actual ARO/PubChem inputs appended before assessment, yielding seventeen inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-6d3a6e6b69 | data/antibiotics/antibacterial/iboxamycin.yaml | generated | iboxamycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema verification | passed | True | antibioticmech:aro-6d3a6e6b69 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-6d3a6e6b69 | Actual focused execution exited 0. |
| Focused chemistry verification | passed | False | antibioticmech:aro-6d3a6e6b69 | Actual focused execution exited 0. |
| Independent exact chemical structure comparison | passed | False | antibioticmech:aro-6d3a6e6b69 | Native, current PubChem and original-complex CCD encodings all reproduce the same full key, neutral formula and eleven assigned stereocentres. |
| Structured public-source grounding | passed | False | antibioticmech:aro-6d3a6e6b69 | Actual catalog and claim-specific searches completed before mechanism web follow-up; expression annotations remain context only. |
| Structured public-source grounding | passed | False | antibioticmech:aro-6d3a6e6b69 | Actual catalog and claim-specific searches completed before mechanism web follow-up; expression annotations remain context only. |
| Structured public-source grounding | passed | False | antibioticmech:aro-6d3a6e6b69 | Actual catalog and claim-specific searches completed before mechanism web follow-up; expression annotations remain context only. |
| Authoritative full QC | failed | True | antibioticmech:aro-6d3a6e6b69 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-6d3a6e6b69 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-6d3a6e6b69 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-6d3a6e6b69 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-6d3a6e6b69 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-6d3a6e6b69 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-6d3a6e6b69 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-6d3a6e6b69 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-6d3a6e6b69 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact synthetic parent and stereochemistry

identity: supported. Targets: antibioticmech:aro-6d3a6e6b69.

Native and current authority graphs agree at all eleven centres, including the deposited original-complex ligand. Primary synthetic drawing and separation distinguish iboxamycin from its epimer and other oxepanoprolinamides. Formate salt and isotope-labelled binding material are qualified rather than automatically made exact native material.

### Minted identity, class and exact references

grounding: supported. Targets: antibioticmech:aro-6d3a6e6b69.

The source-based minted identifier is appropriate for the adopted ARO/PubChem fallback. Both asserted exact references are corroborated. The synthetic aminooctose/oxepanoproline structure and original paper support lincosamide classification; absence of a ChEBI identifier is not a defect.

### Synthetic origin, bacterial translation and resistant-strain activity

evidence: supported. Targets: antibioticmech:aro-6d3a6e6b69.

Primary synthesis, biochemical and ribosome experiments support the qualitative definition. Its claim that some otherwise resistant strains are inhibited is compatible with later ABCF/Cfr resistance and does not promise activity against all strains. No human approval or treatment claim is populated. Two inherited spelling errors remain minor.

### Five database-qualified target-protection relations

evidence: supported. Targets: antibioticmech:aro-6d3a6e6b69.

The current source and exact 2023 original support the five relations within the reported host/construct settings. Effects differ in size, C. difficile plasmid rescue is not uniform, and the N. vireti factor was tested heterologously. These limits do not make the already database-qualified native edges false, nor justify converting them into direct drug-binding protein targets.

### Maintained source reproduction and history

provenance: supported. Targets: antibioticmech:aro-6d3a6e6b69.

All original hashes are preserved and actual ARO/PubChem owners appended before assessment. Source configuration and extraction/seeding branches explain the definition, local identifier, structure, references, resistance qualifications and three history events.

### Optional enrichment and source limits

completeness: unknown. Targets: antibioticmech:aro-6d3a6e6b69.

Every populated field and asserted identifier was assessed. Optional targets, MIC rows, producer, clinical status, causal graphs and datasets need not be added to correct the two typos. Missing synthetic supplements and known source inconsistencies constrain numerical enrichment and complete experimental reanalysis.

## Findings

### F1: Correct two inherited spelling errors without changing scientific identity

minor / open / confirmed; issue key: iboxamycin-inherited-lincosamide-perfringens-spelling.

The definition says licosamide rather than lincosamide, and resistance_mechanisms[2].label says Clostridium perfringes rather than Clostridium perfringens. The source ontology reproduces these errors, while the primary discovery and resistance papers establish the intended class and organism. Correct the maintained text while retaining the ARO determinant identifier, database qualification and underlying biological relation.

## Recommended Actions And Acceptance Checks

### A1

Correct the two source-derived spellings reproducibly.

- The regenerated definition uses lincosamide and the ARO:3007644 label uses Clostridium perfringens.
- Preserve the native identifier, structure/key, exact PubChem reference, determinant accession and explicit database-only evidence status.
- Apply the correction through maintained source normalization or a scoped override, then regenerate and pass focused validation/reproduction checks.

### A2

Preserve experimental scope if optional mechanism or activity evidence is added.

- Keep resistant-strain activity bounded by organism, genotype and assay; do not claim universal resistance evasion or human efficacy from mouse experiments.
- Distinguish direct 23S/ribosome binding from ABCF protein protection, and distinguish apparent Kd, apparent Ki, cell-free assay concentrations and whole-cell MIC. Retain the formate/isotope preparation where applicable.
- Resolve primary dose/concentration inconsistencies and the C. difficile complement row before transferring quantitative values. Do not replace native database qualifiers solely because more detailed primary experiments are available.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/iboxamycin.yaml; Entire native record: identifier/status, definition and PMID, parent/class, full chemistry, two exact xrefs, source concept, five resistance entries and three history events. | supports | The MINTED/SEEDED record represents neutral iboxamycin C22H39ClN2O6S, key JPCLUJPDWMBCAA-SUTQZAMLSA-N, with eleven assigned stereocentres. It asserts a fully synthetic lincosamide acting on bacterial translation, effective against some otherwise lincosamide-resistant strains. All five ABCF protection relations explicitly remain database assertions. There are no native synonyms, clinical-status, quantitative MIC, molecular-target, producer, causal-graph or dataset objects. The definition contains licosamide, and the third resistance label contains Clostridium perfringes. |
| owners | data/raw/aro_antibiotics.tsv:512; data/raw/aro_resistance_edges.tsv:4445; data/raw/pubchem_structures.tsv:219; scripts/enrich_pubchem_structures.py; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py:785; Complete exact raw rows and relevant source configuration/extraction/seeding code, plus hidden/ignored-inclusive owner search. | supports | ARO supplies the definition, class, exact PubChem reference and five qualified resistance edges. PubChem fallback supplies chemistry because no adopted ChEBI structure is available. The PubChem enrichment function and configured properties reproduce the material fields and retrieval date. No exact target-edge, FDA, MIBiG, BindingDB or curator override was found in the inspected hidden/ignored-inclusive search. Original thirteen input hashes remain preserved; ARO molecule/resistance, PubChem structure and its enrichment script were appended as actual owners. |
| adapter | 546-adapter.json; iModulonDB b_subtilis/modulome and e_coli/precise1k; Actual catalog and vmlR/ribosome searches before open-ended mechanism research. | context_only | The B. subtilis search returns BSU_05610/vmlR, annotated ABCF ATPase, and no component. The E. coli query returns generic ribosome-associated genes and dataset-local Translation component 1, not an iboxamycin exposure experiment. The named clostridial organisms and N. vireti are absent from the returned catalog. No biochemical negative or drug-specific response is inferred from missing catalog coverage, and no expression annotation is promoted to binding evidence. |
| aro | ARO:3007636; ARO:0000017; ARO:3004476; ARO:3007637; ARO:3007644; ARO:3007645; ARO:3007646; Complete current official OBO terms independently extracted/read from the shared official snapshot. | supports | Current ARO agrees with the native molecule definition, lincosamide class and five protection relations. The molecule cites PMID34707295; four CplR/VmlR2 entries cite PMID36951104; VmlR additionally cites PMID30126986. Current ARO itself contains both licosamide and perfringes spelling errors. The supported organism in the cited primary is Clostridium perfringens; the native identifier does not refer to a distinct organism named perfringes. |
| chemistry | pubchem.compound:156613433; https://data.rcsb.org/rest/v1/core/entry/7RQ8; https://data.rcsb.org/rest/v1/core/chemcomp/6IF; Complete PubChem properties, original ribosome-entry/nonpolymer metadata and CCD descriptor; six independent native/authority parses. | supports | All six native/PubChem/6IF encodings reproduce JPCLUJPDWMBCAA-SUTQZAMLSA-N, C22H39ClN2O6S and eleven assigned stereocentres. Entry 7RQ8 is the original PMID34707295 complex; its entity 58 is 6IF. The average mass 495.1 is source rounding, not a chemical mismatch. MINTED means a local source-based identifier rather than ambiguous compound identity. No absent ChEBI accession is manufactured. |
| discovery-identity | PMID:34707295; DOI:10.1038/s41586-021-04045-6; https://pmc.ncbi.nlm.nih.gov/articles/PMC8549432/; Complete original main text and Methods read; original Figures1 and 2 visually inspected. Supplemental synthetic Methods were not obtained as a valid DOCX. | supports | The authors identify iboxamycin as OPP-3, a fully synthetic oxepanoprolinamide linked to the clindamycin aminooctose residue. Figure 1 and synthesis distinguish it from OPP-1, OPP-2 and the separately purified less-active 7′ epimer. The native graph matches the drawn parent scaffold and the deposited ligand. The initial route produced a 1:1 epimeric intermediate mixture followed by separation; this does not make isolated iboxamycin a mixture record. Gram-scale synthesis is a distinct referenced route, and no natural producer is inferred. |
| activity2021 | PMID:34707295; original Figure 2a-c and susceptibility Methods; Actual figure rows, associated Results and Methods inspected. | supports | For example, S. aureus ATCC29213 has IBX MIC 0.06 µg/mL versus clindamycin 0.125, while a clinical c-ermA S. aureus isolate has IBX 1 versus clindamycin &gt;256. E. coli ATCC25922 has IBX 8 versus clindamycin &gt;128; P. aeruginosa ATCC27853 remains much less susceptible at 128. General broth microdilution uses cation-adjusted Mueller-Hinton broth, 5×10^5CFU/mL, 24 h, visible growth inhibition, triplicates and clindamycin comparator; special organism methods are delegated to unavailable supplement. These data support activity against some resistant strains, not universal resistance-proof activity or identical efficacy in all taxa. No susceptible/resistant clinical breakpoint classification is invented. |
| mechanism2021 | PMID:34707295; original ribosome structures7RQ8/7RQ9 and toeprinting; Complete original mechanism Results and relevant Methods, captions and deposition paragraph. | supports | T. thermophilus 70S structures show binding spanning the 50S PTC and nascent peptide exit tunnel, with contacts to 23S rRNA and extension into the A-site cleft. Wild-type and Erm-modified complexes support the structural basis of retained activity; A2058 displacement is observed in the modified complex. Toeprinting shows early arrest at start codons, consistent with blocking entry into productive peptide elongation. The proposal of enhanced initiation interference is not a claim that a specific ribosomal protein is the direct target. Results report 50 µM toeprinting antibiotic, whereas Methods report 50 µg/mL; the review does not resolve or transfer that numeric discrepancy. Mutant-selection results in single-rrn/ΔtolC E. coli establish a special experimental context, not universal clinical resistance frequency. |
| animal2021 | PMID:34707295; original animal Results, Figure 2d-e and Methods; Original in vivo methods and figure inspected; no extrapolation to human treatment or approval. | context_only | Mouse thigh bacterial-burden and systemic survival studies support preclinical antibacterial efficacy. Figure 2d labels E. coli treatment120 mg/kg whereas general thigh Methods specify60 mg/kg; the systemic Results name ATCC19606 while Methods name S. pyogenes ATCC19615. These source inconsistencies limit unqualified numeric/strain transfer. The native does not assert a human approval or clinical treatment indication, and cultured-cell tolerance/mouse efficacy is not human safety evidence. |
| resistance2023-bacilli | PMID:36951104; DOI:10.1093/nar/gkad193; https://pmc.ncbi.nlm.nih.gov/articles/PMC10201436/; Original relevant Methods/Results, Tables 1-4 and Discussion independently reread for iboxamycin; shared official XML retained with fetch provenance. | supports | Table 1 gives B. subtilis168 IBX MIC 2 µg/mL versus 0.06 in ΔvmlR, above 2 with VmlR complementation and 0.06 with ATPase-deficient VmlR-EQ2. N. vireti VmlR2 expressed in the B. subtilis ΔvmlR surrogate gives 8 µg/mL, while the tagged ATPase-deficient variant gives 0.03. Table-specific conditions are LB, 1 mM IPTG for expression constructs,16–20 h at 37°C. These support VmlR and VmlR2 protection but do not constitute an N. vireti whole-cell assay. The VmlR2 cryo-EM factor/ribosome structure supports an allosteric protection model, not direct iboxamycin–protein binding. |
| resistance2023-clostridia | PMID:36951104; original Tables2-4 and native-host construction/results; Exact clostridial iboxamycin columns and host/mutant/complementation conditions inspected. | supports | C. perfringens HN13/pJIR750 has IBX MIC 0.0156 µg/mL versus 0.0078 for ΔcplR/vector, and 0.125 after complementation: a small deletion effect with stronger overexpression evidence. C. sporogenes JCM1416 gives 0.125 wild type,0.03125 for cplR::intron-ermB and 16 for the sigD::intron-ermB control, separating the marker’s contribution. C. difficile630 gives 16,630Δerm0.25 and 630ΔermΔcplR0.0156 µg/mL. However, the plasmid-bearing C. difficile complement row gives &lt;0.00781 versus 0.03125 vector, so this is not uniform clean iboxamycin rescue across every experiment. Retain database-qualified relations and exact context; do not claim every orthologue or host universally defeats iboxamycin. C. difficile Table 2 specifies 36–48 h anaerobic BHIS, while the other clostridial tables use 24 h GAM at 37°C, with stated plasmid-selection supplements. |
| older-vmlr | PMID:30126986; DOI:10.1073/pnas.1808535115; Complete indexed abstract of the current ARO lead. | context_only | The 2018 VmlR study characterizes B. subtilis resistance to lincomycin, virginiamycin and tiamulin, and a factor-bound stalled ribosome. It predates the adopted iboxamycin discovery and is not an exact IBX assay. The 2023 original supplies the exact drug evidence. No resistance value is transferred from the older compound panel. |
| binding2023 | PMID:37295615; DOI:10.1016/j.bmcl.2023.129364; https://pmc.ncbi.nlm.nih.gov/articles/PMC10408240/; Complete short original main text and binding figure caption read; detailed supplemental protocol not retrieved. | supports | The authors explicitly show iboxamycin as its formate salt, use tritium-labelled material for equilibrium binding to E. coli ribosomes and report Kd,app 34±14 nM. Competition with unlabelled parent gives Ki,app 41±30 nM, versus clindamycin 2.7±1.1 µM. These are distinct apparent measurements, not interchangeable IC50/MIC values. Isotope-labelled, epimeric by-products and salt preparation remain separate from the native neutral graph. This is useful parent-target support but does not establish identical quantitative binding for every solid form. |
| cfr2024 | PMID:38238495; DOI:10.1038/s41589-023-01525-w; https://pmc.ncbi.nlm.nih.gov/articles/PMC11325235/; Exact IBX Results section, relevant Methods and Figure 5/extended captions; complete paper and supplementary susceptibility tables not independently audited. | supports | The authors determine a Cfr-modified T. thermophilus 70S–IBX complex and observe displacement of methylated A2503 while retaining engagement. Their selected Results explicitly state that Cfr expression can still increase IBX MIC, although less than for conventional lincosamides. This supports the bounded native claim of retained activity in some resistant strains, not immunity to Cfr/ABCF effects. No exact numerical susceptibility row is copied from unavailable supplemental tables. |
| further-leads | PMID:35733912; PMID:39293511; PMID:34264649; PMID:40055575; PMID:42368392; Complete indexed abstracts of focused follow-up results; preprint versions recognized as duplicates and not counted as independent replications. | context_only | The 2022 Listeria study reports IBX activity, a non-bactericidal effect in that system and VmlR/Cfr cooperation; the 2024 ocular-MRSA study reports activity in 50 isolates including erm-positive strains. The 2021 gram-scale and later oxepanoproline studies concern synthesis; the 2025 fluorinated macrobicycle paper principally studies BT-33 and does not transfer that derivative’s activity or contacts to IBX. These follow-ups are leads at abstract depth, separate from fully inspected native-cited 2021 evidence. |
| search | 546-owner-hits.txt;546-local-hits.txt;546-literature.json;546-fetch-results.json through546-fetch7-results.json; Hidden/ignored-inclusive source/cache searches, exact current IDs, all adopted primary leads and bounded TITLE_ABS:iboxamycin query. | context_only | The focused query returned 12 records, including duplicate preprints; all titles and available original indexed abstracts were inspected. The main 2021/2023/2024 originals were accessed by legitimate public PMC routes after EuropePMC XML 500 errors. Supplement endpoints returned 1817-byte HTML challenges rather than PDF/DOCX; a publisher CDN route failed DNS. No invalid supplemental response is claimed as read. No absence of all further iboxamycin literature is inferred. |

## Limits And Additional Notes

- The 2021 main text, all main Methods and Figures 1/2 were inspected. Synthetic supplemental Methods returned HTML rather than a valid DOCX, and the publisher CDN route failed DNS. Raw NMR/crystallographic data and all supplemental spectra were not reanalysed.
- The 2021 paper reports 50 µM versus 50 µg/mL for toeprinting in Results versus Methods, gives a different systemic S. pyogenes accession in Results versus Methods, and labels E. coli thigh dosing 120 mg/kg versus a general 60 mg/kg Methods regimen. None is silently imported as a quantitative native assertion.
- The 2023 resistance review covered exact Methods/Results, Tables 1-4 and Discussion, not every supplemental structural experiment. Small perfringens deletion effects and a non-rescuing C. difficile iboxamycin complement row are retained as context limits. Table-specific incubation differs from generic Methods.
- The 2023 binding paper was read in full main-text depth, but its detailed supplement was unavailable. Formate salt, radiolabel and apparent binding constants are preserved; these do not automatically become neutral-compound material-specific measurements.
- The 2024 Cfr work was read in exact IBX sections, selected Methods and captions rather than a full raw-data audit. Other follow-ups and the 2018 VmlR source were read at complete indexed abstract depth. Derivative and preprint evidence was not transferred or double-counted.
- Structured adapter searches provide expression annotations and catalog coverage only. They establish neither an iboxamycin-responsive component nor absence of biological activity in organisms missing from the catalog.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Fetch manifests preserve actual UTC access times, URLs, statuses and SHA256 hashes. Shared 2023 XML provenance is 541-fetch3-results.json, retrieved 2026-10-21T18:25:29Z with SHA256 3433769330015b23a70824a247fc231c552bae65a61749b745c44c25a6839766; the current official ARO snapshot provenance is 426-fetch2-results.json, retrieved 2026-10-21T15:57:42Z with SHA256 d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4.
- The unavailable MOESM1 PDF request was an initial supplemental route, not the synthetic Methods document. The main article identifies the latter correctly as MOESM4 DOCX; its actual response was HTML and is not represented as an inspected synthesis supplement.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T184510Z-iboxamycin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Iboxamycin: supported exact structure and ribosomal action with minor inherited
  spelling errors'
started_at: '2026-10-21T18:07:36Z'
finished_at: '2026-10-21T18:45:10Z'
reviewer:
  identity: Codex review002 subagent
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
summary: The native neutral iboxamycin graph agrees with current PubChem and the ligand
  deposited with the original ribosome structure. Primary synthetic, antibacterial
  and structural work supports the definition, while later experiments explain the
  five database-qualified target-protection relations. Two inherited spelling errors
  require a minor source correction. Resistance effects are host- and context-dependent;
  the definition does not assert universal activity against every resistant strain.
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
  - path: data/antibiotics/antibacterial/iboxamycin.yaml
    sha256: ce633442fda1fded0df4553fda02e8cee0926b1689739ad33ad3e8edef6c54bb
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: 25f0d80c0bf26da7741a1514a5e1759dde484ab054f0f56df7938bdda8383a91
    role: context
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: context
  - path: data/raw/chebi_antimicrobials.tsv
    sha256: 4c33e56c3c342be657309f720f5b5cb9cad1fae13bec202ef99e449503c32004
    role: context
  - path: data/raw/chebi_role_names.tsv
    sha256: 5c476c0aacd7c98d7241d2343a6fc41ee9eb9338077404c5b011a04bf40c6ac5
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: docs/CURATION.md
    sha256: a364598a9c2bdaf9e0e71895d5b7a2fd61d3e726e0ed0da12bd895cc4c30e98c
    role: context
  - path: docs/HARMONIZATION.md
    sha256: fb8b58abca016ca5a7d856fcc6f1ec2deb210e0927394a480853830b39e1f060
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
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
- target_id: antibioticmech:aro-6d3a6e6b69
  path: data/antibiotics/antibacterial/iboxamycin.yaml
  label: iboxamycin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI/ARO source extraction and class mapping
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Actual maintained source input for the record
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 546; one whole exact record. The original thirteen captured
    hashes remain intact, with four actual ARO/PubChem inputs appended before assessment,
    yielding seventeen inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-6d3a6e6b69
checks:
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-6d3a6e6b69
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/iboxamycin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-6d3a6e6b69
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/iboxamycin.yaml --out /private/tmp/am-review-session/546-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-6d3a6e6b69
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 546
  exit_code: 0
  expected_exit_code: 0
- check_id: authority-chemistry
  name: Independent exact chemical structure comparison
  status: passed
  required: false
  summary: Native, current PubChem and original-complex CCD encodings all reproduce
    the same full key, neutral formula and eleven assigned stereocentres.
  target_ids:
  - antibioticmech:aro-6d3a6e6b69
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/546-authority-check.py
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-0
  name: Structured public-source grounding
  status: passed
  required: false
  summary: Actual catalog and claim-specific searches completed before mechanism web
    follow-up; expression annotations remain context only.
  target_ids:
  - antibioticmech:aro-6d3a6e6b69
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-1
  name: Structured public-source grounding
  status: passed
  required: false
  summary: Actual catalog and claim-specific searches completed before mechanism web
    follow-up; expression annotations remain context only.
  target_ids:
  - antibioticmech:aro-6d3a6e6b69
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism b_subtilis --dataset modulome --query
    vmlR
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-2
  name: Structured public-source grounding
  status: passed
  required: false
  summary: Actual catalog and claim-specific searches completed before mechanism web
    follow-up; expression annotations remain context only.
  target_ids:
  - antibioticmech:aro-6d3a6e6b69
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset precise1k --query ribosome
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
  - antibioticmech:aro-6d3a6e6b69
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
  - antibioticmech:aro-6d3a6e6b69
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
  - antibioticmech:aro-6d3a6e6b69
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
  - antibioticmech:aro-6d3a6e6b69
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
  - antibioticmech:aro-6d3a6e6b69
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
  - antibioticmech:aro-6d3a6e6b69
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
  - antibioticmech:aro-6d3a6e6b69
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
  - antibioticmech:aro-6d3a6e6b69
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
  - antibioticmech:aro-6d3a6e6b69
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/iboxamycin.yaml
  locator: 'Entire native record: identifier/status, definition and PMID, parent/class,
    full chemistry, two exact xrefs, source concept, five resistance entries and three
    history events.'
  accessed_at: '2026-10-21T18:41:58Z'
  support: supports
  summary: The MINTED/SEEDED record represents neutral iboxamycin C22H39ClN2O6S, key
    JPCLUJPDWMBCAA-SUTQZAMLSA-N, with eleven assigned stereocentres. It asserts a
    fully synthetic lincosamide acting on bacterial translation, effective against
    some otherwise lincosamide-resistant strains. All five ABCF protection relations
    explicitly remain database assertions. There are no native synonyms, clinical-status,
    quantitative MIC, molecular-target, producer, causal-graph or dataset objects.
    The definition contains licosamide, and the third resistance label contains Clostridium
    perfringes.
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv:512; data/raw/aro_resistance_edges.tsv:4445;
    data/raw/pubchem_structures.tsv:219; scripts/enrich_pubchem_structures.py; conf/sources.yaml;
    scripts/extract_source_inventory.py; scripts/seed_from_sources.py:785
  locator: Complete exact raw rows and relevant source configuration/extraction/seeding
    code, plus hidden/ignored-inclusive owner search.
  accessed_at: '2026-10-21T18:41:58Z'
  support: supports
  summary: ARO supplies the definition, class, exact PubChem reference and five qualified
    resistance edges. PubChem fallback supplies chemistry because no adopted ChEBI
    structure is available. The PubChem enrichment function and configured properties
    reproduce the material fields and retrieval date. No exact target-edge, FDA, MIBiG,
    BindingDB or curator override was found in the inspected hidden/ignored-inclusive
    search. Original thirteen input hashes remain preserved; ARO molecule/resistance,
    PubChem structure and its enrichment script were appended as actual owners.
  snapshot_sha256: 8e17fa58fd4d9c48c394606b4acf8803738b0b9a296de45e5b217c2524c9839c
- evidence_id: adapter
  kind: database
  reference: 546-adapter.json; iModulonDB b_subtilis/modulome and e_coli/precise1k
  locator: Actual catalog and vmlR/ribosome searches before open-ended mechanism research.
  accessed_at: '2026-10-21T18:41:58Z'
  support: context_only
  summary: The B. subtilis search returns BSU_05610/vmlR, annotated ABCF ATPase, and
    no component. The E. coli query returns generic ribosome-associated genes and
    dataset-local Translation component 1, not an iboxamycin exposure experiment.
    The named clostridial organisms and N. vireti are absent from the returned catalog.
    No biochemical negative or drug-specific response is inferred from missing catalog
    coverage, and no expression annotation is promoted to binding evidence.
  snapshot_sha256: 1aa6eb8369ed8ce2b353cab26b45ec45033a1b12f5cd86ef85dd96412d54aa46
- evidence_id: aro
  kind: authority
  reference: ARO:3007636; ARO:0000017; ARO:3004476; ARO:3007637; ARO:3007644; ARO:3007645;
    ARO:3007646
  locator: Complete current official OBO terms independently extracted/read from the
    shared official snapshot.
  accessed_at: '2026-10-21T18:41:58Z'
  support: supports
  summary: Current ARO agrees with the native molecule definition, lincosamide class
    and five protection relations. The molecule cites PMID34707295; four CplR/VmlR2
    entries cite PMID36951104; VmlR additionally cites PMID30126986. Current ARO itself
    contains both licosamide and perfringes spelling errors. The supported organism
    in the cited primary is Clostridium perfringens; the native identifier does not
    refer to a distinct organism named perfringes.
  snapshot_sha256: 5ff8e9e36c8a9977f6aed669c254d4f23de62f0c2e7a84381505be5a22c549b9
- evidence_id: chemistry
  kind: authority
  reference: pubchem.compound:156613433; https://data.rcsb.org/rest/v1/core/entry/7RQ8;
    https://data.rcsb.org/rest/v1/core/chemcomp/6IF
  locator: Complete PubChem properties, original ribosome-entry/nonpolymer metadata
    and CCD descriptor; six independent native/authority parses.
  accessed_at: '2026-10-21T18:41:58Z'
  support: supports
  summary: All six native/PubChem/6IF encodings reproduce JPCLUJPDWMBCAA-SUTQZAMLSA-N,
    C22H39ClN2O6S and eleven assigned stereocentres. Entry 7RQ8 is the original PMID34707295
    complex; its entity 58 is 6IF. The average mass 495.1 is source rounding, not
    a chemical mismatch. MINTED means a local source-based identifier rather than
    ambiguous compound identity. No absent ChEBI accession is manufactured.
  snapshot_sha256: 7b967f8ad06eb17596816f047956353d032d8b311f9478c720d0b8d0f8d59d1f
- evidence_id: discovery-identity
  kind: primary_source
  reference: PMID:34707295; DOI:10.1038/s41586-021-04045-6; https://pmc.ncbi.nlm.nih.gov/articles/PMC8549432/
  locator: Complete original main text and Methods read; original Figures1 and 2 visually
    inspected. Supplemental synthetic Methods were not obtained as a valid DOCX.
  accessed_at: '2026-10-21T18:38:12Z'
  support: supports
  summary: The authors identify iboxamycin as OPP-3, a fully synthetic oxepanoprolinamide
    linked to the clindamycin aminooctose residue. Figure 1 and synthesis distinguish
    it from OPP-1, OPP-2 and the separately purified less-active 7′ epimer. The native
    graph matches the drawn parent scaffold and the deposited ligand. The initial
    route produced a 1:1 epimeric intermediate mixture followed by separation; this
    does not make isolated iboxamycin a mixture record. Gram-scale synthesis is a
    distinct referenced route, and no natural producer is inferred.
  snapshot_sha256: 1e9060af53dca4781cd2210573aa55d7201cb8696ae8315e5fdeb38670215c01
- evidence_id: activity2021
  kind: primary_source
  reference: PMID:34707295; original Figure 2a-c and susceptibility Methods
  locator: Actual figure rows, associated Results and Methods inspected.
  accessed_at: '2026-10-21T18:38:43Z'
  support: supports
  summary: For example, S. aureus ATCC29213 has IBX MIC 0.06 µg/mL versus clindamycin
    0.125, while a clinical c-ermA S. aureus isolate has IBX 1 versus clindamycin
    >256. E. coli ATCC25922 has IBX 8 versus clindamycin >128; P. aeruginosa ATCC27853
    remains much less susceptible at 128. General broth microdilution uses cation-adjusted
    Mueller-Hinton broth, 5×10^5CFU/mL, 24 h, visible growth inhibition, triplicates
    and clindamycin comparator; special organism methods are delegated to unavailable
    supplement. These data support activity against some resistant strains, not universal
    resistance-proof activity or identical efficacy in all taxa. No susceptible/resistant
    clinical breakpoint classification is invented.
  snapshot_sha256: ed4b6a0951499af3398a60070ef3270f217eefd179aa6edca924db8cec1d43fa
- evidence_id: mechanism2021
  kind: primary_source
  reference: PMID:34707295; original ribosome structures7RQ8/7RQ9 and toeprinting
  locator: Complete original mechanism Results and relevant Methods, captions and
    deposition paragraph.
  accessed_at: '2026-10-21T18:38:12Z'
  support: supports
  summary: T. thermophilus 70S structures show binding spanning the 50S PTC and nascent
    peptide exit tunnel, with contacts to 23S rRNA and extension into the A-site cleft.
    Wild-type and Erm-modified complexes support the structural basis of retained
    activity; A2058 displacement is observed in the modified complex. Toeprinting
    shows early arrest at start codons, consistent with blocking entry into productive
    peptide elongation. The proposal of enhanced initiation interference is not a
    claim that a specific ribosomal protein is the direct target. Results report 50
    µM toeprinting antibiotic, whereas Methods report 50 µg/mL; the review does not
    resolve or transfer that numeric discrepancy. Mutant-selection results in single-rrn/ΔtolC
    E. coli establish a special experimental context, not universal clinical resistance
    frequency.
  snapshot_sha256: 1e9060af53dca4781cd2210573aa55d7201cb8696ae8315e5fdeb38670215c01
- evidence_id: animal2021
  kind: primary_source
  reference: PMID:34707295; original animal Results, Figure 2d-e and Methods
  locator: Original in vivo methods and figure inspected; no extrapolation to human
    treatment or approval.
  accessed_at: '2026-10-21T18:38:12Z'
  support: context_only
  summary: Mouse thigh bacterial-burden and systemic survival studies support preclinical
    antibacterial efficacy. Figure 2d labels E. coli treatment120 mg/kg whereas general
    thigh Methods specify60 mg/kg; the systemic Results name ATCC19606 while Methods
    name S. pyogenes ATCC19615. These source inconsistencies limit unqualified numeric/strain
    transfer. The native does not assert a human approval or clinical treatment indication,
    and cultured-cell tolerance/mouse efficacy is not human safety evidence.
  snapshot_sha256: 1e9060af53dca4781cd2210573aa55d7201cb8696ae8315e5fdeb38670215c01
- evidence_id: resistance2023-bacilli
  kind: primary_source
  reference: PMID:36951104; DOI:10.1093/nar/gkad193; https://pmc.ncbi.nlm.nih.gov/articles/PMC10201436/
  locator: Original relevant Methods/Results, Tables 1-4 and Discussion independently
    reread for iboxamycin; shared official XML retained with fetch provenance.
  accessed_at: '2026-10-21T18:41:58Z'
  support: supports
  summary: Table 1 gives B. subtilis168 IBX MIC 2 µg/mL versus 0.06 in ΔvmlR, above
    2 with VmlR complementation and 0.06 with ATPase-deficient VmlR-EQ2. N. vireti
    VmlR2 expressed in the B. subtilis ΔvmlR surrogate gives 8 µg/mL, while the tagged
    ATPase-deficient variant gives 0.03. Table-specific conditions are LB, 1 mM IPTG
    for expression constructs,16–20 h at 37°C. These support VmlR and VmlR2 protection
    but do not constitute an N. vireti whole-cell assay. The VmlR2 cryo-EM factor/ribosome
    structure supports an allosteric protection model, not direct iboxamycin–protein
    binding.
  snapshot_sha256: 65395f0a8f5e8162378085f2b5ad57e620779540f1f45ee58203f531803a6ce5
- evidence_id: resistance2023-clostridia
  kind: primary_source
  reference: PMID:36951104; original Tables2-4 and native-host construction/results
  locator: Exact clostridial iboxamycin columns and host/mutant/complementation conditions
    inspected.
  accessed_at: '2026-10-21T18:41:58Z'
  support: supports
  summary: 'C. perfringens HN13/pJIR750 has IBX MIC 0.0156 µg/mL versus 0.0078 for
    ΔcplR/vector, and 0.125 after complementation: a small deletion effect with stronger
    overexpression evidence. C. sporogenes JCM1416 gives 0.125 wild type,0.03125 for
    cplR::intron-ermB and 16 for the sigD::intron-ermB control, separating the marker’s
    contribution. C. difficile630 gives 16,630Δerm0.25 and 630ΔermΔcplR0.0156 µg/mL.
    However, the plasmid-bearing C. difficile complement row gives <0.00781 versus
    0.03125 vector, so this is not uniform clean iboxamycin rescue across every experiment.
    Retain database-qualified relations and exact context; do not claim every orthologue
    or host universally defeats iboxamycin. C. difficile Table 2 specifies 36–48 h
    anaerobic BHIS, while the other clostridial tables use 24 h GAM at 37°C, with
    stated plasmid-selection supplements.'
  snapshot_sha256: 65395f0a8f5e8162378085f2b5ad57e620779540f1f45ee58203f531803a6ce5
- evidence_id: older-vmlr
  kind: primary_source
  reference: PMID:30126986; DOI:10.1073/pnas.1808535115
  locator: Complete indexed abstract of the current ARO lead.
  accessed_at: '2026-10-21T18:37:33Z'
  support: context_only
  summary: The 2018 VmlR study characterizes B. subtilis resistance to lincomycin,
    virginiamycin and tiamulin, and a factor-bound stalled ribosome. It predates the
    adopted iboxamycin discovery and is not an exact IBX assay. The 2023 original
    supplies the exact drug evidence. No resistance value is transferred from the
    older compound panel.
  snapshot_sha256: 9f64f01af74191becfbd61c92ff0596df2fc3af52996dab3597cd29a6819e0d7
- evidence_id: binding2023
  kind: primary_source
  reference: PMID:37295615; DOI:10.1016/j.bmcl.2023.129364; https://pmc.ncbi.nlm.nih.gov/articles/PMC10408240/
  locator: Complete short original main text and binding figure caption read; detailed
    supplemental protocol not retrieved.
  accessed_at: '2026-10-21T18:38:12Z'
  support: supports
  summary: The authors explicitly show iboxamycin as its formate salt, use tritium-labelled
    material for equilibrium binding to E. coli ribosomes and report Kd,app 34±14
    nM. Competition with unlabelled parent gives Ki,app 41±30 nM, versus clindamycin
    2.7±1.1 µM. These are distinct apparent measurements, not interchangeable IC50/MIC
    values. Isotope-labelled, epimeric by-products and salt preparation remain separate
    from the native neutral graph. This is useful parent-target support but does not
    establish identical quantitative binding for every solid form.
  snapshot_sha256: 22c83ab4dbafc16a298cda55c0ac09667242aaa7f84f8302310b4c75a271fecd
- evidence_id: cfr2024
  kind: primary_source
  reference: PMID:38238495; DOI:10.1038/s41589-023-01525-w; https://pmc.ncbi.nlm.nih.gov/articles/PMC11325235/
  locator: Exact IBX Results section, relevant Methods and Figure 5/extended captions;
    complete paper and supplementary susceptibility tables not independently audited.
  accessed_at: '2026-10-21T18:41:58Z'
  support: supports
  summary: The authors determine a Cfr-modified T. thermophilus 70S–IBX complex and
    observe displacement of methylated A2503 while retaining engagement. Their selected
    Results explicitly state that Cfr expression can still increase IBX MIC, although
    less than for conventional lincosamides. This supports the bounded native claim
    of retained activity in some resistant strains, not immunity to Cfr/ABCF effects.
    No exact numerical susceptibility row is copied from unavailable supplemental
    tables.
  snapshot_sha256: d911014ca310f113dfb30e9f0507790d5570b690847162801654cd326c3ab405
- evidence_id: further-leads
  kind: primary_source
  reference: PMID:35733912; PMID:39293511; PMID:34264649; PMID:40055575; PMID:42368392
  locator: Complete indexed abstracts of focused follow-up results; preprint versions
    recognized as duplicates and not counted as independent replications.
  accessed_at: '2026-10-21T18:37:33Z'
  support: context_only
  summary: The 2022 Listeria study reports IBX activity, a non-bactericidal effect
    in that system and VmlR/Cfr cooperation; the 2024 ocular-MRSA study reports activity
    in 50 isolates including erm-positive strains. The 2021 gram-scale and later oxepanoproline
    studies concern synthesis; the 2025 fluorinated macrobicycle paper principally
    studies BT-33 and does not transfer that derivative’s activity or contacts to
    IBX. These follow-ups are leads at abstract depth, separate from fully inspected
    native-cited 2021 evidence.
  snapshot_sha256: 9225e675086080997865f02adba90a382c6e7b8d9911bf61159e902e6514a028
- evidence_id: search
  kind: search
  reference: 546-owner-hits.txt;546-local-hits.txt;546-literature.json;546-fetch-results.json
    through546-fetch7-results.json
  locator: Hidden/ignored-inclusive source/cache searches, exact current IDs, all
    adopted primary leads and bounded TITLE_ABS:iboxamycin query.
  accessed_at: '2026-10-21T18:37:33Z'
  support: context_only
  summary: The focused query returned 12 records, including duplicate preprints; all
    titles and available original indexed abstracts were inspected. The main 2021/2023/2024
    originals were accessed by legitimate public PMC routes after EuropePMC XML 500
    errors. Supplement endpoints returned 1817-byte HTML challenges rather than PDF/DOCX;
    a publisher CDN route failed DNS. No invalid supplemental response is claimed
    as read. No absence of all further iboxamycin literature is inferred.
  snapshot_sha256: 9225e675086080997865f02adba90a382c6e7b8d9911bf61159e902e6514a028
  search_scope: 2026-10-21; hidden and ignored repository/cache files included. Exact
    PubChem/ARO IDs, adopted PMID and bounded iboxamycin title/abstract follow-up;
    read depths and failed public routes stated explicitly.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact synthetic parent and stereochemistry
  outcome: supported
  summary: Native and current authority graphs agree at all eleven centres, including
    the deposited original-complex ligand. Primary synthetic drawing and separation
    distinguish iboxamycin from its epimer and other oxepanoprolinamides. Formate
    salt and isotope-labelled binding material are qualified rather than automatically
    made exact native material.
  target_ids:
  - antibioticmech:aro-6d3a6e6b69
  evidence_ids:
  - native
  - chemistry
  - discovery-identity
  - binding2023
- assessment_id: classification
  area: grounding
  topic: Minted identity, class and exact references
  outcome: supported
  summary: The source-based minted identifier is appropriate for the adopted ARO/PubChem
    fallback. Both asserted exact references are corroborated. The synthetic aminooctose/oxepanoproline
    structure and original paper support lincosamide classification; absence of a
    ChEBI identifier is not a defect.
  target_ids:
  - antibioticmech:aro-6d3a6e6b69
  evidence_ids:
  - owners
  - aro
  - chemistry
  - discovery-identity
- assessment_id: definition
  area: evidence
  topic: Synthetic origin, bacterial translation and resistant-strain activity
  outcome: supported
  summary: Primary synthesis, biochemical and ribosome experiments support the qualitative
    definition. Its claim that some otherwise resistant strains are inhibited is compatible
    with later ABCF/Cfr resistance and does not promise activity against all strains.
    No human approval or treatment claim is populated. Two inherited spelling errors
    remain minor.
  target_ids:
  - antibioticmech:aro-6d3a6e6b69
  evidence_ids:
  - activity2021
  - mechanism2021
  - animal2021
  - cfr2024
  - aro
- assessment_id: resistance
  area: evidence
  topic: Five database-qualified target-protection relations
  outcome: supported
  summary: The current source and exact 2023 original support the five relations within
    the reported host/construct settings. Effects differ in size, C. difficile plasmid
    rescue is not uniform, and the N. vireti factor was tested heterologously. These
    limits do not make the already database-qualified native edges false, nor justify
    converting them into direct drug-binding protein targets.
  target_ids:
  - antibioticmech:aro-6d3a6e6b69
  evidence_ids:
  - aro
  - resistance2023-bacilli
  - resistance2023-clostridia
  - older-vmlr
- assessment_id: provenance
  area: provenance
  topic: Maintained source reproduction and history
  outcome: supported
  summary: All original hashes are preserved and actual ARO/PubChem owners appended
    before assessment. Source configuration and extraction/seeding branches explain
    the definition, local identifier, structure, references, resistance qualifications
    and three history events.
  target_ids:
  - antibioticmech:aro-6d3a6e6b69
  evidence_ids:
  - owners
  - native
- assessment_id: coverage
  area: completeness
  topic: Optional enrichment and source limits
  outcome: unknown
  summary: Every populated field and asserted identifier was assessed. Optional targets,
    MIC rows, producer, clinical status, causal graphs and datasets need not be added
    to correct the two typos. Missing synthetic supplements and known source inconsistencies
    constrain numerical enrichment and complete experimental reanalysis.
  target_ids:
  - antibioticmech:aro-6d3a6e6b69
  evidence_ids:
  - adapter
  - search
  - binding2023
  - animal2021
  - mechanism2021
findings:
- finding_id: F1
  issue_key: iboxamycin-inherited-lincosamide-perfringens-spelling
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: Correct two inherited spelling errors without changing scientific identity
  description: The definition says licosamide rather than lincosamide, and resistance_mechanisms[2].label
    says Clostridium perfringes rather than Clostridium perfringens. The source ontology
    reproduces these errors, while the primary discovery and resistance papers establish
    the intended class and organism. Correct the maintained text while retaining the
    ARO determinant identifier, database qualification and underlying biological relation.
  target_ids:
  - antibioticmech:aro-6d3a6e6b69
  field_paths:
  - definition
  - resistance_mechanisms[2].label
  evidence_ids:
  - native
  - aro
  - discovery-identity
  - resistance2023-clostridia
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Inherited definition spelling
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Inherited determinant label spelling
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source-label correction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated prose and label emission
  rule_id: 'Native checklist: accurate compound/class and organism naming'
  native_severity: minor
  normalization_reason: These are confirmed spelling errors in descriptive text. Exact
    compound identity, determinant accession and supported biological relation remain
    unchanged, so minor is proportionate.
actions:
- action_id: A1
  description: Correct the two source-derived spellings reproducibly.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-6d3a6e6b69
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Inherited definition spelling
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Inherited determinant label spelling
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source-label correction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated prose and label emission
  acceptance_checks:
  - The regenerated definition uses lincosamide and the ARO:3007644 label uses Clostridium
    perfringens.
  - Preserve the native identifier, structure/key, exact PubChem reference, determinant
    accession and explicit database-only evidence status.
  - Apply the correction through maintained source normalization or a scoped override,
    then regenerate and pass focused validation/reproduction checks.
- action_id: A2
  description: Preserve experimental scope if optional mechanism or activity evidence
    is added.
  finding_ids: []
  target_ids:
  - antibioticmech:aro-6d3a6e6b69
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/iboxamycin.yaml
    role: Optional curator-owned scientific additions through the validated writer
  acceptance_checks:
  - Keep resistant-strain activity bounded by organism, genotype and assay; do not
    claim universal resistance evasion or human efficacy from mouse experiments.
  - Distinguish direct 23S/ribosome binding from ABCF protein protection, and distinguish
    apparent Kd, apparent Ki, cell-free assay concentrations and whole-cell MIC. Retain
    the formate/isotope preparation where applicable.
  - Resolve primary dose/concentration inconsistencies and the C. difficile complement
    row before transferring quantitative values. Do not replace native database qualifiers
    solely because more detailed primary experiments are available.
limitations:
- The 2021 main text, all main Methods and Figures 1/2 were inspected. Synthetic supplemental
  Methods returned HTML rather than a valid DOCX, and the publisher CDN route failed
  DNS. Raw NMR/crystallographic data and all supplemental spectra were not reanalysed.
- The 2021 paper reports 50 µM versus 50 µg/mL for toeprinting in Results versus Methods,
  gives a different systemic S. pyogenes accession in Results versus Methods, and
  labels E. coli thigh dosing 120 mg/kg versus a general 60 mg/kg Methods regimen.
  None is silently imported as a quantitative native assertion.
- The 2023 resistance review covered exact Methods/Results, Tables 1-4 and Discussion,
  not every supplemental structural experiment. Small perfringens deletion effects
  and a non-rescuing C. difficile iboxamycin complement row are retained as context
  limits. Table-specific incubation differs from generic Methods.
- The 2023 binding paper was read in full main-text depth, but its detailed supplement
  was unavailable. Formate salt, radiolabel and apparent binding constants are preserved;
  these do not automatically become neutral-compound material-specific measurements.
- The 2024 Cfr work was read in exact IBX sections, selected Methods and captions
  rather than a full raw-data audit. Other follow-ups and the 2018 VmlR source were
  read at complete indexed abstract depth. Derivative and preprint evidence was not
  transferred or double-counted.
- Structured adapter searches provide expression annotations and catalog coverage
  only. They establish neither an iboxamycin-responsive component nor absence of biological
  activity in organisms missing from the catalog.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Fetch manifests preserve actual UTC access times, URLs, statuses and SHA256 hashes.
  Shared 2023 XML provenance is 541-fetch3-results.json, retrieved 2026-10-21T18:25:29Z
  with SHA256 3433769330015b23a70824a247fc231c552bae65a61749b745c44c25a6839766; the
  current official ARO snapshot provenance is 426-fetch2-results.json, retrieved 2026-10-21T15:57:42Z
  with SHA256 d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4.
- The unavailable MOESM1 PDF request was an initial supplemental route, not the synthetic
  Methods document. The main article identifies the latter correctly as MOESM4 DOCX;
  its actual response was HTML and is not represented as an inspected synthesis supplement.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
