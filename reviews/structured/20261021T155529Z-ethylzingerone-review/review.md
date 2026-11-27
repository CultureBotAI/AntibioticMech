# Ethylzingerone: exact identity and qualified downstream mechanism supported

- Review: 20261021T155529Z-ethylzingerone-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T15:30:52Z
- Finished UTC: 2026-10-21T15:55:29Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The exact neutral structure, antibacterial and antifungal roles, cosmetic-preservative use and curated downstream stress-response target are supported within the inspected source scope. The mechanism paper combines genetics and expression evidence; it does not identify a direct binding target or directly demonstrate every proposed oxidative lesion. No confirmed record defect was found. Cosmetic safety remains concentration- and formulation-dependent, and optional quantitative or transcriptomic enrichment is not treated as a defect. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 418; one entire native record. All thirteen original input hashes were verified before judgment and retained. The exact protein-example overlay was appended, giving fourteen captured inputs; curator-owned native fields were identified explicitly.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:172922 | data/antibiotics/antibacterial/ethylzingerone.yaml | generated | ethylzingerone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema verification | passed | True | CHEBI:172922 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:172922 | Actual focused execution exited 0. |
| Focused chemistry verification | passed | False | CHEBI:172922 | Actual focused execution exited 0. |
| authority-map | passed | False | CHEBI:172922 | Native SMILES and InChI, current ChEBI molfile and ChemSpider embedded InChI independently agree on the full key, formula, charge and mass. |
| adapter-catalog | passed | False | CHEBI:172922 | The actual complete dataset catalog was inspected before mechanism follow-up. No covered Burkholderia dataset matches the native experiment; this is not biological negative evidence. |
| Authoritative full QC | failed | True | CHEBI:172922 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:172922 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:172922 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:172922 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:172922 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:172922 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:172922 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:172922 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:172922 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact structure, names, parents and external identity

identity: supported. Targets: CHEBI:172922.

The neutral, achiral structure and all asserted chemical identifiers resolve consistently. No salt, mixture, natural producer or opposite isomer is inferred.

### Antibacterial, antifungal and preservative roles

evidence: supported. Targets: CHEBI:172922.

Exact HEPB bacterial and fungal assays support the three roles in their tested conditions. The paper-specific MIC and killing definitions remain distinct and no unqualified clinical susceptibility result is inferred.

### Curated multifactorial mode and downstream process

evidence: supported. Targets: CHEBI:172922.

The native biological-process target is supported as a qualified mechanistic association, with explicit absence of a direct target. Intracellular oxidation and membrane/LPS effects are author interpretations of multi-omics and genetic responses, not a demonstrated unique ligand-binding mechanism. HOST_SHARED_TARGET marks lack of microbial selectivity in the generic process; it does not itself assert measured host toxicity.

### Cosmetic approval and bounded safety wording

evidence: supported. Targets: CHEBI:172922.

The definition is supported in its cosmetic-preservative context, with the official 0.7% ready-for-use limit. Its safety phrase must not be read as an all-dose, all-route or medicinal approval statement. No contradictory native clinical-status claim is present.

### Optional quantitative activity, datasets, targets and examples

completeness: supported. Targets: CHEBI:172922.

The record represents the reported broad mechanism without inventing a direct protein target. Numerical activity, fungal response context and study accessions could be added by separate curation but are not required omissions. The existing overlay correctly excludes a biological-process target from protein-example requirements.

### All adopted leads, evidence placement and REVIEWED history

provenance: supported. Targets: CHEBI:172922.

