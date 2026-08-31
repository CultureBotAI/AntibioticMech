#!/usr/bin/env python3
"""Text-embed every AntibioticRecord into a dense vector with a LOCAL model.

WHAT THIS EMBEDS, AND WHAT IT DOES NOT. These records are chemical structures,
but this is a *text* embedding: it captures what the corpus SAYS about a
compound — its name, class, structural family, definition, mechanism and the
roles its sources assert — not its chemistry. Two structural analogues with
different annotations land far apart; two unrelated scaffolds described the same
way land together. That is the right tool for "find records that talk about the
same thing" and the wrong one for "find similar molecules". A chemical map needs
fingerprints or a molecular language model, and is a separate artifact.

FIELDS DELIBERATELY EXCLUDED, with reasons — the include/exclude list is the
substance of a text embedding, so it is written down rather than implied:

  smiles / standard_inchi / standard_inchi_key
      A sentence embedder tokenizes these as gibberish of a length that would
      dominate every document. They carry the chemistry this model cannot read.
  molecular_formula / masses / charge
      Numeric; no semantic content for a text model.
  mode_of_action_notes
      The seeded note is near-identical across hundreds of records by design
      (it states provenance and a caveat). Including it would manufacture one
      enormous false cluster of "records that carry a seeded mechanism" and
      drown the real signal. The mechanism VALUE is included; its boilerplate
      is not.
  curation_status / grounding_status / source_version
      Facts about our process, not about the compound.

Output (data/embeddings/, vectors gitignored — large and rebuildable):
  vectors.f16.npy   float16 [N, dim], L2-normalized, row i <-> ids[i]
  ids.json          the N record identifiers, in row order
  meta.json         {model, dim, count, normalized, text_mode}

  just embed                          # whole corpus (~2,900 records, seconds)
  python3 scripts/embed_records.py --limit 20 --model BAAI/bge-large-en-v1.5
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_DIR = REPO_ROOT / "data" / "antibiotics"
ROLE_NAMES = REPO_ROOT / "data" / "raw" / "chebi_role_names.tsv"
OUT = REPO_ROOT / "data" / "embeddings"

# Fields whose presence in a document would be noise or leakage. Named here so
# the audit is one list rather than an argument reconstructed from the code.
EXCLUDED = ("smiles", "standard_inchi", "standard_inchi_key", "molecular_formula",
            "average_mass", "monoisotopic_mass", "charge", "mode_of_action_notes",
            "curation_status", "grounding_status", "source_version")


def role_names() -> dict[str, str]:
    """CHEBI role CURIE -> its label, so a document reads 'protein synthesis
    inhibitor' rather than 'CHEBI:48001'. The ids still go in as grounding
    tokens; the names are what carries meaning to a text model."""
    if not ROLE_NAMES.exists():
        return {}
    with ROLE_NAMES.open(encoding="utf-8") as fh:
        return {r["role_id"]: r.get("name", "") for r in csv.DictReader(fh, delimiter="\t")}


def humanize(value: str) -> str:
    """ANTIMICROBIAL_UNSPECIFIED -> 'antimicrobial unspecified'."""
    return (value or "").replace("_", " ").lower()


def build_document(record: dict, names: dict[str, str]) -> str:
    """One document per record, ordered MOST DISCRIMINATIVE FIRST.

    The model's window is 512 tokens and 94 of 2,923 documents exceed it, so the
    tail of those is silently dropped. Order therefore decides what survives.
    Mechanism, roles and targets — short, and the fields that actually separate
    one antibiotic from another — go before the definition; synonyms and
    identifiers, which are verbose and weakly semantic, go last and are the
    first things truncation takes. An earlier ordering put synonyms ahead of
    mechanism, so vancomycin (1,065 tokens) kept a long list of trade names and
    lost its resistance determinants.
    """
    parts: list[str] = [str(record.get("label") or record.get("identifier"))]

    klass = humanize(record.get("antimicrobial_class", ""))
    if klass:
        parts.append(f"{klass} agent")
    if record.get("structural_class"):
        parts.append(str(record["structural_class"]))

    # The mechanism VALUE and its scope, never the boilerplate note.
    if record.get("mode_of_action"):
        moa = humanize(record["mode_of_action"])
        scope = humanize(record.get("mode_of_action_target_scope", ""))
        parts.append(f"mechanism: {moa}" + (f" ({scope})" if scope else ""))

    roles = [names.get(r, "") for r in (record.get("activity_roles") or [])]
    roles = [r for r in roles if r]
    if roles:
        parts.append("roles: " + ", ".join(roles[:10]))

    targets = [str(t.get("label")) for t in (record.get("molecular_targets") or [])
               if t.get("label")]
    if targets:
        parts.append("targets: " + ", ".join(targets[:6]))
    resistance = [str(t.get("label")) for t in (record.get("resistance_mechanisms") or [])
                  if t.get("label")]
    if resistance:
        parts.append("resistance: " + ", ".join(resistance[:6]))

    if record.get("definition"):
        parts.append(str(record["definition"]))

    synonyms = [str(s.get("synonym_text")) for s in (record.get("synonyms") or [])
                if s.get("synonym_text")]
    if synonyms:
        parts.append("also known as " + ", ".join(synonyms[:6]))

    # Identifiers are opaque one at a time, but their SHARED tokens cluster
    # records from the same ChEBI subtree or the same ARO drug class, which is
    # real structure rather than noise. Last: weakest signal per token, so they
    # are what truncation should take first.
    ground = [str(record.get("identifier"))]
    ground += [str(p) for p in (record.get("parent_compounds") or [])]
    ground += [str(x) for x in (record.get("xrefs") or [])]
    ground = list(dict.fromkeys(g for g in ground if g))[:12]
    parts.append("identifiers: " + ", ".join(ground))

    # Strip a trailing period before joining: ChEBI definitions end with one and
    # the join would otherwise produce ".." mid-document.
    return ". ".join(p.rstrip().rstrip(".") for p in parts if p and p.strip())


def corpus_fingerprint(docs: list[str]) -> str:
    """A hash of the embedded DOCUMENTS, not of the record files.

    Vectors and the map derive from these strings, so this is what decides
    whether a committed map still describes the corpus. It is recomputed by
    `tests/test_embeddings.py` in pure python — no torch — which is the only
    reason staleness is detectable in CI at all. A corpus edit that does not
    change any embedded field (a curation_status flip, say) correctly leaves it
    alone; one that changes a definition or a mechanism does not.
    """
    return hashlib.sha256("\x1f".join(docs).encode("utf-8")).hexdigest()[:16]


def load_corpus() -> tuple[list[str], list[str], list[dict]]:
    """(ids, documents, light metadata) in a stable identifier order."""
    names = role_names()
    rows = []
    for path in sorted(CORPUS_DIR.rglob("*.yaml")):
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(record, dict) or not record.get("identifier"):
            continue
        rows.append(record)
    rows.sort(key=lambda r: str(r["identifier"]))
    ids = [str(r["identifier"]) for r in rows]
    docs = [build_document(r, names) for r in rows]
    meta = [{"id": str(r["identifier"]), "label": r.get("label"),
             "class": r.get("antimicrobial_class"),
             "mode_of_action": r.get("mode_of_action")} for r in rows]
    return ids, docs, meta


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", default="BAAI/bge-large-en-v1.5")
    ap.add_argument("--batch", type=int, default=64)
    ap.add_argument("--limit", type=int, default=0, help="embed only the first N (canary)")
    ap.add_argument("--device", default=None, help="mps|cpu|cuda (auto if unset)")
    ap.add_argument("--dry-run", action="store_true",
                    help="print the documents that WOULD be embedded and stop")
    args = ap.parse_args()

    ids, docs, meta = load_corpus()
    if not ids:
        print("no records found under data/antibiotics/", file=sys.stderr)
        return 2
    if args.limit:
        ids, docs, meta = ids[:args.limit], docs[:args.limit], meta[:args.limit]

    if args.dry_run:
        print(f"{len(ids):,} records would be embedded with {args.model}\n")
        for i, d in zip(ids[:3], docs[:3], strict=True):
            print(f"--- {i} ---\n{d}\n")
        lengths = [len(d) for d in docs]
        print(f"document chars: min {min(lengths)}  median "
              f"{sorted(lengths)[len(lengths) // 2]}  max {max(lengths)}")
        print("\n--dry-run: nothing written.")
        return 0

    import numpy as np
    import torch
    from sentence_transformers import SentenceTransformer

    device = args.device or ("mps" if torch.backends.mps.is_available()
                             else "cuda" if torch.cuda.is_available() else "cpu")
    print(f"{len(ids):,} records -> embedding with {args.model} on {device}")
    model = SentenceTransformer(args.model, device=device)
    vectors = model.encode(docs, batch_size=args.batch, convert_to_numpy=True,
                           normalize_embeddings=True, show_progress_bar=True)

    OUT.mkdir(parents=True, exist_ok=True)
    np.save(OUT / "vectors.f16.npy", vectors.astype(np.float16))
    (OUT / "ids.json").write_text(json.dumps(ids), encoding="utf-8")
    (OUT / "records.json").write_text(json.dumps(meta), encoding="utf-8")
    (OUT / "meta.json").write_text(json.dumps({
        "model": args.model, "dim": int(vectors.shape[1]), "count": len(ids),
        "normalized": True, "excluded_fields": list(EXCLUDED),
        "corpus_fingerprint": corpus_fingerprint(docs),
    }, indent=2), encoding="utf-8")
    print(f"wrote {vectors.shape[0]:,} x {vectors.shape[1]} vectors to "
          f"{OUT.relative_to(REPO_ROOT)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
