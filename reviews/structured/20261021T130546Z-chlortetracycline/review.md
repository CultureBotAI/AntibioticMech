# Chlortetracycline: supported identity and ribosomal activity; qualify LamB loss and the Aureomycin trade name

- Review: 20261021T130546Z-chlortetracycline
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T12:48:43Z
- Finished UTC: 2026-10-21T13:05:46Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The neutral ChEBI chlortetracycline structure is internally coherent and supported by independently parsed official encodings. Original experiments support antibacterial activity, cell-free translation inhibition and ribosomal RNA interaction. All 15 resistance edges and the 16S target are faithfully attributed to CARD. One major finding concerns the missing loss/downregulation condition for LamB-mediated reduced permeability; a minor finding concerns the Aureomycin trade name being typed as an exact chemical synonym. The PubChem graph differs by keto-enol placement, not demonstrated epimerism, and is retained as an informational representation boundary. Other database-to-primary evidence gaps remain explicit limitations rather than automatic defects.

## Scope And Provenance

Whole native record: definition, eight synonyms, seven parents, two activity roles, structure, eight chemical xrefs, two drug xrefs, patent document, both source concepts, 15 resistance items, the 16S target and all five history events. Complete ChEBI/ARO source rows and all nine adopted citation leads were inspected.

Selection: Queue 295; initial thirteen hashes retained, six actual source/config/qualification owners appended, total nineteen inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:27644 | data/antibiotics/antibacterial/chlortetracycline.yaml | generated | chlortetracycline |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:27644 | No schema issues found. |
| strict | passed | True | CHEBI:27644 | One record; zero strict errors. |
| chemistry | passed | False | CHEBI:27644 | Both native encodings, formula, zero charge, five stereocentres, masses and both minted source IDs agree. |
| external-chemistry | passed | False | CHEBI:27644 | External encodings successfully parsed. PubChem differs from the native tautomer; this diagnostic does not assert every full key is identical. |
| tautomer-diagnostic | passed | False | CHEBI:27644 | Native and PubChem differ only in the InChI hydrogen layer; canonical tautomer diagnostics agree. DrugCentral matches the native full key. Canonicalization is diagnostic, not a proposed structure replacement. |
| Authoritative full QC | failed | True | CHEBI:27644 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:27644 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:27644 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:27644 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:27644 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:27644 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:27644 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:27644 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:27644 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Neutral exact ChEBI structure and chemical identifiers

identity: supported. Targets: CHEBI:27644.

Native encodings and accessible external graphs support the exact chlortetracycline seed. PubChem is a recognized keto-enol representation boundary; HMDB access is limited. No stereochemical correction is justified.

### Filing, roles, parent classes and producer definition

scope: supported. Targets: CHEBI:27644.

Broader chemical parents and antibacterial filing are coherent. Both drug roles are supported by the adopted authority; direct antibacterial experiments and original producer patent strengthen the native definition. Antiprotozoal primary-outcome verification remains limited.

### 16S RNA target and mechanism scope

evidence: supported. Targets: CHEBI:27644.

The source edge is real and the native record appropriately requests primary evidence. The 1991 original provides exact-compound functional and RNA-footprinting support, while ARO target PMID 9662506 is aminoglycoside-specific. The missing optional mode of action is not itself a defect in a SEEDED record.

### Fifteen database resistance assertions

evidence: concern. Targets: CHEBI:27644.

All fifteen source relationships resolve, but LamB must explicitly preserve loss/downregulation. Exact CTC phenotypes for Tet59 and Tet(W/N/W) have primary support; their detailed mechanisms remain inferred in that paper. Other linked primary abstracts and Tet44 full text do not uniformly establish exact CTC experiments.

### Chemical names versus trade-name aliases

identity: concern. Targets: CHEBI:27644.

Aureomycin is explicitly a trade name in KEGG yet is typed EXACT_SYNONYM in the ARO-derived slice. The independently sourced Aueromycin variant already has BRAND_NAME. Eremomycine is source-attested but historically unverified.

### Native evidence placement and optional enrichment

completeness: unknown. Targets: CHEBI:27644.

All adopted citations were checked at stated depth. No automatic mechanism, current approval, expression dataset, producer BGC or numeric activity is fabricated from source bibliographies. Primary additions are possible with material and assay scope preserved.

## Findings

### F1: Preserve the LamB loss or downregulation condition

major / open / confirmed; issue key: chlortetracycline-lamb-resistance-loss-condition.

resistance_mechanisms[12] names Escherichia coli LamB and repeats that CARD says it confers resistance, but does not state that decreased abundance or loss of this antibiotic influx porin is the resistance-associated state. Both the cited CARD definition and its original 2014 abstract make this condition explicit. REDUCED_PERMEABILITY alone does not specify which genetic/expression state produces the phenotype. Add a maintained qualification preserving the source condition; do not present ordinary LamB presence as a resistance determinant.

### F2: Retain trade-name semantics for Aureomycin

minor / open / confirmed; issue key: chlortetracycline-aureomycin-trade-name-type.

synonyms[6] types Aureomycin as EXACT_SYNONYM because the ARO importer assigns that type to untyped aliases. Official KEGG D07689 expressly marks Aureomycin TN. Preserve it as a trade-name alias with source provenance, consistent with the existing BRAND_NAME Aueromycin entry, without treating every product formulation as the exact neutral graph.

### F3: Record the PubChem keto-enol representation boundary

informational / open / confirmed; issue key: chlortetracycline-pubchem-keto-enol-representation.

PubChem 54675777 and the ChEBI-native graph have different full keys because their keto-enol hydrogen/bond placement differs. Their connectivity and stereo InChI layers agree, and a tautomer diagnostic converges. HARMONIZATION explicitly warns against inferring different compounds solely from unequal Standard InChIKeys. This is not a confirmed wrong-compound or epimer defect. Retain the observation when deciding whether exact xrefs need explicit tautomer qualification; do not replace native structure merely to match PubChem.

## Recommended Actions And Acceptance Checks

### A1

Add the missing LamB state qualification through the maintained CARD evidence-review path.

- Bind the qualification to the exact chlortetracycline resistance row/hash and native identifier/key, preserving CARD ownership. State that reduced LamB abundance or loss reduces antibiotic influx and is associated with resistance.
- Cite inspected CARD and PMID 24412198 at abstract depth; do not import numerical MICs or exact-agent results from the separate 2008 tetracycline study without original material verification.
- Regenerate through the owning seeder and confirm ordinary LamB presence is not described as sufficient for resistance; run focused validation and applicable corpus gates.

### A2

Correct the Aureomycin alias type reproducibly.

- Preserve the source alias text/provenance and emit BRAND_NAME for the official trade-name usage.
- Check the existing Aueromycin brand alias for any deliberate deduplication policy; do not invent a new salt-specific chemical identity from brand wording.
- Reseed the exact record and rerun schema/strict and reproduction checks.

### A3

Resolve optional identity-policy and primary-evidence enrichment questions without automatic status promotion.