All six adopted leads have explicit dispositions. The primary mechanism reference is placed on the curated target and record; source identity remains ChEBI-owned and scientific additions remain curator-owned. Four native history events and the existing REVIEWED status were assessed without promoting or rewriting them.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/ethylzingerone.yaml; Entire native YAML. | supports | The EXACT, REVIEWED CHEBI172922 record describes a neutral ethoxy/hydroxy phenylbutanone. Its four exact synonyms, three structural parents, three activity roles, two xrefs, one ChEBI source concept, one curated biological-process target and four history events were read. The target is explicitly DOWNSTREAM_AFFECTED_PROCESS with PRIMARY_LITERATURE evidence, not a protein-binding assertion. The native record has no numerical activity, resistance, producer, clinical-status, transcriptomics-dataset or causal-graph object. |
| owners | data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; conf/sources.yaml; curation/uniprot_protein_examples.yaml; data/antibiotics/antibacterial/ethylzingerone.yaml; Exact raw row 2819, source configuration, applicable extraction/seeding code, exact overlay entry and curator-owned fields. | supports | ChEBI supplies the native definition, chemistry, names, roles and six adopted literature leads. The mode and target are curator-owned native content supported by PMID32737133. The exact overlay excludes this BIOLOGICAL_PROCESS target from protein-example requirements; it is not a missing UniProt example. No exact ARO, FDA, PubChem or MIBiG row supplies this record. All initial input hashes were retained when the overlay and actual ownership were appended. |
| identity | CHEBI:172922; https://www.ebi.ac.uk/chebi/CHEBI:172922; https://www.ebi.ac.uk/chebi/backend/api/public/molfile/172922; https://www.chemspider.com/Chemical-Structure.24208550.html; Complete ChEBI entry, official molfile and ChemSpider identity metadata with independent structure parsing. | supports | Both native encodings, current ChEBI molfile and ChemSpider InChI agree on MXLOKFOWFPJWCW-UHFFFAOYSA-N, C12H16O3, neutral charge and monoisotopic mass 208.109944372. No stereocentre is present. Current ChEBI resolves all four exact names and parents CHEBI33853 phenols, CHEBI35618 aromatic ether and CHEBI51867 methyl ketone, plus roles CHEBI172949 antimicrobial cosmetic preservative, CHEBI33282 antibacterial agent and CHEBI35718 antifungal agent. The official cosmetic opinion independently identifies CAS569646-79-3 and the same chemical name. Structural similarity to zingerone does not assert that HEPB itself is isolated from ginger. |
| antibacterial | PMID:32737133; DOI:10.1128/AEM.01808-20; PMC7499027; https://pmc.ncbi.nlm.nih.gov/articles/PMC7499027/; Complete main article, all main tables and captions; Figure 1 visually inspected. | supports | The exact L’Oréal HEPB material was tested against 58 Burkholderia strains representing 22 species, including 54 Bcc strains across 20 species. B. vietnamiensis G4 LMG22486 has MIC 0.25% and MBC 0.5% w/v in the reported system. Broth MIC means 80% OD630 reduction; agar MIC means no visible growth. The paper defines MBC as 99% killing, not 99.9%. TSB/TSA incubation is at 30°C. The reported 1% G4 time-kill result is described in the text and explicitly not plotted in Figure 1. These conditions support the antibacterial classification without a species-wide clinical potency claim. |
| mechanism | PMID:32737133; DOI:10.1128/AEM.01808-20; Complete Results, Discussion and Methods, including transposon screen, adaptation/resequencing and RNA-seq. | supports | Transposon phenotypes, adapted derivatives and RNA-seq at 0.125% w/v for 8 h associate HEPB exposure with oxidized-protein repair, electrophile defense, pH homeostasis, permeability and LPS-related biology. The authors propose intracellular oxidation as central to a multifactorial response, while noting that HEPB is not itself considered an oxidant and that reactive metabolites or indirect endogenous ROS could contribute. The main article does not provide a direct binding assay or direct chemical demonstration of every proposed oxidative lesion. Native already labels the target as a downstream process and states that no single direct molecular target was shown. LPS/permeability changes remain mechanistic interpretation rather than proof of a unique primary target. |
| resistance-scope | PMID:32186482; DOI:10.1099/jmm.0.001147; PMC7451044; https://pmc.ncbi.nlm.nih.gov/articles/PMC7451044/; Complete original main body, Methods, Results, Discussion and main tables. | supports | The study exposes P. aeruginosa ATCC19429, S. aureus NCIMB9518 and E. coli ATCC8739 to 0.2% HEPB for 24 h before antibiotic susceptibility retesting. It does not show increased antibiotic resistance in that three-strain experiment. HEPB solubility limits testing above 2%, and Bioscreen versus ISO broth methods yield different apparent inhibition boundaries. This does not establish universal resistance-proof activity. Separately, PMID32737133 obtains modestly HEPB-tolerant derivatives, with persistent chloramphenicol tolerance in its tested adaptation context. The native record does not make an absence-of-resistance assertion. |
| antifungal | PMID:33468481; DOI:10.1128/AAC.02711-20; PMC8097443; https://pmc.ncbi.nlm.nih.gov/articles/PMC8097443/; Main Results, Discussion, Methods, tables and captions; Figures 1 and 4 visually inspected. | supports | The exact HEPB drawing in Figure 1 agrees with native identity. C. albicans SC5314 MIC90 is 10 mg/ml in YPD and RPMI and 20 mg/ml in SD; media, pH and the 30°C assay conditions matter. The 20 mg/ml killing experiment leaves approximately 10% viable cells at 60 min and should not be recast as a 99.9% endpoint. Transcriptomics and yeast mutant profiling implicate amino-acid homeostasis and detoxification. Tryptophan rescue in Figure 4 is demonstrated in S. cerevisiae, while C. albicans TRP1 deletion increases sensitivity. Neither proves direct HEPB binding to Trp1 or transfers a fungal target to Burkholderia. These results support the antifungal role. |
| cosmetic-authority | Commission Regulation (EU) 2019/1858; https://eur-lex.europa.eu/eli/reg/2019/1858/oj/eng; SCCS/1596/18; https://health.ec.europa.eu/document/download/da918b90-b4be-480e-b76d-63875ddab71c_en?filename=sccs_o_225.pdf; EU regulation English text and Annex entry read through the web tool; official 2019 SCCS PDF selected pages 6–8 and 33–35 read. | supports | Annex V entry 60 authorizes hydroxyethoxyphenyl butanone, CAS569646-79-3, at a maximum 0.7% in the ready-for-use cosmetic preparation. The SCCS opinion identifies the exact chemical name, formula and cosmetic material, discusses the prior eye-irritation uncertainty and concludes safety for the specified 0.7% use. This supports cosmetic-preservative approval with concentration and formulation boundaries; it is not drug approval or an unrestricted safety claim. The local EU PDF/HTML requests were empty 202 responses; the earlier full regulation text was inspected through the web tool. A repeat web request later returned a challenge, which does not enlarge the earlier read scope. |
| adopted-leads | PMID:19367122; PMID:28487064; PMID:31170420; PMID:32186482; PMID:32737133; PMID:33468481; All six adopted bibliographic records and all available complete indexed abstracts, plus exact full-text dispositions above. | context_only | PMID19367122, DOI10.1159/000212750, is a secondary ginger-phenolics review: it supplies zingerone context, not exact HEPB antibacterial or producer evidence. PMID28487064, DOI10.1016/j.yrtph.2017.04.014, is the 2017 SCCS opinion bibliographic record with no indexed abstract; its original full article was not obtained. The subsequent official 2019 opinion explicitly discusses that earlier conclusion. PMID31170420, DOI10.1016/j.yrtph.2019.05.018, is the 2019 SCCS opinion abstract and is checked against the selected official PDF sections. The other three adopted leads are the inspected primary bacterial and fungal experiments. Reviews and regulatory opinions are not treated as primary antimicrobial experiments. |
| adapter | iModulonDB public dataset catalog; Actual complete catalog inspected before open-ended mechanism follow-up. | context_only | No covered Burkholderia organism/dataset matches the native experiment. Candida and Saccharomyces follow-up experiments are also outside the inspected catalog. No expression component or unrelated E. coli pathway was substituted for those experiments. Article-reported accessions E-MTAB-7906 for bacterial RNA-seq, E-MTAB-7908 for fungal microarrays and GSE125353 for fitness profiling remain distinct; raw data and independent accession metadata were not reanalysed. |
| search | 418-inclusive-hits.txt; 418-fetch-results.json; 418-fetch2-results.json; 418-fetch3-results.json; 418-fetch4-results.json; 418-fetch5-results.json; Ignored-inclusive local provenance search and exact-compound official/primary follow-up. | context_only | The search included hidden and ignored files across data, curation, conf, scripts, src, docs, .claude, reviews and reports. It located the exact protein-example exclusion overlay and native curator history. Exact official identity routes and all six adopted leads were checked before bounded primary mechanism and cosmetic-authority follow-up. Unread supplements, absent indexed abstracts and retrieval failures were retained as limits rather than evidence of absent biology. |
| checks | 418-focused-results.json; 418-schema.log; 418-strict.tsv; 418-chemistry.json; 418-xref-chemistry.json; Actual focused checks and final captured-input hash recheck. | supports | Schema, strict validation and independent chemistry all pass. The ChEBI source-concept minted alias reproduces exactly. Native and current authority structures agree; these deterministic results supplement, rather than replace, the primary-paper audit. |

