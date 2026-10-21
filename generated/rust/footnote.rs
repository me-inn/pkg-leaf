// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::Footnote;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: Footnote = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// A note hanging off a point in a chapter's text — a footnote, an endnote, a citation, an
/// entry in the bibliography. Its own record, because where it prints depends on the format
/// the book is exported to and not on the sentence it came from.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Footnote {
    /// The offset into the chapter's text where the marker sits. Counted in characters from the
    /// start, so editing the text ahead of it moves the note.
    pub anchor_position: Option<i64>,

    /// The id of the chapter the note belongs to, in the system that holds the chapter.
    pub chapter: String,

    /// What the note says.
    pub content: String,

    pub created_at: Option<String>,

    /// What kind of note it is, which decides where it prints: at the foot of the page, at the
    /// back, inline, or in the list at the end.
    pub footnote_type: Option<FootnoteType>,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// Where it falls among that chapter's notes. What the printed marker is numbered from.
    pub order: Option<i64>,
}

/// What kind of note it is, which decides where it prints: at the foot of the page, at the
/// back, inline, or in the list at the end.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum FootnoteType {
    Bibliography,

    Citation,

    Endnote,

    Footnote,
}