- Document the PubChem tautomer boundary under repository identity policy; preserve native ChEBI structure and do not claim opposite stereochemistry from changed tautomer-sensitive CIP labels.
- For primary enrichment, keep the 1991 whole-cell MIC, cell-free translation and ribosomal footprint assays separate, with exact strains and material limitations.
- Retain Tet59/Tet(W/N/W) exact CTC phenotypes while qualifying mechanism inference. Do not upgrade Tet44 or other family evidence to exact CTC primary support without original experiments.
- Seek freely accessible exact HMDB and Eremomycine historical identity evidence if needed; access failures and optional missing fields alone are not defects.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/chlortetracycline.yaml; Entire YAML. | supports | SEEDED/EXACT/ANTIBACTERIAL. Neutral C22H23ClN2O8; native key CYDMQBQPVICBEU-XRNKAMNCSA-N. Resistance items expressly cite database assertions; the 16S direct target is PRIMARY_EVIDENCE_NEEDED, without invented organism/strain/assay. No numeric activity, clinical approval, causal graph or transcriptomic dataset is asserted. |
| owners | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv; data/raw/aro_resistance_edges.tsv; conf/sources.yaml; conf/aro_target_roles.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; curation/card_evidence_reviews.json; scripts/card_evidence_reviews.py; Complete rows 498, 114, 129 and 2598–2612 respectively; extraction and identity/assembly logic; attach_aro_mechanism and qualification loader/apply function. | supports | ChEBI owns the definition, structure, typed aliases, parents and roles; ARO adds its parent/class, untyped aliases, xrefs and mechanism edges. The seeder types every ARO alias EXACT_SYNONYM. The target map explicitly maps 16S RNA to direct nucleic-acid target while preserving PRIMARY_EVIDENCE_NEEDED. No matching existing CARD qualification was found. ChEBI source references remain curator leads rather than automatically becoming native claim evidence. No PubChem enrichment inventory, FDA or MIBiG row owns this record. |
| chemical | https://www.ebi.ac.uk/chebi/CHEBI:27644; https://card.mcmaster.ca/aro/3000528; https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL404520.json; https://rest.kegg.jp/get/C06571; https://www.lipidmaps.org/rest/compound/lm_id/LMPK07000004/all/json; https://files.rcsb.org/ligands/download/CTC.cif; https://drugcentral.org/drug/624/smiles; Complete chemical entries/descriptors and independent molecular parses. | supports | Current ChEBI, ARO visible graph, ChEMBL 404520, KEGG C06571, LIPID MAPS LMPK07000004, CCD CTC and DrugCentral 624 all resolve to the native full key. CAS 57-62-5 is independently attested in several official records, without paid registry access. The ChEBI systematic name agrees with native stereochemistry. CCD is a chemical-component identifier, not a whole PDB structure or a demonstration of antibacterial target engagement. |
| pubchem-tautomer | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/54675777/property/InChI,InChIKey,MolecularFormula,SMILES,IUPACName/JSON; docs/HARMONIZATION.md; Full official PubChem response; independent InChI/SMILES parse and explicit layer comparison; identity cautions in HARMONIZATION. | partial | PubChem 54675777 gives DHPRQBPJLMKORJ-XRNKAMNCSA-N. Native and PubChem share formula, charge, connectivity layer and stereochemical layers; hydrogen/bond placement differs between keto-enol representations. RDKit canonical tautomers agree, but this operation can erase tautomer-sensitive stereo and is not independent proof of all stereochemical identity. The explicit original InChI layer comparison is retained. PubChem exact native-key lookup returned 404. HARMONIZATION warns unequal Standard InChIKeys are not proof of different compounds. No epimer, wrong natural product or required whole-structure replacement is inferred. |
| ontology | CHEBI:139592; CHEBI:26878; CHEBI:26895; CHEBI:29347; CHEBI:50996; CHEBI:83403; ARO:3000050; CHEBI:35820; CHEBI:36047; Official definitions and ChEBI outgoing relationships, with raw role/class mappings. | supports | The six ChEBI parents are tertiary alpha-hydroxy ketone, tertiary alcohol, tetracyclines, monocarboxylic acid amide, tertiary amino compound and monochlorobenzenes; each is broader and chemically consistent. ARO 3000050 is the tetracycline antibiotic class. Antiprotozoal drug and antibacterial drug are both retained; antibacterial filing does not erase the antiprotozoal role. Current ChEBI also displays additional roles, but source-version differences are not silently treated as original seed errors. |
| drug-aliases | https://rest.kegg.jp/get/D07689; https://drugcentral.org/drugcard/624; https://www.ebi.ac.uk/chebi/CHEBI:27644; https://card.mcmaster.ca/aro/3000528; Drug entry NAME/FORMULA/SOURCE/EFFICACY, chemical descriptors and source synonym types. | partial | KEGG D07689 explicitly identifies chlortetracycline as INN and Aureomycin as TN. ChEBI supplies Aueromycin as a BRAND NAME, already typed correctly in native. The ARO spelling Aureomycin is emitted as EXACT_SYNONYM instead. Eremomycine is attested by ARO, but its independent historical naming basis was not resolved in the bounded exact-spelling search; no confusion with a similarly named glycopeptide is asserted. DrugCentral and KEGG belong in drug_xrefs, and their product lists do not create an unqualified current clinical approval claim. |
| hmdb-access | https://www.hmdb.ca/metabolites/HMDB0014401; https://www.hmdb.ca/metabolites/HMDB0014401.xml; Official page and structured endpoint attempts, plus ChEBI attribution. | unknown | Both direct HMDB routes returned 403; the web tool also failed to inspect the entry. Native HMDB0014401 is attested by current ChEBI, but independent exact HMDB graph verification remains incomplete. No wrong-identity finding follows from access failure. |
| patent-producer | US2482055; https://patents.google.com/patent/US2482055A/en; Original patent description: new antibiotic, free-base/acid-salt distinction, producing organism NRRL-2209 and isolation/fermentation protocol. | supports | The 1949 Duggar patent describes Aureomycin production by the organism named Streptomyces aureofaciens and isolation of the antibiotic, with separate free-base and hydrochloride properties. It supports the native producer/source wording and topical patent document link. Historical activity descriptions are not recast as modern standardized MIC values, and the patent is correctly a document_xref rather than exact chemical xref. |
| primary-target | PMID:1725100; DOI:10.1128/AAC.35.11.2306; https://pmc.ncbi.nlm.nih.gov/articles/PMC245376/; All six original scanned pages 2306–2311 read visually, including Figure 2 exact chlortetracycline, Tables 2/3 and Figure 4. | supports | Rasmussen et al. 1991 directly test chlortetracycline prepared at Lederle. Agar MICs are 0.25 micrograms/mL for E. coli K-12 MC4100 and 0.5 for B. subtilis 168. Cell-free translation is inhibited in both organisms. E. coli MRE600 ribosome experiments show protection at 16S A892 and enhanced DMS reactivity at U1052/C1054. These support ribosomal interaction, not a claim that those footprint changes uniquely cause inhibition. The authors explicitly distinguish direct interaction from indirect RNA perturbation and discuss imperfect correlations across analogues. Bulk counterion is not specified. |
| primary-target-context | PMID:1725100, Materials and Methods, Tables 1–3 and Figure 4; Same full original scans. | context_only | MIC uses agar dilution, 10 microliters of 1e6–5e6 CFU/mL culture, 18 h at 37 C. E. coli growth uses M63 minimal medium and B. subtilis uses LB. Ribosome footprinting incubates 500 micromolar antibiotic with 20 pmol 70S ribosomes under specified MgCl2/NH4Cl conditions; these are not affinity measurements. Cell-free translation is a distinct assay from whole-cell MIC. Anhydro and 4-epi anhydro analogues cannot supply the native mechanism. |
| card-all | https://card.mcmaster.ca/aro/3000755; ARO:3000186; ARO:3000190; ARO:3000191; ARO:3000192; ARO:3000193; ARO:3000194; ARO:3000195; ARO:3000196; ARO:3000197; ARO:3000205; ARO:3000556; ARO:3003969; ARO:3004126; ARO:3004441; ARO:3004442; All 16 official entries: identity, definition, mechanism, exact chlortetracycline relationship and linked publication sections. | supports | Every cited CARD term resolves, names the corresponding native determinant/target and includes the exact chlortetracycline relationship. Ten ribosomal-protection entries, TetX inactivation, LmrP and Tet59 efflux, LamB reduced permeability, and 16S target classifications match the adopted source. This establishes database support, not independent primary confirmation of every compound-specific phenotype or biochemical mechanism. CARD prevalence/model outputs are not transferred as native experimental evidence. |
| lamB-direction | PMID:24412198; DOI:10.1016/j.jprot.2013.12.024; PMID:18620846; DOI:10.1016/j.ijantimicag.2008.04.015; https://card.mcmaster.ca/aro/3004126; Both complete original indexed abstracts; current CARD definition and absence relationship. Publisher full-text route for 2014 returned 403. | partial | CARD explicitly says downregulated LamB increases resistance and classifies it as resistance by absence. The 2014 original abstract identifies prior chlortetracycline-resistant E. coli, decreased LamB abundance, increased growth of a deletion mutant and antibiotic influx through LamB. The 2008 study reports increased MIC after lamB deletion and reversal with complementation, but its abstract names tetracycline, so that numerical or exact-agent phenotype is not transferred to chlortetracycline. Native omits the loss/downregulation condition entirely. |
| tet59-wnw | PMID:27565618; DOI:10.1128/AEM.01754-16; https://pmc.ncbi.nlm.nih.gov/articles/PMC5066362/; Full original main narrative, methods and Tables 1–3 in PMC HTML; figure captions read, full supplementary data not inspected. | supports | Table 3 directly tests chlortetracycline: E. coli DH5alpha/pUC18 control MIC 1, tet(59) clone 128 and tet(W/N/W) clone 64 micrograms/mL. Microdilution with 1 mM IPTG is described. The authors assign efflux and ribosomal protection as probable from sequence/regulatory context, not direct transport or ribosome-protection measurements in this paper. Manure is the DNA source, not a compound producer; inferred host taxa are not experimentally confirmed source organisms. Bulk chlortetracycline salt is unspecified. |
| tet44-boundary | PMID:20479200; DOI:10.1128/AAC.00304-10; https://pmc.ncbi.nlm.nih.gov/articles/PMC2897286/; Complete short original main text and Tables 1/2 in PMC HTML. | context_only | Gene expression and inactivation establish resistance to tetracycline, doxycycline and minocycline in C. fetus subsp. fetus, with Mueller-Hinton broth plus 5% laked horse blood. Chlortetracycline is absent from Table 2 and the listed tested-agent panel. Ribosomal protection is described as likely from sequence and phenotype. The native exact chlortetracycline edge remains a database assertion; this paper alone cannot upgrade it. Lack of a CTC test here is not evidence Tet44 cannot protect against CTC. |
| card-original-leads | PMID:19475445; PMID:9848445; PMID:2841293; PMID:20826220; PMID:9372425; PMID:7840565; PMID:8370538; PMID:8980765; PMID:10681357; PMID:18955517; PMID:11600392; PMID:12839793; PMID:21402075; PMID:16128584; PMID:15452119; PMID:1846135; PMID:7592810; PMID:11577166; PMID:10734605; PMID:9662506; Complete original indexed abstracts, with DOI and publication metadata resolved in 295-card-publications.json. | context_only | TetM transfer, TetO/Q/S/T/W/32/36 occurrence/sequence/transfer and TetX oxidation studies support their stated contexts. Several abstracts test tetracycline or tigecycline rather than explicitly chlortetracycline. LmrP abstracts establish energy-dependent extrusion and broad resistance, while the explicit accumulation experiment names tetracycline. PMID 10734605 concerns a prophage sequence, not a chlortetracycline LamB experiment. PMID 9662506 concerns aminoglycoside model-RNA binding, not chlortetracycline. These distinctions prevent upgrading every CARD edge from a related paper. |
| review-leads | PMID:11381101; DOI:10.1128/MMBR.65.2.232-260.2001; PMID:19862477; DOI:10.1007/s00018-009-0172-6; PMID:15837373; PMID:10532389; Complete indexed abstracts and publication identities; secondary reviews used as context/leads. | context_only | The two adopted ARO definition references are broad tetracycline reviews, not original chlortetracycline experiments. The TetB(P) linked update and lactic-acid-bacteria multidrug review are also secondary sources. They are not typed as primary evidence or used to assert an exact assay. |
| adopted-environment | PMID:23530364; DOI:10.1080/09593330.2012.701332; PMID:25602656; DOI:10.2134/jeq2013.02.0039; All complete original indexed abstracts; all seven adopted ChEBI PMIDs accounted for. | context_only | The former measures aqueous photocatalytic/ozonation degradation; the latter measures runoff losses from manure. Neither demonstrates a native antibacterial molecular target or biosynthetic producer. |
| adopted-veterinary | PMID:24845506; DOI:10.1007/s12038-014-9425-0; PMID:25131164; DOI:10.1111/jvp.12144; All complete original indexed abstracts; all seven adopted ChEBI PMIDs accounted for. | context_only | The farm survey measures feed and egg residues. The ewe study measures feed-grade pharmacokinetics at two doses and explicitly questions how exposure relates to prevention of abortion. Neither is a verified exact-neutral-form MIC or current regulatory assertion. |
| adopted-calcium | PMID:7150561; DOI:10.1021/bi00267a041; PMID:7390959; DOI:10.1093/oxfordjournals.jbchem.a132799; PMID:7988792; DOI:10.1046/j.1432-0436.1994.5730163.x; All complete original indexed abstracts; all seven adopted ChEBI PMIDs accounted for. | context_only | These original studies concern calcium ionophore behavior across organic barriers/vesicles, sarcoplasmic-reticulum fluorescence/permeability, and Dictyostelium cell-fate correlations using a calcium probe. They do not establish a bacterial membrane mechanism or protozoal killing for the native compound. |
| antiprotozoal-boundary | CHEBI:35820; KEGG:D07689; PMID:14878100; DOI:10.4269/ajtmh.1951.s1-31.566; PMID:14815713; DOI:10.1056/NEJM195104052441401; Official role/drug entries; original historical publication metadata and limited publisher excerpt for the 1951 NEJM paper. | partial | ChEBI and KEGG explicitly support antiprotozoal use. Original historical amoebiasis reports are identifiable, but full original outcome/material tables were not accessible in the bounded search; AJTMH returned 403. No cure rate, direct protozoal target, current treatment recommendation or salt-specific clinical efficacy is inferred from bibliographic leads. |
| adapter | iModulonDB e_coli/precise1k/b4036; Actual datasets then lamB search before open-ended web research. | context_only | The covered E. coli dataset resolves b4036/lamB as maltose outer-membrane channel/phage lambda receptor and returns zero matching iModulons. This supports gene context only, not chlortetracycline influx or resistance direction. The catalog lacks the stated S. aureofaciens producer and Lactococcus lactis; taxon-unspecified acquired tet genes do not select a defensible organism-specific dataset. |
| inclusive-search | 295-inclusive-hits.txt; Exact native identifier, label, InChIKey and ARO identifier; hidden and ignored files included. | context_only | The stated local scope contains source rows, native file, PATHS, readiness queue, generated embeddings and an unrelated historical report mention. No exact curator decision or qualification overlay for this record was found. Historical reports and queue flags were leads, not scientific evidence. |
| validation | 295-schema.log; 295-strict.log; 295-chemistry.json; 295-xref-chemistry.json; 295-tautomer-chemistry.json; Actual focused outputs. | supports | Schema and strict validation exit 0; native chemistry and both source-ID mints pass. External structures parse, with PubChem tautomer difference explicitly retained and DrugCentral exact graph confirmed. All nineteen captured source input hashes remain unchanged. |

