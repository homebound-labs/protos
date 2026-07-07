# Homebound Labs Protos

Shared protobuf schemas for cross-repo, machine-to-machine contracts at
Homebound Labs: device telemetry, device auth, the mobile app's phone
location contract, and (future) event-bus messages. Generated Go, Python,
and TypeScript bindings are committed under `gen/`.

## Scope

This repo is for contracts that cross repo boundaries:

- The `aegis-pi` <-> `backend-api` device contract described in
  `homebound-labs/knowledge`'s
  [`decisions/0006-production-device-contract.md`](https://github.com/homebound-labs/knowledge/blob/main/decisions/0006-production-device-contract.md).
- The `mobile` <-> `backend-api` phone location contract
  (`homebound.mobile.v1`), added per
  [`decisions/0008-mobile-location-protobuf.md`](https://github.com/homebound-labs/knowledge/blob/main/decisions/0008-mobile-location-protobuf.md):
  phone location pings (`POST /api/v1/mobile/location`) and the
  latest-location reads the mobile app polls. Mobile is a boundary consumer
  like any other repo, not a reason to stay JSON by default.

Contracts that are only used inside one repo, or that are genuinely
admin/CRUD/debug in nature (device claiming by short code, alert list/ack,
push token registration), are **not** in scope here — see
`homebound-labs/knowledge/communication/api-contracts.md` for the full
contract inventory and classification.

## Layout

```text
proto/homebound/common/v1/     Shared value types (GeoPoint, BatteryStatus, Source)
proto/homebound/telemetry/v1/  TelemetryEvent / TelemetryAck (POST /api/v1/device/telemetry)
proto/homebound/device/v1/     Device auth token exchange, heartbeat/SOS responses
proto/homebound/mobile/v1/     Phone location contract (POST /api/v1/mobile/location, GET .../location/latest, GET .../devices/{id}/location/latest)
proto/homebound/events/v1/     Reserved for future event-bus messages (not wired yet)
gen/go/                        Generated Go bindings (google.golang.org/protobuf)
gen/python/                    Generated Python bindings (protoc --python_out)
gen/ts/                        Generated TypeScript bindings (protoc-gen-es / @bufbuild/protobuf)
scripts/generate.sh            Regenerate gen/go, gen/ts, and gen/python from proto/
scripts/lint.sh                buf lint + breaking-change check + generated-code-is-current check
```

## Requirements

- [buf](https://buf.build) CLI
- `protoc-gen-go`: `go install google.golang.org/protobuf/cmd/protoc-gen-go@latest`
- `protoc` (for Python codegen): https://github.com/protocolbuffers/protobuf/releases
- node/npm (for `protoc-gen-es`, installed into this repo's own
  `./node_modules` via `npm install`; this is dev-only codegen tooling for
  *this* repo, unrelated to any consuming repo's runtime dependencies)

## Usage

```sh
./scripts/generate.sh   # regenerate gen/go, gen/ts, and gen/python
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

### TypeScript

```ts
import { PhoneLocationUpdate, LatestLocationsResponse } from "@homebound-labs/protos/homebound/mobile/v1/location_pb";

const update = new PhoneLocationUpdate({
  location: { latitude: 37.77, longitude: -122.42 },
});
const bytes = update.toBinary();
```

Unlike `gen/python`, npm has no equivalent of pip's `#subdirectory=` fragment
for git dependencies, so `gen/ts` is **not** installable directly as a git
dependency today. Consuming repos (currently `mobile`) vendor the specific
generated `*_pb.ts` files they need under a clearly-marked generated
directory (e.g. `mobile/src/generated/proto/`), copied verbatim from this
repo's `gen/ts/` at a pinned commit, plus the `@bufbuild/protobuf` runtime as
a regular npm dependency. Regenerate and re-copy after any proto change; see
`mobile/src/generated/proto/README.md` for the exact copy step. Publishing
`gen/ts` to a package registry (npm or a private one) would remove this
vendoring step and is a reasonable follow-up — see Known limitations below.

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
- `gen/ts` is generated and committed here but not installable as a git
  dependency from npm (see the TypeScript section above); `mobile` vendors a
  copy of the generated files it needs instead. Publishing `gen/ts` to an
  npm registry (public or private) would remove the vendoring step.
- `proto/homebound/events/v1` is a placeholder for a future event-bus
  contract; nothing currently publishes or consumes it.
- `proto/homebound/mobile/v1` currently only covers the phone location
  contract. The mobile app's device list/claim, alerts, and push-token
  registration endpoints remain JSON — they are CRUD/settings actions on
  backend-owned state, not telemetry-shaped boundary payloads. Revisit if
  they grow into richer machine-readable contracts.
