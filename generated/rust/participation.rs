// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::Participation;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: Participation = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// An organisation's role in an event, a publication, a split or a programme.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Participation {
    /// What kind of thing it participates in.
    pub context: Context,

    /// The id of that thing, in the system that owns it.
    pub context_id: String,

    pub created_at: Option<String>,

    /// The organisation's wallet, or its id under localIds.
    pub organization: String,

    /// Its role there, in that context's own words. Free text: the vocabulary belongs to the
    /// context.
    pub role: String,

    pub status: Option<Status>,
}

/// What kind of thing it participates in.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum Context {
    Event,

    Program,

    Publication,

    Split,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum Status {
    Active,

    Ended,

    Proposed,
}