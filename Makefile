# SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
.PHONY: all build audit contrast validate lint test verify serve clean help

all: verify

help:
	@echo "Available Makefile targets:"
	@echo "  make build      - Compile static site using Rust static-site-generator"
	@echo "  make audit      - Run WCAG 2.2 AAA checks and SSG audit"
	@echo "  make contrast   - Verify color tokens against WCAG 2.2 AAA math ratios"
	@echo "  make validate   - Validate Markdown frontmatter schema integrity"
	@echo "  make lint       - Validate README, release versions, notes, and SPDX headers"
	@echo "  make test       - Run automated regression tests"
	@echo "  make verify     - Run full gate: lint, test, audit"
	@echo "  make serve      - Serve compiled site locally from public/"
	@echo "  make clean      - Remove build artifacts and temporary files"

build:
	@ssg build --content _posts --template _layouts --output public
	@python3 scripts/post-build.py

test:
	@python3 scripts/regression-test.py

audit: contrast validate
	ssg audit -f ssg.toml -o public --severity warn --fail-on warn

contrast:
	@python3 scripts/audit-contrast.py

validate:
	@python3 scripts/validate-frontmatter.py

lint:
	@./scripts/verify_release_version.sh
	@python3 scripts/validate_readme.py
	@python3 scripts/release_notes.py --check
	@python3 scripts/validate_spdx_headers.py

verify: lint test audit

serve: build
	@cd public && python3 -m http.server 8000 --bind 127.0.0.1

clean:
	@rm -rf public dist .cache coverage *.log
	@echo "Workspace cleaned."
