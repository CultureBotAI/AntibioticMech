/* Source subjects remain distinct even when their BioSample is shared. */
(() => {
  "use strict";
  const SIZE = 50;
  const accessionPatterns = {biosample_accession: /^SAM(N|D|EA)[0-9]+$/,
    bioproject_accession: /^PRJ(NA|EB|DB)[0-9]+$/, run_accession: /^[SED]RR[0-9]+$/};
  const integer = (value, minimum = 1) => Number.isSafeInteger(value) && value >= minimum;
  const text = value => typeof value === "string" && value.length > 0 && value.trim() === value;
  const hash = value => typeof value === "string" && /^[a-f0-9]{64}$/.test(value);
  const groupKey = group => JSON.stringify([group.source, group.source_version, group.source_observation_id]);

  function validateIndex(data, context) {
    if (!data || data.format !== "antibioticmech-membership-index-v1" ||
        data.identifier !== context.identifier || data.standard_inchi_key !== context.key ||
        !integer(data.total) || data.total !== Number(context.total) ||
        !Array.isArray(data.collections) || !data.collections.length ||
        !Array.isArray(data.groups) || !data.groups.length) throw new Error("Invalid membership index.");
    const paths = new Map();
    const sources = new Set();
    for (const ref of data.collections) {
      if (!ref || ref.format !== "antibioticmech-activity-memberships-v1" || !hash(ref.sha256) ||
          ref.path !== `membership-${ref.sha256}.json.gz` || paths.has(ref.path) ||
          !text(ref.source) || !text(ref.source_version) ||
          ![ref.subject_count, ref.observation_count, ref.membership_count, ref.measurement_count,
            ref.byte_size, ref.uncompressed_byte_size].every(value => integer(value)) ||
          !integer(ref.unlinked_subject_count, 0) || ref.unlinked_subject_count > ref.subject_count ||
          ref.byte_size > 16777216 || ref.uncompressed_byte_size > 16777216 ||
          !hash(ref.source_snapshot_sha256) || !hash(ref.activity_inventory_sha256)) {
        throw new Error("Invalid membership collection reference.");
      }
      const source = JSON.stringify([ref.source, ref.source_version]);
      if (sources.has(source)) throw new Error("Duplicate membership source.");
      sources.add(source);
      paths.set(ref.path, ref);
    }
    const keys = new Set(), numbers = new Set();
    for (const group of data.groups) {
      const ref = paths.get(group?.collection), observation = group?.observation;
      if (!ref || group.source !== ref.source || group.source_version !== ref.source_version ||
          !text(group.source_observation_id) || !hash(group.observation_sha256) ||
          !integer(group.number) || group.number > data.total || numbers.has(group.number) ||
          keys.has(groupKey(group)) || !observation || observation.source !== group.source ||
          observation.source_version !== group.source_version ||
          observation.source_observation_id !== group.source_observation_id ||
          !integer(observation.isolate_count) || !integer(observation.measurement_count) ||
          group.observation_href !== `activity-${Math.ceil(group.number / 100)}.html#observation-${group.number}`) {
        throw new Error("Invalid membership observation binding.");
      }
      keys.add(groupKey(group)); numbers.add(group.number);
    }
    for (const ref of paths.values()) {
      if (data.groups.filter(group => group.collection === ref.path).length !== ref.observation_count) {
        throw new Error("Incomplete membership observation index.");
      }
    }
    return data;
  }

  function validateCollection(data, index, ref) {
    if (!data || data.format !== ref.format || data.identifier !== index.identifier ||
        data.standard_inchi_key !== index.standard_inchi_key ||
        !["source", "source_version", "source_reference", "source_retrieved_on",
          "source_snapshot_sha256", "activity_inventory_sha256"].every(key => data[key] === ref[key]) ||
        !Array.isArray(data.subjects) || data.subjects.length !== ref.subject_count ||
        !Array.isArray(data.groups) || data.groups.length !== ref.observation_count) {
      throw new Error("Membership data does not match this compound and source.");
    }
    const ids = new Set();
    let unlinked = 0;
    for (const subject of data.subjects) {
      if (!subject || !text(subject.source_isolate_id) || ids.has(subject.source_isolate_id)) {
        throw new Error("Invalid source-isolate registry.");
      }
      ids.add(subject.source_isolate_id);
      if (subject.sequencing_context === null) unlinked++;
      else if (!subject.sequencing_context ||
          Object.keys(subject.sequencing_context).length !== 3 ||
          !Object.entries(accessionPatterns).every(([key, pattern]) =>
            typeof subject.sequencing_context[key] === "string" && pattern.test(subject.sequencing_context[key]))) {
        throw new Error("Invalid paired sequencing context.");
      }
    }
    const expected = new Map(index.groups.filter(group => group.collection === ref.path)
      .map(group => [group.source_observation_id, group]));
    const used = new Set(), groups = new Map();
    let measurements = 0, memberships = 0;
    for (const group of data.groups) {
      const binding = expected.get(group?.source_observation_id);
      if (!binding || groups.has(group.source_observation_id) ||
          group.observation_sha256 !== binding.observation_sha256 ||
          !Array.isArray(group.members) || group.members.length !== binding.observation.isolate_count) {
        throw new Error("Stale membership observation binding.");
      }
      const seen = new Set();
      let count = 0;
      for (const member of group.members) {
        if (!member || !integer(member.subject_index, 0) || member.subject_index >= data.subjects.length ||
            seen.has(member.subject_index) || !integer(member.measurement_count)) {
          throw new Error("Invalid source-isolate membership.");
        }
        seen.add(member.subject_index); used.add(member.subject_index);
        count += member.measurement_count;
      }
      if (count !== binding.observation.measurement_count) throw new Error("Membership measurement count mismatch.");
      measurements += count; memberships += group.members.length;
      groups.set(group.source_observation_id, group);
    }
    if (used.size !== data.subjects.length || measurements !== ref.measurement_count ||
        memberships !== ref.membership_count || unlinked !== ref.unlinked_subject_count) {
      throw new Error("Membership totals mismatch.");
    }
    return groups;
  }

  function selectGroup(index, params) {
    const fields = ["source", "version", "group"];
    if (!fields.some(key => params.has(key))) return index.groups[0];
    const match = index.groups.find(group => group.source === params.get("source") &&
      group.source_version === params.get("version") && group.source_observation_id === params.get("group"));
    if (!match) throw new Error("The requested observation is not in this membership index.");
    return match;
  }

  function filterMembers(subjects, members, query, context) {
    const tokens = query.normalize("NFKC").toLowerCase().trim().split(/\s+/).filter(Boolean);
    return members.filter(member => {
      const subject = subjects[member.subject_index], link = subject.sequencing_context;
      const value = [subject.source_isolate_id, ...Object.values(link || {})].join(" ").normalize("NFKC").toLowerCase();
      return (!context || (context === "linked" ? link !== null : link === null)) &&
        tokens.every(token => value.includes(token));
    });
  }

  async function browser(root) {
    const {fetchJSON, element, fullValue} = globalThis.AntibioticActivityData;
    const form = root.querySelector("form"), status = root.querySelector(".membership-status");
    const output = root.querySelector(".membership-results"), detail = root.querySelector(".membership-observation");
    const pager = root.querySelector(".membership-pager"), retry = root.querySelector(".membership-retry");
    const previous = pager.querySelector('[data-step="-1"]'), next = pager.querySelector('[data-step="1"]');
    const params = new URL(location.href).searchParams;
    const registries = new Map();
    let index, selected, registry, matches = [], page = 0, generation = 0;

    function fail(error) {
      status.textContent = error.message; retry.hidden = false; pager.hidden = true;
      output.replaceChildren(); detail.replaceChildren();
    }
    function render() {
      output.replaceChildren();
      const start = page * SIZE;
      status.textContent = matches.length ? `${matches.length} matching source isolates; ${start + 1}-${Math.min(start + SIZE, matches.length)} shown.` : "No matching source isolates.";
      pager.hidden = !matches.length;
      if (!matches.length) return;
      const region = element("div", undefined, output);
      region.className = "table-scroll"; region.tabIndex = 0;
      region.setAttribute("role", "region"); region.setAttribute("aria-label", "Source-isolate memberships");
      const table = element("table", undefined, region);
      element("caption", `${selected.source} source-isolate memberships`, table);
      const header = element("tr", undefined, element("thead", undefined, table));
      for (const label of ["Source isolate ID", "Measurements", "BioSample", "BioProject", "Sequencing run"]) {
        element("th", label, header).scope = "col";
      }
      const body = element("tbody", undefined, table);
      for (const member of matches.slice(start, start + SIZE)) {
        const subject = registry.subjects[member.subject_index], context = subject.sequencing_context;
        const row = element("tr", undefined, body);
        element("td", subject.source_isolate_id, row);
        element("td", String(member.measurement_count), row);
        for (const key of Object.keys(accessionPatterns)) {
          const cell = element("td", undefined, row);
          cell.append(fullValue(context?.[key] || "Not in snapshot", context ? key : ""));
        }
      }
      previous.disabled = page === 0; next.disabled = start + SIZE >= matches.length;
      pager.querySelector("span").textContent = `Page ${page + 1} of ${Math.ceil(matches.length / SIZE)}`;
    }
    async function search() {
      const ticket = ++generation;
      page = 0; retry.hidden = pager.hidden = true;
      output.replaceChildren(); detail.replaceChildren();
      status.textContent = "Loading source isolates...";
      try {
        const group = index.groups.find(item => groupKey(item) === form.elements.group.value);
        if (!group) throw new Error("Select an observation.");
        if (!registries.has(group.collection)) {
          const data = await fetchJSON(group.collection);
          const ref = index.collections.find(item => item.path === group.collection);
          registries.set(group.collection, {data, groups: validateCollection(data, index, ref)});
        }
        if (ticket !== generation) return;
        selected = group;
        const loaded = registries.get(group.collection);
        registry = loaded.data;
        matches = filterMembers(registry.subjects, loaded.groups.get(group.source_observation_id).members,
          form.elements.query.value, form.elements.context.value);
        const url = new URL(location.href);
        Object.entries({source: group.source, version: group.source_version, group: group.source_observation_id,
          q: form.elements.query.value, context: form.elements.context.value}).forEach(([key, value]) => {
          if (value) url.searchParams.set(key, value); else url.searchParams.delete(key);
        });
        history.replaceState(null, "", url);
        const observation = group.observation;
        const heading = element("h2", undefined, detail);
        element("a", `Observation ${group.number}`, heading).href = group.observation_href;
        element("p", [observation.taxon_label, observation.activity || "Call not reported",
          observation.mic_value === undefined ? "MIC not reported" :
            `${observation.mic_qualifier || ""}${observation.mic_value} ${observation.mic_units}`,
          observation.assay].filter(Boolean).join("; "), detail);
        element("p", `${observation.isolate_count} source isolates; ${observation.measurement_count} measurements`, detail);
        const evidence = element("details", undefined, detail);
        element("summary", "Assay and evidence", evidence); evidence.append(fullValue(observation));
        render();
      } catch (error) { if (ticket === generation) fail(error); }
    }
    async function start() {
      retry.hidden = true;
      try {
        index = validateIndex(await fetchJSON(root.dataset.index), root.dataset);
        form.elements.group.replaceChildren();
        const placeholder = element("option", "Select an observation", form.elements.group);
        placeholder.value = ""; placeholder.disabled = true;
        for (const group of index.groups) {
          const row = group.observation;
          const mic = row.mic_value === undefined ? "MIC not reported" :
            `MIC ${row.mic_qualifier || ""}${row.mic_value} ${row.mic_units}`;
          const option = element("option", `${group.number}: ${row.activity || "Unreported call"}; ${mic}; ${row.assay}; ${group.source_observation_id}`, form.elements.group);
          option.value = groupKey(group);
        }
        form.hidden = false;
        const group = selectGroup(index, params);
        form.elements.group.value = groupKey(group);
        form.elements.query.value = params.get("q") || "";
        const context = params.get("context") || "";
        if (!["", "linked", "unlinked"].includes(context)) throw new Error("Invalid sequencing-context filter.");
        form.elements.context.value = context;
        await search();
      } catch (error) { form.elements.group.value = ""; fail(error); }
    }
    form.addEventListener("submit", event => { event.preventDefault(); search(); });
    let timer;
    form.addEventListener("input", () => { generation++; clearTimeout(timer); timer = setTimeout(search, 120); });
    form.addEventListener("reset", event => {
      event.preventDefault(); form.elements.query.value = form.elements.context.value = ""; search();
    });
    retry.addEventListener("click", () => index && form.elements.group.value ? search() : start());
    for (const button of [previous, next]) button.addEventListener("click", () => {
      page += Number(button.dataset.step); render();
    });
    await start();
  }

  if (typeof module !== "undefined") module.exports = {validateIndex, validateCollection, selectGroup, filterMembers};
  if (typeof document === "undefined") return;
  const root = document.querySelector("#membership-browser");
  if (root && typeof DecompressionStream !== "undefined" && globalThis.crypto?.subtle) browser(root);
})();
