# Antimicrobial data sources: licence and quality landscape

Deep-research report, 2026-08-29. 109 agents, six search angles, three-vote
adversarial verification per claim. Findings below are the ones that survived;
refuted candidates are listed at the end so a future reader does not re-derive
them.

This report is evidence for a curator, never automatic input. It exists to be
folded into `curation/source_queue.tsv` by the `source-queue` skill — one row
at a time, with the licence column moved off UNVERIFIED only where the report
cites the licence page itself.

## Summary

For a CC0-target, one-structure-per-record antibiotic knowledge base, the
verified evidence splits the source landscape along licensing as sharply as
along content: ChEBI (CC BY 4.0, with dedicated 3-star-only SDF bulk files
that exclude ontology class terms by construction) and MIBiG 4.0 (CC BY 4.0,
bulk JSON on Zenodo, with an explicit reviewed/Quality filter) are the two
cleanest fills for the structure and BGC/producer-organism gaps, but both
impose attribution and cannot be re-dedicated as CC0. CARD is licence-
bifurcated in a way that hits the stated use case directly: aro.obo/aro.owl
are CC BY 4.0 and redistributable with credit, while card.json — precisely
where the authoritative determinant-to-mechanism, AMR Gene Family and Drug
Class categories live — falls under restrictive McMaster terms prohibiting
reproduction by any commercial organization without written permission and
asking that materials be used unmodified, which conflicts with both
harmonization and a CC0 release. On activity data, ChEMBL is the best assay-
attached source (it carries CO-ADD's ~100K antimicrobial screening
measurements under src_id 40 with organism, concentration, medium and
detection method attached) but is CC BY-SA 3.0 copyleft, so it can be
aggregated alongside CC0 content and never relabelled CC0; BV-BRC's AMR
phenotypes are ~93% machine-learning predictions that must be filtered on
evidence="Laboratory Method". The confirmed data-quality traps are structural
rather than cosmetic: ChEMBL's GetParent does not reduce genuine mixtures or
all-salt records to one component, PubChem CIDs are standardized away from
depositor SMILES in ~44% of cases, ARO carries only a few hundred
structureless antibiotic-molecule terms, and Standard InChIKey silently fails
on some tautomers, organometallic cis/trans, and relative stereochemistry.

## Verified findings

### 1. CARD is licence-bifurcated: the ARO ontology files are CC BY 4.0 and redistributable with attribution, but card.json and the rest of the CARD data (reference sequences, mutations, AMR Gene Family / Drug Class / Resistance Mechanism annotations, detection models) sit under restrictive McMaster terms — so the determinant-to-mechanism categories the knowledge base most needs are the part hardest to redistribute.

**Confidence:** high · **Verification:** 3-0 (merged from 5 unanimous claims)

CARD's /about and /download pages both state verbatim that "Ontologies at the
Comprehensive Antibiotic Resistance Database are freely available under the
Creative Commons CC-BY license version 4.0", and both carry the countervailing
term for everything else: "Use or reproduction of these materials, in whole or
in part, by any commercial organization whether or not for non-commercial
(including research) or commercial purposes is prohibited, except with written
permission of McMaster University." The academic/non-profit clause (section 4)
permits free reproduction but only if "The Materials not be modified and used
'as is'" and "McMaster University be identified as the source" — conditions
that conflict with both harmonization (modification) and CC0 (attribution
waiver). Independently confirmed: github.com/arpcard/aro ships the full CC BY
4.0 legal code as LICENSE and GitHub's API reports spdx_id "CC-BY-4.0"; OBO
Foundry's ARO registry entry independently records "CC BY 4.0". Verified live
2026-08-29 (the /about page cites 2026 CARD publications, so these are the
terms in force). Practical consequence: a pipeline harvesting antibiotic-
molecule terms from aro.obo is licensed with credit; the same content pulled
from card.json is not. Merged from five separately verified unanimous claims.

- https://card.mcmaster.ca/about
- https://card.mcmaster.ca/download
- https://github.com/arpcard/aro
- https://obofoundry.org/ontology/aro.html

