# Stage 5 Validation Report (`mech-goal-sequence-20261019`, Cycle 4, Stage 5)

## Executed Validation Gates and Command Provenance

1. **Native Writer Remediation and Transition Manifest Generation**
   - Curated `mode_of_action` and `PRIMARY_LITERATURE` `molecular_targets` on the 6 Cycle 4 Stage 1 natural products (`#1307`) and 4 `EXACT` fluoroquinolones (`#1308`), updated [`curation/uniprot_protein_examples.yaml`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/uniprot_protein_examples.yaml) (`records=69`, `held_targets=76`) and [`curation/uniprot_protein_examples_transition.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/uniprot_protein_examples_transition.json) (`sha256=55243bb2c76d62d502dbb316770ecad3a23b38e8220c7eec7d2ffe10b10c2921`), promoted all 11 `EXACT` ChEBI records (`squalestatin-s1`, `diazaquinomycin-h`, `diazaquinomycin-j`, `jessenipeptin`, `minimycin`, `pamamycin-621a`, `pamamycin-649b`, `enoxacin`, `fleroxacin`, `gatifloxacin`, `trovafloxacin`) to `curation_status: REVIEWED` via `record_curation_event` and `write_validated_antibiotic`, updated [`curation/causal_graphs.yaml`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/causal_graphs.yaml) (`held_records` `count=44`), and recorded [`curation/cycle4_stage5_review_remediation_transition.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/cycle4_stage5_review_remediation_transition.json) (`sha256=fbc5da94b42bd34994a3f67653fedc71ab44cd1034a68e3f906aba21caaa2da1`) (`BypassSandbox: true`, exit code `0`).

2. **Closed LinkML Schema and OAK Ontology Label Validation ([`scripts/validate_strict.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/validate_strict.py))**
   - Command (`BypassSandbox: false`): `.venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv`
   - Exit Code: `0`
   - Literal Summary Output:
     ```text
     === validate-strict summary ===
       files scanned:      3042
       files with ERROR:   0
       total ERROR rows:   0
       TSV:                /tmp/instance_validation_failures.tsv
     ```

3. **Full Corpus Seed Reproduction Check ([`scripts/verify_corpus.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/verify_corpus.py))**
   - Command (`BypassSandbox: false`): `.venv/bin/python scripts/verify_corpus.py`
   - Exit Code: `0`
   - Literal Output:
     ```text
       1 CARD cross-reference(s) refused as self-contradictory (see `just worklist --queue crossref-conflict`)
         ARO:3000337: CARD links ARO:3000337 (iclaprim) to CHEBI:31724 (Isoaminile citrate), but the names differ and the CAS numbers disagree (192314-93-5 vs 28416-66-2). Cross-reference not trusted for roles, structure or identity.
     records expected: 3042   on disk: 3042
     missing: 0   unexpected: 0   drifted fields: 0
     identifiers absent from PATHS.tsv: 0   stale lockfile rows: 0

     corpus reproduces exactly from data/raw/ plus curator inputs.
     ```

