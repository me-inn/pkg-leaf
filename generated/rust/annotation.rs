// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::Annotation;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: Annotation = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// A note somebody left on a book, and where in the text they left it. The note is the
/// record; the passage it points at stays in the chapter, quoted here only so the note still
/// reads once the text around it has moved.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Annotation {
    /// Where the passage ends, counted the same way.
    pub anchor_end: Option<i64>,

    /// Where the passage starts in the chapter text, counted in characters from the beginning.
    /// Valid against the revision that was open at the time.
    pub anchor_start: Option<i64>,

    /// What kind of remark it is, which decides who it is addressed to: a todo waits on the
    /// author, a beta_feedback came from a reader, an ai_suggestion was not written by a person
    /// at all.
    pub annotation_type: AnnotationType,

    /// The id of the book it was left on, in the system that owns it.
    pub book: String,

    /// The id of the chapter it was left on, in the system that owns it. Absent for a note about
    /// the book as a whole.
    pub chapter: Option<String>,

    pub created_at: Option<String>,

    /// The wallet, handle, or id under localIds of whoever left it. Absent for a note no person
    /// wrote.
    pub created_by: Option<String>,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// What they wrote.
    pub note: String,

    /// Whether the note has been dealt with. It stays on the record once resolved; nothing here
    /// is removed by being answered.
    pub resolved: bool,

    /// The passage as it read when the note was made. Kept verbatim because the anchors drift
    /// once the chapter is edited, and the quote is what survives that.
    pub text_selection: Option<String>,
}

/// What kind of remark it is, which decides who it is addressed to: a todo waits on the
/// author, a beta_feedback came from a reader, an ai_suggestion was not written by a person
/// at all.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum AnnotationType {
    #[serde(rename = "ai_suggestion")]
    AiSuggestion,

    #[serde(rename = "beta_feedback")]
    BetaFeedback,

    Note,

    Question,

    Todo,
}