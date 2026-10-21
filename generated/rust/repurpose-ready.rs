// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::RepurposeReady;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: RepurposeReady = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};
use std::collections::HashMap;

/// The shorter pieces were written and are handed over in full, for the same reason a
/// generation is. Keys are snake_case, not the camelCase the rest of leaf uses: this travels
/// inside a Liquid envelope, whose own fields (event_id, occurred_at, event_type,
/// owner_unit_ref) are snake_case and pinned byte-exact by signed golden vectors. The shape
/// follows the wire.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RepurposeReady {
    /// What came out, keyed by the format that was asked for — hooks, captions, and the rest. A
    /// format that was asked for and produced nothing is simply not here.
    pub formats: HashMap<String, String>,

    /// The job the work was done under, which is what the asker was waiting on.
    pub job_id: String,

    /// The working session it was done in.
    pub session_id: String,
}