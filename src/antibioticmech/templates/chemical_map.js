(() => {
  "use strict";

  const root = document.getElementById("chemical-map");
  if (!root) return;

  const canvas = document.getElementById("map-canvas");
  const context = canvas.getContext("2d");
  const search = document.getElementById("map-search");
  const classFilter = document.getElementById("map-class");
  const colorMode = document.getElementById("map-color");
  const reset = document.getElementById("map-reset");
  const status = document.getElementById("map-status");
  const legend = document.getElementById("map-legend");
  const selection = document.getElementById("map-selection");
  const results = document.getElementById("map-results");
  const tooltip = document.getElementById("map-tooltip");

  const classColors = {
    ANTIBACTERIAL: "#3764a5",
    ANTIMYCOBACTERIAL: "#6c4ca5",
    ANTIFUNGAL: "#b45f35",
    ANTIPROTOZOAL: "#168477",
    ANTIVIRAL: "#be3f70",
    BIOCIDE: "#8b6a18",
    ANTIMICROBIAL_UNSPECIFIED: "#64748b",
    OTHER: "#64748b"
  };
  const alternatePalettes = {
    input: {SMILES: "#3764a5", INCHI_FALLBACK: "#d36b28"},
    fragments: {single: "#3764a5", multiple: "#be3f70"}
  };

  const state = {
    records: [],
    byId: new Map(),
    visible: [],
    selected: null,
    hovered: null,
    bounds: null,
    width: 0,
    height: 0,
    dpr: 1
  };

  function colorKey(record) {
    if (colorMode.value === "input") return record.structure_input;
    if (colorMode.value === "fragments") {
      return record.fragment_count > 1 ? "multiple" : "single";
    }
    return record.antimicrobial_class;
  }

  function pointColor(record) {
    if (colorMode.value === "class") {
      return classColors[record.antimicrobial_class] || "#64748b";
    }
    return alternatePalettes[colorMode.value][colorKey(record)] || "#64748b";
  }

  function rebuildLegend() {
    const entries = new Map();
    state.visible.forEach((record) => entries.set(colorKey(record), pointColor(record)));
    legend.replaceChildren();
    [...entries.entries()].sort(([left], [right]) => left.localeCompare(right))
      .forEach(([label, color]) => {
        const item = document.createElement("span");
        const swatch = document.createElement("i");
        swatch.style.backgroundColor = color;
        item.append(swatch, document.createTextNode(label.replaceAll("_", " ")));
        legend.append(item);
      });
  }

  function resizeCanvas() {
    const rect = canvas.getBoundingClientRect();
    state.dpr = Math.min(window.devicePixelRatio || 1, 2);
    state.width = Math.max(320, Math.round(rect.width));
    state.height = Math.max(420, Math.round(rect.height));
    canvas.width = Math.round(state.width * state.dpr);
    canvas.height = Math.round(state.height * state.dpr);
    context.setTransform(state.dpr, 0, 0, state.dpr, 0, 0);
    draw();
  }

  function projected(record) {
    const padding = 24;
    const width = Math.max(1, state.bounds.maxX - state.bounds.minX);
    const height = Math.max(1, state.bounds.maxY - state.bounds.minY);
    return {
      x: padding + ((record.x - state.bounds.minX) / width) * (state.width - 2 * padding),
      y: state.height - padding -
        ((record.y - state.bounds.minY) / height) * (state.height - 2 * padding)
    };
  }

  function draw() {
    if (!state.bounds || !context) return;
    context.clearRect(0, 0, state.width, state.height);
    context.fillStyle = getComputedStyle(canvas).backgroundColor;
    context.fillRect(0, 0, state.width, state.height);
    state.visible.forEach((record) => {
      const point = projected(record);
      const selected = state.selected && record.identifier === state.selected.identifier;
      const hovered = state.hovered && record.identifier === state.hovered.identifier;
      context.beginPath();
      context.arc(point.x, point.y, selected ? 6 : hovered ? 5 : 2.6, 0, Math.PI * 2);
      context.fillStyle = pointColor(record);
      context.globalAlpha = selected || hovered ? 1 : 0.72;
      context.fill();
      if (selected) {
        context.lineWidth = 2;
        context.strokeStyle = "#111827";
        context.stroke();
      }
    });
    context.globalAlpha = 1;
  }

  function nearestPoint(event) {
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    let closest = null;
    let closestDistance = 144;
    state.visible.forEach((record) => {
      const point = projected(record);
      const squared = (point.x - x) ** 2 + (point.y - y) ** 2;
      if (squared < closestDistance) {
        closest = record;
        closestDistance = squared;
      }
    });
    return closest;
  }

  function link(path, text, className = "") {
    const anchor = document.createElement("a");
    anchor.href = path;
    anchor.textContent = text;
    if (className) anchor.className = className;
    return anchor;
  }

  function selectRecord(record, updateUrl = true) {
    state.selected = record;
    selection.replaceChildren();
    const heading = document.createElement("h2");
    heading.append(link(record.path, record.label));
    const identity = document.createElement("p");
    identity.className = "meta";
    identity.textContent = record.identifier;
    const badges = document.createElement("p");
    badges.className = "map-badges";
    [record.antimicrobial_class.replaceAll("_", " "), record.structure_input]
      .concat(record.fragment_count > 1 ? [`${record.fragment_count} fragments`] : [])
      .forEach((text) => {
        const badge = document.createElement("span");
        badge.className = "pill plain";
        badge.textContent = text;
        badges.append(badge);
      });
    const structure = document.createElement("p");
    const code = document.createElement("code");
    code.textContent = record.canonical_isomeric_smiles;
    structure.append(code);
    const neighborHeading = document.createElement("h3");
    neighborHeading.textContent = "Nearest chemical neighbors";
    const neighborList = document.createElement("ol");
    neighborList.className = "map-neighbors";
    record.neighbors.forEach((neighbor) => {
      const target = state.byId.get(neighbor.identifier);
      const item = document.createElement("li");
      const button = document.createElement("button");
      button.type = "button";
      button.className = "map-neighbor-select";
      button.textContent = target ? target.label : neighbor.identifier;
      button.addEventListener("click", () => selectRecord(target));
      const distance = document.createElement("span");
      distance.textContent = `distance ${neighbor.distance.toFixed(3)}`;
      item.append(button, distance);
      neighborList.append(item);
    });
    selection.append(heading, identity, badges, structure, neighborHeading, neighborList);
    status.textContent = `Selected ${record.label}; showing ${state.visible.length} points.`;
    if (updateUrl) {
      const url = new URL(window.location.href);
      url.searchParams.set("id", record.identifier);
      history.replaceState(null, "", url);
    }
    draw();
  }

  function updateResults() {
    const query = search.value.trim().toLocaleLowerCase();
    results.replaceChildren();
    if (!query) {
      const item = document.createElement("li");
      item.textContent = "Enter a name, synonym, or identifier.";
      results.append(item);
      return;
    }
    const matches = state.visible.filter((record) => record.search.includes(query)).slice(0, 20);
    if (!matches.length) {
      const item = document.createElement("li");
      item.textContent = "No visible compounds match.";
      results.append(item);
      return;
    }
    matches.forEach((record) => {
      const item = document.createElement("li");
      const button = document.createElement("button");
      button.type = "button";
      button.textContent = record.label;
      button.addEventListener("click", () => selectRecord(record));
      const id = document.createElement("span");
      id.textContent = record.identifier;
      item.append(button, id);
      results.append(item);
    });
  }

  function applyFilters() {
    const selectedClass = classFilter.value;
    state.visible = state.records.filter(
      (record) => !selectedClass || record.antimicrobial_class === selectedClass
    );
    if (state.selected && !state.visible.includes(state.selected)) {
      state.selected = null;
      selection.innerHTML = "<h2>Select a compound</h2><p>The previous selection is hidden by the class filter.</p>";
    }
    status.textContent = `Showing ${state.visible.length} of ${state.records.length} compounds.`;
    rebuildLegend();
    updateResults();
    draw();
  }

  function showTooltip(event, record) {
    if (!record) {
      tooltip.hidden = true;
      return;
    }
    tooltip.textContent = `${record.label} · ${record.identifier}`;
    const stage = canvas.parentElement.getBoundingClientRect();
    tooltip.style.left = `${event.clientX - stage.left + 12}px`;
    tooltip.style.top = `${event.clientY - stage.top + 12}px`;
    tooltip.hidden = false;
  }

  async function initialize() {
    try {
      const response = await fetch(root.dataset.source);
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const artifact = await response.json();
      state.records = artifact.records.map((record) => ({
        ...record,
        search: [record.identifier, record.label, record.structural_class, ...record.synonyms]
          .join("\n").toLocaleLowerCase()
      }));
      state.records.forEach((record) => state.byId.set(record.identifier, record));
      state.visible = state.records.slice();
      state.bounds = {
        minX: Math.min(...state.records.map((record) => record.x)),
        maxX: Math.max(...state.records.map((record) => record.x)),
        minY: Math.min(...state.records.map((record) => record.y)),
        maxY: Math.max(...state.records.map((record) => record.y))
      };
      [...new Set(state.records.map((record) => record.antimicrobial_class))]
        .sort()
        .forEach((name) => {
          const option = document.createElement("option");
          option.value = name;
          option.textContent = name.replaceAll("_", " ");
          classFilter.append(option);
        });
      rebuildLegend();
      resizeCanvas();
      updateResults();
      status.textContent = `Showing all ${state.records.length} compounds.`;
      const requested = new URL(window.location.href).searchParams.get("id");
      if (requested && state.byId.has(requested)) selectRecord(state.byId.get(requested), false);
    } catch (error) {
      status.textContent = `Chemical map could not be loaded: ${error.message}`;
      status.classList.add("error");
    }
  }

  search.addEventListener("input", updateResults);
  classFilter.addEventListener("change", applyFilters);
  colorMode.addEventListener("change", () => {
    rebuildLegend();
    draw();
  });
  reset.addEventListener("click", () => {
    search.value = "";
    classFilter.value = "";
    colorMode.value = "class";
    const url = new URL(window.location.href);
    url.searchParams.delete("id");
    history.replaceState(null, "", url);
    applyFilters();
  });
  canvas.addEventListener("click", (event) => {
    const record = nearestPoint(event);
    if (record) selectRecord(record);
  });
  canvas.addEventListener("pointermove", (event) => {
    state.hovered = nearestPoint(event);
    canvas.style.cursor = state.hovered ? "pointer" : "default";
    showTooltip(event, state.hovered);
    draw();
  });
  canvas.addEventListener("pointerleave", () => {
    state.hovered = null;
    tooltip.hidden = true;
    draw();
  });
  new ResizeObserver(resizeCanvas).observe(canvas);
  initialize();
})();