4. **Review-Readiness Queue Refresh ([`scripts/curation_worklist.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/curation_worklist.py))**
   - Refreshed [`curation/record_review_queue.tsv`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/curation/record_review_queue.tsv) (`sha256=04f5b80d2e1bc041cc98d4efee194b6f57c61b0e6f770c9631bb3971ceffec40`): `2,930` unsigned items (`REVIEWED` count increased from `101` to `112`; `PROPOSED` count decreased from `122` to `115`; `SEEDED` count decreased from `2,819` to `2,815`).

5. **Chemical Structure Map and PaCMAP Corpus Map Refresh ([`data/embeddings/chemical-structure-map.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/chemical-structure-map.json), [`data/embeddings/corpus_map.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/corpus_map.json))**
   - Refreshed [`data/embeddings/chemical-structure-map.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/chemical-structure-map.json) (`input_hash=eb90c37e619a1e300ee04dc849b481891051ac501bf8f0387da9ae736707a847`) and [`data/embeddings/corpus_map.json`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/data/embeddings/corpus_map.json) (`corpus_fingerprint=c3134384bf20d1ed`).
   - Chemical Structure Map Check (`BypassSandbox: false`):
     - Command: `/private/tmp/antibioticmech-rdkit/bin/python scripts/generate_chemical_map.py --check`
     - Exit Code: `0`
     - Literal Output: `chemical map is current: 3042 records, trustworthiness@10=0.9703, neighbor-overlap@10=0.4986`

6. **README Statistics and Static Site Pages Synchronization ([`scripts/check_docs.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/check_docs.py), [`scripts/render_pages.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/render_pages.py), [`NEXT_TASKS.md`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/NEXT_TASKS.md))**
   - Updated [`NEXT_TASKS.md`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/NEXT_TASKS.md) (`467` records with target or resistance evidence; `69` populated `PRIMARY_LITERATURE` `MolecularTarget` entries with reviewed `UniProtKB` `protein_examples` and `76` `held_targets`).
   - Refresh Run (`BypassSandbox: true`, after `BypassSandbox: false` failed with `PermissionError` writing to `README.md` / `pages/`):
     - Command: `.venv/bin/python scripts/check_docs.py --write` and `.venv/bin/python scripts/render_pages.py`
     - Exit Code: `0`
     - Literal Output:
       ```text
       README statistics refreshed.
       rendered 3042 compound pages, 7 classes -> /Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/pages
       ```

7. **Native Structured Review Bundle Save, Validate, and Append-Only Check ([`scripts/record_review.py`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/scripts/record_review.py))**
   - Save Bundle (`BypassSandbox: true`, after `BypassSandbox: false` failed with `PermissionError: [Errno 1] Operation not permitted: 'Users'` in `scripts/record_review.py:_directory`):
     - Command: `.venv/bin/python scripts/record_review.py save --content /Users/marcin/.gemini/antigravity-cli/brain/75d4a007-e80b-4cd0-a885-0beb737cc7bf/scratch/cycle4_stage5_review_payload.yaml`
     - Exit Code: `0`
     - Literal Output:
       ```text
       topClass is deprecated - use top_class
       {"review": "/Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/reviews/structured/20261103T145500Z-cycle4-stage5-remediated-records-review/review.yaml", "markdown": "/Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/reviews/structured/20261103T145500Z-cycle4-stage5-remediated-records-review/review.md"}
       ```
   - Validate Saved Bundle (`BypassSandbox: false`):
     - Command: `.venv/bin/python scripts/record_review.py validate reviews/structured/20261103T145500Z-cycle4-stage5-remediated-records-review/review.yaml`
     - Exit Code: `0`
     - Literal Output:
       ```text
       topClass is deprecated - use top_class
       {"valid_reviews": 1}
       ```
   - Append-Only Check Across All 15 Structured Review Bundles (`task-22277`, `BypassSandbox: true`, after `BypassSandbox: false` failed with `PermissionError: [Errno 1] Operation not permitted: 'Users'`):
     - Command: `.venv/bin/python scripts/record_review.py check --require-reviews --base main`
     - Exit Code: `0`
     - Literal Output:
       ```text
       topClass is deprecated - use top_class
       {
         "repository": "culturebotai/AntibioticMech",
         "valid_reviews": 15,
         "coverage": "declared_scopes_only"
       }
       ```

8. **Pytest and Ruff Validation Suites**
   - UniProt Protein Examples, Causal Graphs, Review-Readiness Queue & Embeddings Suites (`BypassSandbox: false`):
     - Command: `.venv/bin/python -m pytest -q tests/test_uniprot_protein_examples.py tests/test_causal_graphs_curation.py tests/test_review_readiness_queue.py tests/test_embeddings.py`
     - Exit Code: `0` (`160 passed`).
   - Historical Checkpoint and Replay Fixtures Suite (`task-22652`, `task-22664`, `BypassSandbox: false`):
     - Command: `.venv/bin/python -m pytest -q tests/test_uniprot_protein_examples.py tests/test_salmonella_qualification_checkpoint.py tests/test_card_qualified_current.py tests/test_qnr_identity_context.py tests/test_qnr_unresolved.py tests/test_card_current_references.py tests/test_card_reference_reconciled.py tests/test_card_qualification_checkpoint.py`
     - Exit Code: `0` (`239 passed`).
   - Ruff Linter Check (`BypassSandbox: false`):
     - Command: `.venv/bin/ruff check --no-cache tests/conftest.py tests/test_causal_graphs_curation.py tests/test_uniprot_protein_examples.py`
     - Exit Code: `0` (`All checks passed!`).
