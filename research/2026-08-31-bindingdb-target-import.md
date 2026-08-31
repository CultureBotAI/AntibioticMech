# BindingDB quantitative target import audit

Date: 2026-08-31

BindingDB release: 2026-09 (published 2026-08-30)

Scope: BindingDB-curated primary-article rows only; microbial and viral targets

## Outcome

The evaluated BindingDB lane is now an offline, reproducible source inventory
and corpus import. It contributes 177 quantitative measurements on 45 exact
corpus structures, grouped into 95 compound/target/taxon/relation assertions.
Every accepted measurement retains its reported value and qualifier, nM unit,
BindingDB reactant-set, monomer and assay identifiers, assay name and full assay
description, source release and retrieval date, primary PMID or DOI, target
organism and any source-supplied UniProt chain examples.

This import closes #113. It depends on the target-role model in #93 and does not
infer organism-level antimicrobial activity or mode of action from potency.

## Pinned inputs

| Input | Bytes | SHA-256 |
| --- | ---: | --- |
| `BindingDB_BindingDB_Articles_202609_tsv.zip` | 18,272,073 | `1203194f366623ae9b4caee34f2477d412ebddbda267593df9d1d92d0c66fb74` |
| `BindingDB_Assays_202609_tsv.zip` | 10,095,267 | `b9949b6271de7a3d2e4269498fffc9a5374b0e45d72202c4c347d798876b345e` |
| `BindingDB_rsid_eaids_202609_tsv.zip` | 7,541,165 | `0c967f8a34ab21d766a5e9ca327a02ad45970321f691816f1d27109ef79c7cf9` |
| `taxdmp-2026-08-31.zip` | 78,637,355 | `5b007816d5808387b577724b8da2d835ec7db0d5f5554035997c4019941f1944` |

The committed `data/raw/bindingdb_target_measurements.tsv` has 177 rows,
133,120 bytes, and SHA-256
`faccfe5634f467801aeb256e6560af09d193cdb53bdbf29dea195c9c0488c480`.
All URLs and hashes are also recorded in `data/raw/MANIFEST.yaml`.

## Admission pipeline

The extractor applies these gates in order:

1. Require `Curation/DataSource` to equal exactly
   `Curated from the literature by BindingDB`.
2. Join the reported full ligand InChIKey to exactly one corpus structure.
3. Recompute a Standard InChIKey from BindingDB's ligand SMILES with RDKit and
   require equality with the reported key.
4. Require an Article PMID or Article DOI; BindingDB's own entry DOI is not
   treated as primary evidence.
5. Require at least one Ki, IC50, Kd or EC50 value and parse its complete source
   text into a closed qualifier plus numeric value without discarding the text.
6. Resolve the target-organism name unambiguously in the pinned NCBI Taxonomy
   dump, normalize it to the scientific name, and require descent from Bacteria,
   Archaea, Fungi or Viruses.
7. Resolve the reactant-set ID to exactly one BindingDB EntryID_AssayID and
   require a non-empty assay description.

The so-called curated-only archive contains 689 rows whose row marker is not
BindingDB literature curation: 429 ChEMBL rows and 260 Taylor Research Group
rows. The exact marker gate rejects all of them.

## Counts

| Stage or result | Rows |
| --- | ---: |
| Archive rows | 93,712 |
| Exact BindingDB literature-curation marker | 93,023 |
| Rejected non-BindingDB marker | 689 |
| Out-of-scope exact structure | 92,324 |
| Reported/recomputed Standard InChIKey mismatch | 45 |
| Missing primary citation | 7 |
| Missing quantitative measurement | 3 |
| Identity/citation/measurement candidates | 644 |
| Nonmicrobial target | 367 |
| Unresolved or ambiguous target taxon | 100 |
| Accepted measurements | 177 |

Accepted taxonomy distribution: 149 Viruses, 23 Bacteria and 5 Fungi. No
Archaea row survived the other gates. All 177 accepted rows resolved to one
non-empty assay description, so the new assay gate rejected no otherwise
eligible row.

Measurement distribution: 126 IC50, 31 EC50, 19 Ki and 1 Kd.

## Target semantics

Only the Kd measurement is represented as `DIRECT_BINDING_TARGET`. Kd is a
dissociation constant and directly supports physical binding in this lane. Ki,
IC50 and EC50 can arise from enzyme, cell or pathway assays and therefore remain
`MEASURED_TARGET_ASSOCIATION`, even where the target name looks mechanistically
familiar. This prevents a potency number from being upgraded silently into a
physical-binding claim.

UniProt accessions remain organism-specific `protein_examples`; they are not
used as the assertion's target identity. A multi-chain target remains a
`PROTEIN_COMPLEX`, and each UniProt accession retains its chain role.

## Reproducibility and ownership

`scripts/extract_bindingdb_targets.py` recreates the committed inventory from
the four pinned archives. `scripts/seed_from_sources.py` owns only target items
whose source is `BINDINGDB`; a re-seed replaces that slice while retaining CARD
and curator-owned targets. `scripts/verify_corpus.py` compares the BindingDB
slice independently, making a hand edit or stale import visible. The rendered
record pages expose the measurement, assay context, source IDs and citation.

## Residual limitations

- The import does not independently review each article's methods or conclusions;
  it preserves BindingDB's literature curation and the article reference.
- A source organism on a target assay is not evidence of whole-organism
  susceptibility, clinical efficacy, selectivity or bactericidal action.
- Ki is intentionally not promoted to direct binding because the exported assay
  context is heterogeneous and Ki may be derived from functional inhibition.
- Rows that do not resolve exactly to the corpus, a unique microbial taxon and a
  unique non-empty assay remain excluded rather than guessed.