## Limits And Additional Notes

- The complete main bacterial papers and the fungal main Results, Discussion and Methods were read, with selected original figures inspected. Supplements, raw expression data and mutant libraries were not independently reanalysed.
- The mechanism conclusion rests principally on genetic and expression associations. Direct HEPB binding, the chemical identity of a reactive intermediate and every proposed oxidative or LPS lesion remain unresolved; native already qualifies the target as downstream.
- The 2009 ginger review was read at complete indexed-abstract depth, the 2017 SCCS publication at bibliographic depth because no indexed abstract was supplied, and the 2019 official SCCS PDF at the stated selected-page depth. This is not a complete independent toxicology reassessment.
- Source reporting contains bounded inconsistencies, including P. aeruginosa strain19429 versus19249 in different parts of the bacterial paper and differing fungal fitness-screen concentrations in Results and Methods. No native numerical assay object is asserted, and those discrepancies were not silently harmonized.
- Absence from the inspected iModulonDB catalog is not evidence against the native mechanism. Article-reported dataset accessions were not independently validated beyond their primary-paper descriptions.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No confirmed finding or corrective action is proposed. Optional enrichment should preserve strain, medium, endpoint, concentration and direct-versus-downstream evidence boundaries.
- The initial thirteen input hashes are unchanged. The overlay input was appended and curator ownership identified without editing any native record or native history.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T155529Z-ethylzingerone-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Ethylzingerone: exact identity and qualified downstream mechanism supported'
started_at: '2026-10-21T15:30:52Z'
finished_at: '2026-10-21T15:55:29Z'
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
verdict: blocked
scientific_review: true
summary: The exact neutral structure, antibacterial and antifungal roles, cosmetic-preservative
  use and curated downstream stress-response target are supported within the inspected
  source scope. The mechanism paper combines genetics and expression evidence; it
  does not identify a direct binding target or directly demonstrate every proposed
  oxidative lesion. No confirmed record defect was found. Cosmetic safety remains
  concentration- and formulation-dependent, and optional quantitative or transcriptomic
  enrichment is not treated as a defect. Scientific assessment retains the stated
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
  - path: curation/uniprot_protein_examples.yaml
    sha256: 536ab4cc7ba9be95c80242bcc25321d67a5bdbfecbc50f3be5a449000abfe5f5
    role: context
  - path: data/antibiotics/antibacterial/ethylzingerone.yaml
    sha256: 5c1928d6c532da4d9c540a485bcbc508032d26775f2d56f75995954fa4dd4ba9
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
- target_id: CHEBI:172922
  path: data/antibiotics/antibacterial/ethylzingerone.yaml
  label: ethylzingerone
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
    path: curation/uniprot_protein_examples.yaml
    role: Exact protein-example overlay context
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/ethylzingerone.yaml
    role: Curator-owned mode, target evidence and REVIEWED event
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 418; one entire native record. All thirteen original input
    hashes were verified before judgment and retained. The exact protein-example overlay
    was appended, giving fourteen captured inputs; curator-owned native fields were
    identified explicitly.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:172922
