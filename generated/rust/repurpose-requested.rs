// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::RepurposeRequested;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: RepurposeRequested = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// One piece of text somebody wants turned into several shorter ones. Unlike the other
/// commands, the whole instruction travels in the event: the asking system holds no job of
/// its own to read it back from. Keys are snake_case, not the camelCase the rest of leaf
/// uses: this travels inside a Liquid envelope, whose own fields (event_id, occurred_at,
/// event_type, owner_unit_ref) are snake_case and pinned byte-exact by signed golden
/// vectors. The shape follows the wire.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RepurposeRequested {
    /// Where the result is headed, which changes how it is written. Free text: the channels
    /// belong to whoever publishes.
    pub channel: Option<String>,

    /// The text to work from, in full. Not a reference to an asset: a repurpose can be asked of
    /// words that were never put in.
    pub context: Option<String>,

    /// Which shapes to write. Anything outside the list is dropped rather than refused, and a
    /// request left with none is not worked.
    pub formats: Option<Vec<Format>>,

    /// Anything else the asker wants said, in their own words.
    pub instructions: Option<String>,

    /// The job to report the work against, created by the pipeline if it does not exist yet.
    pub job_id: String,

    /// BCP-47 tag of the language to write in. Detected from the context when absent.
    pub language: Option<String>,

    /// What the result is for, in the vocabulary of whoever asked.
    pub objective: Option<String>,

    /// The working session the request belongs to, which is where the brand voice and the
    /// defaults come from.
    pub session_id: String,

    /// Whether to write in the brand voice held for the session. False writes neutrally.
    pub use_brand_voice: Option<bool>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum Format {
    Captions,

    #[serde(rename = "carousel_copy")]
    CarouselCopy,

    #[serde(rename = "cta_variants")]
    CtaVariants,

    Hashtags,

    Hooks,

    #[serde(rename = "short_scripts")]
    ShortScripts,
}