// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::Membership;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: Membership = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// A person belonging to an organisation.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Membership {
    /// What they may do inside it. Free text: the verbs belong to the system that grants them.
    pub capabilities: Option<Vec<String>>,

    pub created_at: Option<String>,

    /// The wallet or local id of whoever invited them.
    pub invited_by: Option<String>,

    /// The organisation's wallet, or its id under localIds.
    pub organization: String,

    /// The person's wallet, or their id under localIds.
    pub person: String,

    pub status: Option<Status>,

    pub updated_at: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum Status {
    Active,

    Invited,

    Left,

    Suspended,
}