// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::GenerationFeedback;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: GenerationFeedback = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// What somebody did with a generated piece when it was handed to them: took it, threw it
/// away, or rewrote it. An act rather than an opinion — the rewrite is the feedback, and it
/// is the one signal that says what good would have looked like.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct GenerationFeedback {
    /// What they did with it.
    pub action: Action,

    /// When they did it.
    pub created_at: Option<String>,

    /// The piece as they rewrote it. Present when the action was edited; that it must be is a
    /// rule the writing system keeps, not a shape.
    pub edited_output: Option<String>,

    /// The id of the generated piece this was done to, in the system that owns it.
    pub generation: String,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// The id of the working session it happened in, in the system that holds it. Not a person:
    /// a session says the acts came from one sitting, and whether anybody is named is the
    /// holding system's business.
    pub session: Option<String>,
}

/// What they did with it.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum Action {
    Approved,

    Edited,

    Rejected,
}