// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::AssetUrlIngestRequested;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: AssetUrlIngestRequested = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// An address somebody wants fetched and read. The address is not here: the job already
/// names the asset and where it points, and the pipeline reads it from there. Keys are
/// snake_case, not the camelCase the rest of leaf uses: this travels inside a Liquid
/// envelope, whose own fields (event_id, occurred_at, event_type, owner_unit_ref) are
/// snake_case and pinned byte-exact by signed golden vectors. The shape follows the wire.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AssetUrlIngestRequested {
    /// The job that names the asset and the address to fetch.
    pub job_id: String,
}