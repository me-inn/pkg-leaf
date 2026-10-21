// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::GenerationReady;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: GenerationReady = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// Content was written and is handed over in full. The one result that carries the work
/// itself rather than a reference to it: the asking system has no database of generations to
/// read it back from. Keys are snake_case, not the camelCase the rest of leaf uses: this
/// travels inside a Liquid envelope, whose own fields (event_id, occurred_at, event_type,
/// owner_unit_ref) are snake_case and pinned byte-exact by signed golden vectors. The shape
/// follows the wire.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct GenerationReady {
    /// The generation that was made.
    pub content_id: String,

    /// The text, as written.
    pub output: String,

    /// What the pipeline thought of its own output. Absent when nothing scored it, which is not
    /// the same as a score of zero.
    pub overall_score: Option<f64>,

    /// The working session it was made in.
    pub session_id: String,

    /// The assets it was written from, by id.
    pub source_assets: Option<Vec<String>>,

    /// Which template it was written from.
    pub template: String,
}