// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::BookExport;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: BookExport = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// One rendering of a book into a file somebody can hand over — a pdf, an epub, a docx. A
/// pointer and a state, never the file: the bytes live in the store that rendered them, and
/// this says which store, under which key, and whether it finished.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct BookExport {
    /// The id of the book that was rendered, in the system that holds the book.
    pub book: String,

    /// When the rendering finished, whether it succeeded or failed.
    pub completed_at: Option<String>,

    /// When the export was asked for, which is not when the file was ready.
    pub created_at: Option<String>,

    /// Why the rendering failed, in the words of whoever rendered it. Present only when it did.
    pub error_message: Option<String>,

    /// The rendered file, where it is kept and how big it is. Absent until the rendering says
    /// done.
    pub file: Option<StoredFile>,

    /// What was rendered. A pdf for reading on a screen and a pdf for a printer are two formats,
    /// not one: the page, the bleed and the margins differ.
    pub format: Format,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// How the rendering went. The file is only there to fetch once this says done.
    pub status: Option<Status>,
}

/// The rendered file, where it is kept and how big it is. Absent until the rendering says
/// done.
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

/// What was rendered. A pdf for reading on a screen and a pdf for a printer are two formats,
/// not one: the page, the bleed and the margins differ.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum Format {
    Docx,

    Epub,

    #[serde(rename = "pdf_ebook")]
    PdfEbook,

    #[serde(rename = "pdf_print")]
    PdfPrint,
}

/// How the rendering went. The file is only there to fetch once this says done.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum Status {
    Done,

    Failed,

    Processing,

    Queued,
}