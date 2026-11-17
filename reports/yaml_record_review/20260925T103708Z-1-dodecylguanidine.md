# YAML Record Review: 1-dodecylguanidine

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antibacterial/1-dodecylguanidine.yaml`
- Started UTC: 2026-09-25T10:32:00Z
- Finished UTC: 2026-09-25T10:37:08Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:74880` |
| Label | `1-dodecylguanidine` |
| Path | `data/antibiotics/antibacterial/1-dodecylguanidine.yaml` |
| Class | `ANTIBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concept | `CHEBI:74880` / `1-dodecylguanidine` from ChEBI release `2026-08-30` |
| Minted source key | `antibioticmech:chebi-4e645a4f2a` |
| Structure key | `HILAYQUKKYWPJW-UHFFFAOYSA-N` |
| Generated or maintained | Generated from `data/raw/chebi_antimicrobials.tsv` plus `data/antibiotics/PATHS.tsv`; future seeded identity, role, structure, synonym, xref, or source-PMID changes belong upstream rather than as hand edits. |

Resolution:

- `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv`
  regenerated the full queue and kept `CHEBI:74880` as the next unreviewed row:
  `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record
  evidence item(s), 0 target(s)`.
- `data/antibiotics/PATHS.tsv` maps `CHEBI:74880` to `ANTIBACTERIAL` with slug
  `1-dodecylguanidine`, matching the current record path.
- `data/raw/chebi_antimicrobials.tsv` is the ChEBI source row that seeds the
  generated target record.
- The whole target YAML was read before judging generated identity, ChEBI
  provenance, structure, xrefs, source concepts, empty mechanism and evidence
  slots, and curation history.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antibacterial/1-dodecylguanidine.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/antibacterial/1-dodecylguanidine.yaml --out /tmp/antibioticmech-chebi-74880-strict.tsv` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed after emitting the known unrelated `iclaprim` / `CHEBI:31724` CARD diagnostic: 2939 expected records, 2939 on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, and 0 stale lockfile rows. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-74880-worklist.tsv` | Passed; exact `CHEBI:74880` rows appear only in `mechanism` and `review-readiness`. |
| `uv run runoak -i ols:chebi labels CHEBI:74880 CHEBI:33282 CHEBI:35718 CHEBI:86328 CHEBI:24436 CHEBI:86417` | Passed: OLS resolved the compound, `antibacterial agent`, `antifungal agent`, `antifungal agrochemical`, `guanidines`, and `aliphatic nitrogen antifungal agent`. |
| OLS4 term lookup for `CHEBI:74880` | Passed: live OLS4 resolved a current, ChEBI-defining, `3_STAR` term with formula, charge, masses, SMILES, Standard InChI, Standard InChIKey, synonyms, xrefs, and the same source PubMed xref preserved in the committed ChEBI source row. |
| PubChem CID `8204` property lookup | Passed: PubChem reports formula `C13H29N3`, formal charge `0`, exact mass `227.236147938`, Standard InChI, and Standard InChIKey `HILAYQUKKYWPJW-UHFFFAOYSA-N` for the same exact free-base compound. |
| PubChem CID `8204` synonym lookup | Passed: PubChem includes `CHEBI:74880`, `112-65-2`, `1-dodecylguanidine`, `n-dodecylguanidine`, `laurylguanidine`, and `C12-G` among its synonyms or cross-references. |
| Common Chemistry lookup for `112-65-2` | Not independently verified: the public API endpoint returned `Unauthorized`; official ChEBI/OLS and PubChem still preserve the CAS xref. |
| Exact PubMed/Semantic Scholar query for `"1-dodecylguanidine" OR "1-laurylguanidine" OR dodecylguanidine OR laurylguanidine OR "C12-G" OR "112-65-2"` | PubMed returned 40 candidates; Semantic Scholar returned HTTP 429. The exact free-base leads were structure, surfactant, host potassium-channel, and toxicity papers rather than antimicrobial activity or microbial mechanism papers. |
| Exact PubMed title/abstract query for `"dodecylguanidine" OR "laurylguanidine" OR "1-dodecylguanidine" OR "C12-G" OR "N-dodecylguanidine"` | PubMed returned 30 candidates. Most antimicrobial candidates were about acetate, monoacetate, hydrochloride, or synthetic MC12 analog salts rather than exact neutral `CHEBI:74880`. |
| PubMed efetch for committed source `PMID:7623770` | Passed: the exact source PMID resolved and concerns `n-Dodecylguanidine (C12-G)` effects on host A-type potassium channels. |

No narrower single-record reference or curation-history validator is exposed for
this ChEBI-seeded record. The focused strict validator covered closed schema
shape, and `verify-corpus --summary` covered generated drift from the
maintained raw and path-lock inputs.

## Identity and Grounding

The generated identity is consistent with official ChEBI/OLS and PubChem for
exact free-base `CHEBI:74880`:

| Assertion | Record value | Check |
|---|---|---|
| ChEBI identity | `CHEBI:74880`, `1-dodecylguanidine` | OLS4 resolved the term to a current ChEBI-defining class in the `3_STAR` subset. |
| Definition | Guanidine with one amino group substituted by a dodecyl group; used generally as the acetate salt, dodine, as an agrochemical fungicide | Matched OLS4 and the committed ChEBI row. The wording correctly signals the nearby salt boundary with `CHEBI:74889` / `1-dodecylguanidine acetate`. |
| Synonyms | `1-laurylguanidine`; `C12-G`; `dodecylguanidine`; `laurylguanidine`; `n-dodecylguanidine` | Matched official ChEBI/OLS synonym content after collapsing OLS' duplicate exact/related `1-dodecylguanidine` IUPAC annotation. |
| Formula and charge | `C13H29N3`, charge `0` | Matched OLS4 and PubChem CID `8204`. |
| Masses | average `227.396`, monoisotopic `227.23615` | Matched OLS4; PubChem's exact mass also matches the generated monoisotopic mass to the reported precision. |
| SMILES | `CCCCCCCCCCCCNC(=N)N` | Matched the committed ChEBI row and official ChEBI/OLS structure annotation. |
| Standard InChI | `InChI=1S/C13H29N3/c1-2-3-4-5-6-7-8-9-10-11-12-16-13(14)15/h2-12H2,1H3,(H4,14,15,16)` | Matched OLS4 and PubChem CID `8204`. |
| InChIKey | `HILAYQUKKYWPJW-UHFFFAOYSA-N` | Matched OLS4 and PubChem CID `8204`. |
| Parent compounds | `CHEBI:24436`, `CHEBI:86417` | OAK resolved these to `guanidines` and `aliphatic nitrogen antifungal agent`, agreeing with the compound definition and ChEBI structural/role classification. |
| Activity roles | `CHEBI:33282`, `CHEBI:35718`, `CHEBI:86328` | OAK resolved these to `antibacterial agent`, `antifungal agent`, and `antifungal agrochemical`; the generated row preserves the committed ChEBI roles. |
| Filing class | `ANTIBACTERIAL` | The ChEBI `antibacterial agent` role maps this generated record to `data/antibiotics/antibacterial/` by repository filing priority while retaining the antifungal roles. |

Checked exact xrefs:

| Xref | Check |
|---|---|
| `cas:112-65-2` | Present on the committed ChEBI row, the official ChEBI/OLS term, and PubChem CID `8204`; not independently checked in Common Chemistry because its public API endpoint returned `Unauthorized`. |
| `reaxys:637515` | Present on official ChEBI and preserved in the generated ChEBI row; not independently checked because Reaxys is not publicly resolvable. |

## Evidence

The target has no record-level `evidence`, no `mode_of_action`, no
`molecular_targets`, no `activity_spectrum`, no `resistance_mechanisms`, no
`producer_organisms`, and no `causal_graphs`. That is allowed for a freshly
ChEBI-seeded record because the ChEBI source concept supplies database
provenance for identity and role terms, and there are no claim-local activity,
target, resistance, producer, dataset, clinical, or causal assertions that would
require object-level evidence.

Committed source literature:

| PMID | Public title/abstract support |
|---|---|
| `PMID:7623770` | Exact free-base lead, not an antimicrobial lead. The 1995 abstract reports that `n-Dodecylguanidine (C12-G)` shifts A-type K+ channel gating in host systems: an rKv1.4 clone expressed in *Xenopus* oocytes and native A-type potassium channels in canine ventricular myocytes. It supports exact-compound channel pharmacology and an extracellular surface-potential model, not antibacterial activity, antifungal activity, a microbial molecular target, or microbial resistance. |

Additional exact and near-exact publication leads from bounded PubMed searches:

| PMID | Assessment |
|---|---|
| `PMID:31457300` | Exact free-base structure and spectroscopy lead. The abstract reports synthesis of crystalline dodecylguanidine free base for nonpolar-environment spectroscopy; it is useful chemical-identity context but not antimicrobial activity evidence. |
| `PMID:16853157` | Exact free-base spectroscopy lead. The abstract says natural-abundance 15N NMR spectroscopy on dodecylguanidine modeled arginine-side-chain protonation in proteins; it is not an antimicrobial activity or mechanism lead. |
| `PMID:1902648` | Salt mechanism/activity near miss for `CHEBI:74889`. The abstract reports cytoplasmic membrane damage and cell death in *Pseudomonas syringae* ATCC 12271 after treatment with fungicide dodecylguanidine monoacetate, dodine. |
| `PMID:1381663` | Salt antibacterial-mechanism near miss for `CHEBI:74889`. The abstract reports dodine / dodecylguanidine monoacetate treatment of *P. syringae*, RNA degradation, cell lysis, outer-membrane expansion, and a conclusion that antibacterial activity is mainly the result of the surfactant micellar form. |
| `PMID:8229668` | Salt membrane-damage near miss for `CHEBI:74889`. The abstract reports severe cytoplasmic-membrane damage in *P. syringae* above the critical micelle concentration of dodecylguanidine monoacetate, dodine. |
| `PMID:200325` | Salt fungicide near miss for `CHEBI:74889`. The abstract reports membrane effects of dodecylguanidine acetate, dodine, in *Fusarium sulphureum* macroconidia. |
| `PMID:17390586` | Synthetic-analog near miss. The abstract reports synergy between amphotericin B and N-methyl-N-dodecylguanidine, MC12, a synthetic niphimycin alkylguanidinium-chain analog; MC12 is not exact neutral `1-dodecylguanidine`. |
| `PMID:34505331` | Dodine-ion derivative near miss. The abstract reports bifunctional ionic liquids based on a dodine / N-dodecylguanidine cation and modified relative to commercial N-dodecylguanidine acetate; full text would be needed before connecting any derivative assay back to `CHEBI:74880`. |

## Completeness

Complete enough for read-only review:

- Generated identity, exact ChEBI grounding, free-base structure, parent
  compounds, CAS/Reaxys xrefs, ChEBI activity roles, source concept, and
  `ANTIBACTERIAL` filing class agree with the inspected public databases and
  committed source row.
- The free-base record is correctly distinct from `CHEBI:74889`,
  `1-dodecylguanidine acetate`, which carries a different formula, different
  Standard InChIKey, its own pesticide xrefs, and a much larger set of
  dodecylguanidine acetate or dodine source PMIDs in
  `data/raw/chebi_antimicrobials.tsv`.
- The record has only seed and reseed curation-history events from
  `2026-08-30`, accurately matching the generated `SEEDED` state.
- `producer_organisms` is absent; the inspected ChEBI, PubChem, and bounded
  PubMed evidence treats 1-dodecylguanidine and dodine as synthetic compounds or
  agricultural fungicides, not natural products with microbial producers.
- `clinical_status` and `clinical_status_assertions` are absent; no inspected
  source represented exact free-base `1-dodecylguanidine` as an approved
  clinical substance or product.
- `datasets` is absent; the inspected evidence did not expose a public exact
  screening, omics, or structural dataset accession for free-base
  `1-dodecylguanidine`.

Consequential gaps:

- `activity_spectrum` is absent even though ChEBI asserts antibacterial,
  antifungal, and antifungal-agrochemical roles. The bounded exact searches
  mostly found quantitative antimicrobial papers for dodecylguanidine acetate
  / monoacetate / dodine, so a curator must inspect full text and original
  chemical forms before deciding whether any result supports `CHEBI:74880`
  rather than `CHEBI:74889`.
- `molecular_targets` is absent; this review found no inspected source that
  identifies a direct bacterial or fungal molecular target for exact free-base
  `1-dodecylguanidine`.
- `mode_of_action` and `mode_of_action_target_scope` are absent because this
  generated ChEBI record has not been curator-checked against exact primary
  mechanism literature.
- `resistance_mechanisms` is absent; CARD and PHI-base do not currently seed any
  resistance edge for exact `CHEBI:74880`.
- `causal_graphs` is absent; the record has not yet connected any exact
  antimicrobial activity, surfactant-membrane effect, target process, or cell
  death outcome with claim-level evidence on every edge.

Ignored-inclusive absence search:

- Ran `rg --no-ignore --hidden` over `data/antibiotics`, `data/raw`,
  `curation`, `reports/yaml_record_review`, `.claude`, `docs`, `README.md`,
  `conf`, `src`, `scripts`, `tests`, `justfile`, and `pyproject.toml` for exact
  `CHEBI:74880`, `1-dodecylguanidine`, `HILAYQUKKYWPJW`,
  `antibioticmech:chebi-4e645a4f2a`, `112-65-2`, `637515`, and
  `PMID:7623770` / `7623770`.
- The search included ignored files. It found the generated target, the ChEBI
  raw row, `data/antibiotics/PATHS.tsv`, and the derived review-queue row. It
  found no prior `CHEBI:74880` review report, no `curation/decisions.tsv` row,
  and no curated activity, target, resistance, producer, or mechanism addition
  for this exact ChEBI concept. Expected near-miss hits came from the adjacent
  `CHEBI:74889` acetate record because its label and definition contain
  `1-dodecylguanidine`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The record is still a bare ChEBI seed and cannot satisfy the `REVIEWED` gate until a curator resolves whether exact free-base `1-dodecylguanidine`, as distinct from its acetate and monoacetate salts, has claim-level activity and a defensible antimicrobial mechanism. | The target YAML has no record-level `evidence`, no `mode_of_action`, no `molecular_targets`, no `activity_spectrum`, no `producer_organisms`, no `resistance_mechanisms`, and no `causal_graphs`; the regenerated worklist places `CHEBI:74880` only in `mechanism` and `review-readiness` with 1 source literature lead, 0 record evidence items, and 0 targets. The one committed source PMID for `CHEBI:74880` supports exact free-base effects on host A-type potassium channels, while the strongest public antibacterial and antifungal mechanism leads found in bounded searches concern dodecylguanidine acetate / monoacetate or MC12 analogs. | Future curator-owned fields on `data/antibiotics/antibacterial/1-dodecylguanidine.yaml`, and any seed-lead correction in `data/raw/chebi_antimicrobials.tsv` or its extractor if the official ChEBI PubMed xref should be excluded from future review-readiness hints. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Keep the generated `CHEBI:74880` identity, free-base structure, parent
   compounds, CAS/Reaxys xrefs, filing class, and source concept unchanged
   unless full-text review or a future ChEBI update shows that the antimicrobial
   roles belong only to the acetate salt.
2. Inspect full text for `PMID:1902648`, `PMID:1381663`, `PMID:8229668`, and
   `PMID:200325` when curating the adjacent `CHEBI:74889` acetate record. Do
   not copy its *Pseudomonas syringae* or *Fusarium sulphureum* membrane-damage
   observations into this free-base record unless the source actually tested or
   equated neutral `1-dodecylguanidine`.
3. Inspect `PMID:7623770`, `PMID:31457300`, `PMID:16853157`, and any original
   papers behind ChEBI's `antibacterial agent`, `antifungal agent`, and
   `antifungal agrochemical` role assertions before adding exact activity or
   mechanism rows to this record.
4. If full-text inspection supports a membrane-disruption mechanism for exact
   free-base `CHEBI:74880`, add `mode_of_action: MEMBRANE_DISRUPTION`,
   `mode_of_action_target_scope: MICROBIAL_TARGET`, exact bacterial or fungal
   `activity_spectrum` observations with original assay units, and a causal
   graph that distinguishes surfactant membrane damage from micellar or
   salt-specific effects.
5. Promote `curation_status` to `REVIEWED` only after the identity, structure,
   filing-class, and curator-checked mechanism gates in `docs/CURATION.md` all
   pass.

## Follow-up Checks

After any future curation:

1. `just validate data/antibiotics/antibacterial/1-dodecylguanidine.yaml`
2. `just validate-strict data/antibiotics/antibacterial/1-dodecylguanidine.yaml --out /tmp/antibioticmech-chebi-74880-strict.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-74880-worklist.tsv`
5. `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv`

Also re-run exact PubMed and Semantic Scholar searches for
`1-dodecylguanidine`, `dodecylguanidine`, `laurylguanidine`, `C12-G`,
`dodecylguanidine free base`, and `dodecylguanidine acetate` so future curation
can separate exact free-base support from acetate, monoacetate, hydrochloride,
and MC12-analog evidence.

## Additional Notes

- The adjacent `CHEBI:74889` acetate salt appears immediately after this record
  in the review queue and has salt-specific source literature that should be
  reviewed on its own terms.
- ChEBI/OLS also carries `1-dodecylguanidine` as both an exact IUPAC synonym and
  a related IUPAC synonym. The generated record uses the term as its label and
  does not need a duplicate synonym row.
- `PMID:7623770` is a relevant chemical-pharmacology citation for C12-G, but it
  concerns host ion channels. Treat it as a source of non-antimicrobial target
  context, not as a microbial mechanism citation.
