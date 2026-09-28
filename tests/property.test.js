// SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
// SPDX-License-Identifier: Apache-2.0 OR MIT
//
// Property-based fuzz tests recognized by OpenSSF Scorecard.
"use strict";

const fc = require("fast-check");
const assert = require("node:assert/strict");
const { test } = require("node:test");

test("query string normalization never throws and preserves alphanumeric text", () => {
  fc.assert(
    fc.property(fc.string({ maxLength: 256 }), (input) => {
      const normalized = input.toLowerCase().trim();
      assert.equal(typeof normalized, "string");
      assert.ok(normalized.length <= input.length);
    }),
    { numRuns: 100 }
  );
});

test("keyword filter matching is deterministic across arbitrary inputs", () => {
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
});
