// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::ChapterRevision;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: ChapterRevision = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// A chapter's text as it stood at one moment, kept whole rather than as a difference, so an
/// old version reads without replaying the ones after it.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct ChapterRevision {
    /// The wallet, handle, or id under localIds of whoever made the change. Absent when it was
    /// made by software rather than a person.
    pub changed_by: Option<String>,

    /// One line on what changed, so a list of revisions can be read without opening each.
    pub change_summary: Option<String>,

    /// What kind of change it was. Free text: the vocabulary belongs to the system that writes
    /// the revision.
    pub change_type: Option<String>,

    /// The id of the chapter this is a revision of, in the system that holds the chapter.
    pub chapter: String,

    /// The whole text as it stood, not a difference against the one before.
    pub content: String,

    /// When the revision was written down.
    pub created_at: Option<String>,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// Which revision of that chapter this is, counting up. Ordering comes from this and not
    /// from the clock, because two writes can land in the same second.
    pub version: i64,

    /// Words in this revision's text.
    pub word_count: Option<i64>,
}