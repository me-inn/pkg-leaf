// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::Book;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: Book = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// A long-form title somebody is writing: what it is about, how far along it is, and where
/// its cover sits. The chapters are not inside it — each is its own record pointing back, so
/// a book can be read without carrying its whole text.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Book {
    /// The model that helped write it, named as the system that called it names it. Absent when
    /// nothing was asked of one.
    pub ai_model: Option<String>,

    /// The wallet, handle, or id under localIds of whoever is writing it. Absent while the title
    /// belongs to nobody yet.
    pub author: Option<String>,

    /// The cover image, where it is kept. Absent while the title has none.
    pub cover: Option<StoredFile>,

    /// The brief the cover image was asked for with. Kept because the image can be asked for
    /// again.
    pub cover_prompt: Option<String>,

    pub created_at: Option<String>,

    /// Words written so far across the chapters. Counted by whoever holds the text, carried here
    /// so a reader of the book alone can say how far along it is.
    pub current_word_count: Option<i64>,

    /// What the book is about, in the words of whoever is writing it. Written for a reader
    /// deciding, not for a catalogue.
    pub description: Option<String>,

    /// The shelf it belongs on. A closed list because it decides how the title is filed, not how
    /// it reads.
    pub genre: Genre,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// The BISAC subject code given to the store, such as FIC000000. Separate from genre: one is
    /// ours, this one is the trade's.
    pub kdp_bisac: Option<String>,

    /// The keywords the title is listed under on the store. Free text, in the words of whoever
    /// sells it.
    pub kdp_keywords: Option<Vec<String>>,

    /// The language the book is written in, as a BCP 47 tag such as pt, en or pt-BR.
    pub language: Option<String>,

    /// The id of the working session the book was started from, in the system that holds that
    /// session. Absent when it was not started from one.
    pub session: Option<String>,

    /// How far along it is. Which move from which is a rule held beside the type, never in it.
    pub status: Option<Status>,

    /// The line under the title, when there is one.
    pub subtitle: Option<String>,

    /// The length being aimed at, set by whoever is writing. Zero while no target was chosen.
    pub target_word_count: Option<i64>,

    /// The title on the cover.
    pub title: String,

    pub updated_at: Option<String>,
}

/// The cover image, where it is kept. Absent while the title has none.
///
/// Bytes somebody is keeping, pointed at rather than carried. Never the file itself: the
/// store that holds it holds it, and this says which key to ask under and, while it lasts,
/// where it can be fetched. Nothing is required, because a file can be known by its key
/// before any address has been issued for it, and served by an address before anybody
/// recorded a key.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct StoredFile {
    /// How big it is, so whoever is about to fetch it knows what they are asking for.
    pub size_bytes: Option<i64>,

    /// Where the bytes sit in the store that holds them. The lasting handle, meaningful only to
    /// that store: a reader asks the store, never resolves the key itself.
    pub storage_key: Option<String>,

    /// Where the file can be fetched right now. Often signed and short-lived, so it is read at
    /// the moment of use and never kept as the address of the file.
    pub url: Option<String>,
}

/// The shelf it belongs on. A closed list because it decides how the title is filed, not how
/// it reads.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum Genre {
    Academic,

    Biography,

    Business,

    Children,

    Fantasy,

    Fiction,

    Historical,

    Horror,

    #[serde(rename = "non_fiction")]
    NonFiction,

    Other,

    Poetry,

    Romance,

    #[serde(rename = "science_fiction")]
    ScienceFiction,

    #[serde(rename = "self_help")]
    SelfHelp,

    Thriller,

    #[serde(rename = "young_adult")]
    YoungAdult,
}

/// How far along it is. Which move from which is a rule held beside the type, never in it.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum Status {
    Approved,

    Draft,

    Published,

    Review,

    Writing,
}