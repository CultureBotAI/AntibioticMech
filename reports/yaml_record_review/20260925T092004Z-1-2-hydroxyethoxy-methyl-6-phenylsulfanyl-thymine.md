# YAML Record Review: 1-[(2-hydroxyethoxy)methyl]-6-(phenylsulfanyl)thymine

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antiviral/1-2-hydroxyethoxy-methyl-6-phenylsulfanyl-thymine.yaml`
- Started UTC: 2026-09-25T09:00:00Z
- Finished UTC: 2026-09-25T09:20:04Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:43060` |
| Label | `1-[(2-hydroxyethoxy)methyl]-6-(phenylsulfanyl)thymine` |
| Path | `data/antibiotics/antiviral/1-2-hydroxyethoxy-methyl-6-phenylsulfanyl-thymine.yaml` |
| Class | `ANTIVIRAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concept | `CHEBI:43060` / `1-[(2-hydroxyethoxy)methyl]-6-(phenylsulfanyl)thymine` from ChEBI release `2026-08-30` |
| Minted source key | `antibioticmech:chebi-cff3e50e11` |
| Structure key | `HDMHBHNRWDNNCD-UHFFFAOYSA-N` |
| Generated or maintained | Generated from `data/raw/chebi_antimicrobials.tsv` plus `data/antibiotics/PATHS.tsv`; future seeded identity, role, structure, synonym, xref, or source-PMID changes belong upstream rather than as hand edits. |

Resolution:

- `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv`
  regenerated the full queue and kept `CHEBI:43060` as the next unreviewed row:
  `MECHANISM_REVIEW: mechanism is source-seeded and not curator-checked; 3
  source literature lead(s), 0 record evidence item(s), 0 target(s)`.
- `data/antibiotics/PATHS.tsv` maps `CHEBI:43060` to `ANTIVIRAL` with slug
  `1-2-hydroxyethoxy-methyl-6-phenylsulfanyl-thymine`, matching the current
  record path.
- `data/raw/chebi_antimicrobials.tsv` is the ChEBI source row that seeds the
  generated target record.
- The whole target YAML was read before judging generated identity, ChEBI
  provenance, structure, xrefs, source concepts, role-derived mechanism notes,
  and curation history.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antiviral/1-2-hydroxyethoxy-methyl-6-phenylsulfanyl-thymine.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/antiviral/1-2-hydroxyethoxy-methyl-6-phenylsulfanyl-thymine.yaml --out /tmp/antibioticmech-chebi-43060-strict.tsv` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed after emitting the known unrelated `iclaprim` / `CHEBI:31724` CARD diagnostic: 2939 expected records, 2939 on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, and 0 stale lockfile rows. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-43060-worklist.tsv` | Passed; exact `CHEBI:43060` rows appear only in `mechanism` and `review-readiness`. |
| `uv run runoak -i ols:chebi labels CHEBI:43060 CHEBI:36044 CHEBI:53756 CHEBI:15734 CHEBI:35683 CHEBI:38337` | Passed: OLS resolved the compound, `antiviral drug`, `HIV-1 reverse transcriptase inhibitor`, `primary alcohol`, `aryl sulfide`, and `pyrimidone`. |
| OLS4 term lookup for `CHEBI:43060` | Passed: live OLS4 resolved a current, ChEBI-defining, `3_STAR` term with formula, charge, masses, SMILES, Standard InChI, Standard InChIKey, synonyms, xrefs, and PubMed xrefs that match the committed ChEBI source row. |
| `curl -L https://data.rcsb.org/rest/v1/core/chemcomp/HEF` | Passed: RCSB PDB CCD component `HEF` reports formula `C14 H16 N2 O4 S`, charge `0`, ChEBI `CHEBI:43060`, PubChem CID `64993`, CAS `123027-56-5`, and exact InChI/InChIKey `HDMHBHNRWDNNCD-UHFFFAOYSA-N`. |
| PubChem CID `64993` property lookup | Passed: PubChem reports formula `C14H16N2O4S`, formal charge `0`, exact mass `308.08307817`, InChI, and InChIKey `HDMHBHNRWDNNCD-UHFFFAOYSA-N` for the same exact compound. |
| Exact PubMed/Semantic Scholar query for `"1-[(2-hydroxyethoxy)methyl]-6-(phenylthio)thymine" OR "1-[(2-hydroxyethoxy)methyl]-6-phenylthiothymine" OR "6-Hept" OR HMPTT` | PubMed returned 20 candidates; Semantic Scholar returned HTTP 429. The useful exact leads included the 1989 original HEPT HIV-1 activity paper, the 1995 HEPT-resistance paper, a 1995 NNRTI mechanism paper involving HEPT-soaked HIV-1 reverse transcriptase crystals, and later HEPT/RT structural and QSAR literature. |
| Exact PubMed/Semantic Scholar query for `HEPT HIV-1 reverse transcriptase inhibitor 123027-56-5 HDMHBHNRWDNNCD` | PubMed returned 17 candidates; Semantic Scholar returned HTTP 429. The exact and near-exact candidates overlapped the original activity, resistance, and HIV-1 reverse-transcriptase leads above. |
| PubMed efetch for committed source PMIDs `1683214`, `17191775`, and `1992136` | Passed: all three exact source identifiers resolved. |

