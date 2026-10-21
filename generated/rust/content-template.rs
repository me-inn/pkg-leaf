// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::ContentTemplate;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: ContentTemplate = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// A saved starting point for generating something: what kind of piece, for which channel
/// and objective, with the standing instructions to use. Settings somebody wants back, not a
/// piece of content — nothing generated is kept here.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct ContentTemplate {
    /// Where the piece is meant to run, in the words of whoever saved the template. Free text
    /// everywhere it appears: the vocabulary belongs to whoever publishes.
    pub channel: Option<String>,

    /// When the template was saved.
    pub created_at: Option<String>,

    /// What kind of piece it produces. Free text: the names belong to the generation flow, which
    /// adds to them.
    pub generation_type: String,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// The standing instructions to apply, in the person's own words. The template's substance:
    /// everything else only files it.
    pub instructions: Option<String>,

    /// What the person called it, so they recognise it in a list.
    pub name: String,

    /// What the piece is meant to do. Free text, for the same reason as channel.
    pub objective: Option<String>,

    /// The session the template belongs to, as the system that owns the session names it.
    /// Optional: scoping a template to a working session is how Creative Flow holds it, not part
    /// of what it is, and a system without sessions must be able to carry the same shape.
    pub session: Option<String>,
}