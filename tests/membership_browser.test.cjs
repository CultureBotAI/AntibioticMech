const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const zlib = require("node:zlib");
const {validateIndex, validateCollection, selectGroup, filterMembers} = require(path.join(process.argv[2], "membership_browser.js"));
const {filterRows, validatePayload} = require(path.join(process.argv[2], "activity_browser.js"));
const directory = path.dirname(process.argv[3]);
const index = JSON.parse(zlib.gunzipSync(fs.readFileSync(process.argv[3])));
const context = {identifier: index.identifier, key: index.standard_inchi_key, total: String(index.total)};
assert.equal(validateIndex(index, context), index);
const ref = index.collections[0];
const data = JSON.parse(zlib.gunzipSync(fs.readFileSync(path.join(directory, ref.path))));
const groups = validateCollection(data, index, ref);
const members = groups.values().next().value.members;
assert.equal(filterMembers(data.subjects, members, "SAMEA123", "").length, 2);
assert.equal(filterMembers(data.subjects, members, "first ERR456", "").length, 0);
assert.equal(filterMembers(data.subjects, members, "", "unlinked").length, 1);
assert.equal(filterMembers(data.subjects, members, "", "linked").length, 2);
assert.equal(filterMembers(data.subjects, members, "UNMATCHED", "")[0].measurement_count, 2);
assert.equal(selectGroup(index, new URLSearchParams()), index.groups[0]);
assert.equal(selectGroup(index, new URLSearchParams({source: ref.source, version: ref.source_version,
  group: index.groups[0].source_observation_id})), index.groups[0]);
for (const params of [{group: "wrong"}, {source: ref.source, version: ref.source_version, group: "wrong"}]) {
  assert.throws(() => selectGroup(index, new URLSearchParams(params)), /requested observation/);
}
for (const change of [value => {value.identifier = "wrong";}, value => {value.total = 2;},
  value => {value.groups.push(value.groups[0]);}, value => {value.groups[0].observation.source = "wrong";},
  value => {value.groups[0].observation_href = "https://example.org";},
  value => {value.collections[0].path = "../outside.json.gz";}]) {
  const bad = structuredClone(index); change(bad); assert.throws(() => validateIndex(bad, context));
}
for (const change of [value => {value.identifier = "wrong";}, value => {value.source_version = "wrong";},
  value => {value.subjects[0].sequencing_context.run_accession = "GCA_1.1";},
  value => {value.subjects[0].source_isolate_id = value.subjects[1].source_isolate_id;},
  value => {value.groups[0].observation_sha256 = "a".repeat(64);},
  value => {value.groups[0].members[0].subject_index = true;},
  value => {value.groups[0].members[0].subject_index = 3;},
  value => {value.groups[0].members[0].measurement_count = 99;},
  value => {value.groups[0].members.pop();}]) {
  const bad = structuredClone(data); change(bad); assert.throws(() => validateCollection(bad, index, ref));
}
const searchPath = fs.readdirSync(directory).find(name => name.startsWith("search-"));
const search = JSON.parse(zlib.gunzipSync(fs.readFileSync(path.join(directory, searchPath))));
const rows = validatePayload(search, context, true);
assert.equal(filterRows(rows, "samea123", "", "", search.memberships).length, 1);
assert.equal(filterRows(rows, "first err456", "", "", search.memberships).length, 0);
assert.equal(filterRows(rows, "resistant first err123", "=RESISTANT", "", search.memberships).length, 1);
assert.equal(filterRows(rows, "unmatched", "=SUSCEPTIBLE", "", search.memberships).length, 0);
const invalid = structuredClone(search); invalid.memberships[0][1] = [999];
assert.throws(() => validatePayload(invalid, context, true), /membership search/);
