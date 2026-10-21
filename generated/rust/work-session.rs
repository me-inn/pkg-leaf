// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::WorkSession;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: WorkSession = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// A stretch of work somebody keeps coming back to, and the defaults everything made inside
/// it starts from. Named work-session, not session, because it has nothing to do with being
/// signed in: it outlives any login and carries no credential.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct WorkSession {
    /// The brand the work is for, as typed. A name, not a reference: the session is written
    /// before anybody decides whether that brand is a record anywhere.
    pub brand_name: Option<String>,

    /// When the session was opened.
    pub created_at: String,

    /// Where work made here is headed unless told otherwise. Free text: the channels belong to
    /// the system that publishes.
    pub default_channel: Option<String>,

    /// What work made here is for unless told otherwise. Free text, in the vocabulary of whoever
    /// set it.
    pub default_objective: Option<String>,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// When it was last touched. The reason the record is worth keeping: it says which sessions
    /// are still alive.
    pub last_seen: String,

    /// What the person called it. Absent until they bother to name it.
    pub name: Option<String>,

    /// The wallet, handle, or id under localIds of whoever is working. Absent while the work is
    /// anonymous — a session can exist before anybody has signed in for it.
    pub person: Option<String>,

    /// The id of the workspace the session sits in, in the system that owns workspaces.
    pub workspace: Option<String>,
}