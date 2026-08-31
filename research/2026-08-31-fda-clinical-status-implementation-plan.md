# Drugs@FDA + GSRS clinical-status implementation plan

Date: 2026-08-31
Issue: #105

## Decision

Use the official Drugs@FDA 12-table archive for regulatory facts and the
openFDA UNII/GSRS endpoints only for substance identity. Join Applications,
Products, MarketingStatus, MarketingStatus_Lookup, and approved original rows
from Submissions. Exclude tentative approvals and combination products.

`Discontinued` is retained as a product marketing status, not converted to
`WITHDRAWN`: FDA states that this bucket includes products that were never
marketed, stopped being marketed, are military/export-only, or had approval
withdrawn for non-safety reasons. The tables do not distinguish those cases.

## Identity contract

1. Exact normalized single-ingredient name → exactly one FDA UNII-list row.
2. UNII → GSRS chemical structure.
3. GSRS Standard InChIKey → exactly one AntibioticMech record.

Names only select a UNII candidate; the write decision is the exact structure
join. A salt, prodrug, stereochemical mismatch, or parent structure never
inherits another substance's approval.

## Work packages

1. Build a dry-run/archive extractor with cached GSRS batch responses and a
   compact, manifested clinical-status inventory.
2. Extend the schema with versioned, jurisdiction-specific regulatory
   assertions while retaining the coarse `clinical_status` enum.
3. Seed and reproduce the FDA-owned assertion slice without overwriting curator
   assertions.
4. Publish matched/excluded/ambiguous counts before applying writes.
5. Regenerate records/site/docs and pass `just qc`, then conduct an adversarial
   review of combination, tentative-approval, discontinued, salt, and prodrug
   handling.
