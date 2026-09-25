# YAML Record Review: 1-dodecylguanidine acetate

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antibacterial/1-dodecylguanidine-acetate.yaml`
- Started UTC: 2026-09-25T11:00:00Z
- Finished UTC: 2026-09-25T11:06:08Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:74889` |
| Label | `1-dodecylguanidine acetate` |
| Path | `data/antibiotics/antibacterial/1-dodecylguanidine-acetate.yaml` |
| Class | `ANTIBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concept | `CHEBI:74889` / `1-dodecylguanidine acetate` from ChEBI release `2026-08-30` |
| Minted source key | `antibioticmech:chebi-ebebb7bbfb` |
| Structure key | `YIKWKLYQRFRGPM-UHFFFAOYSA-N` |
| Generated or maintained | Generated from `data/raw/chebi_antimicrobials.tsv` plus `data/antibiotics/PATHS.tsv`; future seed-owned identity, synonym, xref, source-PMID, role, parent, or structure changes belong upstream rather than as hand edits. |

Resolution:

- `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv`
  regenerated the full queue and kept `CHEBI:74889` as the first unreviewed row
  after the 170 existing reviewed identifiers: `MECHANISM_REVIEW: mechanism is
  absent; 10 source literature lead(s), 0 record evidence item(s), 0 target(s)`.
- `data/antibiotics/PATHS.tsv` maps `CHEBI:74889` to `ANTIBACTERIAL` with slug
  `1-dodecylguanidine-acetate`, matching the current record path.
- `data/raw/chebi_antimicrobials.tsv` carries the ChEBI row that seeds this
  exact acetate salt record.
- The full target YAML was read before judging ChEBI identity, acetate-salt
  structure, xrefs, source concepts, empty mechanism slots, empty activity,
  target, resistance and causal-graph lists, and curation history.
- A gitignore-independent search with `rg --no-ignore --hidden` over
  `data/antibiotics`, `data/raw`, `curation`, `reports/yaml_record_review`,
  local skills, docs, source, tests, `justfile`, `pyproject.toml`, and
  configuration files found no prior review report for `CHEBI:74889`, no
  `curation/decisions.tsv` row for `antibioticmech:chebi-ebebb7bbfb`, and no
  curated activity, target, resistance, producer, or causal mechanism assertions
  for this exact InChIKey. Expected matches were the target record and its
  ChEBI raw row, the adjacent `CHEBI:74880` free-base row, and near-miss notes
  in the just-merged `1-dodecylguanidine` review.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antibacterial/1-dodecylguanidine-acetate.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/antibacterial/1-dodecylguanidine-acetate.yaml --out /tmp/antibioticmech-chebi-74889-strict.tsv` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed after emitting the known unrelated `iclaprim` / `CHEBI:31724` CARD diagnostic: 2939 expected records, 2939 on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, and 0 stale lockfile rows. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-74889-worklist.tsv` | Passed; exact `CHEBI:74889` rows appear only in `mechanism` and `review-readiness`. |
| `uv run runoak -i ols:chebi labels CHEBI:74889 CHEBI:33282 CHEBI:35718 CHEBI:86328 CHEBI:59230 CHEBI:86417` | Passed: OLS resolved the compound, `antibacterial agent`, `antifungal agent`, `antifungal agrochemical`, `acetate salt`, and `aliphatic nitrogen antifungal agent`. |
| OLS4 term lookup for `CHEBI:74889` | Passed: live OLS4 resolved a current, non-obsolete, ChEBI-defining, `3_STAR` term whose formula, charge, masses, SMILES, Standard InChI, Standard InChIKey, synonyms, PubMed xrefs, registry xrefs, and patent xrefs match the generated ChEBI seed row. |
| PubChem CID lookup for `YIKWKLYQRFRGPM-UHFFFAOYSA-N` | Passed: PubChem maps the target Standard InChIKey to multiple component-normalized CIDs and maps the name `dodine` specifically to CID `17110`. |
| PubChem CID `17110` identity checks | Passed: CID `17110` is `Dodine`, reports the same Standard InChI and Standard InChIKey, and lists `CHEBI:74889`, `2439-10-3`, `C18723`, `1-Dodecylguanidine acetate`, `Dodecylguanidine monoacetate`, `dodine`, and ChEBI acetate-salt synonyms. |
| KEGG `C18723` lookup | Passed: KEGG resolves `C18723` to `Dodine; Dodecylguanidine acetate`, formula `C13H29N3. C2H4O2`, exact mass `287.2573`, molecular weight `287.44`, CAS `2439-10-3`, and ChEBI `74889`. |
| PPDB report `263` lookup | Passed: the University of Hertfordshire PPDB report resolves to `Dodine`, CAS `2439-10-3`, formula `C15H33N3O2`, Standard InChIKey `YIKWKLYQRFRGPM-UHFFFAOYSA-N`, and the same Standard InChI as the record. |
| Common Chemistry lookup for `2439-10-3` | Not independently verified: the public API endpoint returned `Unauthorized`; OLS4, PubChem, KEGG, and PPDB still corroborate the CAS xref carried by official ChEBI. |
| PubMed summary lookup for the ten ChEBI source PMIDs and two adjacent dodine mechanism leads | Passed: all requested PMIDs resolved; exact source papers include toxicity, residue-method, critical-micelle, tart-cherry sensitivity, bacterial combination-activity, and *Pseudomonas syringae* membrane-damage studies about dodine / dodecylguanidine acetate. |
| PubMed efetch for `PMID:1381663`, `PMID:8229668`, `PMID:1902648`, `PMID:200325`, `PMID:23175430`, `PMID:7356304`, and `PMID:7464578` | Passed: abstracts and citation records confirm exact dodecylguanidine acetate / monoacetate / dodine papers covering bacterial membrane damage, bacterial combination activity, fungal membrane damage, and cherry leaf spot MIC data. |
| Exact PubMed/Semantic Scholar query for `"1-dodecylguanidine acetate" OR "dodecylguanidine acetate" OR "dodecylguanidine monoacetate" OR "dodine acetate" OR dodine OR "2439-10-3"` | PubMed returned 30 candidates; Semantic Scholar returned HTTP 429. PubMed candidates included exact residue, toxicology, detection, DNA-interaction, antifungal, fungicide-resistance, and dodine-ion derivative papers. |
| Exact PubMed title/abstract query for `"dodecylguanidine monoacetate" OR "dodecylguanidine acetate" OR dodine` | Passed: PubMed returned 85 title/abstract hits; the first 50 were sufficient to find exact recent antifungal mechanism, DNA-damage, detection, and fungicide-resistance leads. |

No narrower single-record reference or curation-history validator is exposed for
this ChEBI-only seed. The focused strict validator covered closed schema shape,
and `verify-corpus --summary` covered generated drift from the maintained raw
and path-lock inputs.

## Identity and Grounding

The generated identity is consistent with official ChEBI/OLS, PubChem, KEGG,
and PPDB for exact acetate salt `CHEBI:74889`:

| Assertion | Record value | Check |
|---|---|---|
| ChEBI identity | `CHEBI:74889`, `1-dodecylguanidine acetate` | OLS4 resolved the term to a current, ChEBI-defining class in the `3_STAR` subset. |
| Definition | Acetate salt from equimolar 1-dodecylguanidine and acetic acid; used as a fungicide for black spot and foliar diseases on fruit | Matched OLS4, the committed ChEBI row, and the University of Hertfordshire PPDB description. |
| Formula and charge | `C13H29N3.C2H4O2`, charge `0` | Matched OLS4. KEGG and PPDB use the equivalent collapsed formula `C15H33N3O2`. |
| Masses | average `287.448`, monoisotopic `287.25728` | Matched OLS4. KEGG reports exact mass `287.2573` and molecular weight `287.44`, agreeing after rounding. |
| SMILES | `CC(=O)O.CCCCCCCCCCCCNC(=N)N` | Matched the committed ChEBI row and official ChEBI/OLS structure annotation. PPDB's canonical SMILES is the same dot-disconnected acetate/free-base representation with the guanidine tautomer drawn differently. |
| Standard InChI | `InChI=1S/C13H29N3.C2H4O2/c1-2-3-4-5-6-7-8-9-10-11-12-16-13(14)15;1-2(3)4/h2-12H2,1H3,(H4,14,15,16);1H3,(H,3,4)` | Matched OLS4, PubChem CID `17110`, and PPDB report `263`. |
| InChIKey | `YIKWKLYQRFRGPM-UHFFFAOYSA-N` | Matched OLS4, PubChem CID `17110`, and PPDB report `263`. |
| Parent compounds | `CHEBI:59230`, `CHEBI:86417` | OAK resolved these to `acetate salt` and `aliphatic nitrogen antifungal agent`, agreeing with the ChEBI definition and salt boundary. |
| Activity roles | `CHEBI:33282`, `CHEBI:35718`, `CHEBI:86328` | OAK resolved these to `antibacterial agent`, `antifungal agent`, and `antifungal agrochemical`; the generated row preserves ChEBI's activity roles. |
| Filing class | `ANTIBACTERIAL` | The ChEBI `antibacterial agent` role maps this generated record to `data/antibiotics/antibacterial/` by repository filing priority while retaining the antifungal roles. |

Checked exact xrefs:

| Xref | Result |
|---|---|
| `cas:2439-10-3` | Present in OLS4, KEGG `C18723`, PPDB report `263`, and PubChem CID `17110` synonyms. CAS Common Chemistry did not independently resolve it through its public API. |
| `kegg.compound:C18723` | KEGG resolves this entry to Dodine / dodecylguanidine acetate with the same ChEBI and CAS references and matching mass data. |
| `pesticides:dodine` | Preserved from official ChEBI/OLS as an exact database xref. |
| `ppdb:263` | The PPDB report resolves to Dodine and agrees on the target CAS, formula, Standard InChI, and InChIKey. |
| `reaxys:6546960` | Preserved from official ChEBI/OLS as an exact database xref; no public Reaxys check is available. |

The two patent identifiers are correctly kept as `document_xrefs`, not exact
chemical `xrefs`, because the schema reserves `xrefs` for identifiers for the
same structure. OLS4 still carries `patent:US2867562` and `patent:US2921881`
as database cross-references inherited by the seed row.

The adjacent free-base term `CHEBI:74880` is correctly separate: it has a
different formula, different Standard InChI, different Standard InChIKey
`HILAYQUKKYWPJW-UHFFFAOYSA-N`, different CAS `112-65-2`, and a separate
record reviewed in `reports/yaml_record_review/20260925T103708Z-1-dodecylguanidine.md`.

## Evidence

The generated identity, label, definition, synonyms, parent compounds, xrefs,
filing class, activity roles, exact structure, source concept, and ChEBI source
PMIDs reproduce from the committed `data/raw/chebi_antimicrobials.tsv` row with
no `verify-corpus` drift.

The record has no object-level evidence claims yet:

| Claim family | Current state | Review |
|---|---|---|
| Record-level evidence | Absent | Acceptable for a ChEBI seed; the source concept and source row carry ChEBI provenance. |
| Mode of action | Absent | Incomplete. Exact dodine acetate literature supports at least membrane disruption in *Pseudomonas syringae* and points to species-dependent fungal mechanisms. |
| Molecular targets | Absent | Acceptable until a mechanism is curated; the membrane-disruption papers do not by themselves ground a discrete protein target. |
| Activity observations | Absent | Incomplete but not structurally invalid; the tart-cherry paper reports *Blumeriella jaapii* dodine MICs in microgram AI per mL ranges that would need isolate-level full-text extraction before being represented. |
| Resistance mechanisms | Absent | No CARD source concept or resistance import exists. Recent *Venturia inaequalis* and *Blumeriella jaapii* reduced-sensitivity reports are literature leads, not curated routes. |
| Causal graphs | Absent | Incomplete because exact membrane-damage and respiration papers are plausible graph sources; every future edge needs its own primary evidence. |

Inspected exact dodine / acetate evidence leads:

| Source | Relevance |
|---|---|
| `PMID:1381663` | Exact source PMID for dodine / dodecylguanidine monoacetate in *P. syringae*. The abstract supports RNA release, lysis, outer-membrane expansion, micelle uptake, and a conclusion that antibacterial activity mainly results from surfactant micelles. |
| `PMID:8229668` | Exact source PMID for dodine / dodecylguanidine monoacetate in *P. syringae*. The abstract supports K+ release, inorganic-phosphate leakage, altered oxygen consumption, and the interpretation that the micellar form is more damaging to the cytoplasmic membrane than free molecules. |
| `PMID:1902648` | Exact non-ChEBI lead for dodine / dodecylguanidine monoacetate in *P. syringae* ATCC 12271. The abstract supports cytoplasmic-membrane damage and cell death after low-concentration dodine treatment. |
| `PMID:200325` | Exact non-ChEBI lead for dodecylguanidine acetate in *Fusarium sulphureum*. The abstract supports dose-dependent macroconidial plasma-membrane effects including water uptake at low concentration and irreversible loss of divalent-cation impermeability and L-phenylalanine transport at higher concentration. |
| `PMID:32474016` | Exact recent antifungal mechanism lead for dodine in *Ustilago maydis* and *Zymoseptoria tritici*. The abstract reports that dodine primarily inhibits mitochondrial ATP synthesis in both fungi but that plasma-membrane disruption and endocytosis arrest were observed only in *U. maydis*. |
| `PMID:23175430` | Exact ChEBI source PMID with field efficacy and *B. jaapii* in vitro MIC ranges for dodine. The abstract supports activity/sensitivity data but not the membrane mechanism. |
| `PMID:7356304` | Exact ChEBI source PMID for dodecylguanidine acetate combinations with penicillin, streptomycin, levomycetin, and chlortetracycline in *S. aureus* and Gram-negative organisms. The abstract supports sub-bacteriostatic surfactant effects on antibiotic penetration, not an exact dodine MIC. |
| `PMID:7464578` | Exact ChEBI source PMID about antimicrobial properties of dodecylguanidine acetate; no abstract was available in PubMed, so only bibliographic identity was verified. |
| `PMID:17617418` | Exact source PMID about the critical micelle concentration of dodine; it is a colloid-chemistry comment, not a direct antimicrobial mechanism paper. |
| `PMID:21391507`, `PMID:4077947` | Exact source PMIDs about dodine residue analytical methods in fruit, not antimicrobial activity or mechanism. |
| `PMID:13761521`, `PMID:9397185` | Exact source PMIDs about mammalian toxicity of dodine, not antimicrobial activity or mechanism. |
| `PMID:34505331` | Near miss for exact `CHEBI:74889`: it synthesized bifunctional ionic liquids based on the dodine cation and compared their properties with commercial N-dodecylguanidine acetate. The derivative assays should not be lifted onto this exact acetate-salt record. |

## Completeness

The record is a structurally consistent, exact ChEBI seed, but it is not
complete enough for `REVIEWED`.

Exact primary-literature leads exist for this acetate salt; a curator can add a
defensible membrane-related antibacterial `mode_of_action` and likely a
pathogen-specific antifungal causal graph after reading full text and deciding
how to represent:

- direct membrane damage in *P. syringae*;
- concentration-dependent dodine micelle effects;
- mitochondrial ATP-synthesis inhibition versus plasma-membrane disruption in
  fungi;
- activity observations for *B. jaapii* and bacterial potentiation assays; and
- reduced-sensitivity or resistance observations that are phenotypic rather
  than a biochemical resistance mechanism.

Because dodine acts as a surfactant and the fungal data appear species
dependent, a single generic mechanism sentence would overstate the evidence.
Any curation should preserve the organism and concentration context, and should
leave `molecular_targets` empty unless a paper identifies a specific molecular
target instead of a membrane or respiratory process.

Empty optional slots left without unsupported filler:

| Field family | Rationale |
|---|---|
| `producer_organisms` | Dodine is a synthetic agrochemical salt; the inspected exact sources did not indicate microbial biosynthesis. |
| `clinical_status` | Dodine is an agrochemical fungicide; no FDA/clinical regulatory source concept is present. |
| `datasets` | No public exact dataset accession surfaced in the bounded searches. |
| `discussions` | The current seed has no contradictory assertion that requires a source-owned `Discussion`; the missing mechanism is represented by the review queue. |

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| F1 | Major | The exact dodine acetate record is still a bare ChEBI seed even though exact dodecylguanidine acetate / monoacetate literature supports membrane damage in *P. syringae*, membrane effects in *F. sulphureum*, species-dependent antifungal respiration and membrane effects in *U. maydis* and *Z. tritici*, and activity/sensitivity observations. Without a curated `mode_of_action`, claim-level evidence, and a causal graph or bounded veto, the record cannot satisfy the repository `REVIEWED` gate. | Curator-owned fields on `data/antibiotics/antibacterial/1-dodecylguanidine-acetate.yaml`, written through a guarded mutator using `record_curation_event` and `write_validated_antibiotic`. |

No blocker findings.

No minor findings.

## Recommended Edits

1. In `data/antibiotics/antibacterial/1-dodecylguanidine-acetate.yaml`, curate a
   dodine mechanism only after inspecting full text for at least `PMID:1902648`,
   `PMID:1381663`, `PMID:8229668`, `PMID:200325`, and `PMID:32474016`.
   Possible representations to test against the schema are `MEMBRANE_DISRUPTION`
   for the *P. syringae* evidence and either a pathogen-scoped
   `ENERGY_METABOLISM_INHIBITION` or `MULTIPLE` graph for antifungal evidence;
   the full text should decide whether a single record-level mode is honest.
2. Add claim-level `EvidenceItem` entries only on the specific future
   `ActivityObservation`, `MolecularTarget`, or `CausalEdge` objects they
   support. The ChEBI source PMID list and the PubMed search results should
   remain discovery leads, not broad record-level citations.
3. If full text exposes exact isolate rows and methods, add *B. jaapii* dodine
   MIC observations from `PMID:23175430` with `mic_units`, `assay`, source
   strain or isolate context, and evidence.
4. Preserve the acetate-salt boundary with `CHEBI:74880`: do not move free-base
   potassium-channel papers or dodine-ion derivative assays onto this record
   unless the source itself tested the exact acetate salt.

## Follow-up Checks

- `just validate-strict data/antibiotics/antibacterial/1-dodecylguanidine-acetate.yaml --out /tmp/antibioticmech-chebi-74889-strict.tsv`
- `just verify-corpus --summary`
- `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-74889-worklist.tsv`
- `just qc`
- Manually confirm that any future `mode_of_action_notes` begins with
  `CURATOR:` and that a curation-history event accurately names exactly which
  mechanistic, activity, or graph claims were added.
- Manually confirm that every future causal edge has a primary citation and
  that no *P. syringae*, *F. sulphureum*, *U. maydis*, or *Z. tritici* claim is
  generalized beyond the organism and concentration context tested by its
  source.

## Additional Notes

- `just worklist` reported only two exact rows for `CHEBI:74889`: one
  `mechanism` row with 0 CARD targets and 0 resistance edges, and the
  `review-readiness` row with 10 source literature leads, 0 record evidence
  items, and 0 targets.
- PubChem's Standard InChIKey search returned CID `17110` plus three additional
  CIDs sharing the same Standard InChIKey; the name lookup for `dodine`
  resolved specifically to CID `17110`, and that CID was sufficient for the
  exact synonym, ChEBI, KEGG, CAS, Standard InChI, and InChIKey checks.
- Semantic Scholar rate-limited the exact synonym query with HTTP 429. PubMed
  resolved exact title/abstract and source-PMID queries without NCBI contact
  metadata; `NCBI_EMAIL` was unset in the shell environment.
- Full `just qc` was left for the PR-level gate because this read-only review
  intentionally changed no YAML record.
