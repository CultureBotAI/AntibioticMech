# Clorobiocin: supported exact identity and gyrase binding with a narrow definition-citation gap

- Review: 20261021T133822Z-clorobiocin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T13:22:50Z
- Finished UTC: 2026-10-21T13:38:22Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact clorobiocin structure, antibacterial activity, E. coli GyrB binding and DS 12.976 producer are supported. The definition assigns all claims to a 1980 cellular/genetic paper; its direct-binding and producer clauses need appropriately scoped primary citations. This is a minor provenance correction. The nine explicitly qualified ARO target/resistance assertions remain database claims: related-drug experiments do not establish every clorobiocin-specific phenotype.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 314; one exact record. All 13 original input hashes were preserved and all 33 expanded hashes were rechecked.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-e44e701df2 | data/antibiotics/antibacterial/clorobiocin.yaml | generated | clorobiocin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-e44e701df2 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-e44e701df2 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-e44e701df2 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | antibioticmech:aro-e44e701df2 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-e44e701df2 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-e44e701df2 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-e44e701df2 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-e44e701df2 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-e44e701df2 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-e44e701df2 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-e44e701df2 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-e44e701df2 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact clorobiocin parent, class and molecular properties

identity: supported. Targets: antibioticmech:aro-e44e701df2.

Native encodings and all asserted chemical groundings agree. PDB ligand and MIBiG compound independently support the exact graph; no adjacent congener or salt replacement is needed.

### Source mint and MINTED status

grounding: supported. Targets: antibioticmech:aro-e44e701df2.

ARO identity and mint are reproducible; MINTED is historical identifier provenance, not a claim of no external chemical matches. All asserted xrefs resolve exactly.

### Nearest cited source for direct binding and producer clauses

evidence: concern. Targets: antibioticmech:aro-e44e701df2.

PMID:6154685 provides cellular/genetic evidence for gyrase involvement but no direct binding measurement or named Streptomyces producer. The raw row already retains direct-binding PMID:12044152, omitted by the first-reference transform. The producer is independently supported by PMID:12480894. Correct citation coverage while retaining the supported definition.

### Antibacterial activity and E. coli mechanism

evidence: supported. Targets: antibioticmech:aro-e44e701df2.

Direct cellular inhibition and resistant-mutant evidence support antibacterial eligibility. The binding paper and deposited exact complex independently establish the GyrB interaction; they do not make every downstream transcription/division effect a separate direct target.

### molecular_targets[1] and [3]

evidence: supported. Targets: antibioticmech:aro-e44e701df2.

Both imported GyrB terms are source-supported; exact E. coli fragment binding now provides a strong optional primary upgrade. The taxon-agnostic source terms should not be replaced with a species-specific accession, and deposition/adapter mapping alone is not a curated reviewed UniProt example.

### molecular_targets[0] and [2]

evidence: unknown. Targets: antibioticmech:aro-e44e701df2.

The ARO relations are current and the native evidence-needed flags are appropriate. Inspected original studies establish comparator inhibition or resistant-subunit function, not direct exact clorobiocin binding to these sensitive subunits. Absence of that experiment in these papers does not prove the database relations false.

### resistance_mechanisms[2]

evidence: supported. Targets: antibioticmech:aro-e44e701df2.

Exact clorobiocin cellular selection and the 1992 original abstract support E. coli GyrB-associated resistance. Per-allele quantitative curation still requires full original methods/results; no taxon-wide breakpoint follows.

### resistance_mechanisms[0], [1], [3] and [4]

evidence: unknown. Targets: antibioticmech:aro-e44e701df2.

All four are correctly attributed current ARO assertions. S. aureus and Bartonella originals measured other aminocoumarins; the 2003 ParY experiment likewise used comparator drugs, while 2004 exact clorobiocin assay scope remains unverified. Intrinsic resistant variants, selected mutants and exact alleles must remain distinct. No automatic deletion is justified by these bounded checks.

### Exact producer, strain, BGC and method scope

provenance: supported. Targets: antibioticmech:aro-e44e701df2.

The chemical join and taxonomy are coherent, and inspected original production evidence supports DS 12.976. MIBiG quality and method metadata remain source-qualified. The native cautious legacy-reference note reflects its unreviewed import and may be updated only through explicit evidence adjudication.

### Optional quantitative activity, mechanism enum and causal graph

completeness: unknown. Targets: antibioticmech:aro-e44e701df2.

Useful exact primary sources exist, but optional enrichment must preserve fragment binding versus cellular inhibition, MIC versus selection concentration, partial DNA-synthesis inhibition and lack of detected RecA induction under the tested conditions. Missing optional objects alone is not a defect.

### Clinical status, datasets, synonyms and product forms

scope: not_applicable. Targets: antibioticmech:aro-e44e701df2.

No such native assertion is populated. Clinical approval of novobiocin and producing-strain biosynthetic enzymes do not establish corresponding claims for clorobiocin.

### Actual owner chain, adopted leads and six history events

provenance: supported. Targets: antibioticmech:aro-e44e701df2.

All maintained owners were captured before detailed judgment and all original hashes preserved. Every adopted definition/producer PMID was resolved; further ARO-linked citations have explicit original-versus-review dispositions. Historical SEEDED/reseed events were not mistaken for scientific review.

### Focused deterministic checks

schema: supported. Targets: antibioticmech:aro-e44e701df2.

Molecular, schema and strict validation passed. The minor citation-scope issue is scientific provenance rather than invalid native YAML.

## Findings

### F1: The definition citation does not cover its direct-binding and producer clauses

minor / open / confirmed; issue key: clorobiocin-definition-primary-citation-scope.

definition_source selects PMID:6154685 alone. The original 1980 paper establishes cellular effects and genetic linkage near gyrB, but does not directly measure clorobiocin binding or establish the named Streptomyces producer. The maintained ARO row already includes PMID:12044152, whose binding experiment and exact deposited ligand support the direct GyrB clause. PMID:12480894 supplies independent exact-strain production evidence. Preserve the supported definition and repair claim-level citation coverage through maintained source/transform or curator-owned evidence; do not portray the 1980 study itself as a direct-binding experiment.

## Recommended Actions And Acceptance Checks

### A1

Restore narrow primary citation coverage for the supported definition.

- Retain PMID:6154685 for cellular/genetic gyrase evidence without calling it a direct-binding assay.
- Attach PMID:12044152 and the exact E. coli GyrB fragment context to the binding clause, and PMID:12480894 to the DS 12.976 production claim.
- Preserve the maintained multi-reference source list and supported identity; do not substitute a neighboring aminocoumarin.
- Use the maintained source/curator workflow and required native schema, strict, provenance/history and QC checks after separately authorized curation.

### A2

Optionally adjudicate individual ARO target/resistance claims and add exact primary activity or producer evidence.