No narrower single-record reference or curation-history validator is exposed for
this ChEBI-seeded record. The focused strict validator covered closed schema
shape, and `verify-corpus --summary` covered generated drift from the
maintained raw and path-lock inputs.

## Identity and Grounding

The generated identity is consistent with official ChEBI, RCSB PDB CCD, and
PubChem for exact `CHEBI:43060`:

| Assertion | Record value | Check |
|---|---|---|
| ChEBI identity | `CHEBI:43060`, `1-[(2-hydroxyethoxy)methyl]-6-(phenylsulfanyl)thymine` | OLS4 resolved the term to a current ChEBI-defining class in the `3_STAR` subset. |
| Definition | Thymine substituted at positions 1 and 6 by a `(2-hydroxyethoxy)methyl` group and a `phenylsulfanyl` group | Matched OLS4 and the committed ChEBI row. |
| Formula and charge | `C14H16N2O4S`, charge `0` | Matched OLS4, PubChem CID `64993`, and RCSB PDB CCD component `HEF`. |
| Masses | average `308.359`, monoisotopic `308.08308` | Matched OLS4; PubChem's exact mass also matches the generated monoisotopic mass to the reported precision. |
| SMILES | `Cc1c(Sc2ccccc2)n(COCCO)c(=O)nc1=O` | Matched the committed ChEBI row and official ChEBI/OLS4 structure annotation. |
| Standard InChI | `InChI=1S/C14H16N2O4S/c1-10-12(18)15-14(19)16(9-20-8-7-17)13(10)21-11-5-3-2-4-6-11/h2-6,17H,7-9H2,1H3,(H,15,18,19)` | Matched OLS4, PubChem CID `64993`, and RCSB PDB CCD component `HEF`. |
| InChIKey | `HDMHBHNRWDNNCD-UHFFFAOYSA-N` | Matched OLS4, PubChem CID `64993`, and RCSB PDB CCD component `HEF`. |
| Parent compounds | `CHEBI:15734`, `CHEBI:35683`, `CHEBI:38337` | OAK resolved these to `primary alcohol`, `aryl sulfide`, and `pyrimidone`, agreeing with the compound definition and ChEBI structural classification. |
| Activity roles | `CHEBI:36044`, `CHEBI:53756` | OAK resolved these to `antiviral drug` and `HIV-1 reverse transcriptase inhibitor`; the generated row preserves the committed ChEBI roles. |
| Filing class | `ANTIVIRAL` | The ChEBI `HIV-1 reverse transcriptase inhibitor` role maps this generated record to `data/antibiotics/antiviral/`. |

