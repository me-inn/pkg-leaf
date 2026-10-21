// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::AssetChunk;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: AssetChunk = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};
use std::collections::HashMap;

/// One piece of an asset held separately so it can be searched on its own. The text is kept
/// beside the vector so whoever answers from a chunk can show the excerpt it answered from,
/// without opening the asset.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct AssetChunk {
    /// The id of the asset this piece was cut from, in the system that owns it.
    pub asset: String,

    /// Position among the pieces of the same type on the same asset. Zero while a type yields
    /// one piece; it exists so splitting a long text later does not change the shape.
    pub chunk_order: i64,

    /// The text that was embedded, verbatim.
    pub chunk_text: String,

    /// Which reading of the asset this piece is. They are indexed together but recall
    /// differently: title_tags catches a keyword, summary catches a meaning.
    pub chunk_type: ChunkType,

    pub created_at: Option<String>,

    /// The semantic vector of this piece. A reader holding another model recomputes it from
    /// chunkText.
    pub embedding: Option<Vec<f64>>,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// Whatever the splitter recorded about the cut — offsets into the source, token counts.
    pub metadata: Option<HashMap<String, Option<serde_json::Value>>>,
}

/// Which reading of the asset this piece is. They are indexed together but recall
/// differently: title_tags catches a keyword, summary catches a meaning.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum ChunkType {
    #[serde(rename = "article_text")]
    ArticleText,

    Description,

    Metadata,

    Summary,

    #[serde(rename = "title_tags")]
    TitleTags,

    Transcript,

    #[serde(rename = "visual_summary")]
    VisualSummary,
}