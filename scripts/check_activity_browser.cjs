/* Optional live-browser QA: NODE_PATH=<playwright install>/node_modules node this-file URL OUTPUT_DIR */
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const zlib = require("node:zlib");
const {chromium} = require("playwright");

const url = process.argv[2];
const output = process.argv[3];
assert(url && output, "Pass a first activity-page URL and an output directory");
fs.mkdirSync(output, {recursive: true});

function values(value) {
  if (Array.isArray(value)) return value.flatMap(values);
  if (value && typeof value === "object") return Object.values(value).flatMap(values);
  return [String(value)];
}

(async () => {
  const browser = await chromium.launch({channel: process.env.PLAYWRIGHT_CHANNEL || "chrome"});
  const report = {url, browser: browser.version(), viewports: []};
  try {
    for (const viewport of [{width: 1440, height: 1000}, {width: 390, height: 844}]) {
      const context = await browser.newContext({viewport, colorScheme: "light"});
      const page = await context.newPage();
      const errors = [];
      page.on("pageerror", error => errors.push(error.message));
      await page.goto(url);
      await page.locator(".activity-filters").waitFor({state: "visible"});
      assert.equal(await page.locator(".activity-default tbody tr").count(), 100);
      const downloadHref = await page.getByRole("link", {name: "Complete record (JSON.gz)"}).getAttribute("href");
      const response = await context.request.get(new URL(downloadHref, url).href);
      assert(response.ok());
      const record = JSON.parse(zlib.gunzipSync(await response.body()));
      const observations = record.activity_spectrum;
      assert(observations.length > 100, "This QA run requires a multi-page compound");
      const overflow = await page.evaluate(() => ({width: innerWidth, document: document.documentElement.scrollWidth}));
      assert(overflow.document <= overflow.width, JSON.stringify(overflow));
      await page.screenshot({path: path.join(output, `activity-${viewport.width}.png`)});

      const details = page.locator(".activity-evidence").first();
      await details.locator("summary").click();
      await details.locator(".activity-detail > dl").waitFor();
      const text = await details.locator(".activity-detail").textContent();
      for (const value of values(observations[0])) assert(text.includes(value), `Missing evidence value: ${value}`);
      await details.locator("summary").click();

      const query = page.getByRole("searchbox");
      const last = observations.at(-1);
      const term = last.biosample_accession || last.source_observation_id || last.strain;
      assert(term, "The last observation must have a searchable identity");
      await query.fill(term);
      await page.waitForFunction(() => document.querySelector(".activity-status").textContent.includes("matching observations;"));
      const expectedNumber = observations.length;
      // Search may return several assays for one sample, but must reach the final observation.
      while (!await page.locator(".activity-results").getByRole("link", {name: String(expectedNumber), exact: true}).count()) {
        assert(await page.locator('.activity-results-pager [data-step="1"]').isEnabled());
        await page.locator('.activity-results-pager [data-step="1"]').click();
      }
      await page.locator(".activity-results").getByRole("link", {name: String(expectedNumber), exact: true}).click();
      await page.waitForURL(`**#observation-${expectedNumber}`);
      const lastRow = page.locator(`#observation-${expectedNumber}`);
      assert(await lastRow.count());
      await lastRow.locator("summary").click();
      await lastRow.locator(".activity-detail > dl").waitFor();
      const lastText = await lastRow.locator(".activity-detail").textContent();
      for (const value of values(last)) assert(lastText.includes(value), `Missing final evidence: ${value}`);
      await page.goto(url);
      await page.getByLabel("Page", {exact: true}).fill(String(Math.ceil(observations.length / 100)));
      await page.getByRole("button", {name: "Go", exact: true}).click();
      await page.waitForURL(`**/activity-${Math.ceil(observations.length / 100)}.html`);
      assert(await page.locator(`#observation-${expectedNumber}`).count());

      await page.goto(url);
      const filter = page.locator('select[name="activity"]');
      const call = observations.find(row => row.activity)?.activity;
      assert(call);
      await filter.selectOption(`=${call}`);
      const expectedMatches = observations.filter(row => row.activity === call).length;
      await page.waitForFunction(n => document.querySelector(".activity-status").textContent.startsWith(`${n} matching observations;`), expectedMatches);
      assert.equal(await page.locator(".activity-results tbody tr").count(), Math.min(50, expectedMatches));
      if (expectedMatches > 50) {
        await page.locator('.activity-results-pager [data-step="1"]').click();
        assert((await page.locator(".activity-status").textContent()).includes("51-"));
      }
      await page.getByRole("searchbox").fill("nonexistent-accession-qa");
      await page.waitForFunction(() => document.querySelector(".activity-status").textContent === "No matching observations.");
      await page.getByRole("button", {name: "Reset", exact: true}).click();
      await page.locator(".activity-default").waitFor({state: "visible"});
      assert.equal(await page.locator(".activity-default tbody tr").count(), 100);
      assert.deepEqual(errors, []);
      report.viewports.push({viewport, observations: observations.length, overflow, checks: "evidence, cross-page search, page jump, filtering, result pagination, empty state, reset"});
      await context.close();
    }

    const context = await browser.newContext();
    const page = await context.newPage();
    await context.route("**/search-*.json.gz", route => route.fulfill({status: 200, body: "corrupt"}));
    await page.goto(url);
    await page.getByRole("searchbox").fill("coli");
    await page.getByRole("button", {name: "Retry search"}).waitFor({state: "visible"});
    assert((await page.locator(".activity-status").textContent()).includes("checksum mismatch"));
    await context.unroute("**/search-*.json.gz");
    await page.getByRole("button", {name: "Retry search"}).click();
    await page.waitForFunction(() => document.querySelector(".activity-status").textContent.includes("matching observations;"));
    await page.getByRole("button", {name: "Reset", exact: true}).click();
    await page.locator(".activity-default").waitFor({state: "visible"});
    await context.route("**/activity-*-*.json.gz", route => route.fulfill({status: 404, body: "missing"}));
    const details = page.locator(".activity-evidence").first();
    await details.locator("summary").click();
    await details.getByRole("button", {name: "Retry evidence"}).waitFor({state: "visible"});
    await context.unroute("**/activity-*-*.json.gz");
    await details.getByRole("button", {name: "Retry evidence"}).click();
    await details.locator(".activity-detail > dl").waitFor();
    await context.close();

    const nojs = await browser.newContext({javaScriptEnabled: false, viewport: {width: 390, height: 844}});
    const staticPage = await nojs.newPage();
    await staticPage.goto(url);
    assert.equal(await staticPage.locator(".activity-default tbody tr").count(), 100);
    await staticPage.getByRole("navigation", {name: "Activity pages", exact: true}).getByRole("link", {name: "Last", exact: true}).click();
    assert(await staticPage.locator(".activity-default tbody tr").count() <= 100);
    assert(await staticPage.getByRole("link", {name: "Complete record (JSON.gz)"}).count());
    await staticPage.locator(".activity-evidence summary").first().click();
    assert(await staticPage.getByRole("link", {name: "Page data (JSON.gz)"}).first().isVisible());
    await nojs.close();
    report.fallbacks = "corrupt search retry, missing evidence retry, no-JavaScript pagination/downloads";
    fs.writeFileSync(path.join(output, "browser-qa.json"), JSON.stringify(report, null, 2) + "\n");
    console.log(JSON.stringify(report, null, 2));
  } finally { await browser.close(); }
})().catch(error => { console.error(error); process.exitCode = 1; });
