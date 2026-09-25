# YAML Record Review: 1,3,6,8-tetraazatricyclo[4,4,1,13,8]dodecane

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/biocide/1-3-6-8-tetraazatricyclo-4-4-1-13-8-dodecane.yaml`
- Started UTC: 2026-09-25T02:37:00Z
- Finished UTC: 2026-09-25T02:58:46Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:140779` |
| Label | `1,3,6,8-tetraazatricyclo[4,4,1,13,8]dodecane` |
| Class | `BIOCIDE` |
| Status | `SEEDED` |
| Grounding | `EXACT` |
| Maintained owner | Generated from `data/raw/chebi_antimicrobials.tsv`; future identity, synonym, structure, parent, role, and xref changes belong in the ChEBI extractor/seeder path or `curation/decisions.tsv` |

The full 82-line YAML record was read. It is a generated ChEBI-only seed with:

- one source concept, `CHEBI:140779`, minted as
  `antibioticmech:chebi-1b1682dff4`
- one ChEBI antimicrobial role, `CHEBI:48219`
- one ChEBI parent, `CHEBI:140780`
- one brand name, `Dezant`
- eight exact synonyms: `1,3,6,8-tetraazatricyclo[4.4.1.13,8]dodecane`,
  `1,6,3,8-dimethan-tetra-aza-cyclodecane`,
  `1,6,3,8-dimethano-1,3,6,8-tetraazacyclodecane`,
  `1,6,3,8-diméthano-tétra-aza-cyclodécane`,
  `TATD`, `TTD`, `[14.22]adz`, and `tetraazatricyclododecane`
- three exact same-structure registry xrefs, `cas:51-46-7`,
  `chemspider:59511`, and `reaxys:2765`
- three patent document xrefs, `patent:RU2273495`,
  `patent:US4113932`, and `patent:WO2008002199`
- SMILES, Standard InChI, Standard InChIKey
  `YHNNUDUEGSHVGJ-UHFFFAOYSA-N`, formula `C8H16N4`, charge `0`,
  average mass `168.244`, and monoisotopic mass `168.1375`
- no `mode_of_action`, `mode_of_action_target_scope`,
  `molecular_targets`, `activity_spectrum`, `resistance_mechanisms`,
  `producer_organisms`, `causal_graphs`, `datasets`, `discussions`, or
  record-level `evidence`
- only seed/reseed history events from `seed_from_sources`

## Validation

| Check | Result |
|---|---|
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv` | Passed; wrote 2,859 review-readiness rows. The target is row 163 with `MECHANISM_REVIEW: mechanism is absent; 7 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| `just worklist --queue mechanism --limit 0 --tsv /tmp/antibioticmech-mechanism-queue.tsv` | Passed; `CHEBI:140779` is absent from this queue. |
| `just worklist --queue activity-candidate --limit 0 --tsv /tmp/antibioticmech-activity-candidate-queue.tsv` | Passed; `CHEBI:140779` is absent from this queue. |
| `just worklist --queue producer-candidate --limit 0 --tsv /tmp/antibioticmech-producer-candidate-queue.tsv` | Passed; `CHEBI:140779` is absent from this queue. |
| `just worklist --queue xref-unverified --limit 0 --tsv /tmp/antibioticmech-xref-unverified-queue.tsv` | Passed; `CHEBI:140779` is absent from this queue. |
| `just worklist --queue xref-span-conflict --limit 0 --tsv /tmp/antibioticmech-xref-span-conflict-queue.tsv` | Passed; `CHEBI:140779` is absent from this queue. |
| `just worklist --queue multi-component --limit 0 --tsv /tmp/antibioticmech-multi-component-queue.tsv` | Passed; `CHEBI:140779` is absent from this queue. |
| `just worklist --queue moa-scope --limit 0 --tsv /tmp/antibioticmech-moa-scope-queue.tsv` | Passed after the known unrelated `iclaprim` cross-reference diagnostic; `CHEBI:140779` is absent from this queue. |
| `just worklist --queue target-evidence --limit 0 --tsv /tmp/antibioticmech-target-evidence-queue.tsv` | Passed; `CHEBI:140779` is absent from this queue. |
| `just validate data/antibiotics/biocide/1-3-6-8-tetraazatricyclo-4-4-1-13-8-dodecane.yaml` | Passed with `No issues found`. |
| `just validate-strict data/antibiotics/biocide/1-3-6-8-tetraazatricyclo-4-4-1-13-8-dodecane.yaml --out /tmp/tetraazatricyclododecane-140779-validate-strict.tsv` | Passed; one file scanned, zero `ERROR` rows. |
| `just verify-corpus --summary` | Passed after the known unrelated `iclaprim` self-contradictory CARD cross-reference diagnostic; the corpus reproduces exactly. |

