// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::CreativeScore;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: CreativeScore = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// A reading of one generated piece: how it sat against the voice it was written for, how it
/// fitted the channel it was written into, and why. About a piece of work, never about the
/// person who asked for it — nothing here is said about an actor.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct CreativeScore {
    /// When the piece was scored, which is not when it was written.
    pub created_at: Option<String>,

    /// The id of the generated piece this reads, in the system that owns it. A piece of work,
    /// not an actor: it has no wallet.
    pub generation: String,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// The model that read the piece, as it was named at the time. Recorded so two scores can be
    /// told apart when the scorer changed underneath them.
    pub model_used: Option<String>,

    /// What the scorer made of the piece: the two scores, the one carried alongside them, and
    /// why.
    pub reading: CreativeReading,
}

/// What the scorer made of the piece: the two scores, the one carried alongside them, and
/// why.
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