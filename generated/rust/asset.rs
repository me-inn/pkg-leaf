// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::Asset;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: Asset = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};
use std::collections::HashMap;

/// Something somebody put in — a file uploaded or a page ingested from a URL — and
/// everything a machine later said about it. The bytes never travel: what travels is where
/// they are kept, what kind of thing they are, and the reading a pipeline made of them.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Asset {
    /// What a machine said the asset is.
    pub ai_description: Option<String>,

    /// The longer reading a machine made of it.
    pub ai_summary: Option<String>,

    /// Tags a machine put on it. Free text: the vocabulary belongs to whoever enriched the
    /// asset, not to this shape.
    pub ai_tags: Option<Vec<String>>,

    /// A title a machine gave it, which is not the filename and not a title a person wrote.
    pub ai_title: Option<String>,

    /// What kind of thing it is, which decides which pipeline reads it.
    pub asset_type: AssetType,

    /// The media type, as declared on arrival.
    pub content_type: String,

    /// When the asset was recorded, which is not when the file was made.
    pub created_at: Option<String>,

    /// The semantic vector of the whole asset.
    pub embedding: Option<Vec<f64>>,

    /// Size in bytes.
    pub file_size: i64,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// Raw technical metadata as the extractor read it off the file — dimensions, duration,
    /// codec, whatever the format carries.
    pub metadata: Option<HashMap<String, Option<serde_json::Value>>>,

    /// The name the file had when it arrived. Never the name it is stored under.
    pub original_filename: String,

    /// The wallet, handle, or id under localIds of whoever the asset belongs to. Absent for an
    /// asset that was put in before anybody claimed it.
    pub owner: Option<String>,

    /// Which step it was on. Read together with the status, it says where a run stopped: failed
    /// at ai_enrichment is a different repair from failed at embedding_indexing. Absent before
    /// the first step runs.
    pub processing_stage: Option<ProcessingStage>,

    /// Where the pipeline stands on this asset.
    pub processing_status: ProcessingStatus,

    /// The id of the working session it was put in during, in the system that owns the session.
    /// Absent when it was not put in through one.
    pub session: Option<String>,

    /// How it arrived: handed over as a file, or fetched from an address.
    pub source_type: Option<SourceType>,

    /// The address it was fetched from, when it was fetched. Kept even after ingestion, because
    /// the copy and the original drift apart.
    pub source_url: Option<String>,

    /// Where the bytes sit in the store that holds them. Meaningful only to that store; a reader
    /// asks it, never resolves the key itself.
    pub storage_key: String,

    /// A preview image made from the asset. A second file the asset owns, not the asset itself:
    /// it is derived, and absent until something made one.
    pub thumbnail: Option<StoredFile>,

    /// What was said in it, for an asset that is heard rather than read.
    pub transcript_text: Option<String>,

    pub updated_at: Option<String>,

    /// What is seen in it, for an asset that is looked at rather than read.
    pub visual_summary: Option<String>,
}

/// What kind of thing it is, which decides which pipeline reads it.
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

/// Which step it was on. Read together with the status, it says where a run stopped: failed
/// at ai_enrichment is a different repair from failed at embedding_indexing. Absent before
/// the first step runs.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum ProcessingStage {
    #[serde(rename = "ai_enrichment")]
    AiEnrichment,

    Completed,

    #[serde(rename = "embedding_indexing")]
    EmbeddingIndexing,

    #[serde(rename = "metadata_extraction")]
    MetadataExtraction,
}

/// Where the pipeline stands on this asset.
///
/// Where a pipeline stands on the thing it was given. Which move from which is a rule held
/// beside the type, never in it.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum ProcessingStatus {
    Completed,

    Failed,

    Pending,

    Processing,
}

/// How it arrived: handed over as a file, or fetched from an address.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum SourceType {
    Upload,

    Url,
}

/// A preview image made from the asset. A second file the asset owns, not the asset itself:
/// it is derived, and absent until something made one.
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