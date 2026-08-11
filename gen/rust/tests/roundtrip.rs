//! Smoke tests for the generated Rust bindings.
//!
//! The equivalent of this repo's Go build check and Python import check: it
//! proves the committed `gen/rust` actually compiles and round-trips, and
//! that cross-package references (telemetry -> common, device -> common and
//! google.protobuf) resolve.
//!
//! These are hand-written and are not touched by `scripts/generate.sh`.

use homebound_protos::homebound::common::v1::{GeoPoint, Source};
use homebound_protos::homebound::device::v1::{DeviceAuthTokenRequest, HeartbeatRequest};
use homebound_protos::homebound::telemetry::v1::{TelemetryAck, TelemetryEvent};
use prost::Message;

#[test]
fn telemetry_event_round_trips() {
    let event = TelemetryEvent {
        event_id: "evt_01h".to_string(),
        sequence: 1042,
        recorded_at: Some(prost_types::Timestamp { seconds: 1_786_365_296, nanos: 0 }),
        location: Some(GeoPoint { latitude: 37.77, longitude: -122.42, ..Default::default() }),
        source: Some(Source {
            firmware_version: "0.1.0".into(),
            hardware_profile: "nrf9151-dk".into(),
        }),
        ..Default::default()
    };

    let bytes = event.encode_to_vec();
    let decoded = TelemetryEvent::decode(bytes.as_slice()).expect("decode");

    assert_eq!(decoded, event);
    assert_eq!(decoded.event_id, "evt_01h");
    assert_eq!(decoded.sequence, 1042);
}

#[test]
fn optional_fields_stay_absent_when_unset() {
    // `optional` in proto3 maps to Option, so an unset location must decode
    // back as None rather than a zeroed GeoPoint -- backend-api relies on
    // this to tell "no fix" from "fix at 0,0".
    let event = TelemetryEvent { event_id: "evt_02".to_string(), ..Default::default() };

    let decoded = TelemetryEvent::decode(event.encode_to_vec().as_slice()).expect("decode");

    assert!(decoded.location.is_none());
    assert!(decoded.battery.is_none());
    assert!(decoded.signal_strength.is_none());
}

#[test]
fn device_auth_and_heartbeat_messages_round_trip() {
    let request =
        DeviceAuthTokenRequest { device_id: "dev-1".into(), device_secret: "secret".into() };
    let decoded =
        DeviceAuthTokenRequest::decode(request.encode_to_vec().as_slice()).expect("decode");
    assert_eq!(decoded, request);

    let heartbeat = HeartbeatRequest {
        status: "ok".into(),
        sent_at: Some(prost_types::Timestamp { seconds: 1_786_365_296, nanos: 0 }),
        source: Some(Source {
            firmware_version: "0.1.0".into(),
            hardware_profile: "nrf9151-dk".into(),
        }),
    };
    let decoded = HeartbeatRequest::decode(heartbeat.encode_to_vec().as_slice()).expect("decode");
    assert_eq!(decoded, heartbeat);
}

#[test]
fn ack_decodes_from_bytes_produced_by_another_implementation() {
    // Hand-encoded TelemetryAck{accepted: true, event_id: "evt_01h"}:
    // field 1 (varint) = 1, field 2 (len-delimited) = "evt_01h".
    let wire = [0x08, 0x01, 0x12, 0x07, b'e', b'v', b't', b'_', b'0', b'1', b'h'];

    let ack = TelemetryAck::decode(wire.as_slice()).expect("decode");

    assert!(ack.accepted);
    assert_eq!(ack.event_id, "evt_01h");
    assert!(ack.server_received_at.is_none());
}
