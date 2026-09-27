#!/usr/bin/env bash
# SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"
version="$(tr -d '[:space:]' < VERSION)"

[[ "$version" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || {
  echo "VERSION is not SemVer: $version" >&2
  exit 1
}

grep -q "version: $version" CITATION.cff || {
  echo "CITATION.cff does not match VERSION $version" >&2
  exit 1
}

if [[ "${GITHUB_REF_TYPE:-}" == "tag" ]]; then
  [[ "${GITHUB_REF_NAME:-}" == "v$version" ]] || {
    echo "Tag ${GITHUB_REF_NAME:-<unset>} does not match VERSION v$version" >&2
    exit 1
  }
fi

echo "release version is consistent: v$version"