## Limits And Additional Notes

- HMDB0014401 page and XML routes returned 403; independent exact HMDB structure was not inspected. CAS was checked through official public database cross-attribution, without paid registry access.
- All nine adopted abstracts and all source-linked CARD publication abstracts were inspected. Full original follow-up covered the six-page 1991 target paper, the 2016 mobilome paper and the short Tet44 study; most other resistance papers remain abstract-depth only.
- The LamB 2014 publisher route returned 403. Its complete original abstract and the official CARD definition establish the missing loss/downregulation condition, but original full experimental tables and exact bulk chlortetracycline form were unavailable.
- Antiprotozoal use is supported by official ChEBI/KEGG and identifiable historical primary reports; the original outcome/material tables were not fully accessible. No clinical efficacy estimate, direct protozoal mechanism or current treatment recommendation is claimed.
- PubChem differs by keto-enol representation. Tautomer canonicalization is a diagnostic and may alter stereochemical labels; explicit original InChI layers are retained. No natural-product stereo revision is proposed.
- Eremomycine is attested by CARD but its independent historical naming basis was not established by the bounded exact-spelling search. This is unresolved provenance, not proof of a false alias.
- No primary support is transferred from anhydro/epimeric analogues, different tetracyclines, animal-feed mixtures or salt formulations to an unqualified exact-neutral structure claim. Scientific completion is partial; deterministic validation does not promote native REVIEWED status.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T130546Z-chlortetracycline
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Chlortetracycline: supported identity and ribosomal activity; qualify LamB
  loss and the Aureomycin trade name'
