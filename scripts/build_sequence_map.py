#!/usr/bin/env python3
"""Build 2-D ESM-2 protein sequence embedding map for AntibioticMech.

Extracts all UniProtKB proteins referenced across AntibioticMech records,
joins with the cross-Mech UniProt sequence and inventory catalogs in
ProteinTraitsMech, embeds any uncached sequences with
facebook/esm2_t33_650M_UR50D (1,022-aa windows, 256-aa overlap, final-layer
residue mean excluding CLS/EOS/padding), mean-centres and L2-normalises the
1,280-D vectors, projects to 2-D with PaCMAP (n_neighbors=10, init="pca",
random_state=42), and writes data/embeddings/sequence_map.json.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CORPUS_DIR = REPO_ROOT / "data" / "antibiotics"
OUT_PATH = REPO_ROOT / "data" / "embeddings" / "sequence_map.json"

PTM_ROOT = REPO_ROOT.parent / "ProteinTraitsMech"
CROSS_MECH_DIR = PTM_ROOT / "data" / "cross_mech"
PTM_ESM2_DIR = PTM_ROOT / "data" / "embeddings" / "esm2"
SHARED_CACHE_DIR = Path("/tmp/cross-mech-esm2-cache")

MECH_KEY = "antibioticmech"
GROUP_LABEL = "Antimicrobial class"

MODEL = "facebook/esm2_t33_650M_UR50D"
REVISION = "08e4846e537177426273712802403f7ba8261b6c"
MAX_RESIDUES = 1022
OVERLAP = 256
VALID_SEQUENCE = re.compile(r"^[A-Z]+$")

CLASS_LABEL = {
    "antibacterial": "Antibacterial",
    "antimycobacterial": "Antimycobacterial",
    "antifungal": "Antifungal",
    "antiprotozoal": "Antiprotozoal",
    "biocide": "Biocide",
    "unspecified": "Unspecified",
}

ROLE_ORDER = ("TARGET", "EXAMPLE", "GRAPH_NODE", "REFERENCE")
ROLE_LABELS = {
    "TARGET": "Molecular target",
    "EXAMPLE": "Resistance protein",
    "GRAPH_NODE": "Causal graph node",
    "REFERENCE": "Text / evidence reference",
}

LENGTH_BINS = ("<= 200 aa", "201-500 aa", "501-1,022 aa", "> 1,022 aa")


def length_bin(n: int) -> str:
    if n <= 200:
        return LENGTH_BINS[0]
    if n <= 500:
        return LENGTH_BINS[1]
    if n <= 1022:
        return LENGTH_BINS[2]
    return LENGTH_BINS[3]


def sha(seq: str) -> str:
    return hashlib.sha256(seq.encode("ascii")).hexdigest()


def cache_key(model: str, revision: str, dtype: str) -> str:
    return hashlib.sha256(f"{model}@{revision}@{dtype}".encode()).hexdigest()[:12]


def windows(length: int, window: int = MAX_RESIDUES, overlap: int = OVERLAP) -> list[tuple[int, int]]:
    if length <= window:
        return [(0, length)]
    stride = window - overlap
    out = []
    start = 0
    while True:
        end = min(start + window, length)
        out.append((start, end))
        if end >= length:
            return out
        start += stride


def load_cache_dir(cache_dir: Path, model: str, revision: str, dtype: str) -> dict:
    import numpy as np

    key = cache_key(model, revision, dtype)
    index_p = cache_dir / f"cache_{key}.json"
    vec_p = cache_dir / f"cache_{key}.f32.npy"
    if not (index_p.exists() and vec_p.exists()):
        return {}
    try:
        index = json.loads(index_p.read_text(encoding="utf-8"))
        hashes = index["hashes"]
        vecs = np.load(vec_p)
    except Exception as exc:
        print(f"warning: unreadable cache {index_p}: {exc}", file=sys.stderr)
        return {}
    n = min(len(hashes), vecs.shape[0])
    return {hashes[i]: vecs[i] for i in range(n)}


def save_cache_dir(cache_dir: Path, cache: dict, model: str, revision: str, dtype: str) -> None:
    import numpy as np

    if not cache:
        return
    cache_dir.mkdir(parents=True, exist_ok=True)
    key = cache_key(model, revision, dtype)
    index_p = cache_dir / f"cache_{key}.json"
    vec_p = cache_dir / f"cache_{key}.f32.npy"
    hashes = list(cache.keys())
    vecs = np.stack([cache[k] for k in hashes]).astype(np.float32)
    tmp_v = vec_p.with_name(f"cache_{key}.{os.getpid()}.f32.tmp.npy")
    np.save(tmp_v, vecs)
    tmp_i = index_p.with_name(f"cache_{key}.{os.getpid()}.json.tmp")
    tmp_i.write_text(
        json.dumps(
            {
                "meta": {
                    "model": model,
                    "revision": revision,
                    "dtype": dtype,
                    "dim": int(vecs.shape[1]),
                },
                "hashes": hashes,
            }
        ),
        encoding="utf-8",
    )
    os.replace(tmp_v, vec_p)
    os.replace(tmp_i, index_p)


def embed_missing(todo_seqs: dict[str, str], model_name: str, revision: str, dtype_name: str) -> dict:
    import numpy as np
    import torch
    from transformers import AutoTokenizer, EsmModel

    if torch.backends.mps.is_available():
        device = torch.device("mps")
    elif torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")

    dtype = {"float32": torch.float32, "float16": torch.float16, "bfloat16": torch.bfloat16}[dtype_name]
    print(f"loading {model_name}@{revision[:8]} ({dtype_name}) on {device} for {len(todo_seqs)} sequences", file=sys.stderr)
    tok = AutoTokenizer.from_pretrained(model_name, revision=revision)
    model = EsmModel.from_pretrained(model_name, revision=revision, dtype=dtype, add_pooling_layer=False)
    model.eval().to(device)

    hashes = list(todo_seqs.keys())
    seqs = [todo_seqs[h] for h in hashes]
    order = sorted(range(len(seqs)), key=lambda i: -len(seqs[i]))
    plan = [(i, s, e) for i in order for (s, e) in windows(len(seqs[i]))]
    remaining = {i: len(windows(len(seqs[i]))) for i in order}
    acc_sum: dict[int, np.ndarray] = {}
    acc_cnt: dict[int, np.ndarray] = {}
    out: dict[str, np.ndarray] = {}

    max_tokens = 16384
    max_batch = 64
    pos = 0
    t0 = time.time()
    while pos < len(plan):
        batch = []
        width = 0
        while pos < len(plan) and len(batch) < max_batch:
            i, s, e = plan[pos]
            w = max(width, e - s + 2)
            if batch and w * (len(batch) + 1) > max_tokens:
                break
            width = w
            batch.append(plan[pos])
            pos += 1
        texts = [seqs[i][s:e] for i, s, e in batch]
        enc = tok(texts, padding=True, return_tensors="pt")
        counts = enc["attention_mask"].sum(dim=1).numpy()
        enc = {k: v.to(device) for k, v in enc.items()}
        with torch.inference_mode():
            hid = model(**enc).last_hidden_state
        hid = hid.float().cpu().numpy()
        for row, (i, s, e) in enumerate(batch):
            n = e - s
            if int(counts[row]) != n + 2:
                raise ValueError(f"Unexpected token count {counts[row]} for window length {n}")
            rep = hid[row, 1 : n + 1]
            if i not in acc_sum:
                acc_sum[i] = np.zeros((len(seqs[i]), rep.shape[1]), dtype=np.float32)
                acc_cnt[i] = np.zeros(len(seqs[i]), dtype=np.float32)
            acc_sum[i][s:e] += rep
            acc_cnt[i][s:e] += 1.0
            remaining[i] -= 1
            if remaining[i] == 0:
                per_res = acc_sum.pop(i) / acc_cnt.pop(i)[:, None]
                vec = per_res.mean(axis=0).astype(np.float32)
                out[hashes[i]] = vec
    print(f"embedded {len(out)} sequences in {time.time() - t0:.1f}s", file=sys.stderr)
    return out


def load_corpus_records() -> dict[str, dict]:
    try:
        from yaml import CSafeLoader as Loader
    except ImportError:
        from yaml import SafeLoader as Loader

    records: dict[str, dict] = {}
    for path in sorted(CORPUS_DIR.rglob("*.yaml")):
        with path.open(encoding="utf-8") as fh:
            doc = yaml.load(fh, Loader=Loader)
        if not isinstance(doc, dict) or not doc.get("identifier"):
            continue
        rel = str(path.relative_to(REPO_ROOT))
        class_dir = path.parent.name
        class_label = CLASS_LABEL.get(class_dir, class_dir.replace("-", " ").title())
        records[rel] = {
            "id": str(doc["identifier"]),
            "label": str(doc.get("label") or path.stem),
            "page": f"{class_dir}/{path.stem}.html",
            "group": class_label,
            "class_slug": class_dir,
        }
    return records


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=OUT_PATH)
    ap.add_argument("--neighbors", type=int, default=10)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    import numpy as np
    import pacmap

    corpus_records = load_corpus_records()

    inventory: dict[str, dict] = {}
    inv_path = CROSS_MECH_DIR / "protein_inventory.jsonl"
    with inv_path.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                d = json.loads(line)
                inventory[d["protein_id"]] = d

    sequences: dict[str, dict] = {}
    seq_path = CROSS_MECH_DIR / "protein_sequences.jsonl"
    with seq_path.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                d = json.loads(line)
                sequences[d["protein_id"]] = d

    mentions_by_protein: dict[str, list[dict]] = collections.defaultdict(list)
    mentions_path = CROSS_MECH_DIR / "protein_mentions.jsonl"
    n_mentions = 0
    with mentions_path.open(encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            d = json.loads(line)
            if d.get("mech") != MECH_KEY:
                continue
            rec_path = d.get("record_path", "")
            if rec_path not in corpus_records:
                continue
            n_mentions += 1
            mentions_by_protein[d["protein_id"]].append(d)

    protein_rows = []
    for pid in sorted(mentions_by_protein.keys()):
        inv = inventory.get(pid, {})
        seq_key = inv.get("sequence_key") or pid
        seq_entry = sequences.get(seq_key) or sequences.get(pid)
        if not seq_entry:
            continue
        raw_seq = (seq_entry.get("sequence") or "").strip().upper()
        if not raw_seq or not VALID_SEQUENCE.match(raw_seq):
            continue

        mentions = mentions_by_protein[pid]
        label = inv.get("protein_label")
        taxon_label = inv.get("taxon_label")
        taxon_id = inv.get("taxon_id")
        for m in mentions:
            if not label and m.get("sibling_label"):
                label = m["sibling_label"]
            if not taxon_id and m.get("sibling_taxon_id"):
                taxon_id = m["sibling_taxon_id"]
        label = label or pid
        organism = (taxon_label or "Unknown").split(" (")[0]

        rec_map: dict[str, dict] = {}
        roles_seen: set[str] = set()
        channels_seen: set[str] = set()
        groups_counter: collections.Counter[str] = collections.Counter()

        for m in mentions:
            rinfo = corpus_records[m["record_path"]]
            role = m.get("role") or "REFERENCE"
            ch_raw = m.get("channel") or m.get("relation") or "reference"
            ch = ch_raw.split(".")[-1]
            roles_seen.add(role)
            channels_seen.add(ch)
            groups_counter[rinfo["group"]] += 1

            rid = rinfo["id"]
            existing = rec_map.get(rid)
            if existing is None or ROLE_ORDER.index(role) < ROLE_ORDER.index(existing["role"]):
                rec_map[rid] = {
                    "id": rid,
                    "label": rinfo["label"],
                    "page": rinfo["page"],
                    "group": rinfo["group"],
                    "role": role,
                    "role_label": ROLE_LABELS.get(role, role.title()),
                    "channel": ch,
                }

        primary_role = next((r for r in ROLE_ORDER if r in roles_seen), sorted(roles_seen)[0])
        primary_group = groups_counter.most_common(1)[0][0]
        seq_len = len(raw_seq)

        protein_rows.append(
            {
                "id": pid,
                "label": label,
                "organism": organism,
                "taxon_id": taxon_id or "",
                "length": seq_len,
                "length_bin": length_bin(seq_len),
                "sequence": raw_seq,
                "sequence_sha256": sha(raw_seq),
                "primary_group": primary_group,
                "groups": sorted(groups_counter.keys()),
                "primary_role": primary_role,
                "primary_role_label": ROLE_LABELS.get(primary_role, primary_role.title()),
                "roles": [r for r in ROLE_ORDER if r in roles_seen],
                "channels": sorted(channels_seen),
                "records": sorted(rec_map.values(), key=lambda r: r["label"].lower()),
            }
        )

    cache = load_cache_dir(PTM_ESM2_DIR, MODEL, REVISION, "float32")
    shared_cache = load_cache_dir(SHARED_CACHE_DIR, MODEL, REVISION, "float32")
    cache.update(shared_cache)

    uniq_seqs = {r["sequence_sha256"]: r["sequence"] for r in protein_rows}
    todo = {h: seq for h, seq in uniq_seqs.items() if h not in cache}
    print(
        f"{MECH_KEY}: {len(protein_rows)} proteins with sequences, "
        f"{len(uniq_seqs) - len(todo)} cached, {len(todo)} to embed",
        file=sys.stderr,
    )
    if todo:
        new_vecs = embed_missing(todo, MODEL, REVISION, "float32")
        shared_cache.update(new_vecs)
        save_cache_dir(SHARED_CACHE_DIR, shared_cache, MODEL, REVISION, "float32")
        cache.update(new_vecs)

    raw_vecs = np.stack([cache[r["sequence_sha256"]] for r in protein_rows]).astype(np.float32)
    X = raw_vecs - raw_vecs.mean(axis=0, keepdims=True)
    X /= np.maximum(np.linalg.norm(X, axis=1, keepdims=True), 1e-12)

    n_neighbors = min(args.neighbors, max(1, len(protein_rows) - 1))
    coords = pacmap.PaCMAP(
        n_components=2,
        n_neighbors=n_neighbors,
        apply_pca=False,
        random_state=args.seed,
    ).fit_transform(X, init="pca")
    coords = np.asarray(coords, dtype=float)
    lo, hi = coords.min(axis=0), coords.max(axis=0)
    span = np.where(hi - lo == 0, 1.0, hi - lo)
    norm = (coords - lo) / span

    distinct_records = {rec["id"] for r in protein_rows for rec in r["records"]}
    all_groups = sorted({g for r in protein_rows for g in r["groups"]})
    all_roles = [r for r in ROLE_ORDER if any(r in p["roles"] for p in protein_rows)]
    all_channels = sorted({c for r in protein_rows for c in r["channels"]})

    out_proteins = []
    for i, r in enumerate(protein_rows):
        out_proteins.append(
            {
                "id": r["id"],
                "label": r["label"],
                "organism": r["organism"],
                "taxon_id": r["taxon_id"],
                "length": r["length"],
                "length_bin": r["length_bin"],
                "x": round(float(norm[i, 0]), 4),
                "y": round(float(norm[i, 1]), 4),
                "primary_group": r["primary_group"],
                "groups": r["groups"],
                "primary_role": r["primary_role"],
                "primary_role_label": r["primary_role_label"],
                "roles": r["roles"],
                "channels": r["channels"],
                "records": r["records"],
            }
        )

    payload = {
        "mech": MECH_KEY,
        "model": MODEL,
        "revision": REVISION,
        "dim": int(raw_vecs.shape[1]),
        "pooling": "final-layer residue mean, excluding CLS/EOS/padding",
        "window": MAX_RESIDUES,
        "overlap": OVERLAP,
        "method": "pacmap",
        "prep": "centre",
        "neighbors": n_neighbors,
        "seed": args.seed,
        "n_proteins": len(out_proteins),
        "n_records": len(distinct_records),
        "n_mentions": n_mentions,
        "group_label": GROUP_LABEL,
        "groups": all_groups,
        "roles": [{"id": r, "label": ROLE_LABELS.get(r, r.title())} for r in all_roles],
        "channels": all_channels,
        "length_bins": list(LENGTH_BINS),
        "proteins": out_proteins,
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, separators=(",", ":"), ensure_ascii=False) + "\n", encoding="utf-8")
    print(
        f"wrote {len(out_proteins)} proteins across {len(distinct_records)} records -> {args.out}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
