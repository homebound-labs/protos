# Homebound Labs Protos

Shared protobuf schemas for cross-repo, machine-to-machine contracts at
Homebound Labs: device telemetry, device auth, and (future) event-bus
messages. Generated Go and Python bindings are committed under `gen/`.

## Scope

This repo is for contracts that cross repo boundaries — currently the
`aegis-pi` <-> `backend-api` device contract described in
`homebound-labs/knowledge`'s
[`decisions/0006-production-device-contract.md`](https://github.com/homebound-labs/knowledge/blob/main/decisions/0006-production-device-contract.md).

Contracts that are only used inside one repo, or user-facing/admin CRUD APIs
(e.g. the `mobile-app` <-> `backend-api` mobile API), are **not** in scope
here — see `homebound-labs/knowledge/communication/api-contracts.md` for the
full contract inventory and classification.

## Layout

```text
proto/homebound/common/v1/     Shared value types (GeoPoint, BatteryStatus, Source)
proto/homebound/telemetry/v1/  TelemetryEvent / TelemetryAck (POST /api/v1/device/telemetry)
proto/homebound/device/v1/     Device auth token exchange, heartbeat/SOS responses
proto/homebound/events/v1/     Reserved for future event-bus messages (not wired yet)
gen/go/                        Generated Go bindings (google.golang.org/protobuf)
gen/python/                    Generated Python bindings (protoc --python_out)
scripts/generate.sh            Regenerate gen/go and gen/python from proto/
scripts/lint.sh                buf lint + breaking-change check + generated-code-is-current check
```

## Requirements

- [buf](https://buf.build) CLI
- `protoc-gen-go`: `go install google.golang.org/protobuf/cmd/protoc-gen-go@latest`
- `protoc` (for Python codegen): https://github.com/protocolbuffers/protobuf/releases

## Usage

```sh
./scripts/generate.sh   # regenerate gen/go and gen/python
./scripts/lint.sh        # lint + breaking-change check + verify gen/ is committed and current
```

### Go

```go
import telemetryv1 "github.com/homebound-labs/protos/gen/go/homebound/telemetry/v1"

evt := &telemetryv1.TelemetryEvent{
    EventId:  "evt_01h...",
    Sequence: 1042,
}
data, err := proto.Marshal(evt)
```

Add to a consuming repo's `go.mod` with:

```sh
go get github.com/homebound-labs/protos@latest
```

### Python

```python
from homebound.telemetry.v1 import telemetry_pb2

evt = telemetry_pb2.TelemetryEvent(event_id="evt_01h...", sequence=1042)
data = evt.SerializeToString()
```

`gen/python` is a pip-installable package (`homebound-protos`,
`gen/python/pyproject.toml`). Add it to a consuming repo's dependencies as a
git dependency pinned to a ref, e.g. in `pyproject.toml`:

```toml
dependencies = [
  "homebound-protos @ git+https://github.com/homebound-labs/protos.git@main#subdirectory=gen/python",
]
```

## Versioning and compatibility

- Proto packages are versioned (`v1`) per message family. Breaking changes to
  an existing `v1` message require a new `v2` package, not an in-place
  breaking change — enforced by `buf breaking` in CI.
- `scripts/lint.sh` fails if `gen/` is out of date relative to `proto/`, so
  generated code is always committed and reviewable in PRs (no build-time
  codegen in consumers).

## Known limitations / follow-ups

- Python bindings are installed as a git dependency (`pip install
  git+...#subdirectory=gen/python`), not yet published to a package index
  (e.g. a private PyPI). Publishing to an index is a reasonable follow-up if
  install-from-git friction becomes a problem.
- No generated TypeScript bindings yet. `mobile-app`'s contracts with
  `backend-api` are user-facing CRUD JSON and are intentionally out of scope
  for this repo (see `api-contracts.md`). If a shared mobile-facing
  protobuf contract emerges, add a `protoc-gen-es` (or similar) plugin here.
- `proto/homebound/events/v1` is a placeholder for a future event-bus
  contract; nothing currently publishes or consumes it.
