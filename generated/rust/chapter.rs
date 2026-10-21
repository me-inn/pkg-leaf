// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::Chapter;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: Chapter = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// One chapter of a book: its place in the running order and the text as it stands now.
/// Earlier states of that text are revisions, each its own record.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Chapter {
    /// The id of the book this chapter belongs to, in the system that holds the book.
    pub book: String,

    /// The text as it stands now. Empty while the chapter is only a heading.
    pub content: Option<String>,

    pub created_at: Option<String>,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// Where it falls in the running order. The number the chapters are sorted by, not the
    /// number printed on the page.
    pub order: Option<i64>,

    /// How far along this chapter is, which moves on its own and not with the book's.
    pub status: Option<Status>,

    /// What happens in it, in a few lines. Written so the chapter can be reasoned about without
    /// reading it whole.
    pub summary: Option<String>,

    /// The chapter heading.
    pub title: String,

    pub updated_at: Option<String>,

    /// Words in the current text, counted by whoever holds it.
    pub word_count: Option<i64>,
}

/// How far along this chapter is, which moves on its own and not with the book's.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum Status {
    Approved,

    Draft,

    Review,

    Writing,
}