checks:
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:172922
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/ethylzingerone.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:172922
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/ethylzingerone.yaml --out /private/tmp/am-review-session/418-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:172922
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 418
  exit_code: 0
  expected_exit_code: 0
- check_id: authority-map
  name: authority-map
  status: passed
  required: false
  summary: Native SMILES and InChI, current ChEBI molfile and ChemSpider embedded
    InChI independently agree on the full key, formula, charge and mass.
  target_ids:
  - CHEBI:172922
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/418-xref-check.py
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-catalog
  name: adapter-catalog
  status: passed
  required: false
  summary: The actual complete dataset catalog was inspected before mechanism follow-up.
    No covered Burkholderia dataset matches the native experiment; this is not biological
    negative evidence.
  target_ids:
  - CHEBI:172922
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
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
  - CHEBI:172922
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
  - CHEBI:172922
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
  - CHEBI:172922
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
  - CHEBI:172922
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
  - CHEBI:172922
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
  - CHEBI:172922
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
  - CHEBI:172922
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
  - CHEBI:172922
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
  - CHEBI:172922
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/ethylzingerone.yaml
  locator: Entire native YAML.
  accessed_at: '2026-10-21T15:48:22Z'
  support: supports
  summary: The EXACT, REVIEWED CHEBI172922 record describes a neutral ethoxy/hydroxy
    phenylbutanone. Its four exact synonyms, three structural parents, three activity
    roles, two xrefs, one ChEBI source concept, one curated biological-process target
    and four history events were read. The target is explicitly DOWNSTREAM_AFFECTED_PROCESS
    with PRIMARY_LITERATURE evidence, not a protein-binding assertion. The native
    record has no numerical activity, resistance, producer, clinical-status, transcriptomics-dataset
    or causal-graph object.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py; conf/sources.yaml; curation/uniprot_protein_examples.yaml;
    data/antibiotics/antibacterial/ethylzingerone.yaml
  locator: Exact raw row 2819, source configuration, applicable extraction/seeding
    code, exact overlay entry and curator-owned fields.
  accessed_at: '2026-10-21T15:48:22Z'
  support: supports
  summary: ChEBI supplies the native definition, chemistry, names, roles and six adopted
    literature leads. The mode and target are curator-owned native content supported
    by PMID32737133. The exact overlay excludes this BIOLOGICAL_PROCESS target from
    protein-example requirements; it is not a missing UniProt example. No exact ARO,
    FDA, PubChem or MIBiG row supplies this record. All initial input hashes were
    retained when the overlay and actual ownership were appended.
  snapshot_sha256: 062a3a3742306b68f7eb8121a6b0241f5bf75f0fc965ba11ba9ec54c2680e83f