- Keep all native database-only and PRIMARY_EVIDENCE_NEEDED qualifications unless exact-compound evidence supports an explicit upgrade.
- Do not transfer novobiocin/coumermycin MICs, allele effects or ParE/ParY binding to clorobiocin merely from class membership.
- Resolve the upstream ARO:3003253 PMID:1260451 mismatch without silently replacing the identifier or claiming the native record directly cites it.
- Preserve organism, strain, resistant versus sensitive subunit, original material, assay endpoint, concentration units and uncertainty.
- Treat the MIBiG v4 versus exact adopted 4.0.1 archive access boundary explicitly; do not promote all method categories based solely on the first producer paper.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/clorobiocin.yaml; Entire 172-line YAML: identity/class, three xrefs, five resistance entries, four targets, producer and six history events | supports | The record is a neutral stereodefined parent, ANTIBACTERIAL, SEEDED and MINTED. The definition cites PMID:6154685. All resistance evidence explicitly says database assertion; all four direct-target entries carry PRIMARY_EVIDENCE_NEEDED and unspecified assay/organism context. The MIBiG legacy citation is explicitly not yet adjudicated as producer proof. No native quantitative activity, causal graph, clinical-product or dataset assertion is populated. |
| owners | data/raw/aro_antibiotics.tsv; aro_resistance_edges.tsv; aro_target_edges.tsv; pubchem_structures.tsv; mibig_producers.tsv; Exact rows 72, 2029-2033, 76-79, 16 and 373; conf/aro_target_roles.tsv and source transforms | supports | All twelve source rows were read. The ARO identity row retains three definition PMIDs, while scripts/seed_from_sources.py selects only definition_refs[0]. Target role mapping preserves explicit primary-evidence-needed status. MIBiG linking requires exact full key and complete stereo and labels one-compound entry evidence COMPOUND_SPECIFIC. These are the actual owners, replacing the generic initial ChEBI ownership only in the expanded capture. |
| rubric | .claude/skills/review-yaml-record/SKILL.md; docs/record-review-profile.md; native review checklist; Claim-level citation scope, source attribution and optional fields | supports | Qualified database assertions are not represented as primary experiments. Missing optional activity, mode_of_action or causal graphs is not automatically a native defect. Exact source support is assessed independently from validator success and historical SEEDED status. |
| chemistry | Independent native molecular and source-mint calculations; 314-chemistry.json; 313314-xref-chemistry.json; 314-deposition-chemistry.json | supports | Both native encodings reproduce FJAQNRBDVKIIKK-LFLQOBSNSA-N, one neutral component, four assigned stereocentres, formula C35H37ClN2O11 and exact mass 696.208587684. Average mass 697.137 rounds to the native 697.1. The ARO mint is reproducible. Current PubChem, ChEMBL, official MIBiG v4 entry and PDB CBN isomeric encodings independently reproduce the complete native key. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/54706138/property/InChI,InChIKey,IsomericSMILES,MolecularFormula,MolecularWeight,ExactMass/JSON; Current CID 54706138 full properties | supports | The asserted PubChem identifier resolves to the same exact parent, charge, formula and full stereochemical key. Its current graph agrees with the historical adopted PubChem row. |
| chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL303984.json; Current CHEMBL303984 complete molecule record | supports | The asserted ChEMBL record has the same complete molecular graph and full key. No salt, hydrate, mixture or stereochemical mismatch was identified. |
| aro-identity | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3000132; Current ARO:3000132 and retained ARO:3000103/ARO:0001001 term lookups | supports | The exact antibiotic term, aminocoumarin parent/class and target-alteration mechanism term resolve. The current antibiotic definition retains PMIDs 12044152, 6154685 and 8231802. This corroborates source attribution, while each original publication has a distinct experimental scope. |
| aro-resistance | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms; Five 314-aro-*-confers_resistance_to_antibiotic.json responses and term descriptions | supports | All five retained determinant terms, ARO:3003301, 3003302, 3003303, 3003314 and 3003318, currently link to clorobiocin ARO:3000132. The last is described as an intrinsically resistant ParY variant despite its mutant label. These relations verify the native database assertions, not every exact clorobiocin allele/phenotype. |
| aro-targets | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms; Four 314-aro-*-targeted_by_antibiotic.json responses plus role-map contexts | supports | ARO:3000023, 3000734, 3003253 and 3003260 all currently link to clorobiocin. The two GyrB terms overlap semantically but are distinct retained source terms. The native record does not claim a measured affinity, specific organism or primary experiment for any imported target. |
| adapter | iModulonDB structured catalog and exact gene searches; 314-adapter-results.json; all four actual commands exited zero before open protein research | context_only | Catalog and gene searches identified e_coli/precise1k/b3699 (gyrB), s_aureus/staph_precise108/USA300HOU_RS00025 (gyrB), and USA300HOU_RS06890 (parE), each with zero component hits. No covered Bartonella, S. rishiriensis or exact producer dataset was available. No unrelated Streptomyces surrogate was substituted. These are gene annotations, not drug-binding or resistance experiments. |
| original1980 | https://doi.org/10.1128/jb.142.1.153-161.1980; PMID:6154685 / PMC293920; all nine pages read by OCR; original p154 Figure 1/Methods and p159 Table 1 visually inspected | supports | The study uses clorobiocin isolated by L. Ninet and supplied through May and Baker, prepared fresh in ethanol. E. coli K-12 LE234 derivatives show preferential DNA-synthesis inhibition, altered transcription/division and resistant mutants mapping at or near gyrB. The paper infers gyrase involvement from cellular/genetic evidence; it does not measure direct ligand binding or establish the named Streptomyces producer. |
| original1980-assays | https://doi.org/10.1128/jb.142.1.153-161.1980; Original pp154-159, twofold broth assay, nucleotide incorporation and Table 1 | supports | MIC used tryptone soy broth absorbance after 16 h; initial K-12 strains gave 30-60 micrograms/mL. At 50 micrograms/mL cellular DNA synthesis was strongly inhibited but persisted. Mutants selected at 100 micrograms/mL and tested at 50 were LE316, LE701 and LE739; LE234 was sensitive. These are experimental selection/phenotype conditions, not clinical breakpoints. No detectable RecA/protein-X induction was observed under tested conditions. |
| binding-primary | https://doi.org/10.1021/bi0159837; PMID:12044152; author-deposited original text pp7217-7222, Methods, Table 2, Results and figure captions | supports | Purified clorobiocin was assayed with the E. coli 24-kDa GyrB fragment in 3% methanol at pH 7.5 and 25 C. Displacement ITC gives association constant (8.6 ± 2.2)×10^8 M^-1 and approximately 1:1 binding. The cocrystal places the ligand at the ATP-pocket entrance. This is direct fragment-binding evidence, distinct from a cellular MIC. Direct downloads failed, but the author PDF text was readable; requested screenshots supplied no inspectable pixels, so figures were not visually verified. |
| pdb | https://data.rcsb.org/rest/v1/core/entry/1KZN; Deposited 1KZN entry, polymer entity 1, nonpolymer entity 2 and chemical component CBN | supports | The experimental X-ray deposition cites PMID:12044152 and explicitly identifies E. coli GyrB 24-kDa domain with clorobiocin ligand CBN. The ligand has the exact native full key; independent parsing confirms it. Refined resolution is 2.3 angstrom. The UniProt P0AES6 mapping is deposition context, not a newly curated protein example or evidence for ParE/ParY. |
| producer-primary | https://doi.org/10.1099/00221287-148-12-3901; PMID:12480894; author-uploaded original Methods and Results pp3902-3908, metabolite analysis and cloR experiment | supports | The producer is S. roseochromogenes var. oscitans DS 12.976 from Aventis, grown for production at 33 C for seven days. Major peak A was matched to authentic clorobiocin by HPLC, FAB-MS and proton NMR. cloR deletion abolished production; Ring A feeding restored about one-third of wild-type output. Minor same-mass peak B was only proposed as a positional isomer and must not be conflated with exact clorobiocin. This directly supports the producer link; the paper does not establish all retained MIBiG method categories. |
| mibig | https://dl.secondarymetabolites.org/mibig/mibig_json_4.0.tar.gz; Official release 4.0 archive, BGC0000832 entry version 4; all entry fields inspected | supports | The active questionable-quality entry has one exact clorobiocin compound, NCBITaxon:1352936, locus AF329398.1 and the retained knock-out, enzymatic-assay and heterologous-expression evidence categories. Independent chemical parsing matches the full native key. Categories are entry/locus-level metadata; one compound explains the seeder scope, but the first legacy paper alone does not verify every method. |
| mibig-version | https://zenodo.org/records/14835872; Official release landing page; repository MANIFEST archive URL; separate archive-access boundary | context_only | The exact manifest-linked landing page identifies release 4.0.1 with a file named mibig_json_4.0.tar.gz. Its download/API returned 403. The independently downloaded official 4.0 archive corroborates entry version 4 and substantive fields but was not claimed byte-identical to the adopted 4.0.1 package. The older official GitHub copy is only historical context. |
| taxonomy | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1352936; ENA taxonomy NCBITaxon:1352936 | supports | The taxon resolves at strain rank to Streptomyces roseochromogenus subsp. oscitans DS 12.976 and lists roseochromogenes spellings as synonyms. Native shortened taxon_label plus its separate strain field describes that same strain; spelling variation is not evidence of a different producer. |
| saureus-comparator | https://doi.org/10.1128/AAC.49.9.3810-3815.2005; PMID:16127057 / PMC1195401; full Methods, Results/Discussion, Tables 1-2 and figure captions | context_only | S. aureus RN4220 mutants were selected with novobiocin and tested with novobiocin, coumermycin A1 and quinolone comparators. Agar-dilution MICs and purified gyrase/topoisomerase-IV inhibition were measured. Some GyrB substitutions increased novobiocin resistance without increasing coumermycin resistance. ParE mutations arose after GyrB changes. No clorobiocin experiment is reported in these methods/tables; neither exact clorobiocin allele resistance nor direct clorobiocin-ParE binding follows automatically. |
| bartonella-comparator | https://doi.org/10.1128/AAC.42.11.2906; PMID:9797224 / PMC105964; material, selection/MIC methods, Results, Tables 1-3 and Discussion | context_only | B. bacilliformis KC583 mutants were selected and tested with Sigma coumermycin A1 in erythrocyte-supplemented heart-infusion agar. The seven-day MIC endpoint and GyrB substitutions concern that drug; clorobiocin appears only in background class discussion. The original table contains an Arg184 Glu/Gln inconsistency, another reason to inspect exact source sequences before allele curation. No clorobiocin MIC or exact resistance phenotype was transferred. |
| ecoli-resistance | https://doi.org/10.1111/j.1365-2958.1992.tb00886.x; PMID:1323022; complete original abstract and publisher Summary | supports | The original explicitly compares chlorobiocin, novobiocin and coumermycin in E. coli mutant GyrB ATPase/supercoiling assays. It identifies Arg136 substitutions and Gly164Val and reports different drug-susceptibility patterns. This is exact-name clorobiocin resistance-mechanism support at abstract depth. Full assay concentrations, per-allele effects and material details were not recovered and are not invented. |
| pary2003 | https://doi.org/10.1128/AAC.47.3.869-877.2003; PMID:12604514 / PMC149333; complete main text, Methods, Tables 1-3 and figure captions | context_only | The title includes clorobiocin because its biosynthetic cluster is investigated. Functional resistance experiments express S. rishiriensis genes in S. lividans TK24 and test novobiocin or coumermycin A1, using about 10^6 spores and six-day growth at 30 C. Table 2 has no clorobiocin column. Purification of resistant proteins failed, and the proposed sensitive ParY proteins were inferred from sequence/hybridization. These experiments do not directly demonstrate clorobiocin binding to sensitive ParY. |
| pary2004 | https://doi.org/10.1099/mic.0.26867-0; PMID:14993313; complete original abstract; full-article and thesis access boundaries | context_only | The 2004 paper subsequently purified resistant S. rishiriensis subunits and functionally distinguished GyrA/GyrBR ATP-dependent supercoiling from ParX/ParYR ATP-dependent decatenation/relaxation. Thus the 2003 tentative functional assignment is not the final state of evidence. Exact clorobiocin dose-response/material scope was not verified from the abstract. Publisher full text failed; the author thesis yielded front matter only before later 503 responses. |
| review-leads | https://www.ebi.ac.uk/europepmc/webservices/rest/search; PMIDs 8231802, 1657531 and 9293187; complete available abstracts and publication types | context_only | The adopted definition lead 8231802 is a coumarin-gyrase review. Linked target leads 1657531 and 9293187 are gyrase/topoisomerase reviews, the latter focused on quinolones. They provide background/discovery, not new exact clorobiocin binding experiments or grounds to import quinolone DNA-cleavage/SOS mechanisms. |
| upstream-citation | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3003253; ARO:3003253 obo_definition_citation versus resolved PMID:1260451 | context_only | The current sensitive-ParY term cites PMID:1260451, which resolves to a 1976 hamster GABA-receptor study. PMID:12604514 is the relevant 2003 topoisomerase paper, but an upstream truncation is only an inference. Native evidence cites the ARO term, not the wrong PMID; this source-quality problem is retained as a follow-up, not misreported as a native broken-reference finding. |
| search | Ignored-inclusive local ownership and primary-source follow-up; 314-local-hits.txt; 314-focused-local-search.json; original source/core files | context_only | Search included hidden and ignored files. Prior aminocoumarin tests/reports were discovery only. No exact clorobiocin curator/CARD adjudication override was found. All three adopted ARO definition leads and the MIBiG legacy lead were resolved; linked target/resistance primary sources were checked individually at the stated reading depths. |
| access | Free public retrieval and reading manifests; 313314-fetch/primary/scans/followup/recovery; 314-final-primary-fetch, recover-pdfs, target-fetch and mibig-manifest-fetch | context_only | PMC base article URLs recovered full comparator papers after query URLs returned browser challenges; EPMC XML and BioC routes did not return usable full text. Author PDF/browser text recovered binding and producer passages despite direct 403 downloads. Screenshots returned no inspectable pixels. The 2004 full paper and exact MIBiG 4.0.1 archive remained inaccessible. No failed HTML was treated as PDF or as a read figure. |
| gates | Actual focused chemistry, schema and strict validation; 314-focused-results.json and companion logs | supports | All three focused commands exited zero on the unchanged record. These deterministic results do not resolve definition citation placement or exact ligand/allele evidence boundaries. |

