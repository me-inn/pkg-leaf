// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::Notice;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: Notice = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// A link somebody put out — a video, a magazine, a product — and one line about it. A
/// pointer, never content: the system that holds the link holds what it says, and whoever
/// carries the notice only says that the link exists and when.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Notice {
    /// The wallet, handle, or id under localIds of whoever put the link out.
    pub by: String,

    /// When the notice was recorded, which is not when the link was published.
    pub created_at: Option<String>,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// One line about it, in the words of whoever put it out. Read by a person; never fetched
    /// from the link.
    pub line: Option<String>,

    /// Where the link goes. https, so a page vouching for it can hand it to a machine.
    pub url: String,
}