// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::AssetRelation;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: AssetRelation = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// One asset pointing at another, and what the pointing means. An edge rather than a column:
/// an asset has no single related asset, and each kind of tie — one derived from another,
/// one resembling another — would otherwise add a field to a thing it was never an attribute
/// of.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct AssetRelation {
    pub created_at: Option<String>,

    /// The id of the asset the tie starts at, in the system that owns it. The direction carries
    /// the meaning: derived_from read the other way is false.
    pub from_asset: String,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// What the tie means, in the words of whoever drew it. Free text: the vocabulary belongs to
    /// the system that relates them.
    pub relation_type: String,

    /// The id of the asset the tie points at, in the system that owns it.
    pub to_asset: String,
}