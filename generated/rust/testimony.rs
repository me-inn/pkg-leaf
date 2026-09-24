// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::Testimony;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: Testimony = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// Something one person wrote about another, published with the subject's consent and their
/// author's name attached.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Testimony {
    /// The wallet, or the id under localIds, of whoever wrote it.
    pub author: String,

    pub created_at: Option<String>,

    /// What was written, in the author's own words. A scene rather than an attribute: what the
    /// subject did, told by whoever was there.
    pub detail: Option<String>,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    pub published_at: Option<String>,

    /// While set, the subject is told the record exists and not what it says. Opens when they
    /// write their own, or when this passes.
    pub sealed_until: Option<String>,

    /// ed25519 over the record, hex. Signed by the author's wallet, so the words can be shown to
    /// have come from them.
    pub signature: Option<String>,

    /// Published only once the subject has agreed. Pending is written and not readable by anyone
    /// but its author.
    pub state: Option<State>,

    /// The wallet, or the id under localIds, of whoever it is about.
    pub subject: String,
}

/// Published only once the subject has agreed. Pending is written and not readable by anyone
/// but its author.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum State {
    Hidden,

    Pending,

    Published,
}