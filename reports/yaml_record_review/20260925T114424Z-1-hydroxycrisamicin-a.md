# YAML Record Review: 1-hydroxycrisamicin A

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antibacterial/1-hydroxycrisamicin-a.yaml`
- Started UTC: 2026-09-25T11:38:00Z
- Finished UTC: 2026-09-25T11:44:24Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:66042` |
| Label | `1-hydroxycrisamicin A` |
| Path | `data/antibiotics/antibacterial/1-hydroxycrisamicin-a.yaml` |
| Class | `ANTIBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concept | `CHEBI:66042` / `1-hydroxycrisamicin A` from ChEBI release `2026-08-30` |
| Minted source key | `antibioticmech:chebi-29bdc403ae` |
| Structure key | `RGOCVNGEBMGCNA-WIDQCZIUSA-N` |
| Generated or maintained | Generated from `data/raw/chebi_antimicrobials.tsv` plus `data/antibiotics/PATHS.tsv`; seed-owned identity, label, parent, role, xref, synonym, source-PMID, and structure changes belong in the maintained source inputs rather than as hand edits to this YAML. |

Resolution:

- `just review-queue --limit 0 --tsv /tmp/antibioticmech-chebi-66042-review-queue.tsv`
  kept `CHEBI:66042` at `review-readiness` row 173, immediately after the
  merged `CHEBI:74889` review row: `MECHANISM_REVIEW: mechanism is absent; 1
  source literature lead(s), 0 record evidence item(s), 0 target(s)`.
- `data/antibiotics/PATHS.tsv` maps `CHEBI:66042` to class `ANTIBACTERIAL` and
  slug `1-hydroxycrisamicin-a`, matching the current YAML path.
- `data/raw/chebi_antimicrobials.tsv` carries the exact ChEBI source row that
  seeds this record.
- The full target YAML was read before judging the label, exact ChEBI
  grounding, structure, ChEBI parents, antibacterial role, Reaxys xref, empty
  mechanism, empty activity, empty producer, empty target, empty resistance,
  empty dataset, empty causal-graph lists, and seed-only curation history.
- A gitignore-independent search with `rg --no-ignore --hidden` over
  `data/antibiotics`, `data/raw`, `curation`, `reports/yaml_record_review`,
  local skills, docs, source, tests, `justfile`, `pyproject.toml`, README, and
  configuration paths found no prior review report, `curation/decisions.tsv`
  row, exact-structure activity, exact-structure producer, mechanism, target,
  resistance, causal graph, or dataset assertion for `CHEBI:66042`,
  `antibioticmech:chebi-29bdc403ae`, `RGOCVNGEBMGCNA-WIDQCZIUSA-N`, DOI
  `10.7164/antibiotics.51.82`, or *Micromonospora* sp. SA246.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antibacterial/1-hydroxycrisamicin-a.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/antibacterial/1-hydroxycrisamicin-a.yaml --out /tmp/antibioticmech-chebi-66042-strict.tsv` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed after emitting the known unrelated `iclaprim` / `CHEBI:31724` CARD diagnostic: 2939 expected records, 2939 on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, and 0 stale lockfile rows. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-next-worklist.tsv` | Passed; exact `CHEBI:66042` rows appear in `mechanism`, `producer-candidate`, `activity-candidate`, and `review-readiness`. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-chebi-66042-review-queue.tsv` | Passed; `CHEBI:66042` appears at `review-readiness` row 173. |