started_at: '2026-10-21T12:48:43Z'
finished_at: '2026-10-21T13:05:46Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author this seed. Read the entire native YAML, complete
    source rows and actual extraction/seeding/qualification logic. Captured actual
    additional owners while preserving initial input hashes, before assessment. Checked
    official chemical and ontology entries, every adopted abstract, all cited CARD
    entries and their publication abstracts, and focused original full articles.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The neutral ChEBI chlortetracycline structure is internally coherent and
  supported by independently parsed official encodings. Original experiments support
  antibacterial activity, cell-free translation inhibition and ribosomal RNA interaction.
  All 15 resistance edges and the 16S target are faithfully attributed to CARD. One
  major finding concerns the missing loss/downregulation condition for LamB-mediated
  reduced permeability; a minor finding concerns the Aureomycin trade name being typed
  as an exact chemical synonym. The PubChem graph differs by keto-enol placement,
  not demonstrated epimerism, and is retained as an informational representation boundary.
  Other database-to-primary evidence gaps remain explicit limitations rather than
  automatic defects.
source:
  git_revision: baf3b3203d748d098686e166cdb2a6138f47eb59
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 5e2e1f975f8aa64f92a06c134c98c750c968fd78f02620a73c9cb611ac018ed8
    role: context
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: context
  - path: conf/sources.yaml
    sha256: 4a2dcd7a3a88953b6cb35b51a48ed77b626c3af2cbb542b0d38ba10540ed7df9
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
  - path: curation/curator_antibiotics.tsv
    sha256: 224cbb7261add427184b2762a29c2ff3e85c85e0a06cf22b144545346487247b
    role: context
  - path: curation/decisions.tsv
    sha256: a5834b44307b0449b0df9362c551b7fcd707f3ae51f73d429d37d51f5a169d61
    role: context
  - path: data/antibiotics/antibacterial/chlortetracycline.yaml
    sha256: a7c816be91942bd441b54611580cb972ea5d91ebdf566af54c7fea5ed23aa4a0
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
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
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
  - path: scripts/card_evidence_reviews.py
    sha256: f9ec8aff30066bf04b9c2757af7d6f5d179d045e57b9f3b352bbed0b851f50a8
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
- target_id: CHEBI:27644
  path: data/antibiotics/antibacterial/chlortetracycline.yaml
  label: chlortetracycline
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
    path: data/raw/aro_antibiotics.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Direct binding target relation mapping
scope:
  description: 'Whole native record: definition, eight synonyms, seven parents, two
    activity roles, structure, eight chemical xrefs, two drug xrefs, patent document,
    both source concepts, 15 resistance items, the 16S target and all five history
    events. Complete ChEBI/ARO source rows and all nine adopted citation leads were
    inspected.'
  selection: Queue 295; initial thirteen hashes retained, six actual source/config/qualification
    owners appended, total nineteen inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:27644
  exclusions:
  - target: Hydrochloride and other salts, epimers, anhydrochlortetracycline, tetracycline
      and other family members
    reason: They are not automatically exact material evidence for the selected neutral
      structure. Family evidence and salt formulation data remain qualified.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: No schema issues found.
  target_ids:
  - CHEBI:27644
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/chlortetracycline.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: One record; zero strict errors.
  target_ids:
  - CHEBI:27644
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/chlortetracycline.yaml --out /private/tmp/am-review-session/295-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Both native encodings, formula, zero charge, five stereocentres, masses
    and both minted source IDs agree.
  target_ids:
  - CHEBI:27644
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 295
  exit_code: 0
  expected_exit_code: 0
- check_id: external-chemistry
  name: external-chemistry
  status: passed
  required: false
  summary: External encodings successfully parsed. PubChem differs from the native
    tautomer; this diagnostic does not assert every full key is identical.
  target_ids:
  - CHEBI:27644
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/295-xref-check.py
  exit_code: 0
  expected_exit_code: 0
- check_id: tautomer-diagnostic
  name: tautomer-diagnostic
  status: passed
  required: false
  summary: Native and PubChem differ only in the InChI hydrogen layer; canonical tautomer
    diagnostics agree. DrugCentral matches the native full key. Canonicalization is
    diagnostic, not a proposed structure replacement.
  target_ids:
  - CHEBI:27644
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/295-tautomer-check.py
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
  - CHEBI:27644
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
  - CHEBI:27644
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
  - CHEBI:27644
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
  - CHEBI:27644
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
  - CHEBI:27644
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
  - CHEBI:27644
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
  - CHEBI:27644
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
  - CHEBI:27644
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
  - CHEBI:27644
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/chlortetracycline.yaml
  locator: Entire YAML.
  accessed_at: '2026-10-21T12:58:46Z'
  support: supports
  summary: SEEDED/EXACT/ANTIBACTERIAL. Neutral C22H23ClN2O8; native key CYDMQBQPVICBEU-XRNKAMNCSA-N.
    Resistance items expressly cite database assertions; the 16S direct target is
    PRIMARY_EVIDENCE_NEEDED, without invented organism/strain/assay. No numeric activity,
    clinical approval, causal graph or transcriptomic dataset is asserted.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv;
    data/raw/aro_resistance_edges.tsv; conf/sources.yaml; conf/aro_target_roles.tsv;
    scripts/extract_source_inventory.py; scripts/seed_from_sources.py; curation/card_evidence_reviews.json;
    scripts/card_evidence_reviews.py
  locator: Complete rows 498, 114, 129 and 2598–2612 respectively; extraction and
    identity/assembly logic; attach_aro_mechanism and qualification loader/apply function.
  accessed_at: '2026-10-21T12:58:46Z'
  support: supports
  summary: ChEBI owns the definition, structure, typed aliases, parents and roles;
    ARO adds its parent/class, untyped aliases, xrefs and mechanism edges. The seeder
    types every ARO alias EXACT_SYNONYM. The target map explicitly maps 16S RNA to
    direct nucleic-acid target while preserving PRIMARY_EVIDENCE_NEEDED. No matching
    existing CARD qualification was found. ChEBI source references remain curator
    leads rather than automatically becoming native claim evidence. No PubChem enrichment
    inventory, FDA or MIBiG row owns this record.
  snapshot_sha256: 73b9154955a585ea453080925ebb7b269c217d9faf87236beda654da635346fe
