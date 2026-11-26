// SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
// SPDX-License-Identifier: Apache-2.0 OR MIT
//
// Lighthouse CI over every page of the built site (docs/, the tree the
// deploy job publishes), with Lighthouse's default simulated mobile
// throttling. The page list is derived from the build, not hand-kept:
//
// - redirect stubs (meta refresh, from config/redirects.json) are not
//   collected, because Lighthouse would follow them to the live site;
// - noindex pages (404, offline) skip the SEO category, which fails
//   is-crawlable by design there, and assert every other SEO audit.
"use strict";

const fs = require("node:fs");
const path = require("node:path");

const SITE = "docs";
const REDIRECT = /<meta http-equiv="refresh"/;
const NOINDEX = /<meta name="robots" content="[^"]*noindex/;
// Lighthouse 13's weighted SEO audits, less is-crawlable.
const SEO_AUDITS = [
  "document-title",
  "meta-description",
  "http-status-code",
  "link-text",
  "crawlable-anchors",
  "robots-txt",
  "image-alt",
  "hreflang",
  "canonical",
];

function htmlFiles(dir) {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
    const full = path.join(dir, entry.name);
    if (entry.name.startsWith(".")) return [];
    if (entry.isDirectory()) return htmlFiles(full);
    return entry.name.endsWith(".html") ? [full] : [];
  });
}

const pages = htmlFiles(SITE)
  .sort()
  .map((file) => ({
    rel: path.relative(SITE, file).split(path.sep).join("/"),
    html: fs.readFileSync(file, "utf8"),
  }))
  .filter((page) => !REDIRECT.test(page.html));

const escape = (text) => text.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
const noindex = pages.filter((page) => NOINDEX.test(page.html)).map((page) => escape(page.rel));
// `(?!)` never matches, so with no noindex page every page gets SEO.
const noindexUrl = noindex.length ? `/(?:${noindex.join("|")})$` : "(?!)";

const shared = {
  "categories:performance": ["error", { minScore: 1 }],
  "categories:accessibility": ["error", { minScore: 1 }],
  "categories:best-practices": ["error", { minScore: 1 }],
  "first-contentful-paint": ["error", { maxNumericValue: 1000 }],
  "largest-contentful-paint": ["error", { maxNumericValue: 1200 }],
  "cumulative-layout-shift": ["error", { maxNumericValue: 0 }],
  "color-contrast": "error",
  "document-title": "error",
  "html-has-lang": "error",
  "meta-description": "error",
};

module.exports = {
  ci: {
    collect: {
      staticDistDir: `./${SITE}`,
      url: pages.map((page) => `http://localhost/${page.rel}`),
      numberOfRuns: 3,
      settings: {
        // GitHub's Ubuntu 24.04 runners forbid the user namespaces
        // Chrome's sandbox needs; the flag does not change any metric.
        chromeFlags: process.env.CI ? "--no-sandbox" : "",
      },
    },
    assert: {
      assertMatrix: [
        {
          matchingUrlPattern: `^(?!.*${noindexUrl})`,
          assertions: { ...shared, "categories:seo": ["error", { minScore: 1 }] },
        },
        {
          matchingUrlPattern: noindexUrl,
          assertions: {
            ...shared,
            ...Object.fromEntries(SEO_AUDITS.map((id) => [id, "error"])),
          },
        },
      ],
    },
  },
};
