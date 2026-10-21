// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::ReadCompleted;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: ReadCompleted = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// An asset was read through: metadata out, a machine's reading of it written, and its
/// chunks indexed. Says the asset is now worth searching, and nothing about what it says.
/// Keys are snake_case, not the camelCase the rest of leaf uses: this travels inside a
/// Liquid envelope, whose own fields (event_id, occurred_at, event_type, owner_unit_ref) are
/// snake_case and pinned byte-exact by signed golden vectors. The shape follows the wire.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ReadCompleted {
    /// The asset that was read.
    pub content_id: String,

    /// The working session it was read in. Empty when the asset belongs to none.
    pub session_id: String,
}