- evidence_id: chemical
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:27644; https://card.mcmaster.ca/aro/3000528;
    https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL404520.json; https://rest.kegg.jp/get/C06571;
    https://www.lipidmaps.org/rest/compound/lm_id/LMPK07000004/all/json; https://files.rcsb.org/ligands/download/CTC.cif;
    https://drugcentral.org/drug/624/smiles
  locator: Complete chemical entries/descriptors and independent molecular parses.
  accessed_at: '2026-10-21T12:58:46Z'
  support: supports
  summary: Current ChEBI, ARO visible graph, ChEMBL 404520, KEGG C06571, LIPID MAPS
    LMPK07000004, CCD CTC and DrugCentral 624 all resolve to the native full key.
    CAS 57-62-5 is independently attested in several official records, without paid
    registry access. The ChEBI systematic name agrees with native stereochemistry.
    CCD is a chemical-component identifier, not a whole PDB structure or a demonstration
    of antibacterial target engagement.
  snapshot_sha256: c22e1892fd79ef94e1ec96c42ff3e474045404bd8e9bd211f6a1bbc2ae25e98d
- evidence_id: pubchem-tautomer
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/54675777/property/InChI,InChIKey,MolecularFormula,SMILES,IUPACName/JSON;
    docs/HARMONIZATION.md
  locator: Full official PubChem response; independent InChI/SMILES parse and explicit
    layer comparison; identity cautions in HARMONIZATION.
  accessed_at: '2026-10-21T12:58:46Z'
  support: partial
  summary: PubChem 54675777 gives DHPRQBPJLMKORJ-XRNKAMNCSA-N. Native and PubChem
    share formula, charge, connectivity layer and stereochemical layers; hydrogen/bond
    placement differs between keto-enol representations. RDKit canonical tautomers
    agree, but this operation can erase tautomer-sensitive stereo and is not independent
    proof of all stereochemical identity. The explicit original InChI layer comparison
    is retained. PubChem exact native-key lookup returned 404. HARMONIZATION warns
    unequal Standard InChIKeys are not proof of different compounds. No epimer, wrong
    natural product or required whole-structure replacement is inferred.
  snapshot_sha256: 86875a8bd009be91ad260f4443e4a71fc2fe25bcd429e1ed5d1311a5eaacc3be
- evidence_id: ontology
  kind: database
  reference: CHEBI:139592; CHEBI:26878; CHEBI:26895; CHEBI:29347; CHEBI:50996; CHEBI:83403;
    ARO:3000050; CHEBI:35820; CHEBI:36047
  locator: Official definitions and ChEBI outgoing relationships, with raw role/class
    mappings.
  accessed_at: '2026-10-21T12:53:21Z'
  support: supports
  summary: The six ChEBI parents are tertiary alpha-hydroxy ketone, tertiary alcohol,
    tetracyclines, monocarboxylic acid amide, tertiary amino compound and monochlorobenzenes;
    each is broader and chemically consistent. ARO 3000050 is the tetracycline antibiotic
    class. Antiprotozoal drug and antibacterial drug are both retained; antibacterial
    filing does not erase the antiprotozoal role. Current ChEBI also displays additional
    roles, but source-version differences are not silently treated as original seed
    errors.
  snapshot_sha256: bd20a404ce963345dbb87af54983b17a3c28386ce0c3aec7807b4bd5f137ea32
- evidence_id: drug-aliases
  kind: database
  reference: https://rest.kegg.jp/get/D07689; https://drugcentral.org/drugcard/624;
    https://www.ebi.ac.uk/chebi/CHEBI:27644; https://card.mcmaster.ca/aro/3000528
  locator: Drug entry NAME/FORMULA/SOURCE/EFFICACY, chemical descriptors and source
    synonym types.
  accessed_at: '2026-10-21T12:53:36Z'
  support: partial
  summary: KEGG D07689 explicitly identifies chlortetracycline as INN and Aureomycin
    as TN. ChEBI supplies Aueromycin as a BRAND NAME, already typed correctly in native.
    The ARO spelling Aureomycin is emitted as EXACT_SYNONYM instead. Eremomycine is
    attested by ARO, but its independent historical naming basis was not resolved
    in the bounded exact-spelling search; no confusion with a similarly named glycopeptide
    is asserted. DrugCentral and KEGG belong in drug_xrefs, and their product lists
    do not create an unqualified current clinical approval claim.
  snapshot_sha256: 86c41331f5ce1f33519a1865a6efe7aa696fc07d0d70175946b575ed0071f1c3
- evidence_id: hmdb-access
  kind: database
  reference: https://www.hmdb.ca/metabolites/HMDB0014401; https://www.hmdb.ca/metabolites/HMDB0014401.xml
  locator: Official page and structured endpoint attempts, plus ChEBI attribution.
  accessed_at: '2026-10-21T12:58:46Z'
  support: unknown
  summary: Both direct HMDB routes returned 403; the web tool also failed to inspect
    the entry. Native HMDB0014401 is attested by current ChEBI, but independent exact
    HMDB graph verification remains incomplete. No wrong-identity finding follows
    from access failure.
  snapshot_sha256: ada653bfed3a4be8e9ed0662e394ca844a6a2cba738ed3cd5c38e6f93257924a
- evidence_id: patent-producer
  kind: primary_source
  reference: US2482055; https://patents.google.com/patent/US2482055A/en
  locator: 'Original patent description: new antibiotic, free-base/acid-salt distinction,
    producing organism NRRL-2209 and isolation/fermentation protocol.'
  accessed_at: '2026-10-21T12:53:37Z'
  support: supports
  summary: The 1949 Duggar patent describes Aureomycin production by the organism
    named Streptomyces aureofaciens and isolation of the antibiotic, with separate
    free-base and hydrochloride properties. It supports the native producer/source
    wording and topical patent document link. Historical activity descriptions are
    not recast as modern standardized MIC values, and the patent is correctly a document_xref
    rather than exact chemical xref.
  snapshot_sha256: 84f54c79b1c6c7c667e02de68c8abde5dd635329b8a6f4cbfbbf83eb74d82645
- evidence_id: primary-target
  kind: primary_source
  reference: PMID:1725100; DOI:10.1128/AAC.35.11.2306; https://pmc.ncbi.nlm.nih.gov/articles/PMC245376/
  locator: All six original scanned pages 2306–2311 read visually, including Figure
    2 exact chlortetracycline, Tables 2/3 and Figure 4.
  accessed_at: '2026-10-21T12:58:46Z'
  support: supports
  summary: Rasmussen et al. 1991 directly test chlortetracycline prepared at Lederle.
    Agar MICs are 0.25 micrograms/mL for E. coli K-12 MC4100 and 0.5 for B. subtilis
    168. Cell-free translation is inhibited in both organisms. E. coli MRE600 ribosome
    experiments show protection at 16S A892 and enhanced DMS reactivity at U1052/C1054.
    These support ribosomal interaction, not a claim that those footprint changes
    uniquely cause inhibition. The authors explicitly distinguish direct interaction
    from indirect RNA perturbation and discuss imperfect correlations across analogues.
    Bulk counterion is not specified.
  snapshot_sha256: 9e6700a821bd0ebd38aba0e6c4ae13982cf8fb7c3eb2a914af77e40df853af10
