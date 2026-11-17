const assert = require("node:assert/strict");
const fs = require("node:fs");
const http = require("node:http");
const path = require("node:path");
const zlib = require("node:zlib");
const {chromium} = require(process.env.PLAYWRIGHT_MODULE || "playwright");
if (process.argv.length !== 4) throw new Error("Usage: node tests/membership_browser.playwright.cjs <site> <report-directory>");
const root = path.resolve(process.argv[2]);
const output = path.resolve(process.argv[3]);
fs.mkdirSync(output, {recursive:true});
const folder = path.join(root, "antimycobacterial/isoniazide");
const name = fs.readdirSync(folder).find(name => name.startsWith("membership-index-"));
const index = JSON.parse(zlib.gunzipSync(fs.readFileSync(path.join(folder, name))));
const group = index.groups.reduce((a,b) => a.observation.isolate_count > b.observation.isolate_count ? a : b);
const data = JSON.parse(zlib.gunzipSync(fs.readFileSync(path.join(folder, group.collection))));
const members = data.groups.find(row => row.source_observation_id === group.source_observation_id).members;
const linked = members.find(member => data.subjects[member.subject_index].sequencing_context);
const subject = data.subjects[linked.subject_index];
const server = http.createServer((request,response) => {
  const filename = path.resolve(root, "." + decodeURIComponent(new URL(request.url,"http://local").pathname));
  if (!filename.startsWith(root + path.sep)) {response.writeHead(403).end(); return;}
  fs.readFile(filename, (error,bytes) => {
    if (error) {response.writeHead(404).end(); return;}
    const type = filename.endsWith(".js") ? "application/javascript" : filename.endsWith(".css") ? "text/css" :
      filename.endsWith(".html") ? "text/html" : "application/octet-stream";
    response.writeHead(200, {"Content-Type":type}); response.end(bytes);
  });
});
(async () => {
  await new Promise(resolve => server.listen(0,"127.0.0.1",resolve));
  let browser;
  try {
    browser = await chromium.launch({headless:true,channel:process.env.CHROMIUM_CHANNEL || "chrome"});
    const origin = `http://127.0.0.1:${server.address().port}`;
    const context = await browser.newContext({viewport:{width:1440,height:1000}});
    const errors = [], external = [];
    await context.route("**/*", route => {
      if (new URL(route.request().url()).origin !== origin) { external.push(route.request().url()); return route.abort(); }
      return route.continue();
    });
    const page = await context.newPage();
    page.on("pageerror", error => errors.push(error.message));
    const params = new URLSearchParams({source:group.source,version:group.source_version,group:group.source_observation_id});
    const url = `${origin}/antimycobacterial/isoniazide/memberships.html?${params}`;
    await page.goto(url);
    await page.waitForFunction(() => document.querySelector(".membership-status").textContent.includes("matching source isolates"), {timeout:30000});
    assert.equal(await page.locator(".membership-results tbody tr").count(),50);
    const first = await page.locator(".membership-results tbody tr").first().textContent();
    await page.getByRole("button",{name:"Next isolates",exact:true}).click();
    assert.notEqual(await page.locator(".membership-results tbody tr").first().textContent(),first);
    await page.getByRole("button",{name:"Previous isolates",exact:true}).click();
    assert.equal(await page.locator(".membership-results tbody tr").first().textContent(),first);
    await page.screenshot({path:path.join(output,"desktop.png"),fullPage:true});
    await page.locator('input[name="query"]').fill(subject.source_isolate_id);
    await page.waitForFunction(() => document.querySelectorAll(".membership-results tbody tr").length === 1);
    assert.ok((await page.locator(".membership-results tbody tr").innerText()).includes(subject.sequencing_context.run_accession));
    await page.locator('input[name="query"]').fill(subject.sequencing_context.run_accession);
    await page.waitForTimeout(250);
    assert.equal(await page.locator(".membership-results tbody tr").count(),1);
    await page.getByRole("button",{name:"Reset",exact:true}).click();
    await page.waitForFunction(() => document.querySelectorAll(".membership-results tbody tr").length === 50);
    await page.locator('select[name="context"]').selectOption("unlinked");
    await page.waitForTimeout(300);
    const unlinked = members.filter(member => data.subjects[member.subject_index].sequencing_context === null).length;
    assert.ok((await page.locator(".membership-status").innerText()).startsWith(String(unlinked)+" "));
    if (unlinked) assert.ok((await page.locator(".membership-results tbody tr").first().innerText()).includes("Not in snapshot"));
    await page.setViewportSize({width:390,height:844});
    await page.screenshot({path:path.join(output,"mobile.png"),fullPage:true});
    const overflow = await page.evaluate(() => ({body:document.documentElement.scrollWidth, width:innerWidth,
      controls:[...document.querySelectorAll("input,select,button")].filter(node => !node.closest("[hidden]"))
        .filter(node => node.getBoundingClientRect().right > innerWidth + 1).map(node=>node.outerHTML)}));
    assert.ok(overflow.body <= overflow.width+1,JSON.stringify(overflow));
    assert.deepEqual(overflow.controls,[]);
    const geometry = await page.locator(".membership-results tbody tr").evaluateAll(rows =>
      rows.map(row => ({height:row.getBoundingClientRect().height, width:row.cells[0].getBoundingClientRect().width})));
    assert.ok(geometry.every(row => row.height < 100 && row.width >= 300),JSON.stringify(geometry));
    await page.goto(`${origin}/antimycobacterial/isoniazide/activity-1.html?q=${encodeURIComponent(subject.sequencing_context.run_accession)}`);
    await page.waitForFunction(() => document.querySelector(".activity-status").textContent.includes("matching observations"));
    assert.ok(await page.locator(".activity-results tbody tr").count() > 0);
    await page.goto(url.replace(/group=[^&]+/,"group=not-an-observation"));
    await page.waitForFunction(() => document.querySelector(".membership-status").textContent.includes("requested observation"));
    assert.equal(await page.locator(".membership-results tbody tr").count(),0);
    await page.getByRole("button",{name:"Retry",exact:true}).click();
    await page.waitForTimeout(250);
    assert.equal(await page.locator(".membership-results tbody tr").count(),0);
    await context.close();
    const corrupt = await browser.newContext();
    await corrupt.route("**/*", route => {
      if (new URL(route.request().url()).origin !== origin) { external.push(route.request().url()); return route.abort(); }
      return route.continue();
    });
    const broken = await corrupt.newPage();
    const registryRoute = /\/membership-[a-f0-9]{64}\.json\.gz$/;
    await broken.route(registryRoute, route => route.fulfill({status:200,body:"corrupt"}));
    await broken.goto(url);
    await broken.waitForFunction(() => document.querySelector(".membership-status").textContent.includes("checksum mismatch"));
    assert.equal(await broken.locator(".membership-results tbody tr").count(),0);
    await broken.unroute(registryRoute);
    await broken.getByRole("button",{name:"Retry",exact:true}).click();
    await broken.waitForFunction(() => document.querySelector(".membership-status").textContent.includes("matching source isolates"));
    await corrupt.close();
    assert.deepEqual(errors,[]); assert.deepEqual(external,[]);
    fs.writeFileSync(path.join(output,"browser-report.json"),JSON.stringify({group:group.source_observation_id,
      isolate_count:group.observation.isolate_count, unlinked, pagination:true, search:true, invalid_group:true,
      corrupt_download_retry:true, desktop_mobile:true, errors, external},null,2)+"\n");
    console.log("Browser checks passed",{group:group.source_observation_id,unlinked});
  } finally {
    if (browser) await browser.close();
    await new Promise(resolve => server.close(resolve));
  }
})().catch(error=>{console.error(error);process.exitCode=1;});
