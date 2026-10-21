// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::Collection;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: Collection = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// A named gathering of assets, made by a person because they belong together for a reason
/// no pipeline would find. It holds no assets: it holds the edges that say which ones are in
/// it, and when each was put there.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Collection {
    /// The assets in it, each as its own edge: being in a collection is not an attribute of an
    /// asset, and the moment it was added belongs to the putting-in, not to either side.
    pub assets: Option<Vec<Asset>>,

    pub created_at: Option<String>,

    /// Why these belong together. Written by a person; never derived from what is inside.
    pub description: Option<String>,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// What it is called, in the words of whoever gathered it.
    pub name: String,

    /// The id of the working session it was made in, in the system that owns the session. Absent
    /// when it was not made through one.
    pub session: Option<String>,

    pub updated_at: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Asset {
    /// When it was put in, which is not when the asset was recorded.
    pub added_at: Option<String>,

    /// The id of the asset, in the system that owns it.
    pub asset: String,

    /// The edge's own id in the system that holds it.
    pub id: Option<String>,
}