- evidence_id: primary-target-context
  kind: primary_source
  reference: PMID:1725100, Materials and Methods, Tables 1–3 and Figure 4
  locator: Same full original scans.
  accessed_at: '2026-10-21T12:54:52Z'
  support: context_only
  summary: MIC uses agar dilution, 10 microliters of 1e6–5e6 CFU/mL culture, 18 h
    at 37 C. E. coli growth uses M63 minimal medium and B. subtilis uses LB. Ribosome
    footprinting incubates 500 micromolar antibiotic with 20 pmol 70S ribosomes under
    specified MgCl2/NH4Cl conditions; these are not affinity measurements. Cell-free
    translation is a distinct assay from whole-cell MIC. Anhydro and 4-epi anhydro
    analogues cannot supply the native mechanism.
  snapshot_sha256: f4cdd51f00346add81135d518325b98268c6e1135a443fb310adda27272f011f
- evidence_id: card-all
  kind: database
  reference: https://card.mcmaster.ca/aro/3000755; ARO:3000186; ARO:3000190; ARO:3000191;
    ARO:3000192; ARO:3000193; ARO:3000194; ARO:3000195; ARO:3000196; ARO:3000197;
    ARO:3000205; ARO:3000556; ARO:3003969; ARO:3004126; ARO:3004441; ARO:3004442
  locator: 'All 16 official entries: identity, definition, mechanism, exact chlortetracycline
    relationship and linked publication sections.'
  accessed_at: '2026-10-21T12:58:46Z'
  support: supports
  summary: Every cited CARD term resolves, names the corresponding native determinant/target
    and includes the exact chlortetracycline relationship. Ten ribosomal-protection
    entries, TetX inactivation, LmrP and Tet59 efflux, LamB reduced permeability,
    and 16S target classifications match the adopted source. This establishes database
    support, not independent primary confirmation of every compound-specific phenotype
    or biochemical mechanism. CARD prevalence/model outputs are not transferred as
    native experimental evidence.
  snapshot_sha256: 54f68ef088612a8f32000864cfbf1a63e12366a7215d8163c5edcd7896aeee69
- evidence_id: lamB-direction
  kind: primary_source
  reference: PMID:24412198; DOI:10.1016/j.jprot.2013.12.024; PMID:18620846; DOI:10.1016/j.ijantimicag.2008.04.015;
    https://card.mcmaster.ca/aro/3004126
  locator: Both complete original indexed abstracts; current CARD definition and absence
    relationship. Publisher full-text route for 2014 returned 403.
  accessed_at: '2026-10-21T12:54:06Z'
  support: partial
  summary: CARD explicitly says downregulated LamB increases resistance and classifies
    it as resistance by absence. The 2014 original abstract identifies prior chlortetracycline-resistant
    E. coli, decreased LamB abundance, increased growth of a deletion mutant and antibiotic
    influx through LamB. The 2008 study reports increased MIC after lamB deletion
    and reversal with complementation, but its abstract names tetracycline, so that
    numerical or exact-agent phenotype is not transferred to chlortetracycline. Native
    omits the loss/downregulation condition entirely.
  snapshot_sha256: 97cb5616ba5cb73cfc7431e0aebc1796d8e46fb4be132da04122371c91de2b67
- evidence_id: tet59-wnw
  kind: primary_source
  reference: PMID:27565618; DOI:10.1128/AEM.01754-16; https://pmc.ncbi.nlm.nih.gov/articles/PMC5066362/
  locator: Full original main narrative, methods and Tables 1–3 in PMC HTML; figure
    captions read, full supplementary data not inspected.
  accessed_at: '2026-10-21T12:55:19Z'
  support: supports
  summary: 'Table 3 directly tests chlortetracycline: E. coli DH5alpha/pUC18 control
    MIC 1, tet(59) clone 128 and tet(W/N/W) clone 64 micrograms/mL. Microdilution
    with 1 mM IPTG is described. The authors assign efflux and ribosomal protection
    as probable from sequence/regulatory context, not direct transport or ribosome-protection
    measurements in this paper. Manure is the DNA source, not a compound producer;
    inferred host taxa are not experimentally confirmed source organisms. Bulk chlortetracycline
    salt is unspecified.'
  snapshot_sha256: faca05b443162a778ed600a6a217961575e9278092bae9c60ec7a7023ea0c84f
- evidence_id: tet44-boundary
  kind: primary_source
  reference: PMID:20479200; DOI:10.1128/AAC.00304-10; https://pmc.ncbi.nlm.nih.gov/articles/PMC2897286/
  locator: Complete short original main text and Tables 1/2 in PMC HTML.
  accessed_at: '2026-10-21T12:55:19Z'
  support: context_only
  summary: Gene expression and inactivation establish resistance to tetracycline,
    doxycycline and minocycline in C. fetus subsp. fetus, with Mueller-Hinton broth
    plus 5% laked horse blood. Chlortetracycline is absent from Table 2 and the listed
    tested-agent panel. Ribosomal protection is described as likely from sequence
    and phenotype. The native exact chlortetracycline edge remains a database assertion;
    this paper alone cannot upgrade it. Lack of a CTC test here is not evidence Tet44
    cannot protect against CTC.
  snapshot_sha256: b899c041aead2df5981cecdacdc2f0fdf60aa9035ef5db1c909b5792242219a0
- evidence_id: card-original-leads
  kind: primary_source
  reference: PMID:19475445; PMID:9848445; PMID:2841293; PMID:20826220; PMID:9372425;
    PMID:7840565; PMID:8370538; PMID:8980765; PMID:10681357; PMID:18955517; PMID:11600392;
    PMID:12839793; PMID:21402075; PMID:16128584; PMID:15452119; PMID:1846135; PMID:7592810;
    PMID:11577166; PMID:10734605; PMID:9662506
  locator: Complete original indexed abstracts, with DOI and publication metadata
    resolved in 295-card-publications.json.
  accessed_at: '2026-10-21T12:54:06Z'
  support: context_only
  summary: TetM transfer, TetO/Q/S/T/W/32/36 occurrence/sequence/transfer and TetX
    oxidation studies support their stated contexts. Several abstracts test tetracycline
    or tigecycline rather than explicitly chlortetracycline. LmrP abstracts establish
    energy-dependent extrusion and broad resistance, while the explicit accumulation
    experiment names tetracycline. PMID 10734605 concerns a prophage sequence, not
    a chlortetracycline LamB experiment. PMID 9662506 concerns aminoglycoside model-RNA
    binding, not chlortetracycline. These distinctions prevent upgrading every CARD
    edge from a related paper.
  snapshot_sha256: 97cb5616ba5cb73cfc7431e0aebc1796d8e46fb4be132da04122371c91de2b67
- evidence_id: review-leads
  kind: database
  reference: PMID:11381101; DOI:10.1128/MMBR.65.2.232-260.2001; PMID:19862477; DOI:10.1007/s00018-009-0172-6;
    PMID:15837373; PMID:10532389
  locator: Complete indexed abstracts and publication identities; secondary reviews
    used as context/leads.
  accessed_at: '2026-10-21T12:54:06Z'
  support: context_only
  summary: The two adopted ARO definition references are broad tetracycline reviews,
    not original chlortetracycline experiments. The TetB(P) linked update and lactic-acid-bacteria
    multidrug review are also secondary sources. They are not typed as primary evidence
    or used to assert an exact assay.
  snapshot_sha256: 97cb5616ba5cb73cfc7431e0aebc1796d8e46fb4be132da04122371c91de2b67
- evidence_id: adopted-environment
  kind: primary_source
  reference: PMID:23530364; DOI:10.1080/09593330.2012.701332; PMID:25602656; DOI:10.2134/jeq2013.02.0039
  locator: All complete original indexed abstracts; all seven adopted ChEBI PMIDs
    accounted for.
  accessed_at: '2026-10-21T12:53:37Z'
  support: context_only
  summary: The former measures aqueous photocatalytic/ozonation degradation; the latter
    measures runoff losses from manure. Neither demonstrates a native antibacterial
    molecular target or biosynthetic producer.
  snapshot_sha256: e5824116451437d99b6dfbd210a4465734023718e284c15cdf434567c8da0ace
