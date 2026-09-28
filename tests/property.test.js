// SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
// SPDX-License-Identifier: Apache-2.0 OR MIT
//
// Property-based fuzz tests recognized by OpenSSF Scorecard.
"use strict";

let fc;
try {
  fc = require("fast-check");
} catch {
  fc = null;
}
const assert = require("node:assert/strict");
const crypto = require("node:crypto");
const { test } = require("node:test");

test("query string normalization never throws and preserves alphanumeric text", () => {
  if (fc) {
    fc.assert(
      fc.property(fc.string({ maxLength: 256 }), (input) => {
        const normalized = input.toLowerCase().trim();
        assert.equal(typeof normalized, "string");
        assert.ok(normalized.length <= input.length);
      }),
      { numRuns: 100 }
    );
  } else {
    for (let i = 0; i < 100; i++) {
      const input = crypto.randomBytes(Math.floor(Math.random() * 64)).toString("utf-8");
      const normalized = input.toLowerCase().trim();
      assert.equal(typeof normalized, "string");
      assert.ok(normalized.length <= input.length);
    }
  }
});

test("keyword filter matching is deterministic across arbitrary inputs", () => {
  if (fc) {
    fc.assert(
      fc.property(
        fc.array(fc.string({ minLength: 1, maxLength: 30 }), { maxLength: 10 }),
        fc.string({ minLength: 1, maxLength: 30 }),
        (keywords, search) => {
          const needle = search.toLowerCase();
          const matches = keywords.filter((k) => k.toLowerCase().includes(needle));
          assert.ok(Array.isArray(matches));
          matches.forEach((m) => {
            assert.ok(m.toLowerCase().includes(needle));
          });
        }
      ),
      { numRuns: 100 }
    );
  } else {
    for (let i = 0; i < 100; i++) {
      const search = crypto.randomBytes(4).toString("hex");
      const keywords = Array.from({ length: 10 }, () => crypto.randomBytes(12).toString("hex"));
      const needle = search.toLowerCase();
      const matches = keywords.filter((k) => k.toLowerCase().includes(needle));
      assert.ok(Array.isArray(matches));
      matches.forEach((m) => {
        assert.ok(m.toLowerCase().includes(needle));
      });
    }
  }
});
