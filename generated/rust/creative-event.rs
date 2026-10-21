// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::CreativeEvent;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: CreativeEvent = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};
use std::collections::HashMap;

/// One thing the creative pipeline was asked to do, or one thing it finished — as it travels
/// between the system that asks and the system that works. Commands go one way and results
/// come back the other way over the same relay, so they are one shape with one type field
/// rather than two. The event carries no content: what it carries is an id of something a
/// system already holds, and enough words to act on it. Keys are snake_case, not the
/// camelCase the rest of leaf uses: this travels inside a Liquid envelope, whose own fields
/// (event_id, occurred_at, event_type, owner_unit_ref) are snake_case and pinned byte-exact
/// by signed golden vectors. The shape follows the wire.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CreativeEvent {
    /// ed25519 public key, hex, of whoever signed the event. The only thing that says who asked:
    /// a reader admits an event by this key, never by the name below.
    pub author: Option<String>,

    /// What the signing system calls itself, such as creativeflow. A label for reading a log; it
    /// proves nothing, and two systems may well claim the same one.
    pub author_name: Option<String>,

    /// The asset, generation or job the event is about, repeated outside the payload so a reader
    /// can file the event without opening it. Absent for events about no single thing, such as
    /// an error.
    pub content_id: Option<String>,

    /// The device the event was written on, when more than one writes for the same author.
    pub device_id: Option<String>,

    /// What happened, written as <domain>.<action>. The requested forms are commands addressed
    /// to the pipeline; the rest are results it emits. It alone decides which payload shape
    /// applies — two different commands can carry the same single id and are told apart by
    /// nothing else.
    pub event_type: EventType,

    /// The record's own id in the system that holds it. Also what makes the event replayable
    /// without doing the work twice: a reader that has seen this id has already acted.
    pub id: Option<String>,

    /// A counter for ordering events from one author when wall clocks disagree. Comparable only
    /// against events from the same author.
    pub lamport: Option<i64>,

    /// When the author says it happened, which is not when a reader received it.
    pub occurred_at: Option<String>,

    /// The session or unit the event belongs to, which is who answers for it. Set on errors
    /// above all, where it is the only thing saying whose work broke.
    pub owner_unit_ref: Option<String>,

    /// What the event is about. Open on purpose: eventType decides which schema the payload is,
    /// and a reader picks that type rather than matching on the shape. The union used to live
    /// here as anyOf and the generator kept only its first branch, so the other fourteen
    /// payloads had no type at all; each is now its own schema. asset.ingest_requested ->
    /// AssetIngestRequested; asset.url_ingest_requested -> AssetUrlIngestRequested;
    /// generation.requested -> GenerationRequested; repurpose.requested -> RepurposeRequested;
    /// rag.query_requested -> RagQueryRequested; asset.edit_requested -> AssetEditRequested;
    /// read.completed -> ReadCompleted; derivative.created -> DerivativeCreated;
    /// citation.created -> CitationCreated; value.snapshot -> ValueSnapshot; signal.error ->
    /// SignalError; generation.ready -> GenerationReady; rag.result_ready -> RagResultReady;
    /// repurpose.ready -> RepurposeReady; asset.edit_ready -> AssetEditReady.
    pub payload: HashMap<String, Option<serde_json::Value>>,
}

/// What happened, written as <domain>.<action>. The requested forms are commands addressed
/// to the pipeline; the rest are results it emits. It alone decides which payload shape
/// applies — two different commands can carry the same single id and are told apart by
/// nothing else.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum EventType {
    #[serde(rename = "asset.edit_ready")]
    AssetEditReady,

    #[serde(rename = "asset.edit_requested")]
    AssetEditRequested,

    #[serde(rename = "asset.ingest_requested")]
    AssetIngestRequested,

    #[serde(rename = "asset.url_ingest_requested")]
    AssetUrlIngestRequested,

    #[serde(rename = "citation.created")]
    CitationCreated,

    #[serde(rename = "derivative.created")]
    DerivativeCreated,

    #[serde(rename = "generation.ready")]
    GenerationReady,

    #[serde(rename = "generation.requested")]
    GenerationRequested,

    #[serde(rename = "rag.query_requested")]
    RagQueryRequested,

    #[serde(rename = "rag.result_ready")]
    RagResultReady,

    #[serde(rename = "read.completed")]
    ReadCompleted,

    #[serde(rename = "repurpose.ready")]
    RepurposeReady,

    #[serde(rename = "repurpose.requested")]
    RepurposeRequested,

    #[serde(rename = "signal.error")]
    SignalError,

    #[serde(rename = "value.snapshot")]
    ValueSnapshot,
}