- evidence_id: adopted-veterinary
  kind: primary_source
  reference: PMID:24845506; DOI:10.1007/s12038-014-9425-0; PMID:25131164; DOI:10.1111/jvp.12144
  locator: All complete original indexed abstracts; all seven adopted ChEBI PMIDs
    accounted for.
  accessed_at: '2026-10-21T12:53:37Z'
  support: context_only
  summary: The farm survey measures feed and egg residues. The ewe study measures
    feed-grade pharmacokinetics at two doses and explicitly questions how exposure
    relates to prevention of abortion. Neither is a verified exact-neutral-form MIC
    or current regulatory assertion.
  snapshot_sha256: e5824116451437d99b6dfbd210a4465734023718e284c15cdf434567c8da0ace
- evidence_id: adopted-calcium
  kind: primary_source
  reference: PMID:7150561; DOI:10.1021/bi00267a041; PMID:7390959; DOI:10.1093/oxfordjournals.jbchem.a132799;
    PMID:7988792; DOI:10.1046/j.1432-0436.1994.5730163.x
  locator: All complete original indexed abstracts; all seven adopted ChEBI PMIDs
    accounted for.
  accessed_at: '2026-10-21T12:53:37Z'
  support: context_only
  summary: These original studies concern calcium ionophore behavior across organic
    barriers/vesicles, sarcoplasmic-reticulum fluorescence/permeability, and Dictyostelium
    cell-fate correlations using a calcium probe. They do not establish a bacterial
    membrane mechanism or protozoal killing for the native compound.
  snapshot_sha256: e5824116451437d99b6dfbd210a4465734023718e284c15cdf434567c8da0ace
- evidence_id: antiprotozoal-boundary
  kind: database
  reference: CHEBI:35820; KEGG:D07689; PMID:14878100; DOI:10.4269/ajtmh.1951.s1-31.566;
    PMID:14815713; DOI:10.1056/NEJM195104052441401
  locator: Official role/drug entries; original historical publication metadata and
    limited publisher excerpt for the 1951 NEJM paper.
  accessed_at: '2026-10-21T12:58:46Z'
  support: partial
  summary: ChEBI and KEGG explicitly support antiprotozoal use. Original historical
    amoebiasis reports are identifiable, but full original outcome/material tables
    were not accessible in the bounded search; AJTMH returned 403. No cure rate, direct
    protozoal target, current treatment recommendation or salt-specific clinical efficacy
    is inferred from bibliographic leads.
- evidence_id: adapter
  kind: database
  reference: iModulonDB e_coli/precise1k/b4036
  locator: Actual datasets then lamB search before open-ended web research.
  accessed_at: '2026-10-21T12:58:46Z'
  support: context_only
  summary: The covered E. coli dataset resolves b4036/lamB as maltose outer-membrane
    channel/phage lambda receptor and returns zero matching iModulons. This supports
    gene context only, not chlortetracycline influx or resistance direction. The catalog
    lacks the stated S. aureofaciens producer and Lactococcus lactis; taxon-unspecified
    acquired tet genes do not select a defensible organism-specific dataset.
  snapshot_sha256: 1d9037f5d2af598112c34f34581b123f9120856bdd3b26715b86a296a951e966
- evidence_id: inclusive-search
  kind: search
  reference: 295-inclusive-hits.txt
  locator: Exact native identifier, label, InChIKey and ARO identifier; hidden and
    ignored files included.
  accessed_at: '2026-10-21T12:58:46Z'
  support: context_only
  summary: The stated local scope contains source rows, native file, PATHS, readiness
    queue, generated embeddings and an unrelated historical report mention. No exact
    curator decision or qualification overlay for this record was found. Historical
    reports and queue flags were leads, not scientific evidence.
  snapshot_sha256: 4db55951a2a82148b28e19e0f976142a426f800cfecebe18e4910ee374c48aa2
  search_scope: rg --no-ignore --hidden -n -F for CHEBI:27644, chlortetracycline,
    CYDMQBQPVICBEU-XRNKAMNCSA-N and ARO:3000528 across data, curation, conf, scripts,
    src, docs, .claude, reviews and reports; bounded public official identifiers,
    exact name, LamB, ribosome and historical antiprotozoal searches on 2026-10-21.
- evidence_id: validation
  kind: validation
  reference: 295-schema.log; 295-strict.log; 295-chemistry.json; 295-xref-chemistry.json;
    295-tautomer-chemistry.json
  locator: Actual focused outputs.
  accessed_at: '2026-10-21T12:58:46Z'
  support: supports
  summary: Schema and strict validation exit 0; native chemistry and both source-ID
    mints pass. External structures parse, with PubChem tautomer difference explicitly
    retained and DrugCentral exact graph confirmed. All nineteen captured source input
    hashes remain unchanged.
  snapshot_sha256: b672223e828bae3ac299441738d74286235cbb9351b836b3979d9aad9f67325a
assessments:
- assessment_id: identity
  area: identity
  topic: Neutral exact ChEBI structure and chemical identifiers
  outcome: supported
  summary: Native encodings and accessible external graphs support the exact chlortetracycline
    seed. PubChem is a recognized keto-enol representation boundary; HMDB access is
    limited. No stereochemical correction is justified.
  target_ids:
  - CHEBI:27644
  evidence_ids:
  - native
  - chemical
  - pubchem-tautomer
  - hmdb-access
  - validation
- assessment_id: roles
  area: scope
  topic: Filing, roles, parent classes and producer definition
  outcome: supported
  summary: Broader chemical parents and antibacterial filing are coherent. Both drug
    roles are supported by the adopted authority; direct antibacterial experiments
    and original producer patent strengthen the native definition. Antiprotozoal primary-outcome
    verification remains limited.
  target_ids:
  - CHEBI:27644
  evidence_ids:
  - ontology
  - patent-producer
  - primary-target
  - antiprotozoal-boundary
- assessment_id: target
  area: evidence
  topic: 16S RNA target and mechanism scope
  outcome: supported
  summary: The source edge is real and the native record appropriately requests primary
    evidence. The 1991 original provides exact-compound functional and RNA-footprinting
    support, while ARO target PMID 9662506 is aminoglycoside-specific. The missing
    optional mode of action is not itself a defect in a SEEDED record.
  target_ids:
  - CHEBI:27644
  evidence_ids:
  - card-all
  - primary-target
  - primary-target-context
  - card-original-leads
- assessment_id: resistance
  area: evidence
  topic: Fifteen database resistance assertions
  outcome: concern
  summary: All fifteen source relationships resolve, but LamB must explicitly preserve
    loss/downregulation. Exact CTC phenotypes for Tet59 and Tet(W/N/W) have primary
    support; their detailed mechanisms remain inferred in that paper. Other linked
    primary abstracts and Tet44 full text do not uniformly establish exact CTC experiments.
  target_ids:
  - CHEBI:27644
  evidence_ids:
  - card-all
  - lamB-direction
  - tet59-wnw
  - tet44-boundary
  - card-original-leads
  - review-leads
- assessment_id: synonyms
  area: identity
  topic: Chemical names versus trade-name aliases
  outcome: concern
  summary: Aureomycin is explicitly a trade name in KEGG yet is typed EXACT_SYNONYM
    in the ARO-derived slice. The independently sourced Aueromycin variant already
    has BRAND_NAME. Eremomycine is source-attested but historically unverified.
  target_ids:
  - CHEBI:27644
  evidence_ids:
  - drug-aliases
  - owners