- evidence_id: identity
  kind: authority
  reference: CHEBI:172922; https://www.ebi.ac.uk/chebi/CHEBI:172922; https://www.ebi.ac.uk/chebi/backend/api/public/molfile/172922;
    https://www.chemspider.com/Chemical-Structure.24208550.html
  locator: Complete ChEBI entry, official molfile and ChemSpider identity metadata
    with independent structure parsing.
  accessed_at: '2026-10-21T15:48:22Z'
  support: supports
  summary: Both native encodings, current ChEBI molfile and ChemSpider InChI agree
    on MXLOKFOWFPJWCW-UHFFFAOYSA-N, C12H16O3, neutral charge and monoisotopic mass
    208.109944372. No stereocentre is present. Current ChEBI resolves all four exact
    names and parents CHEBI33853 phenols, CHEBI35618 aromatic ether and CHEBI51867
    methyl ketone, plus roles CHEBI172949 antimicrobial cosmetic preservative, CHEBI33282
    antibacterial agent and CHEBI35718 antifungal agent. The official cosmetic opinion
    independently identifies CAS569646-79-3 and the same chemical name. Structural
    similarity to zingerone does not assert that HEPB itself is isolated from ginger.
  snapshot_sha256: 30109d72596a5ec9683aec5b21c4570341c115732e37c913288aadf31a208c27
- evidence_id: antibacterial
  kind: primary_source
  reference: PMID:32737133; DOI:10.1128/AEM.01808-20; PMC7499027; https://pmc.ncbi.nlm.nih.gov/articles/PMC7499027/
  locator: Complete main article, all main tables and captions; Figure 1 visually
    inspected.
  accessed_at: '2026-10-21T15:43:32Z'
  support: supports
  summary: The exact L’Oréal HEPB material was tested against 58 Burkholderia strains
    representing 22 species, including 54 Bcc strains across 20 species. B. vietnamiensis
    G4 LMG22486 has MIC 0.25% and MBC 0.5% w/v in the reported system. Broth MIC means
    80% OD630 reduction; agar MIC means no visible growth. The paper defines MBC as
    99% killing, not 99.9%. TSB/TSA incubation is at 30°C. The reported 1% G4 time-kill
    result is described in the text and explicitly not plotted in Figure 1. These
    conditions support the antibacterial classification without a species-wide clinical
    potency claim.
  snapshot_sha256: 74b559af5df5e1b0113f7a6451cad491b9baf1a2acd922ec94398419fb444a37
