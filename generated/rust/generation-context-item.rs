// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::GenerationContextItem;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: GenerationContextItem = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// One piece of material that was put in front of the model for a generation, and where it
/// came from. Written down because the source can change afterwards: this says what was
/// actually read, in the order it was read.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct GenerationContextItem {
    /// The material as it was handed to the model. A copy on purpose — the source may be edited
    /// or deleted later, and this is what was read.
    pub content: String,

    /// The generation this was given to, by its id in the system that holds it.
    pub generation: String,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// Its place in the order the items were assembled in, counting from the first. Position,
    /// not score.
    pub rank: i64,

    /// How close the retrieval judged it to the ask. Absent when the item was not chosen by
    /// similarity. The scale belongs to whichever retrieval produced it.
    pub similarity_score: Option<f64>,

    /// The id of that thing, in the system that owns it. Paired with sourceType, which says what
    /// kind of id it is.
    pub source_id: String,

    /// What kind of thing the material came from. Free text: the kinds belong to whatever the
    /// retrieving system can reach.
    pub source_type: String,
}