## Limits And Additional Notes

- The 1980 paper was read across all nine OCR pages and original Figure 1/Methods and Table 1 were visually inspected. The 2003/2005 full main text and tables were read; the 1998 material, susceptibility, result and discussion sections/tables were inspected. Figures beyond the specified scans were not independently quantified.
- The 2002 binding paper was read through author-deposited full PDF text (Methods, Results and Discussion); screenshot responses lacked inspectable pixels. The independently inspected PDB deposition and ligand graph support exact binding identity. Source prose/caption residue-label inconsistencies were not converted into residue-level curation.
- The producer paper was inspected through author-uploaded original Methods and relevant Results, including HPLC/MS/NMR and deletion/rescue. Plot captions/text were read; no claim of visual verification of the original producer plots is made.
- PMID:1323022 and PMID:14993313 remain abstract-level for exact assay adjudication. The three review articles were used only for background/discovery. Additional legacy MIBiG references not adopted into this record were not exhaustively reviewed.
- The exact manifest-linked MIBiG 4.0.1 archive/API returned 403. Its official landing page version was verified; another official release 4.0 archive corroborated entry version 4 but was not claimed byte-identical.
- No clorobiocin-specific resistance or direct-binding experiment was verified for every imported ParE/ParY or non-E. coli determinant. These are unresolved source-scope boundaries, not proof of absent biology or grounds for blanket deletion.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native record, source table, status or history was altered.
- Focused native schema/strict checks used batch 032; independent chemistry used the existing batch 019 RDKit interpreter against batch 032 cwd.
- All optional links, tags and notes were checked for this exact target. Source publications, compound forms and taxon/allele scopes were not inherited from neighboring records.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T133822Z-clorobiocin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Clorobiocin: supported exact identity and gyrase binding with a narrow definition-citation
  gap'
