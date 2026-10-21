// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::Webhook;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: Webhook = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// A standing instruction to call a URL when something happens. The subscription only: what
/// is to be called and for which events. No signing secret travels here — whoever signs a
/// delivery holds the key for it, and a shared shape carrying it would be a secret in every
/// system that read the shape.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Webhook {
    /// Whether it is still being called. Turned off rather than deleted, so the deliveries
    /// already made keep pointing at something.
    pub active: Option<bool>,

    /// When the subscription was registered.
    pub created_at: Option<String>,

    /// Which events to post. Free text: the names belong to whoever emits them, and a shape that
    /// fixed them would go stale the first time one is added.
    pub events: Vec<String>,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// The session the subscription belongs to, as the system that owns the session names it.
    /// Deliveries are scoped by it, and so is who may read the subscription back. Optional:
    /// scoping a subscription to a working session is how Creative Flow holds it, not part of
    /// what it is, and a system without sessions must be able to carry the same shape.
    pub session: Option<String>,

    /// Where to post. http or https, as given: a subscription to a URL that no longer answers is
    /// still a fact about what was asked for.
    pub url: String,
}