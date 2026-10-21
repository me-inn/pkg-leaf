// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::GenerationNote;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: GenerationNote = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// Something somebody wrote beside a generation — a remark about the text, not part of it.
/// It stays its own record so the generation reads as the model left it.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct GenerationNote {
    /// What they wrote, in their words.
    pub body: String,

    /// When the note was written.
    pub created_at: Option<String>,

    /// The generation the note is about, by its id in the system that holds it.
    pub generation: String,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// The working session the note was written in, by that session's id in the system that
    /// holds it. The note is attributed to the session, not to a wallet: who was at the keyboard
    /// is the session's own business.
    pub session: String,

    /// When it was last rewritten. A note is editable, so this differs from createdAt once it
    /// has been.
    pub updated_at: Option<String>,
}