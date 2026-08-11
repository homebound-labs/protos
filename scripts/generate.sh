#!/usr/bin/env bash
# Generates Go, TypeScript, Rust, and Python bindings for all protos in this
# repo.
#
# Requirements on PATH. Use the same versions CI pins (see the `env:` block
# in .github/workflows/ci.yml) -- generated output is version-sensitive, and
# a mismatch here shows up as an unrelated diff in someone else's PR:
#   - buf              1.72.0   (https://buf.build)
#   - protoc-gen-go    v1.36.11 (go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.36.11)
#   - protoc           29.3     (https://github.com/protocolbuffers/protobuf/releases) for Python codegen
#   - node/npm                  (for protoc-gen-es, pinned in package.json,
#                                installed into ./node_modules via `npm install`)
#   - protoc-gen-prost, protoc-gen-prost-crate 0.5.0
#                       (cargo install protoc-gen-prost@0.5.0 protoc-gen-prost-crate@0.5.0)
#
# Usage: ./scripts/generate.sh
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

if [ ! -x node_modules/.bin/protoc-gen-es ]; then
  echo "==> Installing TypeScript codegen tooling (npm install)"
  npm install --no-audit --no-fund
fi

# Drop previously generated Rust so a deleted or renamed proto package does
# not leave an orphan module behind. lib.rs is hand-written -- keep it.
find gen/rust/src -mindepth 1 ! -name 'lib.rs' -exec rm -rf {} +

echo "==> Generating Go, TypeScript, and Rust bindings (buf)"
buf generate

echo "==> Generating Python bindings (protoc)"
find gen/python -mindepth 1 -maxdepth 1 ! -name 'pyproject.toml' -exec rm -rf {} +
protoc \
  --proto_path=proto \
  --python_out=gen/python \
  --pyi_out=gen/python \
  $(find proto -name '*.proto')

# protoc's python_out does not emit package __init__.py files; add empty ones
# so `import homebound.telemetry.v1.telemetry_pb2` works as a regular package
# and so gen/python is installable as the homebound-protos package (see
# gen/python/pyproject.toml).
find gen/python -type d ! -path 'gen/python' | while read -r dir; do
  touch "$dir/__init__.py"
done

echo "==> Done"
