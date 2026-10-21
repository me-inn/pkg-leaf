// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::PerformanceSignal;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: PerformanceSignal = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// One number a platform reported about one generated piece, at one moment. A reading and
/// not a total: a second reading of the same metric is another record, so what a piece did
/// over time is the series and never a field that gets overwritten.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct PerformanceSignal {
    /// The id of the generated piece the number is about, in the system that owns it.
    pub generation: String,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// What was counted, in the platform's own word for it. Free text for the same reason, and
    /// never translated on the way in: a platform's reach is not another platform's reach.
    pub metric_name: String,

    /// The number, as reported. No unit travels with it — the unit is whatever the platform
    /// means by that metric name.
    pub metric_value: f64,

    /// Where the piece ran and who counted. Free text: the names belong to the platforms, and a
    /// list here would be out of date the week somebody publishes somewhere new.
    pub platform: String,

    /// When the reading was taken, which is not when the piece was published and not when the
    /// platform computed it.
    pub recorded_at: Option<String>,
}