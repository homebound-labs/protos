#!/usr/bin/env bash
# Generates Go and Python bindings for all protos in this repo.
#
# Requirements on PATH:
#   - buf              (https://buf.build)
#   - protoc-gen-go     (go install google.golang.org/protobuf/cmd/protoc-gen-go@latest)
#   - protoc            (https://github.com/protocolbuffers/protobuf/releases) for Python codegen
#
# Usage: ./scripts/generate.sh
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

echo "==> Generating Go bindings (buf)"
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
