// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::ChatMessage;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: ChatMessage = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// One turn of a conversation held against a library: what was asked, or what was answered,
/// and for an answer the chunks it was grounded on. The sources are pointers with enough of
/// the text to recognise them — never the chunk itself, which stays with the asset it came
/// from.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct ChatMessage {
    /// What was said. The question as typed, or the answer as generated.
    pub content: String,

    /// When the turn was recorded. The only ordering the conversation has.
    pub created_at: Option<String>,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// Who spoke. Two values: a person asks and the model answers, and nothing else writes a
    /// turn.
    pub role: Role,

    /// The session the turn belongs to, as the system that owns the session names it. Absent on
    /// rows written before turns were scoped.
    pub session: Option<String>,

    /// The chunks the answer was grounded on, in relevance order. Absent on a question, and
    /// empty on an answer that was grounded on nothing.
    pub sources: Option<Vec<RagSource>>,
}

/// Who spoke. Two values: a person asks and the model answers, and nothing else writes a
/// turn.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum Role {
    Assistant,

    User,
}

/// One retrieved chunk an answer leaned on, as it was at the time of the answer. A pointer
/// plus what a person needs to judge it — never the chunk, which stays with the asset it
/// came from — so the citation still reads once the chunk has changed.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct RagSource {
    /// The asset the chunk came from, as the system that owns the asset names it.
    pub asset: String,

    /// What the parent asset was called when the answer was written. Kept as a copy on purpose:
    /// a citation should still read after the asset is retitled.
    pub asset_title: Option<String>,

    /// The chunk itself, as the system that owns the chunk names it.
    pub chunk: String,

    /// Which part of the asset the chunk is — a summary, a transcript, a block of article text.
    /// Free text: the vocabulary belongs to whoever chunks.
    pub chunk_type: Option<String>,

    /// The opening of the chunk, carried so a person can see what was cited without fetching it.
    pub excerpt: Option<String>,

    /// How close the chunk sat to the question, as the retrieval scored it. Comparable inside
    /// one search, not across searches: the scale belongs to the model that searched.
    pub score: Option<f64>,

    /// A picture of the parent asset, when the system that serves it offers one. Derived, and
    /// resolvable only against the deploy that built it.
    pub thumbnail_url: Option<String>,
}