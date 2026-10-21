// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::ValueSnapshot;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: ValueSnapshot = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// What something was worth over a stretch of time — a score, or a person saying yes or no
/// to a generation. A reading taken, never a running total: two snapshots of the same thing
/// are both true of their own window. Keys are snake_case, not the camelCase the rest of
/// leaf uses: this travels inside a Liquid envelope, whose own fields (event_id,
/// occurred_at, event_type, owner_unit_ref) are snake_case and pinned byte-exact by signed
/// golden vectors. The shape follows the wire.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ValueSnapshot {
    /// What was scored.
    pub content_id: String,

    /// The working session it was taken in.
    pub session_id: String,

    /// The reading, normalised. A thumb up is 1 and a thumb down is 0; what any other number
    /// means belongs to whoever took it.
    pub value: f64,

    /// End of the stretch the reading covers.
    pub window_end: String,

    /// Start of the stretch the reading covers. Equal to the end for a reading of one moment,
    /// such as a thumb.
    pub window_start: String,
}