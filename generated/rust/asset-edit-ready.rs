// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::AssetEditReady;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: AssetEditReady = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// An edit was applied and saved as a new asset. Both ids travel, because the point of the
/// event is the pair: the original still stands and this one came from it. Keys are
/// snake_case, not the camelCase the rest of leaf uses: this travels inside a Liquid
/// envelope, whose own fields (event_id, occurred_at, event_type, owner_unit_ref) are
/// snake_case and pinned byte-exact by signed golden vectors. The shape follows the wire.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AssetEditReady {
    /// The new asset the edit became. Named contentId and not assetId so every result event
    /// points at its subject under one name.
    pub content_id: String,

    /// The asset that was edited, unchanged.
    pub original_asset_id: String,

    /// The working session the edit was made in.
    pub session_id: String,

    /// Where the edited bytes sit in the store that holds them. Meaningful only to that store.
    pub storage_key: String,
}