<!-- SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau -->
<!-- SPDX-License-Identifier: Apache-2.0 OR MIT -->

# Security Policy

## Supported Versions

Only the current production deployment and latest source on `main` receive security fixes. Historical website tags are immutable records and are not maintained deployments.

| Version | Supported          |
| ------- | ------------------ |
| v0.0.2  | :white_check_mark: |
| < 0.0.2 | :x:                |

## Reporting a Vulnerability

Report vulnerabilities privately to **sebastian.rousseau@gmail.com** or use GitHub's private vulnerability reporting for this repository. Machine-readable disclosure metadata lives at [`/.well-known/security.txt`](.well-known/security.txt) per [RFC 9116](https://www.rfc-editor.org/rfc/rfc9116).

Please include:
- A description of the issue and its potential impact.
- Step-by-step reproduction instructions or a minimal proof of concept.
- Affected URLs or repository files.
- Do not submit real banking, payment, or confidential financial statement data.

You should receive an initial acknowledgement within 48 hours. Please allow reasonable time for investigation and coordinated remediation before public disclosure.

## How a Report is Handled

1. **Acknowledge**: The report is acknowledged privately within 48 hours.
2. **Assess**: We reproduce the issue, verify severity using CVSS metrics, and confirm remediation scope.
3. **Fix**: A fix is prepared and validated on a private branch with automated regression tests.
4. **Release**: The fix is deployed to `main` and released in a signed patch version.
5. **Disclose**: A GitHub Security Advisory is published detailing the vulnerability, with CVE assignment when applicable.

## Credit

Security researchers are credited by name in the release notes and GitHub Security Advisory, unless they request to remain anonymous.