Checked exact xrefs:

| Xref | Check |
|---|---|
| `pdb-ccd:HEF` | RCSB resolves component `HEF` to the same formula, zero charge, Standard InChI, Standard InChIKey, ChEBI ID, and PubChem CID as the generated record. |
| `cas:123027-56-5` | Present on the committed ChEBI row, official ChEBI/OLS4 term, and RCSB `HEF` record. |
| `reaxys:4271052` | Present on official ChEBI and preserved in the generated ChEBI row; not independently checked because Reaxys is not publicly resolvable. |

## Evidence

The target has no record-level `evidence`, no `molecular_targets`, no
`activity_spectrum`, no `resistance_mechanisms`, and no `causal_graphs`.
That is allowed for a ChEBI-seeded record because the ChEBI source concept
supplies database provenance, and there are no claim-local activity, target,
resistance, producer, dataset, clinical, or causal assertions that would require
object-level evidence.

The seeded `mode_of_action` and `mode_of_action_target_scope` are honest about
their provenance: the note says they were assigned from ChEBI role
`CHEBI:53756`, that ChEBI asserts the role on the compound, and that the field
is not a curator's mechanistic review. The corresponding ChEBI term still
asserts the HIV-1 reverse-transcriptase-inhibitor role.

Committed source literature:

| PMID | Public title/abstract support |
|---|---|
| `PMID:1683214` | Exact-HEPT activity lead. The 1991 `Antiviral Research` abstract reports synergistic inhibition of HIV-1 replication by HEPT and recombinant alpha interferon in vitro, including MT-4 cells and peripheral blood lymphocytes. The public abstract supports exact-compound anti-HIV-1 activity, not a claim-local HIV-1 reverse-transcriptase target by itself. |
| `PMID:1992136` | Exact-HEPT and analog synthesis/activity lead. The 1991 `Journal of Medicinal Chemistry` abstract reports HEPT analog synthesis and anti-HIV-1 activity of substituted HEPT derivatives. It is useful for SAR discovery but not a direct exact-HEPT molecular-target citation from its public abstract. |
| `PMID:17191775` | Secondary NNRTI history lead. The 2004 `Chemistry & Biodiversity` abstract mentions HEPT and TIBO as historical non-nucleoside reverse-transcriptase-inhibitor starting points; use cited primary papers for record activity, target, or resistance curation. |

Additional exact and near-exact publication leads from bounded PubMed searches:

| PMID | Assessment |
|---|---|
| `PMID:2575380` | Primary exact-HEPT activity lead. The 1989 abstract reports potent, selective HIV-1 inhibition across T4 cell cultures, peripheral blood lymphocytes, and macrophages; an HIV-1 HTLV-IIIB / MT-4 `EC50` of `7.0 microM`; mock-infected MT-4 `CC50` of `740 microM`; no effect on HIV-2 or other tested retroviruses; and states that HEPT triphosphate did not interact with HIV-1 reverse transcriptase and that the mechanism remained under study. This is the best public lead for an exact `activity_spectrum` observation, but not for the seeded RT target. |
| `PMID:7540784` | Future resistance and target lead. The 1995 abstract reports that a virus isolate selected in HEPT carried reverse-transcriptase `P236L` and was resistant to HEPT plus another HEPT derivative. Full text is needed before converting that into structured exact-drug resistance evidence. |
| `PMID:7540935` | Future structural/mechanism lead. The 1995 abstract says unliganded HIV-1 reverse transcriptase was produced by soaking weak-binding HEPT out of pregrown crystals, and compares that unliganded structure with four RT/NNRTI complexes to suggest that NNRTIs lock the polymerase site in an inactive conformation. This supports NNRTI mechanism generally, but the public abstract alone should not be represented as an exact HEPT-bound target observation. |
| `PMID:10195434` | Future exact structural lead. The 1999 abstract compares computed HEPT conformations to X-ray structures of HEPT associated with HIV-1 reverse transcriptase and analyzes the inhibition-complex interactions. Inspect the full text and PDB accessions before adding any `structural_observations`. |

