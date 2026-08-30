#!/usr/bin/env python3
"""Render the browsable site under pages/ from data/antibiotics/.

A corpus of 2,600+ YAML files, each carrying dozens to hundreds of nested
resistance and target claims, is not readable by anyone who is not already
running the tooling — which makes the curation backlog (what has structure but
no mechanism, what is grounded but unreviewed) invisible to exactly the people
best placed to work on it. The site publishes the records themselves.

Generated, committed, and served from `main` at the repo root, matching the
sibling Mech repos (HabitatMech, CultureMech, ...). Regenerate with
`just render`; CI checks the output is in step with the corpus, the same way
`verify-corpus` does for the records themselves.

Ported from HabitatMech's scripts/render_pages.py with two deliberate
differences: this corpus has no git history yet, so there is no retired-URL /
redirect system and no ENVO-term-request page (both HabitatMech features);
and record pages are NOT flattened into one directory: pages/ mirrors the
corpus, data/antibiotics/<class>/<slug>.yaml -> pages/<class>/<slug>.html.

Slugs are corpus-wide unique — assign_slugs keeps a single `taken` set across
every class — so a flat layout would work too. Mirroring is chosen because a
reader holding a YAML path can guess the URL and back, and because a record
that changes class then changes its URL in exactly one place.

Usage:
    python3 scripts/render_pages.py
    python3 scripts/render_pages.py --out /tmp/site --check
"""

from __future__ import annotations

import argparse
import filecmp
import json
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

REPO_ROOT = Path(__file__).resolve().parent.parent
CORPUS_DIR = REPO_ROOT / "data" / "antibiotics"
TEMPLATES_DIR = REPO_ROOT / "src" / "antibioticmech" / "templates"
PAGES_DIR = REPO_ROOT / "pages"
SCHEMA_PATH = REPO_ROOT / "src" / "antibioticmech" / "schema" / "antibioticmech.yaml"

# Enum value -> the directory the corpus files it under. Mirrors CLASS_DIRS in
# scripts/seed_from_sources.py; the schema test keeps the two enumerations honest.
CLASS_DIRS = {
    "ANTIBACTERIAL": "antibacterial",
    "ANTIMYCOBACTERIAL": "antimycobacterial",
    "ANTIFUNGAL": "antifungal",
    "ANTIPROTOZOAL": "antiprotozoal",
    "ANTIVIRAL": "antiviral",
    "BIOCIDE": "biocide",
    "ANTIMICROBIAL_UNSPECIFIED": "unspecified",
    "OTHER": "other",
}
MANIFEST_PATH = REPO_ROOT / "data" / "raw" / "MANIFEST.yaml"

# Where the site is served from; the sitemap needs absolute URLs.
SITE_BASE = "https://culturebotai.github.io/AntibioticMech/pages/"

# Rows per class page. antibacterial alone is 977 records; a single 977-row
# table is the heaviest page on the site for no reason — the filter already
# searches the whole class via the JSON index, same trade HabitatMech makes
# for its category pages.
CLASS_PAGE_SIZE = 300

# Folder names under data/antibiotics/ (== antimicrobial_class, lowercased,
# except ANTIMICROBIAL_UNSPECIFIED and OTHER which both file under
# "unspecified" — see the seeder). Display label + one-line description for
# the browse/index pages.
CLASS_LABEL = {
    "antibacterial": "Antibacterial",
    "antimycobacterial": "Antimycobacterial",
    "antifungal": "Antifungal",
    "antiprotozoal": "Antiprotozoal",
    "biocide": "Biocide",
    "unspecified": "Unspecified",
}
CLASS_BLURB = {
    "antibacterial": "Active against bacteria — antibacterial drugs and agents.",
    "antimycobacterial": "Antitubercular, antimycobacterial and leprostatic agents.",
    "antifungal": "Antifungal agents, drugs and agrochemical fungicides.",
    "antiprotozoal": "Antimalarial, antileishmanial, trypanocidal, coccidiostat and antitrichomonal agents.",
    "biocide": "Disinfectants and antimicrobial food or cosmetic preservatives.",
    "unspecified": "Asserted as an antimicrobial agent without a named microbial target group, "
                   "or in scope by curation but fitting no other class.",
}

GROUNDING_MEANING = {
    "EXACT": "The identifier is an ontology term asserted by ChEBI or ARO themselves.",
    "MINTED": "No defensible ontology identity; the record keeps a content-hashed antibioticmech: CURIE.",
    "REVIEW_NEEDED": "Grounding has not been decided yet.",
}

