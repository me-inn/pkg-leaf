// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::GenerationRequested;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: GenerationRequested = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// A piece of content somebody wants written. What to write is in the job, not in the event.
/// Keys are snake_case, not the camelCase the rest of leaf uses: this travels inside a
/// Liquid envelope, whose own fields (event_id, occurred_at, event_type, owner_unit_ref) are
/// snake_case and pinned byte-exact by signed golden vectors. The shape follows the wire.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct GenerationRequested {
    /// The job holding the template, the sources and everything else the generation needs.
    pub job_id: String,
}