started_at: '2026-10-21T13:22:50Z'
finished_at: '2026-10-21T13:38:22Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the native record. All native fields
    and actual maintained rows were read. Independent chemistry, official chemical
    and ontology groundings, structured protein adapter, original cellular studies,
    deposited binding structure and original producer evidence were assessed with
    explicit reading and access boundaries.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'The exact clorobiocin structure, antibacterial activity, E. coli GyrB binding
  and DS 12.976 producer are supported. The definition assigns all claims to a 1980
  cellular/genetic paper; its direct-binding and producer clauses need appropriately
  scoped primary citations. This is a minor provenance correction. The nine explicitly
  qualified ARO target/resistance assertions remain database claims: related-drug
  experiments do not establish every clorobiocin-specific phenotype.'
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
  - path: data/antibiotics/antibacterial/clorobiocin.yaml
    sha256: 4e73efdaeff849a22524531769f50afc1392ca20336c536ca8b2ae9e222228cc
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
  - path: CLAUDE.md
    sha256: 36fb92f8919481cfbf3f17ddde4a1e244c81f76c64396dbbac910c4815fb9f16
    role: context
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
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
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: data/raw/mibig_producers.tsv
    sha256: d55289619e77e035ed437d432dd692ab382f254c3841c9a314752ef22578a01b
    role: context
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
  - path: scripts/card_evidence_reviews.py
    sha256: f9ec8aff30066bf04b9c2757af7d6f5d179d045e57b9f3b352bbed0b851f50a8
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
  - path: scripts/extract_mibig_producers.py
    sha256: a078cdf4c9b2d09999800ab7ae03f93d3972f29b7d2f460ebbbe7d7ec6b31c53
    role: context
  - path: tests/test_aminocoumarin_reference_followup.py
    sha256: 11de72cf50cd46935698167d1fb2a9e0248d1a6e213fd42c242f4d303bb71c01
    role: context
  - path: tests/test_aminocoumarin_primary_curation.py
    sha256: 8dc5cdf7f027c6912a515cc5193a42b0736ebd4a37e6f5950f3153e63a8a552e
    role: context
targets:
- target_id: antibioticmech:aro-e44e701df2
  path: data/antibiotics/antibacterial/clorobiocin.yaml
  label: clorobiocin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, definition and class
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Five imported resistance assertions
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Four imported target assertions
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Native target relation and evidence-status mapping
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact structure
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/mibig_producers.tsv
    role: Producer and BGC assertion
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_mibig_producers.py
    role: MIBiG extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated source-owned fields
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Any evidence-scope overrides
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Any grounding or exclusion override
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 314; one exact record. All 13 original input hashes were
    preserved and all 33 expanded hashes were rechecked.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-e44e701df2
  exclusions:
  - target: Novobiocin/coumermycin phenotypes as automatic clorobiocin measurements;
      biosynthetic enzymes as antibacterial direct targets
    reason: Exact ligand, organism, allele, assay and biological role differ. Native
      entries already identify database-only evidence, which is preserved while exact-compound
      support is adjudicated.
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-e44e701df2
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    314 (cwd /private/tmp/antibioticmech-record-reviews-032)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-e44e701df2
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/clorobiocin.yaml (cwd /private/tmp/antibioticmech-record-reviews-032)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-e44e701df2
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/clorobiocin.yaml --out /private/tmp/am-review-session/314-strict.tsv
    (cwd /private/tmp/antibioticmech-record-reviews-032)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:aro-e44e701df2
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
  - antibioticmech:aro-e44e701df2
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
  - antibioticmech:aro-e44e701df2
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
  - antibioticmech:aro-e44e701df2
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
  - antibioticmech:aro-e44e701df2
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
  - antibioticmech:aro-e44e701df2
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
  - antibioticmech:aro-e44e701df2
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
  - antibioticmech:aro-e44e701df2
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
  - antibioticmech:aro-e44e701df2
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/clorobiocin.yaml
  locator: 'Entire 172-line YAML: identity/class, three xrefs, five resistance entries,
    four targets, producer and six history events'
  accessed_at: '2026-10-21T13:37:32Z'
  support: supports
  summary: The record is a neutral stereodefined parent, ANTIBACTERIAL, SEEDED and
    MINTED. The definition cites PMID:6154685. All resistance evidence explicitly
    says database assertion; all four direct-target entries carry PRIMARY_EVIDENCE_NEEDED
    and unspecified assay/organism context. The MIBiG legacy citation is explicitly
    not yet adjudicated as producer proof. No native quantitative activity, causal
    graph, clinical-product or dataset assertion is populated.
  snapshot_sha256: 91269af1bf4313474501b6ab63ef5dd5209fb1817de744b592e70fefb4a72f15
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; aro_resistance_edges.tsv; aro_target_edges.tsv;
    pubchem_structures.tsv; mibig_producers.tsv
  locator: Exact rows 72, 2029-2033, 76-79, 16 and 373; conf/aro_target_roles.tsv
    and source transforms
  accessed_at: '2026-10-21T13:37:32Z'
  support: supports
  summary: All twelve source rows were read. The ARO identity row retains three definition
    PMIDs, while scripts/seed_from_sources.py selects only definition_refs[0]. Target
    role mapping preserves explicit primary-evidence-needed status. MIBiG linking
    requires exact full key and complete stereo and labels one-compound entry evidence
    COMPOUND_SPECIFIC. These are the actual owners, replacing the generic initial
    ChEBI ownership only in the expanded capture.
  snapshot_sha256: 91269af1bf4313474501b6ab63ef5dd5209fb1817de744b592e70fefb4a72f15
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/review-yaml-record/SKILL.md; docs/record-review-profile.md;
    native review checklist
  locator: Claim-level citation scope, source attribution and optional fields
  accessed_at: '2026-10-21T13:37:32Z'
  support: supports
  summary: Qualified database assertions are not represented as primary experiments.
    Missing optional activity, mode_of_action or causal graphs is not automatically
    a native defect. Exact source support is assessed independently from validator
    success and historical SEEDED status.
- evidence_id: chemistry
  kind: validation
  reference: Independent native molecular and source-mint calculations
  locator: 314-chemistry.json; 313314-xref-chemistry.json; 314-deposition-chemistry.json
  accessed_at: '2026-10-21T13:37:32Z'
  support: supports
  summary: Both native encodings reproduce FJAQNRBDVKIIKK-LFLQOBSNSA-N, one neutral
    component, four assigned stereocentres, formula C35H37ClN2O11 and exact mass 696.208587684.
    Average mass 697.137 rounds to the native 697.1. The ARO mint is reproducible.
    Current PubChem, ChEMBL, official MIBiG v4 entry and PDB CBN isomeric encodings
    independently reproduce the complete native key.
  snapshot_sha256: 53b97182b958178efb0791327b77ef44a45290c5e8dbcac4df9b28191a725c7b
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/54706138/property/InChI,InChIKey,IsomericSMILES,MolecularFormula,MolecularWeight,ExactMass/JSON
  locator: Current CID 54706138 full properties
  accessed_at: '2026-10-21T13:25:45.088188Z'
  support: supports
  summary: The asserted PubChem identifier resolves to the same exact parent, charge,
    formula and full stereochemical key. Its current graph agrees with the historical
    adopted PubChem row.
  snapshot_sha256: 1b626a94816ee4209c88a3b50f96784a5cd46446cc47bab5c8f54a8dfcfec5a0
