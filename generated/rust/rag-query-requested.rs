// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::RagQueryRequested;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: RagQueryRequested = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// A question somebody wants answered out of what was put in. Carries the whole question,
/// for the same reason repurpose does. Keys are snake_case, not the camelCase the rest of
/// leaf uses: this travels inside a Liquid envelope, whose own fields (event_id,
/// occurred_at, event_type, owner_unit_ref) are snake_case and pinned byte-exact by signed
/// golden vectors. The shape follows the wire.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RagQueryRequested {
    /// Search only this kind of asset. Absent searches all of them.
    pub asset_type: Option<AssetType>,

    /// The job to report the answer against, created by the pipeline if it does not exist yet.
    pub job_id: String,

    /// BCP-47 tag of the language to answer in. Detected from the question when absent.
    pub language: Option<String>,

    /// The question, in natural language. A blank one is not worked.
    pub query: Option<String>,

    /// What to return: an answer grounded in the sources, or only the rewritten text, with
    /// nothing around it, for an editor that drops it straight into a document.
    pub response_mode: Option<ResponseMode>,

    /// The working session to search in. The question is answered out of that session's
    /// material, not out of everything.
    pub session_id: String,

    /// How many chunks to retrieve before answering. Absent leaves it to whoever searches.
    pub top_k: Option<i64>,
}

/// Search only this kind of asset. Absent searches all of them.
///
/// What kind of thing an asset is, which decides which pipeline reads it. A document covers
/// an article, a PDF, or raw text.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum AssetType {
    Document,

    Image,

    Video,
}

/// What to return: an answer grounded in the sources, or only the rewritten text, with
/// nothing around it, for an editor that drops it straight into a document.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum ResponseMode {
    Answer,

    Rewrite,
}