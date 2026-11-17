"""Bounded publication of grouped activity subjects without inline registry rows."""

import unicodedata
from collections import defaultdict
from urllib.parse import urlencode

from antibioticmech.activity_memberships import collection_bytes, read_memberships


def prepare_memberships(doc, record_path, directory):
    registries = read_memberships(doc, record_path)
    numbers = {(row.get("source"), row.get("source_version"), row.get("source_observation_id")): number
               for number, row in enumerate(doc["activity_spectrum"], 1)}
    groups, entries, links, downloads, written = [], [], {}, [], set()
    for reference, value in registries:
        path = directory / reference["path"]
        path.write_bytes(collection_bytes(reference, record_path))
        written.add(path)
        downloads.append(reference)
        inverted = defaultdict(list)
        for group in value["groups"]:
            key = (reference["source"], reference["source_version"], group["source_observation_id"])
            number = numbers[key]
            observation = doc["activity_spectrum"][number - 1]
            groups.append({
                "number": number, "collection": reference["path"], "source": key[0],
                "source_version": key[1], "source_observation_id": key[2],
                "observation_sha256": group["observation_sha256"], "observation": observation,
                "observation_href": f"activity-{(number - 1) // 100 + 1}.html#observation-{number}",
            })
            links[number] = {
                "href": "memberships.html?" + urlencode(dict(source=key[0], version=key[1], group=key[2])),
                "count": len(group["members"]), "measurements": observation["measurement_count"],
            }
            for member in group["members"]:
                inverted[member["subject_index"]].append(number)
        for ordinal, subject in enumerate(value["subjects"]):
            text = " ".join([subject["source_isolate_id"], *(subject["sequencing_context"] or {}).values()])
            entries.append([unicodedata.normalize("NFKC", text).lower(), sorted(inverted[ordinal])])
    return dict(groups=sorted(groups, key=lambda group: group["number"]), entries=entries, links=links,
                downloads=downloads, written=written)