- evidence_id: chembl
  kind: authority
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL303984.json
  locator: Current CHEMBL303984 complete molecule record
  accessed_at: '2026-10-21T13:25:45.183680Z'
  support: supports
  summary: The asserted ChEMBL record has the same complete molecular graph and full
    key. No salt, hydrate, mixture or stereochemical mismatch was identified.
  snapshot_sha256: bc98fc16ed48c3e5b7d078607d492745663bcd442117741562e61e2162cef495
- evidence_id: aro-identity
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3000132
  locator: Current ARO:3000132 and retained ARO:3000103/ARO:0001001 term lookups
  accessed_at: '2026-10-21T13:25:46.266089Z'
  support: supports
  summary: The exact antibiotic term, aminocoumarin parent/class and target-alteration
    mechanism term resolve. The current antibiotic definition retains PMIDs 12044152,
    6154685 and 8231802. This corroborates source attribution, while each original
    publication has a distinct experimental scope.
  snapshot_sha256: 4bdd94155a0ed023452871f5cdfa4895bc3ad04aedae99af626c0848e8df4981
- evidence_id: aro-resistance
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms
  locator: Five 314-aro-*-confers_resistance_to_antibiotic.json responses and term
    descriptions
  accessed_at: '2026-10-21T13:37:32Z'
  support: supports
  summary: All five retained determinant terms, ARO:3003301, 3003302, 3003303, 3003314
    and 3003318, currently link to clorobiocin ARO:3000132. The last is described
    as an intrinsically resistant ParY variant despite its mutant label. These relations
    verify the native database assertions, not every exact clorobiocin allele/phenotype.
  snapshot_sha256: 2b3e816432c6232657e7e3e75b6eda71bb07fcfcc589497c25eebac8be83b4b1
- evidence_id: aro-targets
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms
  locator: Four 314-aro-*-targeted_by_antibiotic.json responses plus role-map contexts
  accessed_at: '2026-10-21T13:37:32Z'
  support: supports
  summary: ARO:3000023, 3000734, 3003253 and 3003260 all currently link to clorobiocin.
    The two GyrB terms overlap semantically but are distinct retained source terms.
    The native record does not claim a measured affinity, specific organism or primary
    experiment for any imported target.
  snapshot_sha256: 90e005403fef50802a3041e7715533082cc31e409f5f27bbb98321a9873106c6
- evidence_id: adapter
  kind: database
  reference: iModulonDB structured catalog and exact gene searches
  locator: 314-adapter-results.json; all four actual commands exited zero before open
    protein research
  accessed_at: '2026-10-21T13:25:14.906659Z'
  support: context_only
  summary: Catalog and gene searches identified e_coli/precise1k/b3699 (gyrB), s_aureus/staph_precise108/USA300HOU_RS00025
    (gyrB), and USA300HOU_RS06890 (parE), each with zero component hits. No covered
    Bartonella, S. rishiriensis or exact producer dataset was available. No unrelated
    Streptomyces surrogate was substituted. These are gene annotations, not drug-binding
    or resistance experiments.
  snapshot_sha256: 9420a50c7cde15362f858741b8285f770d20b6254e3df94008b0911cd2bccffd
- evidence_id: original1980
  kind: primary_source
  reference: https://doi.org/10.1128/jb.142.1.153-161.1980
  locator: PMID:6154685 / PMC293920; all nine pages read by OCR; original p154 Figure
    1/Methods and p159 Table 1 visually inspected
  accessed_at: '2026-10-21T13:27:35.323149Z'
  support: supports
  summary: The study uses clorobiocin isolated by L. Ninet and supplied through May
    and Baker, prepared fresh in ethanol. E. coli K-12 LE234 derivatives show preferential
    DNA-synthesis inhibition, altered transcription/division and resistant mutants
    mapping at or near gyrB. The paper infers gyrase involvement from cellular/genetic
    evidence; it does not measure direct ligand binding or establish the named Streptomyces
    producer.
  snapshot_sha256: 9714ae1f6df1c3c36219b6435753ef5cac3b029442e627626374e6420d3c2ad2
- evidence_id: original1980-assays
  kind: primary_source
  reference: https://doi.org/10.1128/jb.142.1.153-161.1980
  locator: Original pp154-159, twofold broth assay, nucleotide incorporation and Table
    1
  accessed_at: '2026-10-21T13:27:35.590379Z'
  support: supports
  summary: MIC used tryptone soy broth absorbance after 16 h; initial K-12 strains
    gave 30-60 micrograms/mL. At 50 micrograms/mL cellular DNA synthesis was strongly
    inhibited but persisted. Mutants selected at 100 micrograms/mL and tested at 50
    were LE316, LE701 and LE739; LE234 was sensitive. These are experimental selection/phenotype
    conditions, not clinical breakpoints. No detectable RecA/protein-X induction was
    observed under tested conditions.
  snapshot_sha256: 15d754067f9753862ae6c3320683c14c8446f9007697a27c57e1b4175ad914d1
- evidence_id: binding-primary
  kind: primary_source
  reference: https://doi.org/10.1021/bi0159837
  locator: PMID:12044152; author-deposited original text pp7217-7222, Methods, Table
    2, Results and figure captions
  accessed_at: '2026-10-21T13:35:08.102910Z'
  support: supports
  summary: Purified clorobiocin was assayed with the E. coli 24-kDa GyrB fragment
    in 3% methanol at pH 7.5 and 25 C. Displacement ITC gives association constant
    (8.6 ± 2.2)×10^8 M^-1 and approximately 1:1 binding. The cocrystal places the
    ligand at the ATP-pocket entrance. This is direct fragment-binding evidence, distinct
    from a cellular MIC. Direct downloads failed, but the author PDF text was readable;
    requested screenshots supplied no inspectable pixels, so figures were not visually
    verified.
  snapshot_sha256: 4d2e4182b4f47bbaa9038e0d043b820e62453fbd07a9a6b33f0203faf48c1d32
- evidence_id: pdb
  kind: primary_source
  reference: https://data.rcsb.org/rest/v1/core/entry/1KZN
  locator: Deposited 1KZN entry, polymer entity 1, nonpolymer entity 2 and chemical
    component CBN
  accessed_at: '2026-10-21T13:27:35.931275Z'
  support: supports
  summary: The experimental X-ray deposition cites PMID:12044152 and explicitly identifies
    E. coli GyrB 24-kDa domain with clorobiocin ligand CBN. The ligand has the exact
    native full key; independent parsing confirms it. Refined resolution is 2.3 angstrom.
    The UniProt P0AES6 mapping is deposition context, not a newly curated protein
    example or evidence for ParE/ParY.
  snapshot_sha256: ec46b2255d67a4a53adf33d84e8bf8a48e18e00d50daa5387008f6953621ffb4
- evidence_id: producer-primary
  kind: primary_source
  reference: https://doi.org/10.1099/00221287-148-12-3901
  locator: PMID:12480894; author-uploaded original Methods and Results pp3902-3908,
    metabolite analysis and cloR experiment
  accessed_at: '2026-10-21T13:35:08.102910Z'
  support: supports
  summary: The producer is S. roseochromogenes var. oscitans DS 12.976 from Aventis,
    grown for production at 33 C for seven days. Major peak A was matched to authentic
    clorobiocin by HPLC, FAB-MS and proton NMR. cloR deletion abolished production;
    Ring A feeding restored about one-third of wild-type output. Minor same-mass peak
    B was only proposed as a positional isomer and must not be conflated with exact
    clorobiocin. This directly supports the producer link; the paper does not establish
    all retained MIBiG method categories.
  snapshot_sha256: 4d2e4182b4f47bbaa9038e0d043b820e62453fbd07a9a6b33f0203faf48c1d32
