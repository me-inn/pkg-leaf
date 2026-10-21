// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::ScheduledContent;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: ScheduledContent = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// An intention to publish something that was already generated, at a time somebody picked.
/// A plan, not a publication: nothing here says it went out, and the generation itself stays
/// where it was made.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct ScheduledContent {
    /// When the plan was made, which is not when it publishes.
    pub created_at: Option<String>,

    /// What is to be published, as the system that holds the generation names it. A pointer: the
    /// text lives there and is not copied here, so editing it does not leave two versions.
    pub generation: String,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// Anything the person wanted to remember about this one. Read by a person, never acted on.
    pub notes: Option<String>,

    /// Where it is meant to go, in the words of whoever scheduled it. Free text: the vocabulary
    /// belongs to whoever publishes, and nothing here posts anything.
    pub platform: Option<String>,

    /// When it is meant to go out. A moment, not a window, and the only field anything schedules
    /// on.
    pub publish_at: String,

    /// The session the plan belongs to, as the system that owns the session names it. Optional:
    /// scoping a scheduled item to a working session is how Creative Flow holds it, not part of
    /// what it is, and a system without sessions must be able to carry the same shape.
    pub session: Option<String>,
}