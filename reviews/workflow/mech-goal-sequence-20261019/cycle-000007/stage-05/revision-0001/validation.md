# Stage 5 Validation Report (`mech-goal-sequence-20261019`, Cycle 7, Stage 5)

## Executed Validation Gates and Command Provenance

1. **Native Writer Remediation and Transition Manifest Generation**
   - Curated `mode_of_action` and `PRIMARY_LITERATURE` `molecular_targets` on the 5 Cycle 7 Stage 1 natural products (`#1346`) and 6 `EXACT` folate-pathway inhibitors (`#1347`), updated [`curation/uniprot_protein_examples.yaml`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/uniprot_protein_examples.yaml) (`records=95`, `held_targets=125`, `sha256=0505726e3c220b6dff07caaecab79416d43133967b8ddb443d6abb7ea605b341`) and [`curation/uniprot_protein_examples_transition.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/uniprot_protein_examples_transition.json) (`sha256=476de2521b919db2a241950c58ec3fc2ea4aa178161f010ab7c5752c04fadb0a`), promoted all 14 `EXACT` ChEBI records (`neocarzinostatin`, `streptothricin-e`, `epoxomicin`, `benastatin-a`, `benastatin-b`, `tetarimycin-a`, `9-methylstreptimidone`, `7-deoxypactamycin`, `sulfadoxine`, `sulfasalazine`, `sulfisoxazole`, `dapsone`, `brodimoprim`, `tetroxoprim`) to `curation_status: REVIEWED` via `record_curation_event` and `write_validated_antibiotic`, updated [`curation/causal_graphs.yaml`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/causal_graphs.yaml) (`held_records` `count=69`, `sha256=46a7d741f502752e763f051382d6cf13c6764166d4bb4446aa95f61b31fec0a6`), and recorded [`curation/cycle7_stage5_review_remediation_transition.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/cycle7_stage5_review_remediation_transition.json) (`sha256=1a86212ece77e0acc225348e322b0b4b38d177722eeb38d26e209b1ea35d1d46`) (`BypassSandbox: true`, exit code `0`).

2. **Closed LinkML Schema and OAK Ontology Label Validation ([`scripts/validate_strict.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/validate_strict.py))**
   - Command (`BypassSandbox: true`): `.venv/bin/python scripts/validate_strict.py --out .temp/validate_strict_c7s5.tsv`
   - Exit Code: `0`
   - Literal Summary Output:
     ```text
     === validate-strict summary ===
       files scanned:      3105
       files with ERROR:   0
       total ERROR rows:   0
       TSV:                .temp/validate_strict_c7s5.tsv
     ```

3. **Full Corpus Seed Reproduction Check ([`scripts/verify_corpus.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/verify_corpus.py))**
   - Command (`BypassSandbox: false`): `.venv/bin/python scripts/verify_corpus.py`
   - Exit Code: `0`
   - Literal Output:
     ```text
       1 CARD cross-reference(s) refused as self-contradictory (see `just worklist --queue crossref-conflict`)
         ARO:3000337: CARD links ARO:3000337 (iclaprim) to CHEBI:31724 (Isoaminile citrate), but the names differ and the CAS numbers disagree (192314-93-5 vs 28416-66-2). Cross-reference not trusted for roles, structure or identity.
     records expected: 3105   on disk: 3105
     missing: 0   unexpected: 0   drifted fields: 0
     identifiers absent from PATHS.tsv: 0   stale lockfile rows: 0

     corpus reproduces exactly from data/raw/ plus curator inputs.
     ```

