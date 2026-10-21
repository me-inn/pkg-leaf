// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::WebhookDelivery;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: WebhookDelivery = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};
use std::collections::HashMap;

/// One attempt to call a webhook: what was sent, what came back, and how many tries it took.
/// A record of its own rather than a column on the subscription, because one subscription
/// has many deliveries and each outlives the state of the next. No signature travels here,
/// for the same reason none travels on the subscription.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct WebhookDelivery {
    /// How many times this delivery has been tried.
    pub attempts: Option<i64>,

    /// When the attempt was recorded, which is not when the event happened.
    pub created_at: Option<String>,

    /// Which event triggered the call. Free text, matching one of the names on the subscription.
    pub event: String,

    /// The status code the endpoint answered with. Absent when the call never got an answer — a
    /// timeout and a 500 are different failures.
    pub http_status: Option<i64>,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// The body that was posted. Open on purpose: its keys belong to whoever emits the event,
    /// and the delivery only records what went out.
    pub payload: Option<HashMap<String, Option<serde_json::Value>>>,

    /// What the endpoint wrote back, kept as given. Read when a delivery has to be explained,
    /// never parsed.
    pub response_body: Option<String>,

    /// Where the attempt stands. Free text rather than an enum: the source has no declared set,
    /// only a default of pending.
    pub status: Option<String>,

    /// The subscription this attempt was made for, as the system that holds it names it.
    pub webhook: String,
}