No narrower repository `just` targets exist for standalone term, reference, or
history validation; those checks are covered here by the schema, strict writer
schema, generated-corpus reproducibility, and corpus tests in the full `just qc`
gate that should run before merging the report PR.

## Identity and Grounding

ChEBI's live `CHEBI:140779` page agrees with the generated record on the exact
identifier, label, three-star status, definition, formula, net charge, average
and monoisotopic masses, SMILES, Standard InChI, Standard InChIKey, IUPAC name,
synonyms, the `Dezant` brand name, the CAS number, the ChemSpider and Reaxys
identifiers, the three patent document xrefs, the sole antimicrobial role, and
the seven source PubMed citations.

The generated `parent_compounds` entry matches the direct ChEBI `is a` edge:

| Parent | ChEBI label |
|---|---|
| `CHEBI:140780` | `adamanzane` |

The generated `activity_roles` entry correctly keeps the only antimicrobial
role on the ChEBI page:

| Role | ChEBI label |
|---|---|
| `CHEBI:48219` | `disinfectant` |

PubChem resolves the same InChIKey to CID `66123`, and the CID properties agree
with the generated Standard InChI, Standard InChIKey, formula, charge, exact
mass, and monoisotopic mass. Its canonical SMILES is equivalent but not
byte-identical to ChEBI's emitted SMILES, which is acceptable because this
corpus stores the ChEBI representation for ChEBI-grounded records.

The patent document xrefs are document relationships, not same-structure
registry identifiers, and are correctly generated under `document_xrefs`.
Google Patents resolves `RU2273495` to the `Dezant` disinfectant patent and
`WO2008002199` to a biocidal and virucidal sodium-carbonate clathrate patent.
It resolves `US4113932` to a vinyl chloride polymerization process that lists
the exact compound among allowed polycyclic nitrogen-containing additives.

A hidden-inclusive search for `CHEBI:140779`,
`antibioticmech:chebi-1b1682dff4`, `YHNNUDUEGSHVGJ`, `51-46-7`,
`1,3,6,8-tetraazatricyclo`, `tetraazatricyclododecane`, `TATD`, and `TTD`
covered `data/antibiotics`, `data/raw`, `curation`,
`reports/yaml_record_review`, `.claude`, `README.md`, `src`, `scripts`,
`tests`, `justfile`, and `pyproject.toml`; the refined search excluded bulky
generated `data/embeddings/**` and `pages/**` outputs. It found exactly one
generated target record, its `PATHS.tsv` row, the raw ChEBI inventory row, and
the queued review row. It found no prior review report for this record and no
curator inventory row or `curation/decisions.tsv` row for the minted source
concept.

The exact hidden-inclusive ChEBI search also found `CHEBI:6824`
`hexamethylenetetramine` in the raw ChEBI inventory, but that entry has a
different structure and is only a sibling tetraaza cage, not a duplicate of
`CHEBI:140779`.

## Evidence

ChEBI cites seven PubMed records for `CHEBI:140779`:

| PMID | Relevance |
|---|---|
| `PMID:11672395` | Exact chemical synthesis lead; the compound is used to synthesize bis-triazenes. |
| `PMID:11772072` | Exact physical-chemistry lead; the study models the compound's geometry and photophysics. |
| `PMID:11772073` | Exact physical-chemistry lead; the study concerns the radical cation and electron delocalization. |
| `PMID:16833400` | Exact physical-chemistry lead; the study concerns gas-phase radical-cation spectroscopy. |
| `PMID:17909502` | Exact chemistry lead; the study concerns reduction of TATD to TMEDA. |
| `PMID:29438107` | No exact antimicrobial support found from PubMed metadata; the article concerns methyldopa and MHC class II binding in autoimmune diabetes. |
| `PMID:4181061` | Exact non-antimicrobial biological lead; the paper concerns Ehrlich ascites tumor inhibition by tetraazatricyclododecane. |

The Crossref and Springer metadata for DOI `10.1134/S1990793115030240`,
Zubairov et al. 2015, `Russian Journal of Physical Chemistry B` 9(3):471-480,
identify an exact follow-up primary article for TATD biocide curation. The
accessible abstract says the authors screened chlorine-free monoaza-, diaza-,
triaza-, and tetraazaadamantane biocides, selected
`1,3,6,8-tetraazatricyclo[4.4.1.1(3,8)]dodecane` as the most active compound,
then characterized its bactericidal, viricidal, mycocidal, and sporicidal
activities and disinfection conditions. The article body was not freely
available from Springer during this review, so its abstract supports the
existence of exact broad-spectrum biocidal data but not a schema-ready organism,
assay, exposure, or concentration claim.

The exact `Dezant` patent, `patent:RU2273495`, also supports the generated
brand name and disinfectant role. The `patent:WO2008002199` document is a
follow-up lead because it compares exact TATD with a more active
sodium-carbonate clathrate against bacteria and an avian-influenza virus. That
clathrate must not be curated as exact `CHEBI:140779`, but the comparative
assay table may contain exact parent compound bactericidal and virucidal
measurements after manual extraction from a source-language copy.

Bounded publication searches:

- PubMed ESearch for exact-name, `tetraazatricyclododecane`, InChIKey, and
  CAS-number terms returned four PMIDs: `40519109`, `34843735`, `17909502`,
  and `4181061`. The two new hits were an energetic-materials paper and an
  MHC-II Sjogren's-syndrome paper, not antimicrobial TATD activity papers.
- Europe PMC for `"1,3,6,8-tetraazatricyclo"` returned 14 records, including
  the five exact ChEBI chemistry PMIDs, exact or adjacent cage-amine chemistry
  papers, `patent:RU2273495`, a `CHEBI:140779` crystal-structure paper, and no
  PubMed-indexed direct MIC or MBC paper for exact TATD.
- Europe PMC for `"tetraazatricyclododecane" OR "tetramethylenediethylenetetramine" OR "teotropin" OR "theotropin" OR "Dezant"`
  returned 12 records, including `patent:RU2273495`, the ChEBI-cited 1969 tumor
  paper, patents using noisy vaccine or MHC terms, and several PubMed articles
  that do not test exact TATD as an antimicrobial agent.

No exact molecular target or resistance mechanism was found in the inspected
ChEBI PMIDs, the inspected patent abstracts, the 2015 Springer abstract, or the
bounded PubMed/Europe PMC metadata searches.

## Completeness

The current record is a faithful ChEBI seed, but it is not complete enough for
`REVIEWED`.

- The exact identity, ChEBI grounding, source concept, structure, disinfectant
  role, and ChEBI-imported patent relationships are supported.
- Exact activity sources exist, but no inhibitory or bactericidal measurements
  have been curated onto `activity_spectrum`.
- No source-backed molecular target or pathway was found in the bounded
  searches. The accessible exact activity sources frame TATD and Dezant as
  whole-disinfectant leads, not as target-specific mechanism papers.
- The ChEBI-listed PubMed records are useful chemistry and structure leads but
  do not by themselves provide schema-ready biocidal measurement evidence.