| `uv run runoak -i ols:chebi labels CHEBI:66042 CHEBI:33282 CHEBI:25830 CHEBI:33822 CHEBI:37407 CHEBI:37581 CHEBI:38163` | Passed: OAK resolved the compound, `antibacterial agent`, `p-quinones`, `organic hydroxy compound`, `cyclic ether`, `gamma-lactone`, and `organic heterotetracyclic compound`. |
| OLS4 term lookup for `CHEBI:66042` | Passed: live OLS4 resolved a current, non-obsolete, ChEBI-defining, `3_STAR` term whose definition, formula, charge, masses, SMILES, Standard InChI, Standard InChIKey, Reaxys xref, and PubMed xref match the committed ChEBI seed row. |
| OLS4 parent lookup for `CHEBI:66042` | Passed: live OLS4 returned the five generated parent terms: `CHEBI:25830`, `CHEBI:33822`, `CHEBI:37407`, `CHEBI:37581`, and `CHEBI:38163`. |
| OLS4 `has_role` lookup for `CHEBI:66042` | Passed: live OLS4 returns ChEBI roles `CHEBI:25212` and `CHEBI:33282`; the generated record correctly retains only the antimicrobial `CHEBI:33282` role in `activity_roles`. |
| PubChem InChIKey lookup for `RGOCVNGEBMGCNA-WIDQCZIUSA-N` | Passed: the exact Standard InChIKey maps to CID `70678750`. |
| PubChem CID `70678750` identity checks | Passed through the PUG-View, SDF, and synonym endpoints: PubChem labels the entry `1-Hydroxycrisamicin A`, lists `CHEBI:66042`, reports the same formula, Standard InChI, Standard InChIKey, monoisotopic mass, and zero charge, and preserves the same fully stereospecified single-fragment structure. The compact PubChem property endpoint intermittently returned an empty body, so PUG-View/SDF were used instead. |
| PubMed summary lookup for `PMID:9531992` | Passed: PubMed resolves the source PMID to the 1998 Journal of Antibiotics paper `1-Hydroxycrisamicin A, a new isochromanquinone antibacterial antibiotic, produced by Micromonospora sp. SA246`, DOI `10.7164/antibiotics.51.82`. |
| PubMed efetch for `PMID:9531992` | Passed: PubMed confirms DOI `10.7164/antibiotics.51.82`, the 1998 Journal of Antibiotics citation, and MeSH indexing for antibacterial-agent chemistry/isolation and microbial sensitivity tests. No abstract is attached to this short article in PubMed. |
| DOI/J-STAGE lookup for `10.7164/antibiotics.51.82` | Passed: the DOI resolves to a free J-STAGE page for volume 51 issue 1 pages 82-84, with a downloadable 3-page scanned PDF. |
| Visual PDF inspection for the J-STAGE article | Passed by rendering the scanned PDF to `/tmp` with `mutool draw`; the paper shows isolation and structural elucidation of compound 1 from *Micromonospora* sp. SA246 and an antimicrobial Table 3. Local `pdftotext`/`pdfinfo` were unavailable, `tesseract` could not open the valid rendered PNGs, and Ghostscript was unusable because `/usr/local/bin/gs-X11` cannot load `/usr/X11/lib/libXt.6.dylib`. |
| Exact PubMed title/abstract query for `"hydroxycrisamicin"` OR `"crisamicin"` OR `"1-hydroxycrisamicin"` | Passed: PubMed returned 13 title/abstract hits; close hits concerned exact `PMID:9531992`, 9-hydroxycrisamicin A, crisamicin A, crisamicin C, crisamicin biosynthesis, and later synthesis/analogue papers. |
| Europe PMC lookup for `EXT_ID:9531992 SRC:MED` | Passed: Europe PMC resolves the PMID to the same DOI, title, journal, pages, and ChEBI cross-reference. |
| Europe PMC query for `"hydroxycrisamicin"` OR `"crisamicin A"` | Passed as a broad discovery search: 68 hits, including the exact discovery paper, close congener and synthesis papers, reviews, and many unrelated text-mining false positives. |
| Semantic Scholar exact query for `"1-hydroxycrisamicin A" OR "9-hydroxycrisamicin A" OR "crisamicin A"` | Not available: the public Graph API returned HTTP 429. |

No narrower single-record reference or curation-history validator is exposed for
this ChEBI-only seed. The focused strict validator covered closed schema shape,
and `verify-corpus --summary` covered generated drift from the maintained raw
and path-lock inputs.

## Identity and Grounding

The generated identity agrees with official ChEBI/OLS and PubChem for exact
`CHEBI:66042`:

