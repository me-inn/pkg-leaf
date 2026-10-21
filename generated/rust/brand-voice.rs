// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::BrandVoice;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: BrandVoice = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// A snapshot of what a session has been approving: how much, how well it scored, and which
/// channels and objectives it kept coming back to. Counted once and written down, so the
/// figures a person saw on a day can be shown again on another day without recounting them.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct BrandVoice {
    /// How many pieces had been approved when the snapshot was taken.
    pub approved_count: i64,

    /// The mean of the latest score of each scored generation. Absent when nothing had been
    /// scored yet, which is not the same as zero.
    pub avg_overall_score: Option<f64>,

    /// When the snapshot was taken. It is what makes the figures readable later: they are true
    /// of that moment and of no other.
    pub created_at: Option<String>,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// The session this was counted over, as the system that owns the session names it.
    /// Optional: scoping a profile to a working session is how Creative Flow holds it, not part
    /// of what it is, and a system without sessions must be able to carry the same shape.
    pub session: Option<String>,

    /// The channels that came up most, most frequent first. A list, whatever a given store
    /// serialises it into.
    pub top_channels: Option<Vec<String>>,

    /// The objectives that came up most, most frequent first.
    pub top_objectives: Option<Vec<String>>,
}