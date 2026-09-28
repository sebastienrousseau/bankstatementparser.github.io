<!-- SPDX-License-Identifier: Apache-2.0 OR MIT -->

# Security Policy

## Supported versions

Only the current production deployment at <https://bankstatementparser.com/>
and the latest source on `main` receive security fixes. Historical release
tags are immutable records, not maintained deployments.

## Reporting a vulnerability

Please do **not** open a public GitHub issue for a suspected security
vulnerability.

Report it privately, either through GitHub's
[private vulnerability reporting](https://github.com/sebastienrousseau/bankstatementparser.github.io/security/advisories/new)
for this repository, or by email to **sebastian.rousseau@gmail.com**.
Machine-readable disclosure metadata is in [`/.well-known/security.txt`](.well-known/security.txt),
per [RFC 9116](https://www.rfc-editor.org/rfc/rfc9116).

Include the affected URL or file, the impact, steps to reproduce, and a safe
proof of concept. Do not send real bank statements or account data.

## How a report is handled

1. **Acknowledge** the report privately within seven days.
2. **Assess** it: reproduce the issue, decide whether it is a vulnerability,
   and rate its severity with CVSS. The reporter hears the outcome.
3. **Fix** it on a private branch or a GitHub security advisory draft, with
   a regression test or gate that fails without the fix.
4. **Release** the fix: deploy the site from `main` and cut a patch release
   whose notes identify the vulnerability.
5. **Disclose** it through a GitHub security advisory once the fix is live,
   with a CVE when one applies. Please allow reasonable time for this
   coordinated disclosure before publishing details yourself.

## Credit

Reporters are credited by name in the advisory and the release notes,
unless they ask to remain anonymous.
