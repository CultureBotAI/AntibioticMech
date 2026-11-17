"""Check published membership registries, observation bindings and search coverage."""

import gzip
import hashlib
import json
import unicodedata
from collections import defaultdict
from html.parser import HTMLParser
from urllib.parse import urlencode

from antibioticmech.activity_memberships import FIELD, MAX_BYTES, read_memberships


class MembershipHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.roots, self.links = [], []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if attributes.get("id") == "membership-browser":
            if len(attrs) != len(attributes):
                raise ValueError("duplicate membership browser attribute")
            self.roots.append(attributes)
        if tag == "a":
            self.links.append(attributes)


def audit_membership_publication(doc, directory):
    if not doc.get(FIELD):
        return {"links": {}, "entries": [], "pages": []}
    # The downloaded complete record resolves exactly the same content-addressed
    # artifacts as the original YAML, including identity and observation digests.
    registries = read_memberships(doc, directory / "record.yaml")
    observations = doc["activity_spectrum"]
    ordinals = {(row.get("source"), row.get("source_version"), row.get("source_observation_id")): number
                for number, row in enumerate(observations, 1)}
    page = directory / "memberships.html"
    parsed = MembershipHTML()
    parsed.feed(page.read_text(encoding="utf-8"))
    if len(parsed.roots) != 1:
        raise ValueError("missing or duplicate membership browser")
    root = parsed.roots[0]
    name = root.get("data-index", "")
    if not name.startswith("membership-index-") or "/" in name or "\\" in name:
        raise ValueError("invalid membership index path")
    payload = (directory / name).read_bytes()
    raw = gzip.decompress(payload)
    if max(len(payload), len(raw)) > MAX_BYTES or name != (
        f"membership-index-{hashlib.sha256(payload).hexdigest()}.json.gz"
    ):
        raise ValueError("membership index bound or checksum mismatch")
    identity = {"identifier": doc["identifier"],
                "standard_inchi_key": doc["chemical_structure"]["standard_inchi_key"],
                "total": len(observations)}
    if root != {"id": "membership-browser", "data-index": name,
                "data-identifier": identity["identifier"], "data-key": identity["standard_inchi_key"],
                "data-total": str(identity["total"])}:
        raise ValueError("membership browser binding mismatch")
    expected_groups, entries, links = [], [], {}
    for reference, registry in registries:
        if not any(link.get("href") == reference["path"] and "download" in link for link in parsed.links):
            raise ValueError("membership registry download missing")
        numbers = defaultdict(list)
        for group in registry["groups"]:
            key = (reference["source"], reference["source_version"], group["source_observation_id"])
            ordinal = ordinals[key]
            observation = observations[ordinal - 1]
            expected_groups.append({
                "number": ordinal, "collection": reference["path"], "source": key[0],
                "source_version": key[1], "source_observation_id": key[2],
                "observation_sha256": group["observation_sha256"], "observation": observation,
                "observation_href": f"activity-{(ordinal - 1) // 100 + 1}.html#observation-{ordinal}",
            })
            links[ordinal] = {
                "href": "memberships.html?" + urlencode(dict(source=key[0], version=key[1], group=key[2])),
                "count": len(group["members"]), "measurements": observation["measurement_count"],
            }
            for member in group["members"]:
                numbers[member["subject_index"]].append(ordinal)
        for ordinal, subject in enumerate(registry["subjects"]):
            text = " ".join([subject["source_isolate_id"], *(subject["sequencing_context"] or {}).values()])
            entries.append([unicodedata.normalize("NFKC", text).lower(), sorted(numbers[ordinal])])
    expected = {"format": "antibioticmech-membership-index-v1", **identity, "collections": doc[FIELD],
                "groups": sorted(expected_groups, key=lambda group: group["number"])}
    if json.loads(raw) != expected:
        raise ValueError("membership observation index differs from the record")
    return {"links": links, "entries": entries, "pages": [page]}