- evidence_id: mechanism
  kind: primary_source
  reference: PMID:32737133; DOI:10.1128/AEM.01808-20
  locator: Complete Results, Discussion and Methods, including transposon screen,
    adaptation/resequencing and RNA-seq.
  accessed_at: '2026-10-21T15:48:22Z'
  support: supports
  summary: Transposon phenotypes, adapted derivatives and RNA-seq at 0.125% w/v for
    8 h associate HEPB exposure with oxidized-protein repair, electrophile defense,
    pH homeostasis, permeability and LPS-related biology. The authors propose intracellular
    oxidation as central to a multifactorial response, while noting that HEPB is not
    itself considered an oxidant and that reactive metabolites or indirect endogenous
    ROS could contribute. The main article does not provide a direct binding assay
    or direct chemical demonstration of every proposed oxidative lesion. Native already
    labels the target as a downstream process and states that no single direct molecular
    target was shown. LPS/permeability changes remain mechanistic interpretation rather
    than proof of a unique primary target.
  snapshot_sha256: a348dd2755187f0fa05898b1b6ee1fc214060efcca7b749071ff1f558c4b3ac2
- evidence_id: resistance-scope
  kind: primary_source
  reference: PMID:32186482; DOI:10.1099/jmm.0.001147; PMC7451044; https://pmc.ncbi.nlm.nih.gov/articles/PMC7451044/
  locator: Complete original main body, Methods, Results, Discussion and main tables.
  accessed_at: '2026-10-21T15:43:33Z'
  support: supports
  summary: The study exposes P. aeruginosa ATCC19429, S. aureus NCIMB9518 and E. coli
    ATCC8739 to 0.2% HEPB for 24 h before antibiotic susceptibility retesting. It
    does not show increased antibiotic resistance in that three-strain experiment.
    HEPB solubility limits testing above 2%, and Bioscreen versus ISO broth methods
    yield different apparent inhibition boundaries. This does not establish universal
    resistance-proof activity. Separately, PMID32737133 obtains modestly HEPB-tolerant
    derivatives, with persistent chloramphenicol tolerance in its tested adaptation
    context. The native record does not make an absence-of-resistance assertion.
  snapshot_sha256: 740cc19c46e2582b2fa66d4fae12bdc9b897f2d2bab656c030597195b092c47c
- evidence_id: antifungal
  kind: primary_source
  reference: PMID:33468481; DOI:10.1128/AAC.02711-20; PMC8097443; https://pmc.ncbi.nlm.nih.gov/articles/PMC8097443/
  locator: Main Results, Discussion, Methods, tables and captions; Figures 1 and 4
    visually inspected.
  accessed_at: '2026-10-21T15:43:32Z'
  support: supports
  summary: The exact HEPB drawing in Figure 1 agrees with native identity. C. albicans
    SC5314 MIC90 is 10 mg/ml in YPD and RPMI and 20 mg/ml in SD; media, pH and the
    30°C assay conditions matter. The 20 mg/ml killing experiment leaves approximately
    10% viable cells at 60 min and should not be recast as a 99.9% endpoint. Transcriptomics
    and yeast mutant profiling implicate amino-acid homeostasis and detoxification.
    Tryptophan rescue in Figure 4 is demonstrated in S. cerevisiae, while C. albicans
    TRP1 deletion increases sensitivity. Neither proves direct HEPB binding to Trp1
    or transfers a fungal target to Burkholderia. These results support the antifungal
    role.
  snapshot_sha256: 43ffd6f10d29c5894fbf4231994706e2f222ee04437f2b6ee7aba088afaf2562
- evidence_id: cosmetic-authority
  kind: authority
  reference: Commission Regulation (EU) 2019/1858; https://eur-lex.europa.eu/eli/reg/2019/1858/oj/eng;
    SCCS/1596/18; https://health.ec.europa.eu/document/download/da918b90-b4be-480e-b76d-63875ddab71c_en?filename=sccs_o_225.pdf
  locator: EU regulation English text and Annex entry read through the web tool; official
    2019 SCCS PDF selected pages 6–8 and 33–35 read.
  accessed_at: '2026-10-21T15:44:41Z'
  support: supports
  summary: Annex V entry 60 authorizes hydroxyethoxyphenyl butanone, CAS569646-79-3,
    at a maximum 0.7% in the ready-for-use cosmetic preparation. The SCCS opinion
    identifies the exact chemical name, formula and cosmetic material, discusses the
    prior eye-irritation uncertainty and concludes safety for the specified 0.7% use.
    This supports cosmetic-preservative approval with concentration and formulation
    boundaries; it is not drug approval or an unrestricted safety claim. The local
    EU PDF/HTML requests were empty 202 responses; the earlier full regulation text
    was inspected through the web tool. A repeat web request later returned a challenge,
    which does not enlarge the earlier read scope.
  snapshot_sha256: 5b9042a2e61ca553477ff96a257cc3d41e3cabf1b98c8ad4ffd8b1cda54e18b3
