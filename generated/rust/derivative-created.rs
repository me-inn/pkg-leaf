// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::DerivativeCreated;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: DerivativeCreated = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// Content was written from assets already put in. The relay understands this type natively,
/// which is why it exists beside generation.ready: this one says a derivative was made, that
/// one hands over what it says. Keys are snake_case, not the camelCase the rest of leaf
/// uses: this travels inside a Liquid envelope, whose own fields (event_id, occurred_at,
/// event_type, owner_unit_ref) are snake_case and pinned byte-exact by signed golden
/// vectors. The shape follows the wire.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DerivativeCreated {
    /// The generation that was made.
    pub content_id: String,

    /// The working session it was made in.
    pub session_id: String,

    /// The assets it was written from, by id. Absent when nothing was drawn on.
    pub source_assets: Option<Vec<String>>,

    /// Which template it was written from. Free text: the templates belong to whoever generates.
    pub template: String,
}