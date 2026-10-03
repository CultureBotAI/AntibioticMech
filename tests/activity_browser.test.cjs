const assert = require("node:assert/strict");
const fs = require("node:fs");
const zlib = require("node:zlib");
const path = require("node:path");
const {filterRows, validatePayload, boundedBytes, fetchJSON} = require(process.argv[2]);
const payload = fs.readFileSync(process.argv[3]);
const index = JSON.parse(zlib.gunzipSync(payload));
const context = {identifier: index.identifier, key: index.standard_inchi_key, total: String(index.total)};
assert.equal(validatePayload(index, context, true).length, 201);
assert.equal(filterRows(index.rows, "gCa_2.1", "", "")[0][0], 201);
assert.equal(filterRows(index.rows, "\uff27\uff23\uff21_\uff12.\uff11", "", "")[0][0], 201);
assert.equal(filterRows(index.rows, "gca_2.1 SAMN200", "=", "=").length, 1);
assert.equal(filterRows(index.rows, "gca_2.1", "=RESISTANT", "").length, 0);
assert.equal(filterRows(index.rows, "", "=RESISTANT", "=NCBI_AST").length, 200);
assert.equal(filterRows(index.rows, "missing", "", "").length, 0);
for (const changed of [
  {...index, total: 200}, {...index, identifier: "wrong"}, {...index, standard_inchi_key: "wrong"},
  {...index, rows: index.rows.slice(1)}, {...index, rows: index.rows.slice().reverse()},
  {...index, format: "wrong"}, {...index, rows: index.rows.map(row => row.slice(0, 7))},
]) assert.throws(() => validatePayload(changed, context, true));
const page = {format: "antibioticmech-activity-page-v1", identifier: index.identifier,
  standard_inchi_key: index.standard_inchi_key, total: 201, offset: 200, observations: [{evidence: []}]};
assert.equal(validatePayload(page, {...context, offset: "200"}).length, 1);
for (const changed of [{...page, offset: 0}, {...page, observations: []}, {...page, observations: [null]},
  {...page, observations: [[], {}]}, {...page, format: "wrong"}]) {
  assert.throws(() => validatePayload(changed, {...context, offset: "200"}));
}

(async () => {
  await assert.rejects(boundedBytes(new Blob([new Uint8Array(16 * 1024 * 1024 + 1)]).stream()), /size limit/);
  const name = path.basename(process.argv[3]);
  let calls = 0;
  global.fetch = async () => { calls++; return new Response("corrupted"); };
  await assert.rejects(fetchJSON(name), /checksum mismatch/);
  global.fetch = async () => { calls++; return new Response(payload); };
  assert.deepEqual(await fetchJSON(name), index);
  assert.deepEqual(await fetchJSON(name), index);
  assert.equal(calls, 2, "failed requests are retriable; successful requests are cached");
  global.fetch = async () => new Response("not found", {status: 404});
  await assert.rejects(fetchJSON(`other-${"0".repeat(64)}.json.gz`), /404/);
  await assert.rejects(fetchJSON("missing-checksum.json.gz"), /checksum/);
})().catch(error => { console.error(error); process.exitCode = 1; });
