# NCBI AST chemical-coverage expansion

NCBI AST remains `EVALUATING`. These are explicit interpretations of submitted
antibiotic names as active moieties, not source-supplied structure identifiers
or assertions about the salt formulation used in a laboratory. No production
inventory or corpus record is added.

## Chemical decisions

The [NCBI antibiogram vocabulary](https://www.ncbi.nlm.nih.gov/biosample/docs/antibiogram/)
recognizes the submitted labels below. Chemical identity is checked separately
against the linked primary structure sources and full corpus Standard InChIKeys.
The nine additional exact labels identify eight structures; cephalothin and
cefalotin are aliases, but their submitted labels and individual observations
are retained. These decisions do not apply to a different source snapshot.

| Submitted label | Structure authority | Identity boundary |
|---|---|---|
| enrofloxacin | [CHEBI:35720](https://www.ebi.ac.uk/chebi/CHEBI:35720) | Neutral active moiety |
| marbofloxacin | [CHEBI:132230](https://www.ebi.ac.uk/chebi/CHEBI:132230) | Neutral active moiety |
| cefpodoxime | [CHEBI:3504](https://www.ebi.ac.uk/chebi/CHEBI:3504) | Not the proxetil prodrug, CHEBI:3505; NCBI lists it separately |
| cefovecin | [PubChem:6336480](https://pubchem.ncbi.nlm.nih.gov/compound/6336480) | Fully specified neutral structure, not sodium salt |
| oxacillin | [CHEBI:7809](https://www.ebi.ac.uk/chebi/CHEBI:7809) | Not conjugate base CHEBI:52132 or a sodium salt |
| telithromycin | [CHEBI:29688](https://www.ebi.ac.uk/chebi/CHEBI:29688) | Neutral active moiety |
| cephalothin; cefalotin | [CHEBI:124991](https://www.ebi.ac.uk/chebi/CHEBI:124991) | ChEBI synonym pair; not cephalothin sodium CHEBI:3542 |
| cefotaxime | [CHEBI:204928](https://www.ebi.ac.uk/chebi/CHEBI:204928) | Not sodium salt or cefotaxime-clavulanic acid |

The committed ChEBI inventory also records `CEPHALOTHIN` and `Cephalothin`
as synonyms of CHEBI:124991. Each new map row pins the full key and its evidence
location. Existing decisions remain unchanged.

Cefovecin required an explicit stereochemistry check. The
[manufacturer label on DailyMed](https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=a8e2e58c-d9ca-45dc-8c82-6913d8e68978&type=display)
specifies the 6R,7R cephem centers, Z oxime, and 2S tetrahydrofuranyl center.
The [PubChem property response for CID 6336480](https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6336480/property/InChIKey,IUPACName,MolecularFormula/JSON)
retrieved on 2026-10-03 agrees at every center and gives
`ZJGQFXVQDVCVOK-QFKLAVHZSA-N`, exactly the corpus structure. By contrast,
[CID 9578573](https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/9578573/property/InChIKey,IUPACName,MolecularFormula/JSON)
currently lacks the 6R specification and returns
`ZJGQFXVQDVCVOK-LTRDADOWSA-N`; it is not substituted for the full identity.
The label describes a sodium product, while the map deliberately represents
its neutral active moiety. This is not evidence of the AST reagent formulation.

## Excluded salt match

The lexical corpus candidate for `ceftiofur`, CHEBI:31383, is sodium ceftiofur:
the committed ChEBI inventory gives `C19H16N5O7S3.Na`, an explicit sodium
component, and `RFLHUYUQCKHUKS-JUODUXDSSA-M`. Its generated ARO-derived label
omits "sodium" and cannot establish neutral identity.

[PubChem:6328657](https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6328657/property/InChIKey,IUPACName,MolecularFormula/JSON)
instead gives neutral `C19H17N5O7S3` and
`ZBHXIWJRIFEVQY-IHMPYVIRSA-N`. A gitignore-independent search of `data/`,
`curation/`, `downloads/`, `reports/`, `conf/`, `scripts/`, and `tests/`
found no such key before this change. The AST map therefore explicitly records
`MISSING_CORPUS_RECORD`; it does not attach these observations to the salt or
silently change the existing corpus structure.

## Review boundary

The original 36 exact mappings, 33 exclusions, and 75 unreviewed labels become
45 exact mappings, 34 exclusions, and 65 unreviewed labels. The earlier dated
188,759-observation production audit remains evidence for its pinned inputs,
not automatic approval of this expanded cohort. Candidate reconstruction,
assay-context coverage, taxonomy/CRyPTIC overlap, and BioSample multiplicity
must be checked against the expanded report before it can be published.
