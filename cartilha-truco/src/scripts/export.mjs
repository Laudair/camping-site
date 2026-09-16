import { mkdir } from "node:fs/promises";
import { createRequire } from "node:module";
import { dirname, join } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const require = createRequire(import.meta.url);

function loadPlaywright() {
  try {
    return require("playwright");
  } catch {
    const runtimeModules = process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES;
    if (!runtimeModules) throw new Error("Playwright nao encontrado. Rode npm install antes de exportar.");
    return require(join(runtimeModules, "playwright"));
  }
}

const { chromium } = loadPlaywright();
const root = dirname(dirname(fileURLToPath(import.meta.url)));
const outputDir = join(root, "exports");
const inputUrl = pathToFileURL(join(root, "index.html")).href;

await mkdir(outputDir, { recursive: true });

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({
  viewport: { width: 1240, height: 1754 },
  deviceScaleFactor: 2,
});

await page.goto(inputUrl, { waitUntil: "networkidle" });
await page.emulateMedia({ media: "print" });
await page.pdf({
  path: join(outputDir, "cartilha-truco.pdf"),
  width: "210mm",
  height: "297mm",
  printBackground: true,
  margin: { top: "0", right: "0", bottom: "0", left: "0" },
});

const pages = await page.locator(".page").count();
for (let index = 0; index < pages; index += 1) {
  const pageNumber = index + 1;
  await page.locator(".page").nth(index).screenshot({
    path: join(outputDir, `pagina-${pageNumber}.png`),
  });
}

await browser.close();
console.log(`Exportados ${pages} PNGs e 1 PDF em ${outputDir}`);
