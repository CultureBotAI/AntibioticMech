# Drugs@FDA + GSRS clinical-status import audit

Date: 2026-08-31  
Issue: #105  
Drugs@FDA snapshot: 2026-08-28  
FDA UNII / GSRS snapshot: 2026-08-31

## Sources and captured artifacts

- [Drugs@FDA data files](https://www.fda.gov/drugs/drug-approvals-and-databases/drugsfda-data-files): official application, product, submission, and marketing-status tables. Archive SHA-256: `2e639056285235b63b4071dfb90f4f4f505a19f66d1f6b790b03e3b7bce9e143`.
- [openFDA UNII download](https://open.fda.gov/data/downloads/): exact normalized ingredient-name to UNII candidate selection. Archive SHA-256: `edb1c477e0ac90a7b6fc440f5666ab7450b7f912d832a728c813488cdf1508bf`.
- [FDA GSRS](https://gsrs.ncats.nih.gov/): versioned substance structures retrieved in batched UNII queries. Compact cache SHA-256: `504ea6edce6e242a6b21ffa8293398fcb6006c2765632292aafcab683c1f4b1f`.

The archive bytes, versions, retrieval metadata, compact inventory, and hashes
are recorded in `data/raw/MANIFEST.yaml`. GSRS is identity evidence only;
regulatory assertions originate solely in Drugs@FDA.

## Pre-write accounting

| Outcome | Product rows | Interpretation |
|---|---:|---|
| all Drugs@FDA products | 51,714 | Starting population |
| excluded combinations | 5,988 | More than one active ingredient cannot map to one structure record |
| excluded without an approved original submission | 4,468 | No `ORIG` submission with status `AP` |
| excluded tentative approvals | 72 | Tentative approval is not final approval |
| rejected without one exact UNII name | 884 | Name matching may select candidates but may not establish identity |
| rejected without a GSRS chemical structure | 2,366 | No structure means no defensible corpus join |
| ambiguous connectivity-only match | 155 | Salt, stereochemical, or protonation mismatch; not written |
| out of current corpus scope | 34,078 | Valid GSRS structure but no corpus match |
| exact matched products | 3,703 | Full Standard InChIKey maps to exactly one corpus record |

The 3,703 accepted product rows cover 211 corpus structures. Their preserved
marketing states are 1,941 prescription, 48 over-the-counter, and 1,714
discontinued products; 1,989 are currently marketed under the deliberately
narrow prescription/OTC rule.

## Semantics and adversarial review

An accepted row says that an FDA application had an approved original
submission for the product's single ingredient. It does not say that the
product is currently sold, safe for every use, or approved in another
jurisdiction. FDA's `Discontinued` marketing bucket includes several histories
and is not sufficient evidence that approval itself was withdrawn. Therefore:

- every imported assertion is `APPROVED` and jurisdiction-scoped to `US-FDA`;
- `Discontinued` remains a separate product marketing status with
  `currently_marketed: false`;
- no `WITHDRAWN` assertion is inferred;
- salts, prodrugs, stereoisomers, and parent compounds do not inherit status;
- combination products and tentative approvals remain excluded.

The importer joins an exact normalized single-ingredient name to exactly one
UNII, obtains that UNII's GSRS chemical structure, computes its Standard
InChIKey with RDKit, and requires a one-to-one full-key corpus match. The name
is candidate-selection evidence, never the final write criterion.

## Reproducibility result

The compact committed inventory contains 3,703 rows and has SHA-256
`a6952f85426afa53c5704c588681a078e599ce245bf18f7c9dd390d70e7bb16c`.
The seeder owns only assertions marked `DRUGS_AT_FDA`; curator-authored
assertions survive re-seeding. Corpus verification reconstructs and compares
that source-owned slice, and regression tests enforce the counts, provenance,
combination/tentative exclusions, marketing-state mapping, and the
discontinued-not-withdrawn rule. Each assertion carries the Drugs@FDA archive
version and retrieval date separately from the UNII snapshot, GSRS record
version, and GSRS retrieval date.
