// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::GenerationPin;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: GenerationPin = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// A session holding on to a generation: kept near, so it is found again. An edge and not a
/// column, because being pinned is not a property of the generation — the same generation is
/// pinned in one session and not in another, and a column would make one session's opinion
/// look like the thing's own.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct GenerationPin {
    /// The generation being held on to, by its id in the system that holds it.
    pub generation: String,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// When it was pinned.
    pub pinned_at: Option<String>,

    /// The working session holding on to it, by that session's id in the system that holds it.
    /// That a session pins a generation at most once is the pinning system's rule, not a
    /// constraint of this shape.
    pub session: String,
}