## Completeness

Complete enough for read-only review:

- Generated identity, exact ChEBI grounding, structure, parent compounds,
  same-structure CAS/PDB CCD/Reaxys xrefs, ChEBI activity roles, source concept,
  and `ANTIVIRAL` filing class agree with the inspected public databases and
  committed source rows.
- The record has only seed and reseed curation-history events from
  `2026-08-30`, accurately matching the generated `SEEDED` state.
- `producer_organisms` is absent; the inspected ChEBI, PubChem, PDB CCD, and
  bounded PubMed evidence did not identify HEPT as a natural product with a
  named producer.
- `clinical_status` and `clinical_status_assertions` are absent; no inspected
  source represented exact HEPT as an approved therapeutic substance or product.
- `datasets` is absent; the inspected evidence did not expose a public exact-HEPT
  screening, omics, or structural dataset accession.

Consequential gaps:

- `activity_spectrum` is absent even though exact primary literature reports
  anti-HIV-1 activity and quantitative `EC50`/`CC50` observations for HEPT.
- `molecular_targets` is absent; the HIV-1 reverse transcriptase target exists
  only as a ChEBI role that seeded `mode_of_action`.
- `mode_of_action: VIRAL_POLYMERASE_INHIBITION` and
  `mode_of_action_target_scope: MICROBIAL_TARGET` are source-seeded and have
  not been curator-checked against primary target evidence.
- `resistance_mechanisms` is absent. The HEPT-selected reverse-transcriptase
  `P236L` literature is a future curation lead, but no exact resistance claim
  has been curated into the YAML.
- `causal_graphs` is absent; the record has not yet connected HEPT, HIV-1
  reverse transcriptase, polymerase inactivation, viral DNA synthesis, and
  decreased HIV replication with claim-level evidence on every edge.
- `structural_observations` is absent. The `pdb-ccd:HEF` xref validates chemical
  identity only; this review did not inspect a macromolecular PDB accession that
  would justify an RT/HEPT structural observation.

Ignored-inclusive absence search:

- Ran `rg --no-ignore --hidden` over `data/antibiotics`, `data/raw`,
  `curation`, `reports/yaml_record_review`, `.claude`, `docs`, `README.md`,
  `conf`, `src`, `scripts`, `tests`, `justfile`, and `pyproject.toml` for exact
  `CHEBI:43060`, `1-[(2-hydroxyethoxy)methyl]-6-(phenylsulfanyl)thymine`,
  `1-2-hydroxyethoxy-methyl-6-phenylsulfanyl-thymine`,
  `HDMHBHNRWDNNCD-UHFFFAOYSA-N`, `antibioticmech:chebi-cff3e50e11`,
  `pdb-ccd:HEF`, `cas:123027-56-5`, `reaxys:4271052`, and PMIDs `1683214`,
  `17191775`, and `1992136`.
- The searches included ignored files. They found the generated target, the
  ChEBI raw row, `data/antibiotics/PATHS.tsv`, and the derived review-queue
  row. They found no prior `CHEBI:43060` review report, no
  `curation/decisions.tsv` row, and no curated activity, target, resistance, or
  producer addition for this exact ChEBI concept.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The record still has only a source-seeded HIV-1 reverse-transcriptase mechanism and cannot satisfy the `REVIEWED` gate until a curator adds claim-level activity and target evidence for exact HEPT. | The target YAML has ChEBI-seeded `mode_of_action` text ending `Not a curator's mechanistic review`, no record-level `evidence`, no `activity_spectrum`, no `molecular_targets`, and no `causal_graphs`; the regenerated worklist places `CHEBI:43060` only in `mechanism` and `review-readiness` with 3 source literature leads, 0 record evidence items, and 0 targets. Exact PubMed searches exposed primary HEPT anti-HIV-1 activity and resistance/target leads that have not yet been curated. | Future curator-owned fields on `data/antibiotics/antiviral/1-2-hydroxyethoxy-methyl-6-phenylsulfanyl-thymine.yaml`, written with `record_curation_event` and `write_validated_antibiotic`. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Keep the generated `CHEBI:43060` identity, label, exact structure, parent
   compounds, CAS/PDB CCD/Reaxys xrefs, ChEBI activity roles, filing class, and
   source concept unchanged.
