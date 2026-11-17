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

## Full candidate and assay comparison

The pinned 505,890-row AST snapshot and exact isolate join reconstruct 254,944
candidate groups on the expanded map, with no unused mapping entries. All
230,294 earlier candidates occur unchanged as complete row dictionaries,
including measurements, qualifiers, observation IDs, and genome metadata.
The 24,650 additional candidates introduce no new assay signatures: all are
covered by the existing 60 explicitly reviewed contexts. Only the candidate
checksum changes in the assay review; no acceptance rule is broadened.

| Added source label | Candidates | Accepted | Explicit resistant calls among accepted |
|---|---:|---:|---:|
| cefalotin | 453 | 452 | 45 |
| cefotaxime | 2,010 | 2,006 | 1,297 |
| cefovecin | 3,369 | 3,369 | 11 |
| cefpodoxime | 3,618 | 3,618 | 205 |
| cephalothin | 2,076 | 2,072 | 209 |
| enrofloxacin | 4,050 | 4,050 | 115 |
| marbofloxacin | 3,966 | 3,966 | 175 |
| oxacillin | 2,924 | 2,616 | 339 |
| telithromycin | 2,184 | 2,184 | 41 |
| Total | 24,650 | 24,333 | 2,437 |

The other accepted additions have 4,807 susceptible, 182 intermediate, and
16,907 absent categorical calls. An absent call is not inferred from the
measurement. These are submitted observations, not taxon-wide resistance
assertions, independent phenotype verification, or counts of unique isolates.
The table is before repeated-target consolidation.

The expanded assay review retains 213,144 groups on 40 structures and
quarantines 41,800. The 317 additional quarantines comprise 165 panel-format
conflicts, 146 MIC/disk-context conflicts, three unexpanded KB labels, and
three vendor conflicts. All retained rows have TaxIDs; 209,007 have assembly
links and 195,495 have strain labels. There are still 433 distinct TaxIDs.

Expanded candidate report:
`reports/ncbi_ast_drug_expanded_candidates_2026-10-03.tsv`, SHA-256
`456c68b9ca0885e0a2d9895327edc10734ea7ac0480a9f935d8757deedfe456b`.

The reviewed report at
`reports/ncbi_ast_drug_expanded_reviewed_2026-10-03/activity.tsv` has SHA-256
`bcac2fb84c9f7df5d78fab90f330738e31dcdb7b82bc3dfc7069a351edacc41a`.
The updated assay review has SHA-256
`460efca4824a3448bfa58034a33056f0924d681d9a07ee0b6f16a0ff85b31032`,
and the drug map has SHA-256
`8b224448e1b2107e40107c4fb99820230249ec1318e36b032bb60324e1948088`.
The original review files remain available at commit
`72658f33ab11e7877226631f28bb8c38c92ed9e9` for reproducing the earlier cohort.
Running an older cohort's commands against the expanded default map is not a
reproduction of those historical audits.

```bash
.venv/bin/python3 scripts/evaluate_ncbi_ast.py \
  --ast downloads/ncbi_ast_snapshot_2026-10-03/ast.tsv \
  --isolate-snapshot downloads/ncbi_ast_isolate_snapshot_2026-10-03 \
  --source-version ast-browser-sha256:ec6901ddfa0da41c0250875abc39b075d345c249cc39dbb17a998efaad2af184 \
  --source-retrieved-on 2026-10-03 \
  --drug-map curation/ncbi_ast_drug_map.tsv \
  --activity-report reports/ncbi_ast_drug_expanded_candidates_2026-10-03.tsv \
  --antibiotic-report reports/ncbi_ast_drug_expanded_names_2026-10-03.tsv

just review-ncbi-ast \
  --activity-report reports/ncbi_ast_drug_expanded_candidates_2026-10-03.tsv \
  --output-directory reports/ncbi_ast_drug_expanded_reviewed_2026-10-03
```