- evidence_id: mibig
  kind: database
  reference: https://dl.secondarymetabolites.org/mibig/mibig_json_4.0.tar.gz
  locator: Official release 4.0 archive, BGC0000832 entry version 4; all entry fields
    inspected
  accessed_at: '2026-10-21T13:30:06.137207Z'
  support: supports
  summary: The active questionable-quality entry has one exact clorobiocin compound,
    NCBITaxon:1352936, locus AF329398.1 and the retained knock-out, enzymatic-assay
    and heterologous-expression evidence categories. Independent chemical parsing
    matches the full native key. Categories are entry/locus-level metadata; one compound
    explains the seeder scope, but the first legacy paper alone does not verify every
    method.
  snapshot_sha256: c5414257d7cc325aa709df7764ab5a0f138a5b20b4a9006c47ee02c2c4ec5cde
- evidence_id: mibig-version
  kind: authority
  reference: https://zenodo.org/records/14835872
  locator: Official release landing page; repository MANIFEST archive URL; separate
    archive-access boundary
  accessed_at: '2026-10-21T13:37:32Z'
  support: context_only
  summary: The exact manifest-linked landing page identifies release 4.0.1 with a
    file named mibig_json_4.0.tar.gz. Its download/API returned 403. The independently
    downloaded official 4.0 archive corroborates entry version 4 and substantive fields
    but was not claimed byte-identical to the adopted 4.0.1 package. The older official
    GitHub copy is only historical context.
  snapshot_sha256: 52a4046b436fab973c2e80eace5b1a63b892feb6a02f874e4f370ba11077c0e5
- evidence_id: taxonomy
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1352936
  locator: ENA taxonomy NCBITaxon:1352936
  accessed_at: '2026-10-21T13:25:45.582127Z'
  support: supports
  summary: The taxon resolves at strain rank to Streptomyces roseochromogenus subsp.
    oscitans DS 12.976 and lists roseochromogenes spellings as synonyms. Native shortened
    taxon_label plus its separate strain field describes that same strain; spelling
    variation is not evidence of a different producer.
  snapshot_sha256: 0f902be490495711d14c80e5a8c9c37e49e77cd4c41188bb81bd4fa690b05411
- evidence_id: saureus-comparator
  kind: primary_source
  reference: https://doi.org/10.1128/AAC.49.9.3810-3815.2005
  locator: PMID:16127057 / PMC1195401; full Methods, Results/Discussion, Tables 1-2
    and figure captions
  accessed_at: '2026-10-21T13:30:38.923413Z'
  support: context_only
  summary: S. aureus RN4220 mutants were selected with novobiocin and tested with
    novobiocin, coumermycin A1 and quinolone comparators. Agar-dilution MICs and purified
    gyrase/topoisomerase-IV inhibition were measured. Some GyrB substitutions increased
    novobiocin resistance without increasing coumermycin resistance. ParE mutations
    arose after GyrB changes. No clorobiocin experiment is reported in these methods/tables;
    neither exact clorobiocin allele resistance nor direct clorobiocin-ParE binding
    follows automatically.
  snapshot_sha256: 98d3be6e4f0d46d2c1fe89ad07ec4d216a79fa9652080b2ac95dec977e741ebe
- evidence_id: bartonella-comparator
  kind: primary_source
  reference: https://doi.org/10.1128/AAC.42.11.2906
  locator: PMID:9797224 / PMC105964; material, selection/MIC methods, Results, Tables
    1-3 and Discussion
  accessed_at: '2026-10-21T13:30:38.924065Z'
  support: context_only
  summary: B. bacilliformis KC583 mutants were selected and tested with Sigma coumermycin
    A1 in erythrocyte-supplemented heart-infusion agar. The seven-day MIC endpoint
    and GyrB substitutions concern that drug; clorobiocin appears only in background
    class discussion. The original table contains an Arg184 Glu/Gln inconsistency,
    another reason to inspect exact source sequences before allele curation. No clorobiocin
    MIC or exact resistance phenotype was transferred.
  snapshot_sha256: e66951034872c89978c483ae2939b33acd616f5e46c129302b9645e95ffb5612
- evidence_id: ecoli-resistance
  kind: primary_source
  reference: https://doi.org/10.1111/j.1365-2958.1992.tb00886.x
  locator: PMID:1323022; complete original abstract and publisher Summary
  accessed_at: '2026-10-21T13:26:49.137888Z'
  support: supports
  summary: The original explicitly compares chlorobiocin, novobiocin and coumermycin
    in E. coli mutant GyrB ATPase/supercoiling assays. It identifies Arg136 substitutions
    and Gly164Val and reports different drug-susceptibility patterns. This is exact-name
    clorobiocin resistance-mechanism support at abstract depth. Full assay concentrations,
    per-allele effects and material details were not recovered and are not invented.
  snapshot_sha256: e1097b5e6fd239dbf3180ed119cefa3eebc88f08b68e5e0581dbae478ad2ceae
- evidence_id: pary2003
  kind: primary_source
  reference: https://doi.org/10.1128/AAC.47.3.869-877.2003
  locator: PMID:12604514 / PMC149333; complete main text, Methods, Tables 1-3 and
    figure captions
  accessed_at: '2026-10-21T13:30:38.923861Z'
  support: context_only
  summary: The title includes clorobiocin because its biosynthetic cluster is investigated.
    Functional resistance experiments express S. rishiriensis genes in S. lividans
    TK24 and test novobiocin or coumermycin A1, using about 10^6 spores and six-day
    growth at 30 C. Table 2 has no clorobiocin column. Purification of resistant proteins
    failed, and the proposed sensitive ParY proteins were inferred from sequence/hybridization.
    These experiments do not directly demonstrate clorobiocin binding to sensitive
    ParY.
  snapshot_sha256: e6a1dd3b113997e7624588cd3120beee45663df719634db6b1db8543792a8015
- evidence_id: pary2004
  kind: primary_source
  reference: https://doi.org/10.1099/mic.0.26867-0
  locator: PMID:14993313; complete original abstract; full-article and thesis access
    boundaries
  accessed_at: '2026-10-21T13:26:49.137888Z'
  support: context_only
  summary: The 2004 paper subsequently purified resistant S. rishiriensis subunits
    and functionally distinguished GyrA/GyrBR ATP-dependent supercoiling from ParX/ParYR
    ATP-dependent decatenation/relaxation. Thus the 2003 tentative functional assignment
    is not the final state of evidence. Exact clorobiocin dose-response/material scope
    was not verified from the abstract. Publisher full text failed; the author thesis
    yielded front matter only before later 503 responses.
  snapshot_sha256: e1097b5e6fd239dbf3180ed119cefa3eebc88f08b68e5e0581dbae478ad2ceae
- evidence_id: review-leads
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search
  locator: PMIDs 8231802, 1657531 and 9293187; complete available abstracts and publication
    types
  accessed_at: '2026-10-21T13:26:49.137888Z'
  support: context_only
  summary: The adopted definition lead 8231802 is a coumarin-gyrase review. Linked
    target leads 1657531 and 9293187 are gyrase/topoisomerase reviews, the latter
    focused on quinolones. They provide background/discovery, not new exact clorobiocin
    binding experiments or grounds to import quinolone DNA-cleavage/SOS mechanisms.
  snapshot_sha256: e1097b5e6fd239dbf3180ed119cefa3eebc88f08b68e5e0581dbae478ad2ceae