- assessment_id: coverage
  area: completeness
  topic: Native evidence placement and optional enrichment
  outcome: unknown
  summary: All adopted citations were checked at stated depth. No automatic mechanism,
    current approval, expression dataset, producer BGC or numeric activity is fabricated
    from source bibliographies. Primary additions are possible with material and assay
    scope preserved.
  target_ids:
  - CHEBI:27644
  evidence_ids:
  - adopted-environment
  - adopted-veterinary
  - adopted-calcium
  - review-leads
  - adapter
  - primary-target
findings:
- finding_id: F1
  issue_key: chlortetracycline-lamb-resistance-loss-condition
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Preserve the LamB loss or downregulation condition
  description: resistance_mechanisms[12] names Escherichia coli LamB and repeats that
    CARD says it confers resistance, but does not state that decreased abundance or
    loss of this antibiotic influx porin is the resistance-associated state. Both
    the cited CARD definition and its original 2014 abstract make this condition explicit.
    REDUCED_PERMEABILITY alone does not specify which genetic/expression state produces
    the phenotype. Add a maintained qualification preserving the source condition;
    do not present ordinary LamB presence as a resistance determinant.
  target_ids:
  - CHEBI:27644
  field_paths:
  - resistance_mechanisms[12]
  evidence_ids:
  - owners
  - card-all
  - lamB-direction
  rule_id: 'native-review-checklist: Resistance; Evidence standard scope preservation'
  native_severity: major
  normalization_reason: This omitted condition changes the biological interpretation
    of a resistance determinant and can invert presence-versus-loss inference. The
    ARO identifier and general reduced-permeability route remain correct; no deletion
    of the database edge is required.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Original LamB database edge
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Row-bound inspected evidence qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Qualification validation and emission
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Resistance item regeneration
- finding_id: F2
  issue_key: chlortetracycline-aureomycin-trade-name-type
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Retain trade-name semantics for Aureomycin
  description: synonyms[6] types Aureomycin as EXACT_SYNONYM because the ARO importer
    assigns that type to untyped aliases. Official KEGG D07689 expressly marks Aureomycin
    TN. Preserve it as a trade-name alias with source provenance, consistent with
    the existing BRAND_NAME Aueromycin entry, without treating every product formulation
    as the exact neutral graph.
  target_ids:
  - CHEBI:27644
  field_paths:
  - synonyms[6].synonym_type
  evidence_ids:
  - owners
  - drug-aliases
  rule_id: 'native-review-checklist: Identity and Equivalence'
  native_severity: minor
  normalization_reason: Bounded alias-type defect; the compound identity and source
    spelling remain recognized.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: ARO synonym source
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Preserve/normalize source alias semantics
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated synonym typing
- finding_id: F3
  issue_key: chlortetracycline-pubchem-keto-enol-representation
  category: identity
  severity: informational
  status: open
  certainty: confirmed
  title: Record the PubChem keto-enol representation boundary
  description: PubChem 54675777 and the ChEBI-native graph have different full keys
    because their keto-enol hydrogen/bond placement differs. Their connectivity and
    stereo InChI layers agree, and a tautomer diagnostic converges. HARMONIZATION
    explicitly warns against inferring different compounds solely from unequal Standard
    InChIKeys. This is not a confirmed wrong-compound or epimer defect. Retain the
    observation when deciding whether exact xrefs need explicit tautomer qualification;
    do not replace native structure merely to match PubChem.
  target_ids:
  - CHEBI:27644
  field_paths:
  - xrefs[7]
  - chemical_structure
  evidence_ids:
  - chemical
  - pubchem-tautomer
  rule_id: 'docs/HARMONIZATION.md: A caution on the InChIKey as identity'
  native_severity: informational
  normalization_reason: A demonstrated representation difference with no established
    biological-identity contradiction. No mandatory corrective structure edit follows.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: PubChem xref owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Identity and xref emission
  - repository: CultureBotAI/AntibioticMech
    path: docs/HARMONIZATION.md
    role: Tautomer policy interpretation
actions:
- action_id: A1
  description: Add the missing LamB state qualification through the maintained CARD
    evidence-review path.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:27644
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Original LamB database edge
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Row-bound inspected evidence qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Qualification validation and emission
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Resistance item regeneration
  acceptance_checks:
  - Bind the qualification to the exact chlortetracycline resistance row/hash and
    native identifier/key, preserving CARD ownership. State that reduced LamB abundance
    or loss reduces antibiotic influx and is associated with resistance.
  - Cite inspected CARD and PMID 24412198 at abstract depth; do not import numerical
    MICs or exact-agent results from the separate 2008 tetracycline study without
    original material verification.
  - Regenerate through the owning seeder and confirm ordinary LamB presence is not
    described as sufficient for resistance; run focused validation and applicable
    corpus gates.
- action_id: A2
  description: Correct the Aureomycin alias type reproducibly.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:27644
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: ARO synonym source
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Preserve/normalize source alias semantics
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated synonym typing
  acceptance_checks:
  - Preserve the source alias text/provenance and emit BRAND_NAME for the official
    trade-name usage.
  - Check the existing Aueromycin brand alias for any deliberate deduplication policy;
    do not invent a new salt-specific chemical identity from brand wording.
  - Reseed the exact record and rerun schema/strict and reproduction checks.
- action_id: A3
  description: Resolve optional identity-policy and primary-evidence enrichment questions
    without automatic status promotion.
  finding_ids:
  - F3
  target_ids:
  - CHEBI:27644
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: PubChem xref owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Identity and xref emission
  - repository: CultureBotAI/AntibioticMech
    path: docs/HARMONIZATION.md
    role: Tautomer policy interpretation
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/chlortetracycline.yaml
    role: Curator-owned primary target/activity additions
  acceptance_checks:
  - Document the PubChem tautomer boundary under repository identity policy; preserve
    native ChEBI structure and do not claim opposite stereochemistry from changed
    tautomer-sensitive CIP labels.
  - For primary enrichment, keep the 1991 whole-cell MIC, cell-free translation and
    ribosomal footprint assays separate, with exact strains and material limitations.
  - Retain Tet59/Tet(W/N/W) exact CTC phenotypes while qualifying mechanism inference.
    Do not upgrade Tet44 or other family evidence to exact CTC primary support without
    original experiments.
  - Seek freely accessible exact HMDB and Eremomycine historical identity evidence
    if needed; access failures and optional missing fields alone are not defects.
limitations:
- HMDB0014401 page and XML routes returned 403; independent exact HMDB structure was
  not inspected. CAS was checked through official public database cross-attribution,
  without paid registry access.
- All nine adopted abstracts and all source-linked CARD publication abstracts were
  inspected. Full original follow-up covered the six-page 1991 target paper, the 2016
  mobilome paper and the short Tet44 study; most other resistance papers remain abstract-depth
  only.
- The LamB 2014 publisher route returned 403. Its complete original abstract and the
  official CARD definition establish the missing loss/downregulation condition, but
  original full experimental tables and exact bulk chlortetracycline form were unavailable.
- Antiprotozoal use is supported by official ChEBI/KEGG and identifiable historical
  primary reports; the original outcome/material tables were not fully accessible.
  No clinical efficacy estimate, direct protozoal mechanism or current treatment recommendation
  is claimed.
- PubChem differs by keto-enol representation. Tautomer canonicalization is a diagnostic
  and may alter stereochemical labels; explicit original InChI layers are retained.
  No natural-product stereo revision is proposed.
- Eremomycine is attested by CARD but its independent historical naming basis was
  not established by the bounded exact-spelling search. This is unresolved provenance,
  not proof of a false alias.
- No primary support is transferred from anhydro/epimeric analogues, different tetracyclines,
  animal-feed mixtures or salt formulations to an unqualified exact-neutral structure
  claim. Scientific completion is partial; deterministic validation does not promote
  native REVIEWED status.
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