Issue [#1033](https://github.com/CultureBotAI/AntibioticMech/issues/1033) tracks
the expanded-cohort integration checks; old checksum-pinned audits are not
silently repurposed as evidence for the additions.

## Taxonomy and source multiplicity

Fresh EFetch retrievals for the expanded report returned the same 434 taxonomy
records and nine BioSamples as before, with byte-identical source XML. Their
new manifests pin the expanded report instead of claiming that the earlier
manifests reviewed it.

The full overlap audit reconstructs both the adopted CRyPTIC inventory and
the expanded AST report. All 213,144 accepted groups are outside the reported
Mycobacterium tuberculosis complex scope, with no taxon-label disagreement,
unresolved lineage, conflicting sample identity, or direct BioSample/BioProject
overlap. The conclusion remains conditional on reported identity and the
CRyPTIC release scope; it is not independent organism re-identification.

Source antibiograms confirm ten additional single results repeated under two
genome targets each: seven oxacillin, two cefotaxime, and one cephalothin.
The previous 52 decisions remain identical in full. The expanded review covers
62 such results, retaining the original antibiogram row numbers and all paired
genome contexts. Distinct measurements and assays are not collapsed together.
Updating review checksums changes the curation-evidence version, not the AST
source version or biological measurement.

The full source-reconstruction and closed-schema audit passes for all 213,082
resulting observations on 40 structures, a gain of 24,323 observations over
the previous 188,759-observation cohort. It accounts for every one of the
213,144 export groups exactly once, preserves all 124 paired genome contexts
and 18 distinct assemblies across nine affected BioSamples, and checks that
unrepeated rows, measurements, identifiers, and original evidence are unchanged
by consolidation. There are 2,429 explicit resistant calls among the added
observations after consolidating the eight duplicated resistant results.

The first attempt to apply the generated review file misplaced two insertions
among repeated JSON contexts. The audit rejected its group ordering despite
identical decision content. The committed file now matches the generated
review byte-for-byte, and the full audit was rerun successfully; no validation
was weakened to accommodate the patch.

| Expanded-cohort artifact | SHA-256 |
|---|---|
| Taxonomy XML | `0b2c5aaad4b05541aaa8282f8382ea45cf590ea289e8f43574aa790496169f26` |
| Taxonomy manifest | `0711c1aa064604b20e944409c3cbc9382db4879536efb379fd2942b7bcfe7577` |
| Full overlap audit | `b573afd9ecf06bcf1adc0f0648e68c4d59ee58d1433869f606b1fbf43a462ca1` |
| BioSample XML | `498ba42ee6acb179edc9b64f8cefd58a85fdf680e62610271c71b63476e7b6e8` |
| BioSample manifest | `0e1d447c44a5d8a96a1af9356a74b1b86e5674d9410bea5ea3653190b97e67ef` |
| Committed BioSample review | `4ca294f58d57e627753e033ab2d3ee29d7c54ea10111bd24b534ddde69f72fbb` |
| Full BioSample/schema audit | `cb25a962609f63d186adc2ef36ad6f44190ed65e631a1ae740431a568cb11c7f` |

```bash
just fetch-ncbi-ast-taxonomy \
  --activity-report reports/ncbi_ast_drug_expanded_reviewed_2026-10-03/activity.tsv \
  --output-directory downloads/ncbi_ast_drug_expanded_taxonomy_2026-10-03

just review-ncbi-ast-biosamples \
  --activity-report reports/ncbi_ast_drug_expanded_reviewed_2026-10-03/activity.tsv \
  --output-directory downloads/ncbi_ast_drug_expanded_biosamples_2026-10-03

just audit-ncbi-ast-overlap \
  --ast downloads/ncbi_ast_snapshot_2026-10-03/ast.tsv \
  --activity-report reports/ncbi_ast_drug_expanded_reviewed_2026-10-03/activity.tsv \
  --isolate-snapshot downloads/ncbi_ast_isolate_snapshot_2026-10-03 \
  --wgs downloads/cryptic_3.4.0/dedupe/WGS_SAMPLES.parquet \
  --assay-review curation/ncbi_ast_assay_review.json \
  --taxonomy-snapshot downloads/ncbi_ast_drug_expanded_taxonomy_2026-10-03 \
  --report reports/ncbi_ast_drug_expanded_overlap_2026-10-03.json

just audit-ncbi-ast-biosamples \
  --activity-report reports/ncbi_ast_drug_expanded_reviewed_2026-10-03/activity.tsv \
  --biosample-snapshot downloads/ncbi_ast_drug_expanded_biosamples_2026-10-03 \
  --report reports/ncbi_ast_drug_expanded_biosample_audit_2026-10-03.json
```

## Lossless evaluation inventory

The reviewed TSV is 116,223,537 bytes. The generated
`reports/ncbi_ast_drug_expanded_compressed_2026-10-03/activity.tsv.gz` is
8,924,250 bytes, SHA-256
`4f396c7843750066afb8225832ac6023305779a4bcd037940de8ff8d0149b4f2`.
Its expanded bytes exactly match the reviewed TSV checksum above; all 213,144
source groups survive. The accompanying inventory manifest has SHA-256
`015c6bc924f8ab455d5231482197d1a675aad21119857e482043eee76977339e`.
This is an ignored evaluation artifact, not an adopted production inventory.

```bash
.venv/bin/python3 scripts/ncbi_ast_inventory.py \
  --activity-report reports/ncbi_ast_drug_expanded_reviewed_2026-10-03/activity.tsv \
  --output-directory reports/ncbi_ast_drug_expanded_compressed_2026-10-03
```

## Validation and remaining gates

- 517 focused AST, inventory, provenance, and source-queue tests pass,
  including the 12 chemical-identity regressions added here.
- All 2,939 production records strictly validate and reproduce from their
  committed inputs. No generated record, schema, or public page changes.
- Lint, source-queue validation, and whitespace checks pass. Linux QC is
  required on the final PR head before merge.
- The expanded cohort now passes the full production merge/write/reload and
  rendered-publication audit, including complete downloads, unchanged reseeding
  and full-site local links. Representative desktop/mobile browser checks also
  pass for cefotaxime and cefovecin, including missing categorical calls. See
  [the expanded publication report](2026-10-03-ncbi-ast-expanded-publication.md)
  for exact artifacts, checksums, scope and reproduction commands.
- Source-terms resolution remains deferred, and adoption still requires source
  configuration, a committed inventory/manifest, and publication gates.
  Unmapped drug labels and quarantined assay contexts remain curation work.