# Mechanism-layer fields curation fills in over time, in the order the index
# page's coverage table shows them. Mirrors scripts/antibiotic_report.py's
# `mechanism` counters so the site and `just report` cannot disagree.
MECHANISM_FIELDS = [
    ("molecular_targets", "Molecular targets"),
    ("resistance_mechanisms", "Resistance mechanisms"),
    ("mode_of_action", "Mode of action"),
    ("causal_graphs", "Causal graphs"),
    ("activity_spectrum", "Activity spectrum"),
    ("producer_organisms", "Producer organisms"),
    ("discussions", "Discussions"),
    ("datasets", "Datasets"),
]

# CURIE prefixes this site resolves to an external page, in the exact casing
# they appear in the corpus (the schema's own `prefixes:` block uses
# different casing for some of these — e.g. CHEMBL.COMPOUND, KEGG — that does
# not match what the seeder actually writes, so it is not used here).
XREF_URL_TEMPLATES = {
    "CHEBI": "http://purl.obolibrary.org/obo/CHEBI_{}",
    "ARO": "http://purl.obolibrary.org/obo/ARO_{}",
    "pubchem.compound": "https://pubchem.ncbi.nlm.nih.gov/compound/{}",
    "chembl": "https://www.ebi.ac.uk/chembl/compound_report_card/{}/",
    "drugbank": "https://go.drugbank.com/drugs/{}",
    "cas": "https://commonchemistry.cas.org/detail?cas_rn={}",
    "kegg.compound": "https://www.kegg.jp/entry/{}",
    "kegg.drug": "https://www.kegg.jp/entry/{}",
}


def load_records() -> list[tuple[Path, dict]]:
    out = []
    for path in sorted(CORPUS_DIR.rglob("*.yaml")):
        with path.open(encoding="utf-8") as fh:
            doc = yaml.safe_load(fh)
        if isinstance(doc, dict):
            out.append((path, doc))
    return out


def extracted_at() -> str:
    if MANIFEST_PATH.exists():
        manifest = yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8"))
        if isinstance(manifest, dict) and manifest.get("retrieved_on"):
            return str(manifest["retrieved_on"])[:10]
    return "an unrecorded date"


def external_iri(identifier: str) -> str | None:
    prefix, _, local = identifier.partition(":")
    template = XREF_URL_TEMPLATES.get(prefix)
    return template.format(local) if template else None


def resolve_curie(curie: str, index: dict[str, dict], root: str) -> dict:
    """Turn a CURIE into a link: internal if it is a record in this corpus,
    external if its prefix is one of the handful this site resolves,
    otherwise a bare, unlinked CURIE."""
    entry = index.get(curie)
    if entry:
        href = f"{root}{entry['class_dir']}/{entry['slug']}.html"
        return {"id": curie, "label": entry["label"], "href": href}
    href = external_iri(curie)
    return {"id": curie, "label": None, "href": href}


def build_record(path: Path, doc: dict, index: dict[str, dict], root: str) -> dict:
    class_dir = path.parent.name

    groups: dict[str, list[dict]] = defaultdict(list)
    for m in doc.get("resistance_mechanisms") or []:
        groups[m.get("mechanism_type") or "UNKNOWN"].append(
            {
                "label": m.get("label", ""),
                "aro_id": resolve_curie(m["aro_id"], index, root) if m.get("aro_id") else None,
                "gene_families": m.get("gene_families") or [],
                "note": m.get("note"),
            }
        )
    # Largest group first, so the compound with 90 CARD-asserted determinants
    # opens on the group a reader is most likely looking for, not alphabetical
    # noise (#erythromycin-a has 90 across 3 mechanism types).
    resistance_groups = [
        {"mechanism_type": name, "rows": sorted(rows, key=lambda r: r["label"])}
        for name, rows in sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    ]

    molecular_targets = [
        {
            "target_label": t.get("target_label", ""),
            "target_type": t.get("target_type"),
            "target_id": resolve_curie(t["target_id"], index, root) if t.get("target_id") else None,
            "protein_examples": t.get("protein_examples") or [],
            "evidence": t.get("evidence") or [],
        }
        for t in (doc.get("molecular_targets") or [])
    ]

    curation_history = [
        {**event, "date": (event.get("timestamp") or "")[:10]}
        for event in (doc.get("curation_history") or [])
    ]

    identifier = doc["identifier"]
    return {
        "identifier": identifier,
        "label": doc["label"],
        "iri": external_iri(identifier),
        "class_slug": class_dir,
        "antimicrobial_class": doc.get("antimicrobial_class", "?"),
        "grounding_status": doc.get("grounding_status", "?"),
        "curation_status": doc.get("curation_status", "?"),
        "definition": doc.get("definition"),
        "definition_source": doc.get("definition_source"),
        "structural_class": doc.get("structural_class"),
        "structural_class_id": (
            resolve_curie(doc["structural_class_id"], index, root)
            if doc.get("structural_class_id")
            else None
        ),
        "parent_compounds": [resolve_curie(c, index, root) for c in (doc.get("parent_compounds") or [])],
        "xrefs": [resolve_curie(c, index, root) for c in (doc.get("xrefs") or [])],
        "activity_roles": [resolve_curie(c, index, root) for c in (doc.get("activity_roles") or [])],
        "structure": doc.get("chemical_structure") or None,
        "synonyms": [
            {"text": s.get("synonym_text", ""), "type": s.get("synonym_type"), "source": s.get("source")}
            for s in (doc.get("synonyms") or [])
        ],
        "source_concepts": doc.get("source_concepts") or [],
        "molecular_targets": molecular_targets,
        "mode_of_action": doc.get("mode_of_action"),
        "mode_of_action_notes": doc.get("mode_of_action_notes"),
        "cidality": doc.get("cidality"),
        "clinical_status": doc.get("clinical_status"),
        "activity_spectrum": doc.get("activity_spectrum") or [],
        "resistance_mechanisms": doc.get("resistance_mechanisms") or [],
        "resistance_groups": resistance_groups,
        "producer_organisms": doc.get("producer_organisms") or [],
        "causal_graphs": doc.get("causal_graphs") or [],
        "discussions": doc.get("discussions") or [],
        "datasets": doc.get("datasets") or [],
        "evidence": doc.get("evidence") or [],
        "curation_history": curation_history,
        "repo_path": str(path.relative_to(REPO_ROOT)),
    }


