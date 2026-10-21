// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::CitationCreated;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: CitationCreated = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// An address was fetched and kept as an asset. The address stays in the event because the
/// copy and the page drift apart from that moment. Keys are snake_case, not the camelCase
/// the rest of leaf uses: this travels inside a Liquid envelope, whose own fields (event_id,
/// occurred_at, event_type, owner_unit_ref) are snake_case and pinned byte-exact by signed
/// golden vectors. The shape follows the wire.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CitationCreated {
    /// The asset the fetched page became.
    pub content_id: String,

    /// The working session it was fetched into.
    pub session_id: String,

    /// The address it was fetched from.
    pub source_url: String,
}