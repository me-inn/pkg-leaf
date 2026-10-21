// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::GenerationVariant;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: GenerationVariant = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// A second take on a generation, asked for as its own piece of work. It says which
/// generation it came from and which job was run for it — the text it produced belongs to
/// that job's own record, not to this edge.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct GenerationVariant {
    /// When the variant was asked for, which is not when the job finished.
    pub created_at: Option<String>,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// The processing job run to produce it, by its id in the system that runs it. The variant
    /// is the link between the two; neither side carries the other.
    pub job: String,

    /// The generation this is a variant of, by its id in the system that holds it.
    pub parent_generation: String,
}