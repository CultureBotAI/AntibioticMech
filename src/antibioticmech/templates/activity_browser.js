/* Static pages remain usable without this progressive enhancement. */
(() => {
  "use strict";
  const MAX_BYTES = 16 * 1024 * 1024;
  const RESULT_SIZE = 50;
  const cache = new Map();
  const normalize = value => value.normalize("NFKC").toLowerCase();

  async function boundedBytes(stream) {
    const reader = stream.getReader();
    const chunks = [];
    let size = 0;
    try {
      while (true) {
        const {value, done} = await reader.read();
        if (done) break;
        size += value.length;
        if (size > MAX_BYTES) throw new Error("Data exceeds the browser size limit.");
        chunks.push(value);
      }
    } catch (error) {
      await reader.cancel().catch(() => {});
      throw error;
    } finally {
      reader.releaseLock();
    }
    const result = new Uint8Array(size);
    let offset = 0;
    for (const chunk of chunks) { result.set(chunk, offset); offset += chunk.length; }
    return result;
  }

  async function fetchJSON(href) {
    if (cache.has(href)) return cache.get(href);
    const pending = (async () => {
      const checksum = /-([a-f0-9]{64})\.json\.gz$/.exec(href)?.[1];
      if (!checksum) throw new Error("Missing data checksum.");
      const controller = new AbortController();
      const timeout = setTimeout(() => controller.abort(), 20000);
      try {
        const response = await fetch(href, {signal: controller.signal});
        if (!response.ok) throw new Error(`Data request failed (${response.status}).`);
        const bytes = await boundedBytes(response.body);
        const digest = new Uint8Array(await crypto.subtle.digest("SHA-256", bytes));
        const actual = Array.from(digest, n => n.toString(16).padStart(2, "0")).join("");
        if (actual !== checksum) throw new Error("Data checksum mismatch.");
        const raw = await boundedBytes(new Blob([bytes]).stream().pipeThrough(new DecompressionStream("gzip")));
        return JSON.parse(new TextDecoder("utf-8", {fatal: true}).decode(raw));
      } finally {
        clearTimeout(timeout);
      }
    })();
    cache.set(href, pending);
    try { return await pending; }
    catch (error) { cache.delete(href); throw error; }
  }

  function validatePayload(data, context, index = false) {
    const total = Number(context.total);
    if (!data || data.identifier !== context.identifier || data.standard_inchi_key !== context.key ||
        !Number.isSafeInteger(total) || total < 1 || data.total !== total) {
      throw new Error("Data does not match this compound.");
    }
    if (index) {
      if (data.format !== "antibioticmech-activity-index-v1" || !Array.isArray(data.rows) ||
          data.rows.length !== total || !data.rows.every((row, i) =>
            Array.isArray(row) && row.length === 8 && row[0] === i + 1 &&
            row.slice(1).every(value => typeof value === "string"))) {
        throw new Error("Incomplete or invalid search index.");
      }
      return data.rows;
    }
    const offset = Number(context.offset);
    if (data.format !== "antibioticmech-activity-page-v1" || !Number.isSafeInteger(offset) ||
        offset < 0 || offset % 100 !== 0 || offset >= total || data.offset !== offset ||
        !Array.isArray(data.observations) || data.observations.length !== Math.min(100, total - offset) ||
        !data.observations.every(row => row && typeof row === "object" && !Array.isArray(row))) {
      throw new Error("Incomplete or invalid observation page.");
    }
    return data.observations;
  }

  function filterRows(rows, query, activity, source) {
    const tokens = normalize(query).trim().split(/\s+/).filter(Boolean);
    return rows.filter(row => (!activity || `=${row[4]}` === activity) &&
      (!source || `=${row[5]}` === source) && tokens.every(token => row[7].includes(token)));
  }

  function element(tag, text, parent) {
    const node = document.createElement(tag);
    if (text !== undefined) node.textContent = text;
    if (parent) parent.append(node);
    return node;
  }

  function fullValue(value) {
    if (Array.isArray(value)) {
      const list = element("ol");
      for (const item of value) element("li", undefined, list).append(fullValue(item));
      return list;
    }
    if (value !== null && typeof value === "object") {
      const list = element("dl");
      for (const [key, item] of Object.entries(value)) {
        element("dt", key.replaceAll("_", " "), list);
        element("dd", undefined, list).append(fullValue(item));
      }
      return list;
    }
    // Source strings are always text, never markup, even for evidence snippets.
    return element("span", value === null ? "null" : String(value));
  }

  function evidenceDetails(details) {
    let loaded = false;
    let loading = false;
    const output = details.querySelector(".activity-detail");
    async function load() {
      if (loaded || loading || !details.open) return;
      loading = true;
      output.textContent = "Loading evidence...";
      try {
        const data = await fetchJSON(details.querySelector(".activity-data").getAttribute("href"));
        const rows = validatePayload(data, details.dataset);
        const row = Number(details.dataset.row);
        if (!Number.isSafeInteger(row) || row < 0 || row >= rows.length) throw new Error("Invalid observation number.");
        output.replaceChildren(fullValue(rows[row]));
        loaded = true;
      } catch (error) {
        output.textContent = `${error.message} `;
        const retry = element("button", "Retry evidence", output);
        retry.type = "button";
        retry.addEventListener("click", load);
      } finally { loading = false; }
    }
    details.addEventListener("toggle", load);
  }

  function browser(root) {
    const form = root.querySelector("form");
    const query = form.elements.query;
    const activity = form.elements.activity;
    const source = form.elements.source;
    const status = root.querySelector(".activity-status");
    const fallback = root.querySelector(".activity-default");
    const output = root.querySelector(".activity-results");
    const pager = root.querySelector(".activity-results-pager");
    const previous = pager.querySelector('[data-step="-1"]');
    const next = pager.querySelector('[data-step="1"]');
    const retry = root.querySelector(".activity-retry");
    const jump = root.querySelector(".activity-jump");
    jump.hidden = false;
    jump.addEventListener("submit", event => {
      event.preventDefault();
      if (jump.reportValidity()) location.href = `activity-${Number(jump.elements.page.value)}.html`;
    });
    let generation = 0;
    let matches = [];
    let page = 0;
    const params = new URL(location.href).searchParams;
    query.value = params.get("q") || "";
    for (const select of [activity, source]) {
      const value = params.get(select.name) || "";
      if (Array.from(select.options).some(option => option.value === value)) select.value = value;
    }

    function showResults() {
      output.replaceChildren();
      output.hidden = !matches.length;
      pager.hidden = !matches.length;
      const start = page * RESULT_SIZE;
      status.textContent = matches.length ? `${matches.length} matching observations; ${start + 1}-${Math.min(start + RESULT_SIZE, matches.length)} shown.` : "No matching observations.";
      if (!matches.length) return;
      const region = element("div", undefined, output);
      region.className = "table-scroll";
      region.setAttribute("role", "region");
      region.setAttribute("aria-label", "Matching activity observations");
      region.tabIndex = 0;
      const table = element("table", undefined, region);
      element("caption", "Matching activity observations", table);
      const header = element("tr", undefined, element("thead", undefined, table));
      for (const label of ["Observation", "Organism", "Strain", "Activity", "Source", "Accessions"]) {
        element("th", label, header).scope = "col";
      }
      const body = element("tbody", undefined, table);
      for (const row of matches.slice(start, start + RESULT_SIZE)) {
        const tr = element("tr", undefined, body);
        const link = element("a", String(row[0]), element("td", undefined, tr));
        link.href = `activity-${Math.ceil(row[0] / Number(root.dataset.pageSize))}.html#observation-${row[0]}`;
        for (const value of [`${row[1]} ${row[2]}`.trim(), row[3], row[4], row[5], row[6]]) {
          element("td", value || "Not reported", tr);
        }
      }
      previous.disabled = page === 0;
      next.disabled = start + RESULT_SIZE >= matches.length;
      pager.querySelector("span").textContent = `Page ${page + 1} of ${Math.ceil(matches.length / RESULT_SIZE)}`;
    }

    async function search() {
      const ticket = ++generation;
      page = 0;
      const values = [query.value, activity.value, source.value];
      const url = new URL(location.href);
      ["q", "activity", "source"].forEach((name, i) => {
        if (values[i]) url.searchParams.set(name, values[i]); else url.searchParams.delete(name);
      });
      history.replaceState(null, "", url);
      retry.hidden = output.hidden = pager.hidden = true;
      const active = values.some(value => value.trim());
      fallback.hidden = Boolean(active);
      status.textContent = active ? "Searching all observations..." : "";
      if (!active) return;
      try {
        const data = await fetchJSON(root.dataset.index);
        const rows = validatePayload(data, root.dataset, true);
        if (ticket !== generation) return;
        matches = filterRows(rows, ...values);
        showResults();
      } catch (error) {
        if (ticket !== generation) return;
        status.textContent = `Search unavailable: ${error.message}`;
        retry.hidden = fallback.hidden = false;
      }
    }
    form.hidden = false;
    form.addEventListener("submit", event => { event.preventDefault(); search(); });
    form.addEventListener("input", search);
    form.addEventListener("reset", () => setTimeout(search, 0));
    retry.addEventListener("click", search);
    for (const button of [previous, next]) button.addEventListener("click", () => {
      page += Number(button.dataset.step);
      showResults();
    });
    search();
  }

  if (typeof module !== "undefined") module.exports = {normalize, filterRows, validatePayload, boundedBytes, fetchJSON};
  if (typeof document === "undefined") return;
  const supported = typeof DecompressionStream !== "undefined" && typeof crypto !== "undefined" && crypto.subtle;
  if (!supported) return;
  document.querySelectorAll(".activity-evidence").forEach(evidenceDetails);
  const root = document.querySelector("#activity-browser");
  if (root) browser(root);
})();
