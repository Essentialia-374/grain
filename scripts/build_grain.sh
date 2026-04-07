#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

echo "Generating protobuf Python sources..."
protoc \
  --proto_path=. \
  --python_out=. \
  grain/proto/execution_summary.proto

echo "Building wheel..."
python -m pip wheel . -w dist

echo "Done. Wheels are in ${ROOT_DIR}/dist"