4. **Review-Readiness Queue Refresh ([`scripts/curation_worklist.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/curation_worklist.py))**
   - Refreshed [`curation/record_review_queue.tsv`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/record_review_queue.tsv) (`sha256=faf50ecaf2f7fa3be079f34a9e9953ce91e562b827982259eaadb5a3302dad88`): `2,946` unsigned items (`REVIEWED` count increased from `145` to `159`; `PROPOSED` count decreased from `106` to `98`; `SEEDED` count decreased from `2,854` to `2,848`).

5. **Chemical Structure Map and PaCMAP Corpus Map Refresh ([`data/embeddings/chemical-structure-map.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/chemical-structure-map.json), [`data/embeddings/corpus_map.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/corpus_map.json))**
   - Refreshed [`data/embeddings/chemical-structure-map.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/chemical-structure-map.json) (`input_hash=19b2d1e2893bf392b47dfbf6389c08a6287be59a570df74a459c8d0916f25dd6`) and [`data/embeddings/corpus_map.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/corpus_map.json) (`corpus_fingerprint=3fa4171847de7e3adf17792bb58046a9bc56fa3e222fae8f097320ae765aeee0`).
   - Embeddings Test Suite (`BypassSandbox: false`):
     - Command: `.venv/bin/python -m pytest -q tests/test_embeddings.py tests/test_corpus_integrity.py`
     - Exit Code: `0` (`37 passed`).

6. **README Statistics and Static Site Pages Synchronization ([`scripts/check_docs.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/check_docs.py), [`scripts/render_pages.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/render_pages.py), [`NEXT_TASKS.md`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/NEXT_TASKS.md))**
   - Updated [`NEXT_TASKS.md`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/NEXT_TASKS.md) (`506` records with target or resistance evidence; `94` populated `PRIMARY_LITERATURE` `MolecularTarget` entries with reviewed `UniProtKB` `protein_examples` and `125` `held_targets`).
   - Refresh Run (`BypassSandbox: true`, after `BypassSandbox: false` failed with `PermissionError` writing to `README.md` / `pages/`):
     - Command: `.venv/bin/python scripts/check_docs.py --write` and `.venv/bin/python scripts/render_pages.py`
     - Exit Code: `0`
     - Literal Output:
       ```text
       README statistics refreshed.
       rendered 3105 compound pages, 7 classes -> /Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/pages
       ```
   - Static Site Pages Check (`BypassSandbox: false`):
     - Command: `.venv/bin/python scripts/render_pages.py --check`
     - Exit Code: `0`
     - Literal Output: `pages/ is in step with the corpus`

7. **Native Structured Review Bundle Save, Validate, and Append-Only Check ([`scripts/record_review.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/record_review.py))**
   - Save and Check Bundle (`BypassSandbox: true`, after `BypassSandbox: false` failed with `PermissionError: [Errno 1] Operation not permitted: 'Users'` in `scripts/record_review.py:_directory`):
     - Command: `.venv/bin/python scripts/record_review.py save --content .temp/cycle7_stage5_remediated_review_input.yaml && .venv/bin/python scripts/record_review.py check`
     - Exit Code: `0`
     - Literal Output:
       ```text
       topClass is deprecated - use top_class
       {"review": "/Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/reviews/structured/20261108T235000Z-cycle7-stage5-remediated-records-review/review.yaml", "markdown": "/Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/reviews/structured/20261108T235000Z-cycle7-stage5-remediated-records-review/review.md"}
       topClass is deprecated - use top_class
       {
         "repository": "culturebotai/AntibioticMech",
         "valid_reviews": 24,
         "coverage": "declared_scopes_only"
       }
       ```

8. **Pytest and Ruff Validation Suites**
   - UniProt Protein Examples & Causal Graphs Curation Suites (`BypassSandbox: false`):
     - Command: `.venv/bin/python -m pytest -q tests/test_causal_graphs_curation.py tests/test_uniprot_protein_examples.py`
     - Exit Code: `0` (`188 passed`).
   - Record Review Contract Suite (`BypassSandbox: true`):
     - Command: `.venv/bin/python -m pytest -q tests/test_record_review_contract.py`
     - Exit Code: `0` (`4 passed`).
   - Ruff Linter Check (`BypassSandbox: false`):
     - Command: `.venv/bin/ruff check .`
     - Exit Code: `0` (`All checks passed!`).