- evidence_id: adopted-leads
  kind: database
  reference: PMID:19367122; PMID:28487064; PMID:31170420; PMID:32186482; PMID:32737133;
    PMID:33468481
  locator: All six adopted bibliographic records and all available complete indexed
    abstracts, plus exact full-text dispositions above.
  accessed_at: '2026-10-21T15:43:10Z'
  support: context_only
  summary: 'PMID19367122, DOI10.1159/000212750, is a secondary ginger-phenolics review:
    it supplies zingerone context, not exact HEPB antibacterial or producer evidence.
    PMID28487064, DOI10.1016/j.yrtph.2017.04.014, is the 2017 SCCS opinion bibliographic
    record with no indexed abstract; its original full article was not obtained. The
    subsequent official 2019 opinion explicitly discusses that earlier conclusion.
    PMID31170420, DOI10.1016/j.yrtph.2019.05.018, is the 2019 SCCS opinion abstract
    and is checked against the selected official PDF sections. The other three adopted
    leads are the inspected primary bacterial and fungal experiments. Reviews and
    regulatory opinions are not treated as primary antimicrobial experiments.'
  snapshot_sha256: f269151cf1ae36909019e08a563f09fce4c092b19d533ed0e671746547b9e53b
- evidence_id: adapter
  kind: database
  reference: iModulonDB public dataset catalog
  locator: Actual complete catalog inspected before open-ended mechanism follow-up.
  accessed_at: '2026-10-21T15:48:22Z'
  support: context_only
  summary: No covered Burkholderia organism/dataset matches the native experiment.
    Candida and Saccharomyces follow-up experiments are also outside the inspected
    catalog. No expression component or unrelated E. coli pathway was substituted
    for those experiments. Article-reported accessions E-MTAB-7906 for bacterial RNA-seq,
    E-MTAB-7908 for fungal microarrays and GSE125353 for fitness profiling remain
    distinct; raw data and independent accession metadata were not reanalysed.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: search
  kind: search
  reference: 418-inclusive-hits.txt; 418-fetch-results.json; 418-fetch2-results.json;
    418-fetch3-results.json; 418-fetch4-results.json; 418-fetch5-results.json
  locator: Ignored-inclusive local provenance search and exact-compound official/primary
    follow-up.
  accessed_at: '2026-10-21T15:48:22Z'
  support: context_only
  summary: The search included hidden and ignored files across data, curation, conf,
    scripts, src, docs, .claude, reviews and reports. It located the exact protein-example
    exclusion overlay and native curator history. Exact official identity routes and
    all six adopted leads were checked before bounded primary mechanism and cosmetic-authority
    follow-up. Unread supplements, absent indexed abstracts and retrieval failures
    were retained as limits rather than evidence of absent biology.
  search_scope: '2026-10-21: rg --no-ignore --hidden for CHEBI:172922, ethylzingerone/name/slug
    and MXLOKFOWFPJWCW across the stated repository paths; exact ChEBI, ChemSpider,
    six adopted PMIDs, SCCS opinion and EU Regulation2019/1858 routes. No paid provider
    or broad compound-analogue substitution was used.'
  snapshot_sha256: 896bfb482f1cab4e3fb033a922ab3ad3f95328353565a6c1ea87a68e4158df2e
- evidence_id: checks
  kind: validation
  reference: 418-focused-results.json; 418-schema.log; 418-strict.tsv; 418-chemistry.json;
    418-xref-chemistry.json
  locator: Actual focused checks and final captured-input hash recheck.
  accessed_at: '2026-10-21T15:48:22Z'
  support: supports
  summary: Schema, strict validation and independent chemistry all pass. The ChEBI
    source-concept minted alias reproduces exactly. Native and current authority structures
    agree; these deterministic results supplement, rather than replace, the primary-paper
    audit.
  snapshot_sha256: ab7b94463577496d0d0ba337b040af7cb0f94c648f103a54844ee7a30bf61552
