// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::GenerationVersion;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: GenerationVersion = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// The text a generation held at one point in its life. Kept as its own record so editing a
/// generation never loses what it said before — the generation carries the current text, the
/// versions carry the ones it had.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct GenerationVersion {
    /// When this version was written.
    pub created_at: Option<String>,

    /// The generation this is a version of, by its id in the system that holds it.
    pub generation: String,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// The text as it stood in this version.
    pub output: String,

    /// Which version this is, counting up within the generation. Ordering is the number's job;
    /// whether it may skip or repeat is the writing system's rule.
    pub version: i64,
}