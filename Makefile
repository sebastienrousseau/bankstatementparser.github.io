# SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
.PHONY: all build audit contrast validate lint style markdown html complexity test coverage lighthouse verify serve clean help

all: verify

help:
	@echo "Available Makefile targets:"
	@echo "  make build      - Compile static site using Rust static-site-generator"
	@echo "  make audit      - Run WCAG 2.2 AAA checks and SSG audit"
	@echo "  make contrast   - Verify color tokens against WCAG 2.2 AAA math ratios"
	@echo "  make validate   - Validate Markdown frontmatter schema integrity"
	@echo "  make lint       - Validate README, release versions, notes, and SPDX headers"
	@echo "  make style      - Lint and format-check the Python scripts with ruff"
	@echo "  make markdown   - Lint every Markdown file with markdownlint-cli2"
	@echo "  make html       - Validate every page of docs/ with html-validate"
	@echo "  make complexity - Hold Python functions under the complexity ceilings"
	@echo "  make test       - Run automated regression tests"
	@echo "  make coverage   - Run the pytest suite with its coverage floor"
	@echo "  make lighthouse - Run Lighthouse CI over every built page (needs Chrome)"
	@echo "  make verify     - Run full gate: lint, style, markdown, html, complexity, test, coverage, audit"
	@echo "  make serve      - Serve compiled site locally from public/"
	@echo "  make clean      - Remove build artifacts and temporary files"

build:
	@rm -rf public
	@ssg build --content _posts --template _layouts --output public
	@python3 scripts/post-build.py

test:
	@python3 scripts/regression-test.py

audit: contrast validate
	ssg audit -f ssg.toml -o public --severity warn --fail-on warn

contrast:
	@python3 scripts/audit-contrast.py
	@python3 audit/contrast.py

# Python tooling comes from requirements/test.txt
# (pip install --require-hashes -r requirements/test.txt); Node tooling
# from package-lock.json (npm ci --ignore-scripts).
style:
	@python3 -m ruff check scripts tests audit fuzz
	@python3 -m ruff format --check scripts tests audit fuzz

markdown:
	@npx --no-install markdownlint-cli2

html:
	@npx --no-install html-validate "docs/**/*.html"

# The floor is the measured line coverage of scripts/ and audit/ (20.9%
# when it was set); raise it as tests grow, never lower it.
coverage:
	@python3 -m pytest tests -q -p no:cacheprovider --cov=scripts --cov=audit --cov-report=term --cov-fail-under=20

validate:
	@python3 scripts/validate-frontmatter.py

lint:
	@./scripts/verify_release_version.sh
	@python3 scripts/validate_readme.py
	@python3 scripts/release_notes.py --check
	@python3 scripts/validate_spdx_headers.py

# Per-function ceilings (cyclomatic 10, cognitive 15, Halstead 30,
# 60 lines; 500 lines per file) against scripts/complexity_baseline.json,
# which may only shrink. Record an improvement with
# `python3 scripts/check_complexity.py --update`.
complexity:
	python3 scripts/check_complexity.py

# Lighthouse CI (the locked @lhci/cli) over every page of docs/, as the
# quality-gate workflow runs it; .lighthouserc.cjs holds the page list and the assertions.
LHCI = npx --no-install lhci
lighthouse:
	@$(LHCI) collect --config=.lighthouserc.cjs
	@$(LHCI) assert --config=.lighthouserc.cjs

verify: lint style markdown html complexity test coverage audit

serve: build
	@cd public && python3 -m http.server 8000 --bind 127.0.0.1

clean:
	@rm -rf public dist .cache coverage *.log
	@echo "Workspace cleaned."