assessments:
- assessment_id: identity
  area: identity
  topic: Exact structure, names, parents and external identity
  outcome: supported
  summary: The neutral, achiral structure and all asserted chemical identifiers resolve
    consistently. No salt, mixture, natural producer or opposite isomer is inferred.
  target_ids:
  - CHEBI:172922
  evidence_ids:
  - native
  - identity
  - owners
  - checks
- assessment_id: activity
  area: evidence
  topic: Antibacterial, antifungal and preservative roles
  outcome: supported
  summary: Exact HEPB bacterial and fungal assays support the three roles in their
    tested conditions. The paper-specific MIC and killing definitions remain distinct
    and no unqualified clinical susceptibility result is inferred.
  target_ids:
  - CHEBI:172922
  evidence_ids:
  - antibacterial
  - antifungal
  - cosmetic-authority
- assessment_id: mode
  area: evidence
  topic: Curated multifactorial mode and downstream process
  outcome: supported
  summary: The native biological-process target is supported as a qualified mechanistic
    association, with explicit absence of a direct target. Intracellular oxidation
    and membrane/LPS effects are author interpretations of multi-omics and genetic
    responses, not a demonstrated unique ligand-binding mechanism. HOST_SHARED_TARGET
    marks lack of microbial selectivity in the generic process; it does not itself
    assert measured host toxicity.
  target_ids:
  - CHEBI:172922
  evidence_ids:
  - native
  - mechanism
  - adapter
- assessment_id: safety
  area: evidence
  topic: Cosmetic approval and bounded safety wording
  outcome: supported
  summary: The definition is supported in its cosmetic-preservative context, with
    the official 0.7% ready-for-use limit. Its safety phrase must not be read as an
    all-dose, all-route or medicinal approval statement. No contradictory native clinical-status
    claim is present.
  target_ids:
  - CHEBI:172922
  evidence_ids:
  - cosmetic-authority
  - native
- assessment_id: completeness
  area: completeness
  topic: Optional quantitative activity, datasets, targets and examples
  outcome: supported
  summary: The record represents the reported broad mechanism without inventing a
    direct protein target. Numerical activity, fungal response context and study accessions
    could be added by separate curation but are not required omissions. The existing
    overlay correctly excludes a biological-process target from protein-example requirements.
  target_ids:
  - CHEBI:172922
  evidence_ids:
  - owners
  - antibacterial
  - antifungal
  - adapter
- assessment_id: provenance
  area: provenance
  topic: All adopted leads, evidence placement and REVIEWED history
  outcome: supported
  summary: All six adopted leads have explicit dispositions. The primary mechanism
    reference is placed on the curated target and record; source identity remains
    ChEBI-owned and scientific additions remain curator-owned. Four native history
    events and the existing REVIEWED status were assessed without promoting or rewriting
    them.
  target_ids:
  - CHEBI:172922
  evidence_ids:
  - native
  - owners
  - adopted-leads
  - search
  - checks
findings: []
actions: []
limitations:
- The complete main bacterial papers and the fungal main Results, Discussion and Methods
  were read, with selected original figures inspected. Supplements, raw expression
  data and mutant libraries were not independently reanalysed.
- The mechanism conclusion rests principally on genetic and expression associations.
  Direct HEPB binding, the chemical identity of a reactive intermediate and every
  proposed oxidative or LPS lesion remain unresolved; native already qualifies the
  target as downstream.
- The 2009 ginger review was read at complete indexed-abstract depth, the 2017 SCCS
  publication at bibliographic depth because no indexed abstract was supplied, and
  the 2019 official SCCS PDF at the stated selected-page depth. This is not a complete
  independent toxicology reassessment.
- Source reporting contains bounded inconsistencies, including P. aeruginosa strain19429
  versus19249 in different parts of the bacterial paper and differing fungal fitness-screen
  concentrations in Results and Methods. No native numerical assay object is asserted,
  and those discrepancies were not silently harmonized.
- Absence from the inspected iModulonDB catalog is not evidence against the native
  mechanism. Article-reported dataset accessions were not independently validated
  beyond their primary-paper descriptions.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No confirmed finding or corrective action is proposed. Optional enrichment should
  preserve strain, medium, endpoint, concentration and direct-versus-downstream evidence
  boundaries.
- The initial thirteen input hashes are unchanged. The overlay input was appended
  and curator ownership identified without editing any native record or native history.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