- evidence_id: upstream-citation
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3003253
  locator: ARO:3003253 obo_definition_citation versus resolved PMID:1260451
  accessed_at: '2026-10-21T13:25:47.130085Z'
  support: context_only
  summary: The current sensitive-ParY term cites PMID:1260451, which resolves to a
    1976 hamster GABA-receptor study. PMID:12604514 is the relevant 2003 topoisomerase
    paper, but an upstream truncation is only an inference. Native evidence cites
    the ARO term, not the wrong PMID; this source-quality problem is retained as a
    follow-up, not misreported as a native broken-reference finding.
  snapshot_sha256: 46acc1eee0d8728023a1f5bb09b673fd5f88ad0bb6b59c669858ed254f02bb76
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local ownership and primary-source follow-up
  locator: 314-local-hits.txt; 314-focused-local-search.json; original source/core
    files
  accessed_at: '2026-10-21T13:37:32Z'
  support: context_only
  summary: Search included hidden and ignored files. Prior aminocoumarin tests/reports
    were discovery only. No exact clorobiocin curator/CARD adjudication override was
    found. All three adopted ARO definition leads and the MIBiG legacy lead were resolved;
    linked target/resistance primary sources were checked individually at the stated
    reading depths.
  snapshot_sha256: 74c9712ccdc18b59d9d12e85136816e541e4fd3e0c35281de20c83481e2e2b07
  search_scope: 2026-10-21; exact clorobiocin and chlorobiocin names, ARO:3000132,
    complete molecular key, all native PMID leads and linked ARO references. Repository-wide
    and focused curation/conf searches included hidden and ignored files. Free primary
    and official retrievals are bounded, not exhaustive literature-absence claims.
- evidence_id: access
  kind: search
  reference: Free public retrieval and reading manifests
  locator: 313314-fetch/primary/scans/followup/recovery; 314-final-primary-fetch,
    recover-pdfs, target-fetch and mibig-manifest-fetch
  accessed_at: '2026-10-21T13:37:32Z'
  support: context_only
  summary: PMC base article URLs recovered full comparator papers after query URLs
    returned browser challenges; EPMC XML and BioC routes did not return usable full
    text. Author PDF/browser text recovered binding and producer passages despite
    direct 403 downloads. Screenshots returned no inspectable pixels. The 2004 full
    paper and exact MIBiG 4.0.1 archive remained inaccessible. No failed HTML was
    treated as PDF or as a read figure.
  snapshot_sha256: 0dd54d299f22c4b3ae98123f6b3abd12466ba5b1ec0918bfff6f8337613075dd
  search_scope: 2026-10-21; exact clorobiocin and chlorobiocin names, ARO:3000132,
    complete molecular key, all native PMID leads and linked ARO references. Repository-wide
    and focused curation/conf searches included hidden and ignored files. Free primary
    and official retrievals are bounded, not exhaustive literature-absence claims.
- evidence_id: gates
  kind: validation
  reference: Actual focused chemistry, schema and strict validation
  locator: 314-focused-results.json and companion logs
  accessed_at: '2026-10-21T13:37:32Z'
  support: supports
  summary: All three focused commands exited zero on the unchanged record. These deterministic
    results do not resolve definition citation placement or exact ligand/allele evidence
    boundaries.
  snapshot_sha256: 1b6bc431d18b41eae6d5e11eb487046581f63c58c0df4bbd621029d34386f806
assessments:
- assessment_id: identity
  area: identity
  topic: Exact clorobiocin parent, class and molecular properties
  outcome: supported
  summary: Native encodings and all asserted chemical groundings agree. PDB ligand
    and MIBiG compound independently support the exact graph; no adjacent congener
    or salt replacement is needed.
  target_ids:
  - antibioticmech:aro-e44e701df2
  evidence_ids:
  - native
  - chemistry
  - pubchem
  - chembl
  - aro-identity
  - pdb
  - mibig
- assessment_id: grounding
  area: grounding
  topic: Source mint and MINTED status
  outcome: supported
  summary: ARO identity and mint are reproducible; MINTED is historical identifier
    provenance, not a claim of no external chemical matches. All asserted xrefs resolve
    exactly.
  target_ids:
  - antibioticmech:aro-e44e701df2
  evidence_ids:
  - owners
  - chemistry
  - pubchem
  - chembl
  - aro-identity
- assessment_id: definition-citation
  area: evidence
  topic: Nearest cited source for direct binding and producer clauses
  outcome: concern
  summary: PMID:6154685 provides cellular/genetic evidence for gyrase involvement
    but no direct binding measurement or named Streptomyces producer. The raw row
    already retains direct-binding PMID:12044152, omitted by the first-reference transform.
    The producer is independently supported by PMID:12480894. Correct citation coverage
    while retaining the supported definition.
  target_ids:
  - antibioticmech:aro-e44e701df2
  evidence_ids:
  - native
  - owners
  - original1980
  - binding-primary
  - pdb
  - producer-primary
- assessment_id: eligibility
  area: evidence
  topic: Antibacterial activity and E. coli mechanism
  outcome: supported
  summary: Direct cellular inhibition and resistant-mutant evidence support antibacterial
    eligibility. The binding paper and deposited exact complex independently establish
    the GyrB interaction; they do not make every downstream transcription/division
    effect a separate direct target.
  target_ids:
  - antibioticmech:aro-e44e701df2
  evidence_ids:
  - original1980
  - original1980-assays
  - binding-primary
  - pdb
- assessment_id: gyrb-targets
  area: evidence
  topic: molecular_targets[1] and [3]
  outcome: supported
  summary: Both imported GyrB terms are source-supported; exact E. coli fragment binding
    now provides a strong optional primary upgrade. The taxon-agnostic source terms
    should not be replaced with a species-specific accession, and deposition/adapter
    mapping alone is not a curated reviewed UniProt example.
  target_ids:
  - antibioticmech:aro-e44e701df2
  evidence_ids:
  - aro-targets
  - binding-primary
  - pdb
  - adapter
  - rubric
- assessment_id: pare-pary-targets
  area: evidence
  topic: molecular_targets[0] and [2]
  outcome: unknown
  summary: The ARO relations are current and the native evidence-needed flags are
    appropriate. Inspected original studies establish comparator inhibition or resistant-subunit
    function, not direct exact clorobiocin binding to these sensitive subunits. Absence
    of that experiment in these papers does not prove the database relations false.
  target_ids:
  - antibioticmech:aro-e44e701df2
  evidence_ids:
  - aro-targets
  - saureus-comparator
  - pary2003
  - pary2004
  - upstream-citation
  - rubric
- assessment_id: ecoli-resistance
  area: evidence
  topic: resistance_mechanisms[2]
  outcome: supported
  summary: Exact clorobiocin cellular selection and the 1992 original abstract support
    E. coli GyrB-associated resistance. Per-allele quantitative curation still requires
    full original methods/results; no taxon-wide breakpoint follows.
  target_ids:
  - antibioticmech:aro-e44e701df2
  evidence_ids:
  - aro-resistance
  - original1980-assays
  - ecoli-resistance
- assessment_id: other-resistance
  area: evidence
  topic: resistance_mechanisms[0], [1], [3] and [4]
  outcome: unknown
  summary: All four are correctly attributed current ARO assertions. S. aureus and
    Bartonella originals measured other aminocoumarins; the 2003 ParY experiment likewise
    used comparator drugs, while 2004 exact clorobiocin assay scope remains unverified.
    Intrinsic resistant variants, selected mutants and exact alleles must remain distinct.
    No automatic deletion is justified by these bounded checks.
  target_ids:
  - antibioticmech:aro-e44e701df2
  evidence_ids:
  - aro-resistance
  - saureus-comparator
  - bartonella-comparator
  - pary2003
  - pary2004
  - rubric