| Assertion | Record value | Check |
|---|---|---|
| ChEBI identity | `CHEBI:66042`, `1-hydroxycrisamicin A` | OLS4 resolved the term to a current, ChEBI-defining class in the `3_STAR` subset. |
| Definition | Organic heterotetracyclic compound from culture broth of *Micromonospora* sp. SA-246 with potent activity against several Gram-positive strains | Matched OLS4, the committed ChEBI row, and the exact J-STAGE source paper. |
| Formula and charge | `C32H22O13`, charge `0` | Matched OLS4, the committed ChEBI row, PubChem PUG-View, and PubChem SDF. |
| Masses | average `614.515`, monoisotopic `614.10604` | Matched OLS4; PubChem reports exact/monoisotopic mass `614.10604075`. |
| SMILES | `[H][C@@]12OC(=O)C[C@]1([H])O[C@@H](C)C1=C2C(=O)c2c(O)cc(-c3cc(O)c4c(c3)C(=O)C3=C(C4=O)[C@]4([H])OC(=O)C[C@]4([H])O[C@]3(C)O)cc2C1=O` | Matched the committed ChEBI row and official ChEBI/OLS. PubChem reports an equivalent fully stereospecified single-fragment SMILES. |
| Standard InChI | `InChI=1S/C32H22O13/c1-9-20-23(30-16(42-9)7-18(35)43-30)28(39)21-12(26(20)37)3-10(5-14(21)33)11-4-13-22(15(34)6-11)29(40)24-25(27(13)38)32(2,41)45-17-8-19(36)44-31(17)24/h3-6,9,16-17,30-31,33-34,41H,7-8H2,1-2H3/t9-,16-,17-,30+,31+,32-/m0/s1` | Matched OLS4 and PubChem CID `70678750`. |
| Standard InChIKey | `RGOCVNGEBMGCNA-WIDQCZIUSA-N` | Matched OLS4 and PubChem CID `70678750`; exact InChIKey lookup maps to PubChem CID `70678750`. |
| Parent compounds | `CHEBI:25830`, `CHEBI:33822`, `CHEBI:37407`, `CHEBI:37581`, `CHEBI:38163` | OAK and live OLS4 resolve these to `p-quinones`, `organic hydroxy compound`, `cyclic ether`, `gamma-lactone`, and `organic heterotetracyclic compound`; the paper shows the expected isochromanquinone/gamma-lactone structure. |
| Activity roles | `CHEBI:33282` | OAK resolved this to `antibacterial agent`; OLS4 carries it as the sole antimicrobial role on the term. |
| Filing class | `ANTIBACTERIAL` | Follows the single retained antibacterial ChEBI role. |

Checked xrefs:

| Xref | Result |
|---|---|
| `reaxys:8180397` | Preserved from official ChEBI/OLS as an exact database xref; no public Reaxys check is available. |

`PMID:9531992` is not a formal `EvidenceItem` in this generated seed, but it is
the sole PubMed source xref on the committed ChEBI row and exact OLS4 term. It
is correctly a discovery/activity paper for this exact structure rather than a
paper about the sibling natural products crisamicin A, crisamicin C, or
9-hydroxycrisamicin A.

PubChem now exposes additional identifiers such as CID `70678750` and synonym
`204198-17-4`, but the current ChEBI row carries neither. Leaving them absent is
not a record defect because this review did not verify whether the new PubChem
synonym denotes a same-structure registry accession stable enough for the
repository's xref contract.

## Evidence

The generated label, definition, IUPAC synonym, parent compounds, Reaxys xref,
filing class, antibacterial role, exact structure, ChEBI source concept, and
sole ChEBI source PMID reproduce from `data/raw/chebi_antimicrobials.tsv` with
no `verify-corpus` drift.

The record has no object-level evidence-bearing claims yet:

| Claim family | Current state | Review |
|---|---|---|
| Record-level evidence | Empty | Acceptable for a ChEBI seed. ChEBI provenance is retained in `source_concepts`; record-level boilerplate is intentionally optional. |
| Mode of action | Empty | No direct target or mode-of-action experiment was found for exact 1-hydroxycrisamicin A in the inspected source paper or bounded PubMed exact-name search. |
| Molecular targets | Empty | Consistent with the absent mechanism; no source-backed target has been omitted from this generated seed. |
| Activity observations | Empty | Incomplete: the J-STAGE source article's Table 3 contains exact MIC values for a narrow organism panel, but the record has not yet promoted them into claim-level `activity_spectrum` rows. |
| Producer organisms | Empty | Incomplete: the exact source states production by *Micromonospora* sp. SA246 and Figure 2 shows recovery of the compound from culture broth, but the strain has not yet been resolved to an NCBI taxon and curated. |
| Resistance mechanisms | Empty | No exact resistance paper, gene, isolate, or ARO term was found in the inspected exact-name literature. |
| Datasets | Empty | No public accessioned exact-compound dataset was found in the bounded checks. |
| Causal graphs | Empty | Consequence of the unresolved mode of action; the exact discovery paper does not support a causal graph. |

The exact primary source paper supports activity only in the narrow context it
reports. Table 3 lists `MIC (ug/ml)` values:

| Organism as printed | MIC |
|---|---:|
| *Staphylococcus aureus* FDA 209P | 3.12 |
| *Bacillus subtilis* IAM 1069 | 1.56 |
| *Sarcina lutea* | 1.56 |
| *Streptococcus* sp. | 3.12 |
| *Streptomyces scabies* | 0.78 |
| *Escherichia coli* AB 1157 | >100 |
| *Pseudomonas aeruginosa* IFO 13130 | >100 |
| *Candida albicans* IAM 4905 | >100 |
| *Saccharomyces cerevisiae* IFO 1008 | >100 |
| *Mucor ramannianus* IAM 6218 | >100 |
| *Aspergillus niger* ATCC 9642 | >100 |
| *Penicillium chrysogenum* ATCC 12690 | >100 |

That table is a useful activity-curation source but not a target or mechanism
source. It also needs a careful curator pass before import: the schema requires
each MIC to carry a method in `assay`, and no broth/agar/diffusion method was
visible in the scanned three-page paper during this review.

Near-miss or contextual literature leads:

| Lead | Assessment |
|---|---|
| `PMID:9711245` | Same producing strain, but for 9-hydroxycrisamicin A. Do not lift activity or structure assertions onto exact `CHEBI:66042`. |
| `PMID:3754547`, `PMID:3700237`, `PMID:3198498`, `PMID:3356603` | Crisamicin A/C isolation and biosynthesis papers cited by `PMID:9531992`; useful for congener context, not direct evidence for exact 1-hydroxycrisamicin A activity or mechanism. |
| `PMID:15184062` | 9-hydroxycrisamicin A HBV-replication paper from the same strain series; different compound, different assay axis. |
| `PMID:18553973`, `PMID:25029027`, `PMID:25677470`, `PMID:32298125` | Later crisamicin A synthesis papers; structurally nearby but not exact record support. |

## Completeness

The seed-owned identity and structure layer is complete enough for this exact
ChEBI term:

- The label, source concept, `EXACT` grounding status, and minted source key
  are internally consistent.
- The generated IUPAC synonym matches official ChEBI/OLS.
- The five parent compounds and single antibacterial role all resolve to
  current ChEBI terms.
- The Reaxys xref is present in live OLS4 and is kept as a chemical xref; no
  document, drug, PDB, or class accession is being misfiled as same-structure
  identity.
- PubChem CID `70678750` independently corroborates the exact Standard
  InChIKey, formula, charge, mass, and stereochemistry.

The following consequential gaps remain:

- `mode_of_action` remains absent, so the record cannot satisfy the local
  `REVIEWED` gate even though its ChEBI identity and source activity role are
  sound.
- The source paper has a clear producer lead, *Micromonospora* sp. SA246, but
  no `producer_organisms` row with `NCBITaxon`, strain, source, and
  citation-level evidence has been curated.
- The source paper has quantitative MIC values for five susceptible
  Gram-positive bacteria and negative bacterial/fungal comparator values, but
  no `activity_spectrum` rows have been curated.
- No exact molecular target, resistance mechanism, public dataset, or
  evidence-backed causal graph was found in the bounded searches.

