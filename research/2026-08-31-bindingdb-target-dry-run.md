# BindingDB-curated target evaluation

Date: 2026-08-31  
Issue: #103  
BindingDB release: 2026-09, updated 2026-08-30  
NCBI taxonomy snapshot: 2026-08-31

## Sources

- [BindingDB download page](https://www.bindingdb.org/rwd/bind/chemsearch/marvin/Download.jsp), specifically `BindingDB_BindingDB_Articles_202609_tsv.zip`, labeled “Only data curated from articles by BindingDB.” SHA-256: `1203194f366623ae9b4caee34f2477d412ebddbda267593df9d1d92d0c66fb74`; publisher MD5 `8c41a1fcf8b828d99070f4bca6bd7a86` was independently reproduced.
- [BindingDB TSV specification](https://www.bindingdb.org/rwd/bind/chemsearch/marvin/BindingDB-TSV-Format.pdf) for ligand, target, measurement, citation, curation-source, and protein-chain fields.
- [NCBI taxonomy dump](https://ftp.ncbi.nlm.nih.gov/pub/taxonomy/), `taxdmp.zip` retrieved 2026-08-31. SHA-256: `5b007816d5808387b577724b8da2d835ec7db0d5f5554035997c4019941f1944`.

The 2025 BindingDB database paper describes BindingDB-curated content as CC BY
4.0 while imported ChEMBL content retains ChEMBL's terms. Consequently, the
archive name alone is not accepted as row-level licence provenance.

## Reconciliation

| Gate/outcome | Rows | Meaning |
|---|---:|---|
| all rows | 93,712 | Curated-article archive population |
| exact BindingDB-curated source marker | 93,023 | Proven BindingDB-curated at row level |
| rejected ChEMBL source marker | 429 | Mixed-licence rows present in the nominally curated-only archive |
| rejected Taylor Research Group source marker | 260 | Not BindingDB literature curation |
| out of corpus structure scope | 92,324 | No reported full InChIKey in the current corpus |
| ambiguous corpus structure | 0 | No candidate key mapped to multiple corpus records |
| reported/computed key mismatch | 45 | BindingDB key did not equal the RDKit Standard InChIKey recomputed from SMILES |
| missing primary citation | 7 | Neither PMID nor Article DOI |
| missing quantitative measurement | 3 | None of Ki, IC50, Kd, or EC50 present |
| identity+citation+measurement candidates | 644 | Passed all pre-taxonomy gates |
| unresolved or ambiguous target taxon | 100 | Exact NCBI name resolution was not unique |
| non-microbial target | 367 | Outside Bacteria, Archaea, Fungi, and Viruses |
| accepted evaluation rows | 177 | 23 bacterial, 5 fungal, and 149 viral measurements |

The 177 rows cover 45 corpus structures and 95 unique
record/target-name/taxon combinations. Their measurement fields comprise 126
IC50, 31 EC50, 19 Ki, and 1 Kd value. These are deliberately reported by type:
IC50 and EC50 must not be silently recast as equilibrium binding constants, and
none of the four fields alone establishes organism-level antimicrobial
activity or a mode of action.

## Adversarial findings and write decision

The curated-only archive is not source-pure. It contains 429 rows explicitly
marked `ChEMBL` and 260 marked `Taylor Research Group, UCSD`; using the filename
as the licence filter would violate issue #103. The evaluator therefore rejects
every row whose marker is not exactly `Curated from the literature by
BindingDB`.

Exact identity is also not established merely because BindingDB supplies an
InChIKey: 45 in-scope rows disagree with the Standard InChIKey recomputed from
the row's own SMILES and are rejected. Connectivity-only, salt, protonation,
tautomer, and stereochemical near-matches never inherit a target measurement.

No claims are written. The current `MolecularTarget` model lacks an
assertion-level relation distinguishing direct binding from susceptibility or
resistance context (#93), and `EvidenceItem` has no fields for measurement
type, qualifier, numeric/text value, unit, assay, or BindingDB reaction-set ID.
Writing now would flatten quantitative measurements into generic target claims
and could make cellular EC50 rows look like direct binding evidence. A follow-up
schema issue, [#113](https://github.com/CultureBotAI/AntibioticMech/issues/113),
records those requirements. UniProt accessions in the evaluation
remain organism-specific examples only; they are not promoted to target IDs.