def class_hierarchy() -> dict[str, list[str]]:
    """Parent class dir -> narrower class dirs, read from the schema's enum.

    LinkML lets a permissible value declare `is_a`, and AntimicrobialClassEnum
    uses it to say ANTIMYCOBACTERIAL is a kind of ANTIBACTERIAL — mycobacteria
    are bacteria. Filing is exclusive and picks the narrower claim, so those
    records are NOT also under antibacterial, and a reader on the antibacterial
    page would otherwise never learn that 78 more sit one click away. Deriving
    the site's cross-links from the schema means the two cannot drift apart.
    """
    schema = yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))
    values = schema["enums"]["AntimicrobialClassEnum"]["permissible_values"]
    out: dict[str, list[str]] = {}
    for name, body in values.items():
        parent = (body or {}).get("is_a")
        if parent and parent in CLASS_DIRS and name in CLASS_DIRS:
            out.setdefault(CLASS_DIRS[parent], []).append(CLASS_DIRS[name])
    return out


def build(out_dir: Path) -> None:
    records = load_records()
    if not records:
        raise SystemExit(f"no records under {CORPUS_DIR}; run `just seed-apply` first")

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    # A CURIE referenced by another record (parent_compounds, xrefs,
    # activity_roles, a molecular target, a resistance determinant) is
    # usually NOT itself a record — that is what makes it a cross-reference —
    # but a few are (e.g. one compound's parent_compounds naming another
    # AntibioticRecord's ChEBI CURIE), and those deserve an internal link with
    # a real label rather than a bare, unlinked CURIE.
    index = {doc["identifier"]: {"class_dir": path.parent.name, "slug": path.stem, "label": doc["label"]}
             for path, doc in records}

    # Rendering PRUNES every unrecognised file under out_dir when it finishes, so
    # check before writing anything that this directory is ours to manage. `--out`
    # is documented and easy to point at a real directory; the marker file makes
    # "previously rendered site" checkable instead of assumed.
    marker_path = out_dir / ".antibioticmech-site"
    if out_dir.exists() and any(out_dir.iterdir()) and not marker_path.exists():
        raise SystemExit(
            f"refusing to render into {out_dir}: it is not empty and carries no "
            f".antibioticmech-site marker, and rendering prunes unrecognised files. "
            f"Render into an empty directory, or create the marker if this really is "
            f"a previously rendered site."
        )
    out_dir.mkdir(parents=True, exist_ok=True)
    class_dirs = sorted({path.parent.name for path, _ in records})
    for class_dir in class_dirs:
        (out_dir / class_dir).mkdir(exist_ok=True)
    (out_dir / "class").mkdir(exist_ok=True)

    # Corpus-wide stats need a full pass before the footer of the FIRST record
    # page can be rendered — reading the fields straight off `doc` here, not
    # through build_record(), so this stays a cheap dict pass rather than a
    # second full page-building pass over 2,603 records.
    total = len(records)
    curation_counts = Counter(doc.get("curation_status", "?") for _, doc in records)
    grounding_counts = Counter(doc.get("grounding_status", "?") for _, doc in records)
    multi_source = sum(
        1 for _, doc in records if len({c["source"] for c in (doc.get("source_concepts") or [])}) > 1
    )
    structure_complete = sum(
        1 for _, doc in records if (doc.get("chemical_structure") or {}).get("standard_inchi_key")
    )
    mechanism_counts = {
        key: sum(1 for _, doc in records if doc.get(key)) for key, _label in MECHANISM_FIELDS
    }

    stats = {
        "total": total,
        "extracted_at": extracted_at(),
        "reviewed": curation_counts.get("REVIEWED", 0),
        "seeded": curation_counts.get("SEEDED", 0),
        "seeded_pct": round(100 * curation_counts.get("SEEDED", 0) / total, 1),
        "grounded": grounding_counts.get("EXACT", 0),
        "multi_source": multi_source,
        "structure_complete": structure_complete,
    }
    groundings = [
        {"name": name, "count": count, "meaning": GROUNDING_MEANING.get(name, "")}
        for name, count in grounding_counts.most_common()
    ]
    mechanism = [
        {"label": label, "count": mechanism_counts[key], "pct": round(100 * mechanism_counts[key] / total, 1)}
        for key, label in MECHANISM_FIELDS
    ]

    by_class: dict[str, list[dict]] = defaultdict(list)
    for path, doc in records:
        class_dir = path.parent.name
        sources = sorted({c["source"] for c in (doc.get("source_concepts") or [])})

        record = build_record(path, doc, index, root="../")
        (out_dir / class_dir / f"{path.stem}.html").write_text(
            env.get_template("record.html").render(r=record, root="../", stats=stats),
            encoding="utf-8",
        )

        by_class[class_dir].append(
            {
                "label": doc["label"],
                "slug": path.stem,
                "structural_class": doc.get("structural_class") or "",
                "grounding": doc.get("grounding_status", "?"),
                "status": doc.get("curation_status", "?"),
                "sources": sources,
            }
        )

    # Filing is exclusive but the classes are not disjoint: mycobacteria are
    # bacteria, so antimycobacterial records ARE antibacterial ones and a reader
    # on the antibacterial page would otherwise never learn that 78 more sit one
    # click away. Read from the schema so the site cannot disagree with it.
    narrower = class_hierarchy()

    classes = []
    class_pages: list[str] = []
    for class_dir in class_dirs:
        items = by_class[class_dir]
        classes.append(
            {
                "label": CLASS_LABEL.get(class_dir, class_dir.replace("-", " ").title()),
                "slug": class_dir,
                "count": len(items),
                "pct": round(100 * len(items) / total),
                "grounded": sum(1 for i in items if i["grounding"] == "EXACT"),
                "description": CLASS_BLURB.get(class_dir, ""),
                "narrower": [
                    {"slug": child, "label": CLASS_LABEL.get(child, child.title()),
                     "count": len(by_class.get(child, []))}
                    for child in narrower.get(class_dir, []) if by_class.get(child)
                ],
                "broader": next(
                    ({"slug": parent, "label": CLASS_LABEL.get(parent, parent.title())}
                     for parent, kids in narrower.items() if class_dir in kids), None),
            }
        )
        ordered = sorted(items, key=lambda r: r["label"])
        chunks = [ordered[i:i + CLASS_PAGE_SIZE] for i in range(0, len(ordered), CLASS_PAGE_SIZE)] or [[]]
        pager = [
            {"n": n, "href": f"{class_dir}.html" if n == 1 else f"{class_dir}-{n}.html"}
            for n in range(1, len(chunks) + 1)
        ]
        for n, chunk in enumerate(chunks, start=1):
            target = out_dir / "class" / (f"{class_dir}.html" if n == 1 else f"{class_dir}-{n}.html")
            target.write_text(
                env.get_template("class.html").render(
                    label=CLASS_LABEL.get(class_dir, class_dir.replace("-", " ").title()),
                    slug=class_dir,
                    description=CLASS_BLURB.get(class_dir, ""),
                    narrower=[c for c in classes if c["slug"] == class_dir][0]["narrower"],
                    broader=[c for c in classes if c["slug"] == class_dir][0]["broader"],
                    records=chunk,
                    total=len(ordered),
                    page=n,
                    pager=pager if len(pager) > 1 else [],
                    index_url=f"{class_dir}.json",
                    root="../",
                    stats=stats,
                ),
                encoding="utf-8",
            )
            class_pages.append(f"class/{target.name}")
        # A compact index so the filter can search the WHOLE class, not just
        # the page in front of you — the same trade HabitatMech's category
        # pages make, for the same reason (antibacterial alone is 4 pages).
        (out_dir / "class" / f"{class_dir}.json").write_text(
            json.dumps(
                [[r["label"], r["slug"], r["structural_class"], r["grounding"], r["status"],
                  ", ".join(r["sources"])] for r in ordered],
                separators=(",", ":"), ensure_ascii=False,
            ),
            encoding="utf-8",
        )

    (out_dir / "index.html").write_text(
        env.get_template("index.html").render(
            stats=stats, classes=classes, groundings=groundings, mechanism=mechanism, root=""
        ),
        encoding="utf-8",
    )
    (out_dir / "browse.html").write_text(
        env.get_template("browse.html").render(stats=stats, classes=classes, root=""),
        encoding="utf-8",
    )
    (out_dir / "404.html").write_text(
        env.get_template("not_found.html").render(root="", stats=stats),
        encoding="utf-8",
    )
    shutil.copyfile(TEMPLATES_DIR / "style.css", out_dir / "style.css")
    # Without this, Pages runs Jekyll over the site and silently drops any
    # path beginning with an underscore — a 404 rather than a visible error.
    (out_dir / ".nojekyll").write_text("", encoding="utf-8")

    listed = ["index.html", "browse.html", "404.html"] + class_pages
    listed += [f"{path.parent.name}/{path.stem}.html" for path, _ in records]
    urls = "\n".join(f"  <url><loc>{SITE_BASE}{page}</loc></url>" for page in listed)
    (out_dir / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}\n</urlset>\n",
        encoding="utf-8",
    )
    (out_dir / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {SITE_BASE}sitemap.xml\n", encoding="utf-8"
    )

    # Remove pages for records that no longer exist. Curation can rename a
    # record's slug or move it to a different class, so the set of live pages
    # shrinks and shifts, not just grows; without this, pages/ keeps serving a
    # stale page forever and --check would have nothing to catch it with.
    written = {
        out_dir / "index.html", out_dir / "browse.html", out_dir / "404.html",
        out_dir / "style.css", out_dir / ".nojekyll", out_dir / "sitemap.xml", out_dir / "robots.txt",
    }
    written |= {out_dir / page for page in class_pages}
    written |= {out_dir / "class" / f"{d}.json" for d in class_dirs}
    written |= {out_dir / path.parent.name / f"{path.stem}.html" for path, _ in records}
    marker = out_dir / ".antibioticmech-site"
    written.add(marker)
    marker.write_text("Generated by scripts/render_pages.py; safe to prune.\n", encoding="utf-8")
    pruned = 0
    for existing in sorted(out_dir.rglob("*")):
        if existing.is_file() and existing not in written:
            existing.unlink()
            pruned += 1
    # A pruned record page can leave its class directory empty (the class was
    # removed entirely, not just shrunk); an empty dir is otherwise silent
    # debris that --check cannot see because filecmp only walks files.
    for existing in sorted(out_dir.rglob("*"), reverse=True):
        if existing.is_dir() and not any(existing.iterdir()):
            existing.rmdir()

    print(f"rendered {total} compound pages, {len(classes)} classes"
          + (f", pruned {pruned} stale" if pruned else "")
          + f" -> {out_dir}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", type=Path, default=PAGES_DIR)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Render to a temp dir and fail if pages/ differs — the site is "
        "committed, so it can go stale against the corpus exactly as records "
        "could go stale against data/raw/.",
    )
    args = parser.parse_args(argv)

    if not args.check:
        build(args.out)
        return 0

    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        target = Path(tmp) / "site"
        build(target)
        stale = []
        for rendered in sorted(target.rglob("*")):
            if rendered.is_dir():
                continue
            committed = PAGES_DIR / rendered.relative_to(target)
            if not committed.exists() or not filecmp.cmp(rendered, committed, shallow=False):
                stale.append(str(rendered.relative_to(target)))
        extra = [
            str(p.relative_to(PAGES_DIR))
            for p in sorted(PAGES_DIR.rglob("*"))
            if p.is_file() and not (target / p.relative_to(PAGES_DIR)).exists()
        ]
        if stale or extra:
            print(f"pages/ is stale: {len(stale)} differing, {len(extra)} orphaned", file=sys.stderr)
            for name in (stale + extra)[:10]:
                print(f"  {name}", file=sys.stderr)
            print("\nRegenerate with `just render`.", file=sys.stderr)
            return 1
        print("pages/ is in step with the corpus")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
