// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::SignalError;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: SignalError = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};
use std::collections::HashMap;

/// Something in the pipeline broke, said in a way another system can route rather than only
/// print. The only event not about one piece of content: it is about a step that failed and
/// who answers for it. Keys are snake_case, not the camelCase the rest of leaf uses: this
/// travels inside a Liquid envelope, whose own fields (event_id, occurred_at, event_type,
/// owner_unit_ref) are snake_case and pinned byte-exact by signed golden vectors. The shape
/// follows the wire.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SignalError {
    /// A machine-readable code such as ENRICHMENT_TIMEOUT. Free text: the vocabulary belongs to
    /// whoever raised it, and a reader matches on it rather than on the summary.
    pub code: String,

    /// The trace this failure belongs to, for tying it to others from the same run.
    pub correlation_id: Option<String>,

    /// Whatever else the raising step knew — the asset, the stage it stopped at. Keys belong to
    /// that step, so none are fixed here.
    pub metadata: Option<HashMap<String, Option<serde_json::Value>>>,

    /// When the failure happened. Carried inside the payload as well as on the event, because
    /// the signal outlives the event that delivered it.
    pub occurred_at: String,

    /// The session or unit the failure belongs to. Who answers for it, which is how an error
    /// finds somebody at all.
    pub owner_unit_ref: String,

    /// How bad it is, as judged where it was raised.
    pub severity: Severity,

    /// The signal's own id, written where it was raised, so the same failure reported twice can
    /// be recognised as one.
    pub signal_id: String,

    /// The module that raised it, such as creativeflow.worker.process_asset. Says where to look,
    /// not who is at fault.
    pub source: String,

    /// Where the handling of it stands. Raised as reported; moved on by whoever picks it up, not
    /// by whoever raised it.
    pub status: Status,

    /// The thing that was being worked on when it broke, when there is one.
    pub subject_ref: Option<String>,

    /// What went wrong, for a person. Never the whole trace.
    pub summary: String,
}

/// How bad it is, as judged where it was raised.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum Severity {
    Critical,

    Error,

    Info,

    Warning,
}

/// Where the handling of it stands. Raised as reported; moved on by whoever picks it up, not
/// by whoever raised it.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum Status {
    Acknowledged,

    Reported,

    Resolved,
}