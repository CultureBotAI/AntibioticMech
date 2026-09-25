# YAML Record Review: 1-carbapenem-3-carboxylic acid

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antibacterial/1-carbapenem-3-carboxylic-acid.yaml`
- Started UTC: 2026-09-25T09:20:05Z
- Finished UTC: 2026-09-25T09:59:48Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:615` |
| Label | `1-carbapenem-3-carboxylic acid` |
| Path | `data/antibiotics/antibacterial/1-carbapenem-3-carboxylic-acid.yaml` |
| Class | `ANTIBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concept | `CHEBI:615` / `1-carbapenem-3-carboxylic acid` from ChEBI release `2026-08-30` |
| Minted source key | `antibioticmech:chebi-79a511e8dd` |
| Structure key | `BSIMZHVOQZIAOY-SCSAIBSYSA-N` |
| Generated or maintained | Generated from `data/raw/chebi_antimicrobials.tsv` plus `data/antibiotics/PATHS.tsv`; future seeded identity, role, structure, synonym, xref, or source-PMID changes belong upstream rather than as hand edits. |

Resolution:

- `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv`
  regenerated the full queue and kept `CHEBI:615` as the next unreviewed row:
  `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record
  evidence item(s), 0 target(s)`.
- `data/antibiotics/PATHS.tsv` maps `CHEBI:615` to `ANTIBACTERIAL` with slug
  `1-carbapenem-3-carboxylic-acid`, matching the current record path.
- `data/raw/chebi_antimicrobials.tsv` is the ChEBI source row that seeds the
  generated target record.
- The whole target YAML was read before judging generated identity, ChEBI
  provenance, structure, xrefs, source concepts, empty mechanism and evidence
  slots, and curation history.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antibacterial/1-carbapenem-3-carboxylic-acid.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/antibacterial/1-carbapenem-3-carboxylic-acid.yaml --out /tmp/antibioticmech-chebi-615-strict.tsv` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed after emitting the known unrelated `iclaprim` / `CHEBI:31724` CARD diagnostic: 2939 expected records, 2939 on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, and 0 stale lockfile rows. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-615-worklist.tsv` | Passed; exact `CHEBI:615` rows appear only in `mechanism` and `review-readiness`. |
| `uv run runoak -i ols:chebi labels CHEBI:615 CHEBI:33281 CHEBI:33282 CHEBI:46634 CHEBI:79020` | Passed: OLS resolved the compound, `antimicrobial agent`, `antibacterial agent`, `carbapenemcarboxylic acid`, and `alpha,beta-unsaturated monocarboxylic acid`. |
| OLS4 term lookup for `CHEBI:615` | Passed: live OLS4 resolved a current, ChEBI-defining, `3_STAR` term with formula, charge, masses, SMILES, Standard InChI, Standard InChIKey, synonyms, xrefs, and the same activity roles preserved in the committed ChEBI source row. |
| KEGG compound lookup for `C06669` | Passed: KEGG resolves `C06669` to `1-Carbapen-2-em-3-carboxylic acid` / `(5R)-Carbapenem-3-carboxylate`, formula `C7H7NO3`, exact mass `153.0426`, and ChEBI cross-reference `615`. |
| BioCyc/MetaCyc lookup for `META:CPD-9377` | Not independently verified: the public BioCyc service returned an account page instead of the compound XML. |
| PubChem name lookup for `1-Carbapen-2-em-3-carboxylic acid` | Not used as exact support: the lookup returned CID `194860`, whose formula matches but whose Standard InChIKey is `QJJUCBSLEIAKSQ-WHFBIAKZSA-N`, not record key `BSIMZHVOQZIAOY-SCSAIBSYSA-N`. |
| Common Chemistry lookup for `82768-37-4` | Not independently verified: the lookup did not resolve locally; official ChEBI/OLS still preserves the CAS xref. |
| Exact PubMed/Semantic Scholar query for `"SQ 27860" OR "carbapenem-3-carboxylic" OR "carbapenem-3-carboxylate" OR "Carbapen-2-em-3-carboxylic" OR "CPD-9377"` in title/abstract | PubMed returned 20 candidates; Semantic Scholar returned HTTP 429. Useful exact leads included producer, biosynthetic-operon, carbapenem synthase, and producer self-resistance literature. |
| Exact PubMed title/abstract query for `"1-carbapen-2-em-3-carboxylic acid" OR "1-carbapen-2-em-3 carboxylic acid" OR "(5R)-carbapen-2-em-3-carboxylic acid" OR "(R)-1-carbapen-2-em-3-carboxylate" OR "SQ 27860"` | PubMed returned 23 candidates. The exact leads overlapped the producer, biosynthetic, regulation, and CarF/CarG intrinsic-resistance literature above. |

No narrower single-record reference or curation-history validator is exposed for
this ChEBI-seeded record. The focused strict validator covered closed schema
shape, and `verify-corpus --summary` covered generated drift from the
maintained raw and path-lock inputs.

## Identity and Grounding

The generated identity is consistent with official ChEBI/OLS and KEGG for exact
`CHEBI:615`:

| Assertion | Record value | Check |
|---|---|---|
| ChEBI identity | `CHEBI:615`, `1-carbapenem-3-carboxylic acid` | OLS4 resolved the term to a current ChEBI-defining class in the `3_STAR` subset. |
| Definition | A 3-carboxy derivative of `2,3-didehydro-1-carbapenam` | Matched OLS4 and the committed ChEBI row. |
| Synonyms | `2,3-didehydro-1-carbapenam-3-carboxylic acid`; `(5R)-7-oxo-1-azabicyclo[3.2.0]hept-2-ene-2-carboxylic acid`; `(5R)-Carbapenem-3-carboxylate`; `(5R)-Carbapenem-3-carboxylic acid`; `1-Carbapen-2-em-3-carboxylic acid`; `SQ 27860`; `carbapenem-3-carboxylic acid` | Matched official ChEBI/OLS synonym content after collapsing OLS' duplicate exact/related annotation for `2,3-didehydro-1-carbapenam-3-carboxylic acid`. |
| Formula and charge | `C7H7NO3`, charge `0` | Matched OLS4 and KEGG `C06669`. |
| Masses | average `153.137`, monoisotopic `153.04259` | Matched OLS4; KEGG's `153.0426` exact mass rounds from the same neutral formula. |
| SMILES | `[H][C@]12CC=C(C(=O)O)N1C(=O)C2` | Matched the committed ChEBI row and official ChEBI/OLS structure annotation. |
| Standard InChI | `InChI=1S/C7H7NO3/c9-6-3-4-1-2-5(7(10)11)8(4)6/h2,4H,1,3H2,(H,10,11)/t4-/m1/s1` | Matched the committed ChEBI row and official ChEBI/OLS structure annotation. |
| InChIKey | `BSIMZHVOQZIAOY-SCSAIBSYSA-N` | Matched the committed ChEBI row and official ChEBI/OLS structure annotation. |
| Parent compounds | `CHEBI:46634`, `CHEBI:79020` | OAK resolved these to `carbapenemcarboxylic acid` and `alpha,beta-unsaturated monocarboxylic acid`, agreeing with the compound definition and ChEBI structural classification. |
| Activity roles | `CHEBI:33281`, `CHEBI:33282` | OAK resolved these to `antimicrobial agent` and `antibacterial agent`; the generated row preserves the committed ChEBI roles. |
| Filing class | `ANTIBACTERIAL` | The ChEBI `antibacterial agent` role maps this generated record to `data/antibiotics/antibacterial/`. |

Checked exact xrefs:

| Xref | Check |
|---|---|
| `kegg.compound:C06669` | KEGG resolves the compound to a matching formula, matching rounded exact mass, matching ChEBI identifier, and names already preserved as ChEBI synonyms. |
| `cas:82768-37-4` | Present on the committed ChEBI row and official ChEBI/OLS term; not independently checked because the Common Chemistry API did not resolve locally. |
| `metacyc.compound:CPD-9377` | Present on the committed ChEBI row and official ChEBI/OLS term; not independently checked because public BioCyc returned an account page. |
| `reaxys:8832318` | Present on official ChEBI and preserved in the generated ChEBI row; not independently checked because Reaxys is not publicly resolvable. |

## Evidence

The target has no record-level `evidence`, no `mode_of_action`, no
`molecular_targets`, no `activity_spectrum`, no `resistance_mechanisms`, no
`producer_organisms`, and no `causal_graphs`. That is allowed for a freshly
ChEBI-seeded record because the ChEBI source concept supplies database
provenance for identity and role terms, and there are no claim-local
activity, target, resistance, producer, dataset, clinical, or causal
assertions that would require object-level evidence.

Exact public title/abstract leads found during this review:

| PMID | Public title/abstract support |
|---|---|
| `PMID:1335238` | The 1992 abstract reports that *Erwinia carotovora* ATCC 39048 produces antibiotic `1-carbapen-2-em-3-carboxylic acid`; it also identifies N-(3-oxohexanoyl)-L-homoserine lactone as an autoregulator of carbapenem biosynthesis rather than as a biosynthetic intermediate. |
| `PMID:7711893` | The 1995 abstract reports that *Erwinia carotovora* strain GS101 makes `1-carbapen-2-em-3-carboxylic acid` and identifies CarR as a LuxR-like regulator of antibiotic production. |
| `PMID:8939426` | The 1996 abstract reports mapping and sequencing of the *Erwinia* genes encoding `1-carbapen-2-em-3-carboxylic acid` production and reconstitution of functional beta-lactam expression in *Escherichia coli*. |
| `PMID:9402024` | The 1997 abstract reports genetic dissection of the *Erwinia carotovora* `carA--H` operon, identifies `carABC` as absolutely required for carbapenem synthesis, and provides evidence that CarF and CarG encode a novel self-resistance mechanism. |
| `PMID:16549672` | The 2006 abstract reports that *Erwinia carotovora* subsp. *carotovora* ATTn10 produces `1-carbapen-2-em-3-carboxylic acid` by expressing the `carABCDEFGH` operon. |
| `PMID:24583229` | The 2014 abstract reports that intrinsic resistance to `1-carbapen-2-em-3-carboxylic acid` in *Erwinia* / *Pectobacterium* and *Serratia* sp. ATCC 39006 is mediated by CarF and CarG by an unknown mechanism, then reports the crystal structure of the *Serratia* CarG protein. |
| `PMID:30533884` | The 2018 abstract reports a draft genome sequence for *Pectobacterium carotovorum* subsp. *carotovorum* ATCC 39048, selected for sequencing because the strain produces `1-carbapen-2-em-3-carboxylic acid`; the public abstract also says the genome contained the carbapenem biosynthetic cluster. |

Additional exact or near-exact leads from bounded PubMed searches:

| PMID | Assessment |
|---|---|
| `PMID:20056700` | Potential producer/regulation lead for *Erwinia carotovora* subsp. *carotovora* ATTn10; inspect full text before curating rpsL effects on carbapenem production. |
| `PMID:21435033` | Potential producer/regulation lead for *Serratia* sp. ATCC 39006 and *Erwinia carotovora* subsp. *carotovora*; inspect full text before curating CarR39006 quorum-sensing control. |
| `PMID:21913298` | Potential biosynthetic-pathway lead; its abstract links simple `(5R)-carbapen-2-em-3-carboxylic acid` biosynthesis in *Pectobacterium carotovorum* to `CarA`, `CarB`, and `CarC`. |
| `PMID:23611403` | Potential exact biosynthetic-enzyme lead for CarC / carbapenem synthase; its abstract states that CarC terminally produces active carbapenem-3-carboxylate from stereoisomeric substrates. |

## Completeness

Complete enough for read-only review:

- Generated identity, exact ChEBI grounding, structure, parent compounds, KEGG,
  CAS, MetaCyc, and Reaxys xrefs, ChEBI activity roles, source concept, and
  `ANTIBACTERIAL` filing class agree with the inspected public databases and
  committed source row.
- The record has only seed and reseed curation-history events from
  `2026-08-30`, accurately matching the generated `SEEDED` state.
- `clinical_status` and `clinical_status_assertions` are absent; no inspected
  source represented exact `1-carbapenem-3-carboxylic acid` as an approved
  clinical substance or product.
- `datasets` is absent; *P. carotovorum* ATCC 39048 genome accession
  information is likely available through `PMID:30533884`, but this review did
  not inspect the full text or sequence archive records far enough to curate an
  exact dataset accession.

Consequential gaps:

- `activity_spectrum` is absent even though ChEBI asserts an antibacterial role
  and exact producer literature repeatedly identifies
  `1-carbapen-2-em-3-carboxylic acid` as a beta-lactam antibiotic. Full text
  is needed before curating quantitative antibacterial activity.
- `producer_organisms` is absent despite exact public abstracts that connect
  `1-carbapen-2-em-3-carboxylic acid` to *Erwinia carotovora* /
  *Pectobacterium carotovorum*, strain ATCC 39048 or GS101, and *Serratia* sp.
  ATCC 39006.
- `molecular_targets` is absent; this review found no inspected source that
  identifies the direct bacterial molecular target of
  `1-carbapen-2-em-3-carboxylic acid`.
- `mode_of_action` and `mode_of_action_target_scope` are absent because this
  generated ChEBI record has not been curator-checked against exact primary
  mechanism literature.
- `resistance_mechanisms` is absent even though exact literature identifies
  CarF and CarG as mediators of producer intrinsic resistance by an unknown
  mechanism.
- `structural_observations` is absent. `PMID:24583229` is a CarG structural
  lead, but it does not identify the antibacterial target and this review did
  not inspect a PDB accession.
- `causal_graphs` is absent; the record has not yet connected carbapenem
  synthesis, exact activity, any bacterial target process, or CarF/CarG
  self-resistance with claim-level evidence on every edge.

Ignored-inclusive absence search:

- Ran `rg --no-ignore --hidden` over `data/antibiotics`, `data/raw`,
  `curation`, `reports/yaml_record_review`, `.claude`, `docs`, `README.md`,
  `conf`, `src`, `scripts`, `tests`, `justfile`, and `pyproject.toml` for exact
  `CHEBI:615`, `1-carbapenem-3-carboxylic acid`,
  `1-carbapenem-3-carboxylic-acid`, `BSIMZHVOQZIAOY-SCSAIBSYSA-N`,
  `antibioticmech:chebi-79a511e8dd`, `cas:82768-37-4`,
  `kegg.compound:C06669`, `metacyc.compound:CPD-9377`, and `reaxys:8832318`.
- The search included ignored files. It found the generated target, the ChEBI
  raw row, `data/antibiotics/PATHS.tsv`, and the derived review-queue row. It
  found no prior `CHEBI:615` review report, no `curation/decisions.tsv` row,
  and no curated activity, target, resistance, producer, or mechanism addition
  for this exact ChEBI concept.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The record is still a bare ChEBI seed and cannot satisfy the `REVIEWED` gate until a curator adds claim-level producer, activity, biosynthesis, and intrinsic-resistance evidence plus a curator-checked mechanism decision for exact `1-carbapenem-3-carboxylic acid`. | The target YAML has no record-level `evidence`, no `mode_of_action`, no `molecular_targets`, no `activity_spectrum`, no `producer_organisms`, no `resistance_mechanisms`, and no `causal_graphs`; the regenerated worklist places `CHEBI:615` only in `mechanism` and `review-readiness` with 0 source literature leads, 0 record evidence items, and 0 targets. Exact PubMed searches exposed producer, biosynthetic, and CarF/CarG self-resistance leads that have not yet been curated. | Future curator-owned fields on `data/antibiotics/antibacterial/1-carbapenem-3-carboxylic-acid.yaml`, written with `record_curation_event` and `write_validated_antibiotic`. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Keep the generated `CHEBI:615` identity, label, exact structure, parent
   compounds, KEGG/CAS/MetaCyc/Reaxys xrefs, ChEBI activity roles, filing
   class, and source concept unchanged.
2. Inspect `PMID:1335238`, `PMID:7711893`, `PMID:8939426`, and `PMID:30533884`
   far enough to curate exact producer-organism observations with organism
   identifiers, strain labels or genome identifiers where available, the
   supported production claim, and narrow evidence snippets.
3. Inspect `PMID:9402024`, `PMID:16549672`, `PMID:21913298`, and
   `PMID:23611403` before adding `carA`, `carB`, `carC`, or
   `carABCDEFGH` biosynthetic claims; distinguish enzymatic biosynthesis from
   the direct antibacterial mechanism.
4. Inspect `PMID:24583229` and `PMID:9402024` before adding
   `resistance_mechanisms` for CarF/CarG producer self-resistance. Preserve the
   fact that the direct CarF/CarG mechanism is unknown unless inspected full
   text resolves it.
5. Inspect full text of the producer and biosynthesis leads before adding
   `activity_spectrum` rows. Preserve original antibacterial measurements and
   units, such as MIC or diffusion-zone observations, rather than converting to
   MIC unless the source reports or justifies a direct conversion.
6. Promote `curation_status` to `REVIEWED` only after the identity, structure,
   filing-class, and curator-checked mechanism gates in `docs/CURATION.md` all
   pass.

## Follow-up Checks

After any future curation:

1. `just validate data/antibiotics/antibacterial/1-carbapenem-3-carboxylic-acid.yaml`
2. `just validate-strict data/antibiotics/antibacterial/1-carbapenem-3-carboxylic-acid.yaml --out /tmp/antibioticmech-chebi-615-strict.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-615-worklist.tsv`
5. `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv`

Also re-run exact PubMed and Semantic Scholar searches for
`1-Carbapen-2-em-3-carboxylic acid`, `carbapenem-3-carboxylic acid`, `SQ
27860`, `carABCDEFGH`, and `CarF CarG` so future curation can include any
newer exact producer, activity, or resistance literature that this review's
bounded searches missed.

## Additional Notes

- The PubMed searches surfaced carbapenem-analog synthesis, prodrug, and
  structure-activity papers that matched by tokenization rather than exact
  `CHEBI:615` identity; ignore those for producer and resistance curation unless
  future full-text inspection proves that they used the exact ChEBI compound.
- PubChem CID `194860` is a same-formula stereochemical near miss for the
  ChEBI/OLS structure in this record, not an independent validation of the
  exact record InChIKey.
- ChEBI/OLS also carries the exact synonym
  `2,3-didehydro-1-carbapenam-3-carboxylic acid` as a related synonym. The
  generated record has one exact copy of the text, which is sufficient for a
  seeded synonym list.
