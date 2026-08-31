# Reuse-terms audit for measured antimicrobial data

Date: 2026-08-31  
Issue: #106

## Outcome

No measured activity or antiviral-resistance data were imported. BacDive now
has a visible CC BY 4.0 site licence compatible with this corpus, but a scoped
confirmation for API/bulk susceptibility rows is still prudent. CO-ADD's own
website terms are restrictive and block systematic redistribution. BV-BRC and
Stanford HIVDB expose useful data and software, but no verified data-reuse grant
covering the requested rows was found.

| Source | Exact data scope | Verified public position | Corpus decision |
|---|---|---|---|
| BV-BRC | `genome_amr` / AMR phenotype rows where `evidence` is exactly `Laboratory Method`; exclude computational prediction/classifier rows | Website, privacy policy, docs, and API-code licence do not state data redistribution rights | UNVERIFIED; request drafted; no import |
| BacDive | Strain-level antibiotic susceptibility fields exposed by pages/API/bulk access | Current BacDive footer links its Copyright & License statement directly to CC BY 4.0 | Compatible with attribution; scope confirmation drafted; no import in #106 |
| CO-ADD | Independent machine-readable screening results with compound identity, organism/strain, assay, concentration/MIC, units, medium, detection method, and citation | Site material is personal/non-commercial only; systematic download/storage and reproduction require written permission. ChEMBL copy is CC BY-SA 3.0 | BLOCKED absent a separate grant/distribution |
| Stanford HIVDB | Download/API resistance mutations, drug-susceptibility interpretation/evidence, version and references | No database-data reuse grant found; CMS GPL is not assumed to license database contents | UNVERIFIED; request drafted; no import |

## Evidence inspected

### BV-BRC

- [BV-BRC home and support contact](https://www.bv-brc.org/) identifies
  `help@bv-brc.org` but contains no data licence. Retrieved-page SHA-256:
  `b1f12ee501ef593207afc6e6112cf4281adfef6c6c95f1c7cc94541eca10da08`.
- [BV-BRC privacy policy](https://www.bv-brc.org/privacy-policy) governs
  personal information, not dataset reuse. SHA-256:
  `93624168368dc815df55c00c43977ed466d54190e798d02a1351d6bf5527556a`.
- The official `BV-BRC/BV-BRC-API` repository is MIT-licensed. That licence
  covers API software; it is not evidence that returned third-party or curated
  data may be modified and commercially redistributed.

### BacDive

- [BacDive](https://bacdive.dsmz.de/) displays a global “Copyright & License”
  footer linked to [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
  Home-page SHA-256:
  `e1a69e118bc57f05f3da071a22da91f69e59d8732718ae55a1c8ded0e44ab123`.
- [BacDive contact form](https://bacdive.dsmz.de/contact) provides explicit
  Content and Web services categories for a scoped confirmation. SHA-256:
  `39bbded9ff40585476a4607eb27de1c2fa3c032b5173c2b7eaa16f5a217557da`.

### CO-ADD

- [CO-ADD Privacy & Copyrights](https://www.co-add.org/?q=content/privacy-copyright)
  reserves site/material rights, permits copies only for personal,
  non-commercial purposes, prohibits systematic download/retrieval/storage,
  and requires prior written permission for reproduction or transmission.
  Retrieved-page SHA-256:
  `8a4a48b73adca5b43c75844a8ea47a836c5bd4bc41ac4da7174863f77d6c3d8a`.
- The same page directs copyright enquiries to `info@co-add.org`. The public
  contact page supplies that address and a University of Queensland contact.
- CO-ADD rows distributed through ChEMBL remain under ChEMBL's CC BY-SA 3.0
  terms; the public CO-ADD pages do not identify a separately licensed bulk
  dataset.

### Stanford HIVDB

- [Stanford HIVDB](https://hivdb.stanford.edu/) is a JavaScript shell and does
  not expose database reuse terms in its HTML. SHA-256:
  `de1ff86d0b3083a044cbda2d5655a961c4bf3d58bb064bde9e8f3db34d349b50`.
- The official `hivdb/hivdb-cms` repository contains the public site's static
  content under GPL-3.0 and names `hivdbteam@lists.stanford.edu` as a support
  contact. GPL licensing of CMS code/content is not treated as a licence to
  redistribute the resistance database.

## Legal/semantic guardrails

- Free access, an API, and an open-source client/server do not establish a data
  licence.
- A response must cover modification and commercial redistribution, not only
  research use or citation.
- Source-specific attribution and version/retrieval requirements must remain
  attached to imported observations.
- BV-BRC predictions must never be mislabeled laboratory measurements.
- A CO-ADD grant must apply to an independent distribution; it cannot erase
  ChEMBL's share-alike terms from the ChEMBL copy.
- HIVDB interpretations or mutation evidence must not be inferred to apply to
  non-HIV viruses.

The ready-to-send requests are archived separately. They are drafts, not proof
of contact or permission; `curation/source_queue.tsv` records `response: none`.
