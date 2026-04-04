#!/usr/bin/env node

/**
 * fix-pwa-assets.mjs
 *
 * Ensures every manifest.json under docs/ has correct local icon entries
 * and that the referenced icon files exist alongside each manifest.
 */

import { readFileSync, writeFileSync, copyFileSync, existsSync, mkdirSync } from "node:fs";
import { execSync } from "node:child_process";
import { dirname, join, resolve } from "node:path";

const ROOT = resolve(import.meta.dirname, "..");
const DOCS = join(ROOT, "docs");
const ICONS_SRC = join(ROOT, "images", "icons");

const ICON_DEFS = [
  { src: "/images/icons/192x192.png", sizes: "192x192", type: "image/png" },
  { src: "/images/icons/512x512.png", sizes: "512x512", type: "image/png" },
];

// Ensure root-level icon files exist in docs/
const docsIcons = join(DOCS, "images", "icons");
if (!existsSync(docsIcons)) {
  mkdirSync(docsIcons, { recursive: true });
}
for (const icon of ICON_DEFS) {
  const srcFile = join(ICONS_SRC, `${icon.sizes}.png`);
  const destFile = join(DOCS, icon.src);
  if (existsSync(srcFile) && !existsSync(destFile)) {
    mkdirSync(dirname(destFile), { recursive: true });
    copyFileSync(srcFile, destFile);
  }
}

// Also ensure favicon.ico is in docs/images/
const faviconSrc = join(ROOT, "images", "favicon.ico");
const faviconDest = join(DOCS, "images", "favicon.ico");
if (existsSync(faviconSrc) && !existsSync(faviconDest)) {
  mkdirSync(dirname(faviconDest), { recursive: true });
  copyFileSync(faviconSrc, faviconDest);
}

// Also ensure logo webp is in docs/images/logos/
const logoSrc = join(ROOT, "images", "logos", "bankstatementparser.webp");
const logoDest = join(DOCS, "images", "logos", "bankstatementparser.webp");
if (existsSync(logoSrc) && !existsSync(logoDest)) {
  mkdirSync(dirname(logoDest), { recursive: true });
  copyFileSync(logoSrc, logoDest);
}

// Find all manifest.json files under docs/
const manifests = execSync(`find ${DOCS} -name manifest.json`, {
  encoding: "utf-8",
})
  .trim()
  .split("\n")
  .filter(Boolean);

let updated = 0;

for (const manifestPath of manifests) {
  const raw = readFileSync(manifestPath, "utf-8");
  let manifest;
  try {
    manifest = JSON.parse(raw);
  } catch {
    continue;
  }

  manifest.icons = ICON_DEFS.map((icon) => ({
    purpose: "any maskable",
    sizes: icon.sizes,
    src: icon.src,
    type: icon.type,
  }));

  const out = JSON.stringify(manifest, null, 2) + "\n";
  if (out !== raw) {
    writeFileSync(manifestPath, out);
    updated++;
  }
}

console.log(`Fixed ${updated} manifest(s), ensured icon assets in docs/`);
