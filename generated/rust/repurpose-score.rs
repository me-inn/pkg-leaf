// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::RepurposeScore;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: RepurposeScore = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// The same reading as a creative score, but of work a job turned into one other format. It
/// is its own record and not a column on the job: one job produces several formats, and each
/// is read on its own.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct RepurposeScore {
    /// When the output was scored, which is not when the job ran.
    pub created_at: Option<String>,

    /// Which of the job's outputs this score is for. One score per format, so the job's own id
    /// does not identify a record.
    pub format: Format,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// The id of the repurpose job that produced the work, in the system that ran it.
    pub job: String,

    /// What the scorer made of that one output. The same shape a creative score carries, read
    /// against the channel the format is meant for.
    pub reading: CreativeReading,
}

/// Which of the job's outputs this score is for. One score per format, so the job's own id
/// does not identify a record.
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

/// What the scorer made of that one output. The same shape a creative score carries, read
/// against the channel the format is meant for.
///
/// What a model made of a piece of work: how it sat against the voice it was written for,
/// how it fitted the channel it was written into, and why. About the work, never about
/// whoever asked for it — nothing here is said about an actor, so none of it is testimony.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct CreativeReading {
    /// How close the work came to the voice it was written for, from 0 to 1. The range is what
    /// the scorer produces, and keeping a number inside it is the job of the code that writes
    /// the record.
    pub brand_voice_score: f64,

    /// How well the work fitted the channel it was written into, from 0 to 1, on the same scale.
    pub channel_fit_score: f64,

    /// The single number carried alongside the two others, from 0 to 1. Stated rather than
    /// derived here: how the scorer weighed voice against fit is its own, and recomputing it
    /// elsewhere would invent a weighting nobody agreed to.
    pub overall_score: f64,

    /// Why those numbers, in the scorer's own words. Kept because a number with no account of
    /// itself cannot be argued with.
    pub reasoning: String,
}