The negative internal search included ignored files via `rg --no-ignore
--hidden` and covered curated records, raw source inventories, curation files,
existing review reports, local skills, docs, source, tests, `justfile`,
`pyproject.toml`, README, and config paths.

## Findings

### Blocker

None found.

### Major

#### F1. The exact ChEBI seed lacks curated mechanism, producer, and activity claims

`data/antibiotics/antibacterial/1-hydroxycrisamicin-a.yaml` is still a bare
generated seed. It has no `mode_of_action`, `molecular_targets`,
`activity_spectrum`, `producer_organisms`, `resistance_mechanisms`,
`causal_graphs`, or claim-level `evidence`, even though the exact source paper
establishes the discovery structure, production by *Micromonospora* sp. SA246,
and a bounded MIC table for Gram-positive bacteria versus Gram-negative/fungal
comparators.

The record is structurally valid and its identity is not wrong, but it cannot
be promoted to `REVIEWED`: the local gate requires identity, structure, class,
and at least a checked mode of action with real citations where targets are
known. Any future activity rows must also carry an assay method, which was not
explicitly visible in the scanned source paper, and any producer row must first
resolve *Micromonospora* sp. SA246 without overstating it as a named species.

Maintained owner: curator-owned mechanism, activity, and producer fields in
`data/antibiotics/antibacterial/1-hydroxycrisamicin-a.yaml`; use the validated
write path described by `.claude/skills/curate-yaml-record/SKILL.md`, not a hand
edit.

### Minor

None found.

## Recommended Edits

1. Curate a mode-of-action disposition for
   `data/antibiotics/antibacterial/1-hydroxycrisamicin-a.yaml`. If a bounded
   primary-literature search still finds no target or mechanism beyond the
   discovery MIC paper, add a curator-owned veto explaining that the exact
   mode of action remains unknown.

2. Resolve *Micromonospora* sp. SA246 conservatively and add a
   `producer_organisms` claim only if the source taxon can be represented
   without inventing a species assignment. At minimum the paper supports the
   source strain label `SA246` and the genus *Micromonospora*.

3. Curate the Table 3 activity observations from DOI
   `10.7164/antibiotics.51.82` only after resolving the assay-method gap. The
   row owner is `data/antibiotics/antibacterial/1-hydroxycrisamicin-a.yaml`,
   but each organism-level observation needs its own evidence object and should
   preserve the strain labels printed by the source.

4. Leave `resistance_mechanisms`, `molecular_targets`, `datasets`, and
   `causal_graphs` empty unless a future exact-compound source supports those
   assertions directly. The inspected discovery paper and the exact-name PubMed
   hits do not.

## Follow-up Checks

After any future curation:

1. Run
   `just validate-strict data/antibiotics/antibacterial/1-hydroxycrisamicin-a.yaml --out /tmp/antibioticmech-chebi-66042-strict.tsv`.

2. Run `just verify-corpus --summary` to prove any curator-owned additions did
   not drift seed-owned ChEBI fields.

3. Run `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-66042-worklist.tsv`
   and confirm `CHEBI:66042` no longer appears in queues whose underlying gaps
   were actually fixed.

4. If MIC rows are added, confirm every `mic_value` has `mic_units`,
   `mic_qualifier` when the source uses `>`, a real `assay`, and narrow
   taxon/strain context.

5. If a producer row is added, verify its `taxon_id` denotes exactly the
   organism rank claimed by `taxon_label`, keeps `SA246` in `strain`, and cites
   the 1998 primary paper as evidence for compound production.

## Additional Notes

- ChEBI/OLS carries `metabolite` (`CHEBI:25212`) as a non-antimicrobial role
  for `CHEBI:66042`; it is intentionally absent from `activity_roles`.
- The discovery paper compares compound 1 with 9-hydroxycrisamicin A and
  crisamicin A. Those are nearby natural products but not exact substitutes for
  this record.
- Semantic Scholar was rate-limited with HTTP 429 for the exact crisamicin
  query. The PubMed, Europe PMC, J-STAGE, OLS4, and PubChem checks were enough
  to verify identity and bound the obvious activity/producer/mechanism gaps.
