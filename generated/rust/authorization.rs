// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::Authorization;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: Authorization = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// Somebody letting a piece of software act for them. What was granted, to whom, and until
/// when — never the credential that proves it. The code and the token are secrets, they are
/// held only as a hash by the system that issued them, and neither has a shape here.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Authorization {
    /// The https URL that identifies the software. It is also where that software describes
    /// itself, so nothing about it has to be copied here.
    pub client: String,

    /// When it stops working on its own, with nobody having to do anything.
    pub expires_at: Option<String>,

    pub granted_at: Option<String>,

    /// What the software calls itself, as it said. Recorded so a person recognises it when
    /// deciding what to take back; never used to decide anything.
    pub label: Option<String>,

    /// When it was taken back. A grant that ended is kept rather than deleted: what was allowed,
    /// and until when, is a fact about the past.
    pub revoked_at: Option<String>,

    /// The wallet, or the id under localIds, of whoever is being acted for. The grant is theirs
    /// and so is taking it back.
    pub subject: String,
}