### 2. ARO's declared scope covers exactly the mechanism layer the knowledge base needs (resistance genes/mutations, their products, mechanisms, phenotypes, plus antibiotics and their molecular targets), but its chemical-entity content is small and structureless — 367 antimicrobial molecules and 33 adjuvants at v3.2.4 — so ARO should be used as a mechanism/determinant vocabulary, not as a structure source.

**Confidence:** high · **Verification:** 3-0 (merged from 2 unanimous claims)

The ARO README and its OBO Foundry description both read: "The Antibiotic
Resistance Ontology describes antibiotic resistance genes and mutations, their
products, mechanisms, and associated phenotypes, as well as antibiotics and
their molecular targets." This is instantiated as real branches, not
aspirational text: antibiotic molecule (ARO:1000003), mechanism of antibiotic
resistance (ARO:1000002), determinant of antibiotic resistance (ARO:3000000),
antibiotic target (ARO:3000708). CARD 2023 (NAR 51:D690) states "As of version
3.2.4, CARD encompasses 6627 ontology terms, 5010 reference sequences, 1933
mutations, 3004 publications, and 5057 AMR detection models" and elsewhere in
the same paper "the ARO contains additional information on 367 antimicrobial
molecules and 33 adjuvants" (verified by raw grep of the Europe PMC full-text
XML, PMC9825576 — under-quoted in the original claim rather than fabricated).
A verifier enumerated the CHEBI:33281 subtree via OLS4 (57 roles) and pulled
incoming has-role relations, finding 4,032 unique compounds by direct
assertion alone — ~11x larger than ARO's molecule set, though only ~3x if
narrowed to the antibacterial branch. ARO antibiotic-molecule terms carry
names, definitions and hierarchy but no SMILES/InChI/InChIKey. Currency
caveats: v3.2.4 is August 2022, and the 33-adjuvant figure is superseded —
CARD's own resistance-modifying-agents paper reports "over 60 new molecules"
and five new adjuvant categories (ARO:3007222–3007226). The "antibiotic
target" branch is also coarse (wild-type components such as membrane or
protein synthesis) rather than protein-level.

- https://github.com/arpcard/aro
- https://academic.oup.com/nar/article/51/D1/D690/6764414
- https://obofoundry.org/ontology/aro.html
- https://doi.org/10.1128/spectrum.02744-23

### 3. ChEBI ships a dedicated 3-star-only SDF bulk file that loads exactly the manually-curated structure set with no post-hoc star filtering — and because all SDF variants exclude ontology classes by construction, the class-terms-as-compounds trap is eliminated for that load path; the trade-off is that the antimicrobial role hierarchy must be pulled separately from OBO/OWL, where star filtering is still post-hoc.

**Confidence:** high · **Verification:** 3-0 (merged from 2 unanimous claims)

Live directory listing of https://ftp.ebi.ac.uk/pub/databases/chebi/SDF/
(fetched 2026-08-29, all files dated 2026-08-14, ChEBI Release 254) contains
exactly: chebi.sdf.gz (139M), chebi_3_stars.sdf.gz (57M), chebi_lite.sdf.gz
(64M), chebi_lite_3_stars.sdf.gz (15M), plus README and LICENSE. The downloads
page states "For each variant, there are files for all 2-star and 3-star
entries, as well as separate files containing only 3-star entries." The FULL
variant carries "structure data (smiles, inchi and inchikey)" plus formula,
charge, mass, synonyms and cross-references, so chebi_3_stars.sdf.gz is
directly usable as the reviewed structure set; size ratios (57M/139M, 15M/64M)
confirm genuine filtered subsets. Critically, the README's Final Notes state
"all SDF files exclude any ontological information as ontological classes are
not able to be represented as they do not contain a structure" — for a one-
complete-structure-per-record KB that exclusion is a feature, but it means
CHEBI:33281 role edges must come from chebi.obo/OWL or the API. Licensing: the
co-located LICENSE file is CC BY 4.0, and separately the ChEBI downloads page
itself states no licence terms at all (grep of the raw HTML for licen[cs]e /
creative commons / copyright / terms matched only Material Design icon-font
glyph names); the terms live at https://www.ebi.ac.uk/chebi/about — "The data
on this website is available under the Creative Commons License ( CC BY 4.0 ),
and governed by EMBL-EBI's terms of use". So ChEBI is redistributable with
attribution, not CC0. NOTE: a related claim about FULL/CORE/LITE tiers and
LITE lacking structures was REFUTED 0-3 — do not assert that tier breakdown.

