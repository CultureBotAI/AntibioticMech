# Semantic text map inputs

`just text-map-inputs` validates a read-only preview of the full YAML corpus.
`just text-map-inputs --limit 10 --output /tmp/antibioticmech-canary.jsonl` exports an
explicit subset; `just text-map-inputs --output /tmp/antibioticmech-full.jsonl` exports
the full corpus. Repeated `--record data/antibiotics/...yaml` selects named records.
The JSON summary states full/subset scope, record count, adapter version and
SHA-256 of the exact JSONL bytes. A failed export preserves any prior output.

Each line contains identifier, label, category, page, source_path, text,
text_sha256 and adapter_version. Paths and identifiers are checked, files are
indexed on disk and documents are emitted one at a time in stable path order.
The adapter does not load models, reuse vector caches, or change corpus records.

The text uses the existing domain-specific `embed_records.py` representation.
It preserves meaningful fields and the documented exclusion of curation process
metadata and raw chemical/protein sequences. Page links follow the current site
renderer and point at individual records. The shared fleet runtime will consume
this input to generate pinned BGE/PaCMAP artifacts after governance integration;
the adapter alone does not publish a map or certify old cache provenance.

Site publication is explicitly disabled in `conf/text_map.yaml` until the shared
runtime and a verified full-corpus bundle are available. When enabled, `just render`
exports fresh full inputs and verifies the pinned BGE encoder and actual PaCMAP
projection before changing the existing site. It stages the bundle into
`pages/text-map/` and adds a Semantic text map navigation link. A missing, stale or
invalid enabled bundle fails the build. Existing specialty maps remain available.
Each row's page is relative to `pages/`: from the deployed `pages/text-map/` URL,
`../` plus that page resolves to the existing record URL.

When enabled, the pinned shared BGE map is the primary text-map navigation target.
Historical full-description/definition-only text coordinates are explicitly legacy
views: their missing model revision and complete input identity are not backfilled
or inferred from a current cache. Chemical and protein-feature maps remain
separate specialty views with their own representations.
