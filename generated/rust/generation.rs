// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::Generation;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: Generation = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// One thing a model wrote when somebody asked for it: what was asked, what it was given to
/// read, and the text that came out. The assets it read are named by id and stay where they
/// are — this record is the asking, not a copy of the material.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Generation {
    /// The assets the model was given to read, by their ids in the system that holds them. Ids,
    /// never the material: the asset is somebody else's record.
    pub asset_ids: Option<Vec<String>>,

    /// Where the text was meant to go. Free text: the channels belong to whoever publishes, not
    /// to this shape.
    pub channel: Option<String>,

    /// Where the text stands. Which status may follow which is a rule held by the system that
    /// moves it, not a constraint of this shape.
    pub content_status: Option<ContentStatus>,

    /// When the generation was recorded.
    pub created_at: Option<String>,

    /// What kind of thing was asked for. Free text: the vocabulary grows with every surface that
    /// asks, so it is not closed here.
    pub generation_type: String,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// What the person asked for, in their own words, before anything was assembled around it.
    pub instructions: Option<String>,

    /// Which model wrote it, under the name its provider gives it. Recorded so a later reading
    /// knows what produced the text — never a key, never a provider credential.
    pub model_used: Option<String>,

    /// What the text was meant to achieve. Free text, for the same reason as channel.
    pub objective: Option<String>,

    /// The text the model produced. Empty while the generation exists and has produced nothing
    /// yet.
    pub output: Option<String>,

    /// The prompt actually sent, after the instructions and the context were assembled into one.
    /// Kept because the instructions alone do not reproduce it.
    pub prompt_used: Option<String>,

    /// The working session it was generated in, by that session's id in the system that holds
    /// it. A session, not a person: who was at the keyboard is the session's own business.
    /// Absent when it was generated outside one.
    pub session: Option<String>,

    /// Labels somebody put on it. Free text, theirs.
    pub tags: Option<Vec<String>>,
}

/// Where the text stands. Which status may follow which is a rule held by the system that
/// moves it, not a constraint of this shape.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum ContentStatus {
    Approved,

    Archived,

    Draft,

    Published,
}