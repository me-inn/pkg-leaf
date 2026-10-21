// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::SessionQuota;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: SessionQuota = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// How much a work session may spend in a day. Its own record rather than fields on the
/// session, because the limits are set by whoever runs the system and the session is written
/// by whoever uses it.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct SessionQuota {
    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// Generations allowed in a day.
    pub max_generations_per_day: i64,

    /// Repurposes allowed in a day.
    pub max_repurpose_per_day: i64,

    /// The wallet, handle, or id under localIds of whoever owns the quota. Carried so the holder
    /// of a session id is not by itself the person allowed to change the limits; absent for a
    /// session nobody has signed in for.
    pub person: Option<String>,

    /// The work session the limits apply to, as the system that owns the session names it. One
    /// quota per session.
    pub session: String,
}