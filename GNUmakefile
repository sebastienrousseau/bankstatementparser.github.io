# SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT

PREFIX ?= /usr/local
DESTDIR ?=
DOCDIR ?= $(DESTDIR)$(PREFIX)/share/doc/bankstatementparser/html

include Makefile

.PHONY: install uninstall

install: build
	@install -d "$(DOCDIR)"
	@cp -R public/. "$(DOCDIR)/"

uninstall:
	@rm -rf "$(DOCDIR)"