- https://www.ebi.ac.uk/chebi/downloads
- https://ftp.ebi.ac.uk/pub/databases/chebi/SDF/
- https://www.ebi.ac.uk/chebi/about

### 4. MIBiG 4.0 is the strongest licence-compatible fill for the producer-organism and BGC gap — bulk JSON on Zenodo under CC BY 4.0 with a machine-readable quality filter — but only ~40% of the 4.0-cycle entries had passed expert peer review at publication, and the authors themselves recommend reviewed entries only for high-confidence applications.

**Confidence:** high · **Verification:** 3-0 (merged from 2 unanimous claims)

The MIBiG 4.0 paper (Zdouc et al., NAR 2025 Database issue,
doi:10.1093/nar/gkae1115, PMC11701617) states in Data availability: "Files in
JSON format following the MIBiG data standard (https://github.com/mibig-
secmet/mibig-json) can be found on the MIBiG webpage
(https://mibig.secondarymetabolites.org/download) and on the MIBiG Zenodo
Community page (https://doi.org/10.5281/zenodo.13367755). ... All data are
freely available with no restrictions for academic and commercial reuse under
the OSI-approved CC BY 4.0 Open Source license." Independently confirmed via
the Zenodo API: record 14835872 (conceptdoi 10.5281/zenodo.13367755), version
4.0.1 dated 2025-02-08, metadata.license.id = "cc-by-4.0", containing
mibig_json_4.0.tar.gz (10.0 MB) alongside GenBank and protein-FASTA bulk
files. On quality: "Of the total 1147 contributed entries (557 new, 590
modified), 464 (40%) have been reviewed at the time of manuscript preparation.
While all entries are available, those that are reviewed are highlighted ...
For applications using the MIBiG data where a high confidence level is
required (e.g. machine learning applications), we recommend the use of
reviewed entries only." A second, independent mechanism: "we also introduced a
'Quality' identifier, and it is possible to filter entries based on high,
medium or questionable quality of data. Note that this label only reflects the
presumed data quality of an MIBiG entry and does not address the quality of
the underlying literature." The live 4.x schema
(raw.githubusercontent.com/mibig-secmet/schema/main/schemas/mibig/entry.json)
has a top-level `quality` property with enum
["questionable","low","medium","high"] — four levels, not the three named in
the paper, so implement against the enum. Provenance hygiene:
github.com/mibig-secmet/mibig-json has NO LICENSE file (GitHub API license:
null; raw LICENSE 404) and was last pushed 2024-03-18; the current schema
moved to mibig-secmet/schema (pushed 2026-04-04), so cite the Zenodo DOI as
licence-of-record. The paper's own phrase "OSI-approved" is factually wrong
(CC BY 4.0 is not an OSI licence) — do not repeat it. Two adjacent MIBiG
claims were REFUTED: the 3059-entries/5002-structures figures (1-2) and the
assertion that MIBiG 4.0 models bioactivity as assay-attached with a
Concentration field (0-3) — do NOT treat MIBiG as an assay-attached activity
source.

- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11701617/
- https://doi.org/10.5281/zenodo.13367755
- https://mibig.secondarymetabolites.org/download
- https://github.com/mibig-secmet/schema

### 5. ChEMBL is the best assay-attached activity source and now carries CO-ADD's antimicrobial screening data (31 datasets, ~100K measurements, src_id 40) with organism, concentration, medium and detection method attached — but its CC BY-SA 3.0 copyleft makes it unmergeable into a CC0 release, and the CO-ADD subset is single-concentration hit-calls rather than full MIC titrations.

**Confidence:** high · **Verification:** 3-0 (merged from 2 unanimous claims)

ChEMBL 2023 (NAR 52:D1180) states under "CO-ADD antimicrobial screening data
(source ID 40)": "31 additional datasets (almost 100 thousand new bioactivity
measurements) have been deposited in the ChEMBL database since release 24."
Verified independently against the live API: GET
/api/data/source.json?src_id=40 returns src_short_name "COADD", description
"CO-ADD Antimicrobial Screening"; GET /api/data/assay.json?src_id=40 returns
total_count 35, e.g. CHEMBL3832900 with assay_organism "Staphylococcus aureus"
and assay_parameters ASSAY_TEST="Inhibition of Bacterial Growth", CONC=32.0
ug.mL-1, DETECTION_METHOD="Absorption (OD600)", MEDIA="CAMHB" — the assay
context the KB requires is genuinely attached. Corroborated by the ChEMBL blog
("Pathogen data in ChEMBL", Sept 2021): 31 datasets, "Overall, 100 K
activities (against approximately 24 K compounds)". Licence: the same NAR
paper states "The ChEMBL database is made available under a Creative Commons
Attribution-ShareAlike 3.0 Unported license"; corroborated by the live ChEMBL
gitbook FAQ (derivatives must be distributed "under an identical license"),
chembl.github.io/chembl-licensing, and the full CC BY-SA legal text shipped as
CHEMBL.LICENSE in the FTP bulk downloads — so the licence attaches to the bulk
artifacts, not just the web UI. Still CC BY-SA as of ChEMBL 36 (Jul 2025) and
37 (May 2026), despite EMBL-EBI's stated CC0 ambition. Legal consequence: CC
BY-SA 3.0 §4(b) requires Adaptations under the same or a compatible licence;
CC0 waives ShareAlike and attribution and is not a permitted downstream
licence. A KB may still aggregate ChEMBL-derived content carried under CC BY-
SA alongside CC0 material — what is barred is relabelling it CC0.
Qualifications: ChEMBL holds a SUBSET of CO-ADD (~24K compounds, 35 assay
definitions vs CO-ADD's own program of hundreds of thousands), so full
coverage still needs db.co-add.org; and ChEMBL carries an extra restriction
that properties computed with commercial software are subject to those
vendors' terms. A separate ChEMBL scale claim (release 33: 20.3M activities /
2.4M compounds / 1.6M assays) was REFUTED 0-3 — do not cite those figures.

- https://academic.oup.com/nar/article/52/D1/D1180/7337608
- https://chembl.gitbook.io/chembl-interface-documentation/frequently-asked-questions/general-questions
- http://chembl.github.io/chembl-licensing/
- https://www.ebi.ac.uk/chembl/api/data/source.json?src_id=40

### 6. BV-BRC's AMR phenotype resource is ~93% machine-learning predictions mixed into the same data type as measured AST results, so any spectrum/activity extraction MUST filter on evidence="Laboratory Method" or it will silently ingest model output as measurement — and the API's evidence string differs from the value shown in BV-BRC's own UI documentation.

**Confidence:** high · **Verification:** 3-0

BV-BRC's data-protocol page states: "BV-BRC collects AMR phenotype data
generated using antimicrobial susceptibility testing methods (AST) from
published studies and collaborators. In addition, BV-BRC also provideS
predicted AMR phenotypes using machine learning classifiers." Because that
page is now Cloudflare-gated (HTTP 403), a verifier confirmed against the live
Solr API instead, which is stronger evidence: GET
/api/genome_amr/?eq(evidence,*) returns predicted and measured rows side by
side in ONE core — {"genome_id":"573.23123","antibiotic":"imipenem","resistant
_phenotype":"Susceptible","evidence":"Computational
Method","computational_method":"AdaBoost Classifier"} next to {"genome_id":"28
901.24388","antibiotic":"azithromycin","resistant_phenotype":"Susceptible","ev
idence":"Laboratory Method","laboratory_typing_method":"MIC","measurement":"<4
","measurement_value":"4","measurement_unit":"mg/L","testing_standard":"CLSI",
"testing_standard_year":2021,"pmid":[35651495]}. Both carry the same
resistant_phenotype field, so a naive antibiotic+phenotype read cannot
distinguish them. Counts queried 2026-08-29: evidence="Computational Method"
16,257,769 rows vs evidence="Laboratory Method" 1,285,111 rows (total
17,542,880) — 92.7% predictions. Implementation trap: BV-BRC's UI quick-
reference documents the value as "Computational Prediction" while the API
returns "Computational Method", so the filter must match the API string.
Circularity trap: the ML classifiers are trained on measured phenotypes from
the same resource, so predictions are not independent evidence. Scope caveat:
the resource is genome-to-antibiotic susceptibility (organism/strain
resistance), not compound-centric spectrum data, and only the ~1.29M
Laboratory Method rows carry assay context (laboratory_typing_method,
measurement/sign/unit, testing_standard, pmid).

- https://www.bv-brc.org/docs/data_protocols/antimicrobial_resistance.html
- https://www.bv-brc.org/api/genome_amr/
- https://www.bv-brc.org/docs/quick_references/organisms_taxon/antimicrobial_resistance.html

### 7. A ChEMBL 'parent' structure is NOT a guarantee of a single-component compound: GetParent deliberately leaves genuine mixtures, all-salt records (sodium chloride, sodium citrate) and organometallics unreduced, so a one-structure-per-record knowledge base must run its own multicomponent filter downstream.

**Confidence:** high · **Verification:** 3-0

Bento et al., "An open source chemical structure curation pipeline using
RDKit", J Cheminform 12:51 (2020), doi 10.1186/s13321-020-00456-1, states
verbatim: "Compounds containing more than one component that are genuine
mixtures (i.e., all of the components are absent from the salt and solvent
lists) has, in the context of the ChEMBL database, its parent registered as
the identical mixture."; "For cases such as sodium chloride and sodium
citrate, where both components are in the salt list, the GetParent module does
not remove any component and the parent remains the same as the salt.";
"Organometallic compounds do not however have salts removed due to the
complexity of how they are often represented in the deposited molfile."
Verified verbatim via PMC7458899 and independently via the BMC full text.
Still current: the ChEMBL_Structure_Pipeline wiki ("Work done by each step",
get_parent_molblock) documents the same no-op behaviour today — "Salts
(defined in a list) are removed unless this step removes all fragments, in
which the molecule is not modified" — and the ChEMBL FAQ corroborates that a
molfile may be "a parent and its salts; a parent, its salts and solvent; a
combination of only salts; or a true mixture", with molregno ==
parent_molregno also occurring where the record "could not be further
processed for various reasons (e.g., inorganic mixture)". Scope nitpick: "left
untouched" is precise only w.r.t. component removal — the standardizer may
still neutralise charges or strip isotopes. Important counterpoint to the
salt-conflation trap named in the research question: because salt and parent
forms have different Standard InChIs, ChEMBL assigns them different CHEMBL_IDs
linked via molecule_hierarchy, so ChEMBL's key SEPARATES salts from parents
rather than conflating them. A related quantitative claim (6% multicomponent,
>1M activity values, published 162-salt/9-solvent lists) was REFUTED 1-2 — do
not cite those numbers.

- https://jcheminf.biomedcentral.com/articles/10.1186/s13321-020-00456-1
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7458899/
- https://github.com/chembl/ChEMBL_Structure_Pipeline/wiki/Work-done-by-each-step
- https://chembl.gitbook.io/chembl-interface-documentation/frequently-asked-questions/drug-and-compound-questions

### 8. The Standard InChIKey — the uniqueness key ChEMBL uses and the natural join key for a structure-per-record KB — has three documented failure modes directly relevant to antibiotic curation: some 1,5 keto-enol tautomer pairs are not recognised as the same compound, cis/trans isomerism in organometallics is not distinguished, and relative stereochemistry is unsupported (absolute or none only).

**Confidence:** high · **Verification:** 3-0

Bento et al. 2020 (J Cheminform, doi 10.1186/s13321-020-00456-1) states: "The
Standard InChI and the corresponding hashed InChIKey are used in ChEMBL as the
measure of uniqueness for a chemical structure ... Thus, when compounds from
different scientific articles have the same Standard InChI and InChIKey they
are considered to be the same compound and are assigned the same ChEMBL
identifier (CHEMBL_ID). ... It should be remembered that there are certain
disadvantages to using Standard InChI as an identifier, such as its inability
to recognise some 1,5 keto-enol tautomers as being the same compound, its
inability to recognise cis/trans isomerism in organometallic compounds (e.g.
cisplatin and transplatin) and it does not support the use of relative
stereochemistry, only absolute or no stereochemistry." Verified verbatim in
the authors' Research Square deposit (rs-34715/v2, CC BY 4.0) and
independently in the published version. Written by the ChEMBL team at EMBL-EBI
about their own registration system — the authority, not a secondary
characterisation. Independently corroborated: Standard InChI applies
disconnected-metal treatment and covers only sp3/sp2 organic stereo, so
square-planar Pt(II) geometry is lost; relative (SREL) and racemic (SRAC)
stereo options exist only in non-standard InChI, making Standard InChI
absolute-or-none by construction. Currency: InChI 1.07 has shipped since (the
paper says "currently version 1.05") but did not add relative stereochemistry
to Standard InChI, so all three failure modes stand. Minor scoping note: the
paper's condition is "same Standard InChI AND InChIKey"; compressing to
InChIKey alone is fair since the key is a hash, though collisions are formally
possible. Relevance to antibiotics: tautomer-sensitive scaffolds
(tetracyclines, quinolones), metal-containing agents, and natural products
reported with relative-only stereochemistry are exactly the classes where a
discovery paper's structure cannot be keyed reliably.

- https://jcheminf.biomedcentral.com/articles/10.1186/s13321-020-00456-1
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7458899/

### 9. PubChem CIDs are standardized records, not depositor submissions — 44% of structures that pass standardization are modified — so a CID's SMILES/InChIKey can differ from the SMILES in the source that supplied it, and cross-toolkit SMILES string comparison is not a valid equality test.

**Confidence:** high · **Verification:** 3-0

Hähnke, Kim & Bolton, "PubChem chemical structure standardization", J
Cheminform 10:36 (2018), PMC6086778, by the PubChem team itself: "Of all
structures that pass standardization, 44% are modified in the process,
reducing the count of unique structures from 53,574,724 in substance to
45,808,881 in compound as identified by de-aromatized canonical isomeric
SMILES." Internally corroborated: "Of the 104,293,434 substances successfully
passing the standardization process, 55.5% were not modified at all. The
remaining 44.5% were altered in at least one of the standardization steps."
Two mandatory qualifications: (1) the absolute counts come from a JANUARY 2013
Substance snapshot ("The version of PubChem Substance used in this study
contained 116,641,122 entries (from January 2013)") — the 44% rate is durable,
the counts are not; PubChem 2025 (NAR 53:D1516) reports 322M substances vs
119M compounds as of 12 Sep 2024, the same architecture at ~2.7x the collapse
ratio. (2) The framing "CID records are not the structures depositors
submitted" is too absolute given 55.5% pass through unmodified — write it as
"may differ". Curation implication for a KB that uses PubChem for CARD-only
molecules lacking structures: the paper's uniqueness metric is de-aromatized
canonical isomeric SMILES and PubChem's canonical SMILES were OpenEye-
generated, so equality must be tested on InChIKey, never on SMILES strings
across toolkits — and provenance should record that the structure is PubChem's
standardized form, not the source publication's depiction.

- https://jcheminf.biomedcentral.com/articles/10.1186/s13321-018-0293-8
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6086778/

### 10. The overall licence stack for every major verified source is CC BY, CC BY-SA, or proprietary — none is CC0 — so a genuinely CC0 release is not achievable by ingestion alone; the KB must segregate licensed content, carry per-record attribution, or seek waivers.

**Confidence:** high · **Verification:** 3-0 (synthesis of unanimous licence claims)

Synthesis across the verified licence findings: ChEBI CC BY 4.0 (LICENSE file
in the SDF directory plus ebi.ac.uk/chebi/about); ARO CC BY 4.0 (repo LICENSE,
GitHub spdx_id CC-BY-4.0, OBO Foundry registry, CARD download page); card.json
restrictive McMaster terms with a commercial prohibition and an unmodified-use
condition; ChEMBL CC BY-SA 3.0 Unported copyleft (NAR 2024 paper, gitbook FAQ,
chembl-licensing page, CHEMBL.LICENSE in the FTP bulk downloads); MIBiG CC BY
4.0 (paper Data availability plus Zenodo metadata.license.id cc-by-4.0). Three
distinct legal postures matter operationally: (a) CC BY sources can be
redistributed inside a mixed KB provided attribution and licence notice ride
along per record — CC BY 4.0 §3(b) permits an Adapter's License only if it
"does not prevent recipients from complying with this Public License", which a
blanket CC0 dedication would; (b) CC BY-SA (ChEMBL) additionally forces
derivative works onto the same licence, so it can be aggregated but never
relabelled; (c) card.json is not redistributable into a CC0 KB at all absent
written McMaster permission, since a CC0 release grants downstream commercial
reuse that McMaster's section 5 prohibits. One genuine grey zone: CC BY-SA 3.0
Unported is copyright-based and does not expressly license EU sui generis
database rights, so enforceable scope over individual factual data points is
jurisdictionally murky — a grey zone, not a licence to treat ChEMBL facts as
CC0.

- https://www.ebi.ac.uk/chebi/about
- https://card.mcmaster.ca/about
- https://academic.oup.com/nar/article/52/D1/D1180/7337608
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11701617/
- https://github.com/arpcard/aro

## Open questions

- What are the actual ARO release cadence and identifier-stability guarantees?
  Both candidate claims were refuted (the 'housekeeping mode / frozen' framing
  1-2 and the 'monthly releases, unstable terms' framing 0-3), leaving no
  verified answer on whether ARO IDs and relation content can be pinned across
  releases — and since ARO is now at v4.0.2 (2026-08-12) versus the v3.2.4
  counts cited here, current molecule and adjuvant counts need re-measuring
  directly from aro.obo.
- Can McMaster grant a waiver or an explicit open licence for the determinant-
  to-mechanism content in card.json? This is the highest-value unblocking
  action identified: the AMR Gene Family / Drug Class / Resistance Mechanism
  categories are a named gap the KB must fill, they are the part CARD's
  licence most restricts, and it is unresolved whether the CC BY-licensed ARO
  subtree alone carries the determinant-level mechanism assignments. Worth a
  direct written request rather than a workaround.
- Which sources supply MIC values with full assay context — organism, strain,
  method (broth microdilution vs agar dilution), medium, inoculum, units and
  breakpoint standard — under a redistribution-compatible licence? ChEMBL has
  the schema but is CC BY-SA; the CO-ADD deposits in ChEMBL are single-
  concentration hit-calls rather than MIC titrations; BV-BRC's Laboratory
  Method rows are genome-centric susceptibility rather than compound-spectrum
  panels; and EUCAST/CLSI breakpoint tables, CO-ADD's own db.co-add.org, SPARK
  and BacDive were never evaluated. The assay-attached-MIC gap is unfilled by
  any verified source.
- How should a curator go from a natural-product discovery paper (e.g. a new
  Streptomyces metabolite) to a structure record, given that MIBiG's quality
  and reviewed flags describe entry curation but explicitly 'do not address
  the quality of the underlying literature', that MIBiG is not an assay-
  attached activity source, and that Standard InChIKey cannot represent the
  relative-only stereochemistry such papers often report? The entire
  discovery-literature question — journals, reporting conventions, whether
  structures are deposited machine-readably, NPAtlas and antiSMASH-DB coverage
  — remains unresearched.

## Refuted candidate claims

Recorded so they are not re-derived. Each failed adversarial verification.

- ChEBI distributes its ontology in three content tiers (FULL, CORE, LITE)
  across three serializations (OWL, OBO, JSON) from
  https://ftp.ebi.ac.uk/pub/databases/chebi/ontology/, and only the FULL
  variant carries the structure fields needed for a structure-keyed knowledge
  base (SMILES, InChI, InChIKey) alongside formula, charge, mass and curated
  cross-references; LITE has no structures at all.
- MIBiG 4.0 holds 3059 total BGC entries (a 22% increase over 3.0), of which
  2634 entries carry 5002 associated chemical structures while 672 entries
  still lack any chemical structure — so a structure-complete knowledge base
  cannot ingest MIBiG entries wholesale and must filter on structure presence,
  with RNPs/RiPPs the known weak spot.
- The salt/parent problem is quantitatively load-bearing for activity data:
  only about 6% of ChEMBL compounds are multicomponent (mostly salts), but
  those records carry over a million activity values — so a knowledge base
  keying on parent structures must run an explicit salt-stripping step or it
  will orphan a disproportionate share of MIC/bioactivity measurements.
  ChEMBL's GetParent does this using explicitly published lists of 162 salts
  and 9 solvents (derived from the USAN Council pharmacological salts list),
  available as files in the GitHub repo.
- As of MIBiG 4.0 bioactivity is modelled as a property of a specific assay,
  drawn from a controlled vocabulary, with an optional quantitative
  'Concentration' field — i.e. MIBiG now records activity with assay context
  attached rather than as a bare qualitative label.
- ChEMBL release 33 (prepared 31 May 2023) contains over 20.3 million
  bioactivity measurements on 2.4 million unique compounds, across more than
  1.6 million assays and more than 17,000 targets, drawn from over 88,000
  publications, patents and deposited datasets — establishing its coverage
  scale as an assay-attached activity source.
- ARO curation is in 'housekeeping mode' — new AMR genes are added but the
  ontology's structure and relationships are not being restructured (except
  anti-fungal resistance terms and finer efflux modelling) — so its class
  hierarchy and relation semantics are effectively frozen for the near term.
- The ARO is under active development with monthly releases, and CARD itself
  warns that terms change significantly between releases and that revisions
  can be incomplete — so ARO identifiers and relation content should not be
  assumed stable across releases in a curated knowledge base.

## Sources consulted

- https://www.ebi.ac.uk/chebi/downloads
- https://card.mcmaster.ca/download
- https://link.springer.com/article/10.1186/s13321-026-01196-4
- https://jcheminf.biomedcentral.com/articles/10.1186/s13321-020-00456-1
- https://jcheminf.biomedcentral.com/articles/10.1186/s13321-018-0293-8
- https://jcheminf.biomedcentral.com/articles/10.1186/s13321-015-0068-4
- https://academic.oup.com/nar/article/52/D1/D1180/7337608
- https://www.bv-brc.org/docs/data_protocols/antimicrobial_resistance.html
- https://db.co-add.org/
- https://academic.oup.com/nar/article/53/D1/D748/7848838
- https://mic.eucast.org/
- https://github.com/arpcard/aro
- https://academic.oup.com/nar/article/51/D1/D690/6764414
- https://academic.oup.com/nar/article/51/D1/D744/6830666
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11701617/
- https://academic.oup.com/nar/article/53/D1/D691/7908803
- https://www.npatlas.org/download
- https://elifesciences.org/articles/70780
- https://pubs.acs.org/doi/10.1021/acs.jnatprod.5c00836
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10767862/
- https://card.mcmaster.ca/about
- https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0213090
- https://reusabledata.org/chembl.html
- https://github.com/ebi-chebi/ChEBI/blob/master/LICENSE
- https://coconut.naturalproducts.net/download
- https://www.ebi.ac.uk/training/online/courses/using-publicly-available-data/data-licences/