- The search for a prior report or curator decision was hidden-inclusive and
  found no existing local override for this seed.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The record has source-supported biocidal activity but no curated antimicrobial mechanism, molecular target, causal graph, or no-known-target discussion. | The YAML has no `mode_of_action`, no `molecular_targets`, no `causal_graphs`, and no `discussions`; `review-readiness` flags `MECHANISM_REVIEW: mechanism is absent`; no exact target was found in the inspected exact-source metadata or abstracts. | Curator-owned fields in `data/antibiotics/biocide/1-3-6-8-tetraazatricyclo-4-4-1-13-8-dodecane.yaml`, written only through `record_curation_event` and `write_validated_antibiotic`. |
| Major | Exact whole-microbe biocide observations are absent despite direct exact-compound leads. | The YAML has no `activity_spectrum`; DOI `10.1134/S1990793115030240` identifies the exact compound as the most active azaadamantane compound in a biocidal-activity study, and `patent:RU2273495` and `patent:WO2008002199` are exact or comparative Dezant/TATD biocide documents. | Curator-owned `activity_spectrum` entries in the same record; use the 2015 full text or source-language patent tables for organism, assay, concentration, exposure, and MBC/MIC-like endpoint extraction. |
| Minor | The ChEBI PubMed source leads mostly support exact chemistry or non-antimicrobial biology rather than the imported `disinfectant` role. | Five of the seven ChEBI PMIDs are exact chemistry, spectroscopy, photophysics, or synthesis papers; `PMID:4181061` is exact but antitumor-specific; PubMed metadata for `PMID:29438107` do not expose an exact TATD antimicrobial claim. | No seeded ChEBI field change recommended; add curator-owned activity evidence from DOI `10.1134/S1990793115030240` and the exact `Dezant` patent family instead. |

## Recommended Edits

1. Keep seeded identity fields unchanged. They agree with ChEBI, PubChem, and the
   committed raw row.
2. Retrieve the full text of DOI `10.1134/S1990793115030240` and extract exact
   `CHEBI:140779` bactericidal, mycocidal, sporicidal, and viricidal
   observations with organism, strain when present, assay, exposure duration,
   endpoint type, numeric concentration, units, and evidence.
3. Inspect the original `RU2273495` and `WO2008002199` patent tables before
   using them as curation sources. Keep sodium-carbonate clathrate observations
   out of this exact free-compound record unless represented as a distinct
   compound or documented comparator.
4. Search the Zubairov 2015 citing and cited literature for a concrete target or
   mechanism before assigning `mode_of_action`, `mode_of_action_target_scope`,
   `molecular_targets`, or `causal_graphs`.
5. If only whole-disinfectant kill curves are available, add a `Discussion`
   documenting that exact broad-spectrum biocide evidence exists while no
   curated molecular target was found.

## Follow-up Checks

After any future curation edit:

1. Read the post-mutation YAML and confirm `identifier: CHEBI:140779`.
2. Run `just validate data/antibiotics/biocide/1-3-6-8-tetraazatricyclo-4-4-1-13-8-dodecane.yaml`.
3. Run `just validate-strict data/antibiotics/biocide/1-3-6-8-tetraazatricyclo-4-4-1-13-8-dodecane.yaml --out /tmp/tetraazatricyclododecane-140779-validate-strict.tsv`.
4. Run `just verify-corpus --summary` to prove generated fields still reproduce.
5. Run `just worklist --queue activity-candidate --limit 0` and confirm exact
   MBC/MIC-like observations make the record visible only in relevant
   mechanism/follow-up queues.
6. Run `just qc` before merging a future curation PR.

Manual checks needed:

1. Full-text extraction from DOI `10.1134/S1990793115030240`.
2. Source-language table extraction from `RU2273495` and `WO2008002199` before
   any patent-backed numeric activity curation.
3. Mechanism search over the 2015 article's cited/citing neighborhood.

## Additional Notes

`US4113932` is a valid ChEBI document xref but not a biocidal-activity source.
It names the exact compound as a polycyclic nitrogen-containing additive in
vinyl chloride polymerization.