- assessment_id: producer
  area: provenance
  topic: Exact producer, strain, BGC and method scope
  outcome: supported
  summary: The chemical join and taxonomy are coherent, and inspected original production
    evidence supports DS 12.976. MIBiG quality and method metadata remain source-qualified.
    The native cautious legacy-reference note reflects its unreviewed import and may
    be updated only through explicit evidence adjudication.
  target_ids:
  - antibioticmech:aro-e44e701df2
  evidence_ids:
  - producer-primary
  - mibig
  - mibig-version
  - taxonomy
  - owners
- assessment_id: activity-graph
  area: completeness
  topic: Optional quantitative activity, mechanism enum and causal graph
  outcome: unknown
  summary: Useful exact primary sources exist, but optional enrichment must preserve
    fragment binding versus cellular inhibition, MIC versus selection concentration,
    partial DNA-synthesis inhibition and lack of detected RecA induction under the
    tested conditions. Missing optional objects alone is not a defect.
  target_ids:
  - antibioticmech:aro-e44e701df2
  evidence_ids:
  - original1980
  - original1980-assays
  - binding-primary
  - rubric
- assessment_id: other-domains
  area: scope
  topic: Clinical status, datasets, synonyms and product forms
  outcome: not_applicable
  summary: No such native assertion is populated. Clinical approval of novobiocin
    and producing-strain biosynthetic enzymes do not establish corresponding claims
    for clorobiocin.
  target_ids:
  - antibioticmech:aro-e44e701df2
  evidence_ids:
  - native
  - review-leads
  - producer-primary
- assessment_id: provenance
  area: provenance
  topic: Actual owner chain, adopted leads and six history events
  outcome: supported
  summary: All maintained owners were captured before detailed judgment and all original
    hashes preserved. Every adopted definition/producer PMID was resolved; further
    ARO-linked citations have explicit original-versus-review dispositions. Historical
    SEEDED/reseed events were not mistaken for scientific review.
  target_ids:
  - antibioticmech:aro-e44e701df2
  evidence_ids:
  - owners
  - native
  - search
  - review-leads
  - mibig-version
- assessment_id: schema
  area: schema
  topic: Focused deterministic checks
  outcome: supported
  summary: Molecular, schema and strict validation passed. The minor citation-scope
    issue is scientific provenance rather than invalid native YAML.
  target_ids:
  - antibioticmech:aro-e44e701df2
  evidence_ids:
  - chemistry
  - gates
findings:
- finding_id: F1
  issue_key: clorobiocin-definition-primary-citation-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: The definition citation does not cover its direct-binding and producer clauses
  description: definition_source selects PMID:6154685 alone. The original 1980 paper
    establishes cellular effects and genetic linkage near gyrB, but does not directly
    measure clorobiocin binding or establish the named Streptomyces producer. The
    maintained ARO row already includes PMID:12044152, whose binding experiment and
    exact deposited ligand support the direct GyrB clause. PMID:12480894 supplies
    independent exact-strain production evidence. Preserve the supported definition
    and repair claim-level citation coverage through maintained source/transform or
    curator-owned evidence; do not portray the 1980 study itself as a direct-binding
    experiment.
  target_ids:
  - antibioticmech:aro-e44e701df2
  field_paths:
  - definition_source
  - definition
  evidence_ids:
  - native
  - owners
  - original1980
  - binding-primary
  - pdb
  - producer-primary
  rule_id: native-review-checklist:Evidence and Provenance
  native_severity: minor non-blocking citation-scope/provenance gap
  normalization_reason: The identity, antibacterial eligibility and core definition
    are independently supported. The defect is incomplete citation placement caused
    by selecting one of several maintained references, rather than a false molecular
    target or producer.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Maintained definition reference list
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: First-reference definition_source selection
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/clorobiocin.yaml
    role: Curator-owned claim-level evidence through the validated writer
actions:
- action_id: A1
  description: Restore narrow primary citation coverage for the supported definition.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-e44e701df2
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Maintained definition reference list
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: First-reference definition_source selection
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/clorobiocin.yaml
    role: Curator-owned claim-level evidence through the validated writer
  acceptance_checks:
  - Retain PMID:6154685 for cellular/genetic gyrase evidence without calling it a
    direct-binding assay.
  - Attach PMID:12044152 and the exact E. coli GyrB fragment context to the binding
    clause, and PMID:12480894 to the DS 12.976 production claim.
  - Preserve the maintained multi-reference source list and supported identity; do
    not substitute a neighboring aminocoumarin.
  - Use the maintained source/curator workflow and required native schema, strict,
    provenance/history and QC checks after separately authorized curation.
- action_id: A2
  description: Optionally adjudicate individual ARO target/resistance claims and add
    exact primary activity or producer evidence.
  finding_ids: []
  target_ids:
  - antibioticmech:aro-e44e701df2
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Claim-level CARD evidence decisions
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Target relation mapping
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/clorobiocin.yaml
    role: Curator-owned primary targets, activity_spectrum and producer evidence
  acceptance_checks:
  - Keep all native database-only and PRIMARY_EVIDENCE_NEEDED qualifications unless
    exact-compound evidence supports an explicit upgrade.
  - Do not transfer novobiocin/coumermycin MICs, allele effects or ParE/ParY binding
    to clorobiocin merely from class membership.
  - Resolve the upstream ARO:3003253 PMID:1260451 mismatch without silently replacing
    the identifier or claiming the native record directly cites it.
  - Preserve organism, strain, resistant versus sensitive subunit, original material,
    assay endpoint, concentration units and uncertainty.
  - Treat the MIBiG v4 versus exact adopted 4.0.1 archive access boundary explicitly;
    do not promote all method categories based solely on the first producer paper.
limitations:
- The 1980 paper was read across all nine OCR pages and original Figure 1/Methods
  and Table 1 were visually inspected. The 2003/2005 full main text and tables were
  read; the 1998 material, susceptibility, result and discussion sections/tables were
  inspected. Figures beyond the specified scans were not independently quantified.
- The 2002 binding paper was read through author-deposited full PDF text (Methods,
  Results and Discussion); screenshot responses lacked inspectable pixels. The independently
  inspected PDB deposition and ligand graph support exact binding identity. Source
  prose/caption residue-label inconsistencies were not converted into residue-level
  curation.
- The producer paper was inspected through author-uploaded original Methods and relevant
  Results, including HPLC/MS/NMR and deletion/rescue. Plot captions/text were read;
  no claim of visual verification of the original producer plots is made.
- PMID:1323022 and PMID:14993313 remain abstract-level for exact assay adjudication.
  The three review articles were used only for background/discovery. Additional legacy
  MIBiG references not adopted into this record were not exhaustively reviewed.
- The exact manifest-linked MIBiG 4.0.1 archive/API returned 403. Its official landing
  page version was verified; another official release 4.0 archive corroborated entry
  version 4 but was not claimed byte-identical.
- No clorobiocin-specific resistance or direct-binding experiment was verified for
  every imported ParE/ParY or non-E. coli determinant. These are unresolved source-scope
  boundaries, not proof of absent biology or grounds for blanket deletion.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native record, source table, status or history was altered.
- Focused native schema/strict checks used batch 032; independent chemistry used the
  existing batch 019 RDKit interpreter against batch 032 cwd.
- All optional links, tags and notes were checked for this exact target. Source publications,
  compound forms and taxon/allele scopes were not inherited from neighboring records.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://pubchem.ncbi.nlm.nih.gov/compound/54706138
- https://doi.org/10.1021/bi0159837
- https://www.rcsb.org/structure/1KZN
- https://doi.org/10.1099/00221287-148-12-3901
tags:
- clorobiocin
- aminocoumarin
- primary-citation-scope
```
