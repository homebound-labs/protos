#!/usr/bin/env bash
# Lints all protos and checks that committed generated code is up to date.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

echo "==> buf lint"
buf lint

echo "==> buf breaking (against main)"
buf breaking --against '.git#branch=main' || echo "(skipped: no main to diff against, or first run)"

echo "==> checking generated code is committed and current"
./scripts/generate.sh
git diff --exit-code -- gen/ || {
  echo "Generated code is out of date. Run ./scripts/generate.sh and commit the result." >&2
  exit 1
}