2. Inspect `PMID:2575380`, `PMID:1683214`, and `PMID:1992136` far enough to
   curate exact-HEPT antiviral activity observations with organism or viral
   strain, cell system, endpoint, value, qualifier, and units. Preserve the
   original assay units, likely as `EC50`, `CC50`, or selectivity observations
   rather than forcing antiviral cell-culture values into MIC fields.
3. Inspect `PMID:7540784` before adding a HEPT-specific resistance mechanism.
   If the full text supports the public abstract, represent the HIV-1
   reverse-transcriptase `P236L` selection phenotype without generalizing it to
   every HEPT analog or to all non-nucleoside reverse-transcriptase inhibitors.
4. Inspect full text and structure accessions behind `PMID:7540935` and
   `PMID:10195434` before adding molecular-target or structural-observation
   rows. Do not assert direct HEPT binding or a specific PDB accession from the
   `pdb-ccd:HEF` chemical-component xref alone.
5. Promote the ChEBI-derived `VIRAL_POLYMERASE_INHIBITION` block to a
   curator-owned mechanism only after primary evidence supports inhibition of
   HIV-1 reverse transcriptase by exact HEPT. If the selected evidence supports
   it, add a causal graph that distinguishes HEPT binding, polymerase-site
   inactivation, impaired viral DNA synthesis, and reduced HIV-1 replication.
6. Move `curation_status` to `REVIEWED` only after the identity, structure,
   filing-class, and curator-checked mechanism gates in `docs/CURATION.md` all
   pass.

## Follow-up Checks

After any future curation:

1. `just validate data/antibiotics/antiviral/1-2-hydroxyethoxy-methyl-6-phenylsulfanyl-thymine.yaml`
2. `just validate-strict data/antibiotics/antiviral/1-2-hydroxyethoxy-methyl-6-phenylsulfanyl-thymine.yaml --out /tmp/antibioticmech-chebi-43060-strict.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-43060-worklist.tsv`
5. `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv`

Also re-run exact PubMed and Semantic Scholar searches for
`1-[(2-hydroxyethoxy)methyl]-6-(phenylthio)thymine`,
`1-[(2-hydroxyethoxy)methyl]-6-phenylthiothymine`, `6-Hept`, `HEPT`,
`HMPTT`, `CHEBI:43060`, `HDMHBHNRWDNNCD-UHFFFAOYSA-N`, `123027-56-5`,
`64993`, and the PMIDs used in any new activity, target, resistance, or causal
edge.

## Additional Notes

- The PDB CCD `HEF` xref is chemical identity metadata. It is useful for
  confirming the exact structure but is not a macromolecular HIV-1
  reverse-transcriptase structure on its own.
- The ChEBI source row lists `pubmed:1683214`, `pubmed:17191775`, and
  `pubmed:1992136` as upstream database provenance. OLS4 preserves these
  references as PubMed cross-references rather than YAML `xrefs`.
- The broad exact-name search term `6-Hept` retrieved some unrelated "hept"
  substrings. The useful hits were recovered by combining exact HEPT synonyms,
  the CAS number, the InChIKey, and HIV-1 reverse-transcriptase terms.
- The NCBI email environment variable was explicitly unset for all
  `scripts/search_publications.py` calls.
- Semantic Scholar was unavailable for both publication-discovery searches
  because it returned HTTP 429. PubMed succeeded and provided the bounded
  exact-literature leads summarized above.
