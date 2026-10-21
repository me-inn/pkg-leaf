// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::TokenUsage;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: TokenUsage = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// What one call to a model cost: who made it, which model answered, how many tokens each
/// way, and the money. Separate from the credit ledger — credits are what the customer is
/// charged, tokens are what the call actually consumed, and the two move for different
/// reasons.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct TokenUsage {
    /// What the call was for, in the words of the system that made it. Free text: the kinds of
    /// call belong to that system.
    pub call_type: String,

    /// What the call cost in US dollars, worked out when it was written from the prices in force
    /// then. Recorded rather than recomputed: prices change, and what was spent does not.
    pub cost_usd: f64,

    /// When the call was recorded.
    pub created_at: Option<String>,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// Tokens sent.
    pub input_tokens: i64,

    /// The id of the job that made the call, in the system that owns jobs.
    pub job: Option<String>,

    /// The model name as the provider gives it, verbatim. Kept exactly because the price was
    /// read against this string.
    pub model: String,

    /// Tokens returned.
    pub output_tokens: i64,

    /// The wallet, handle, or id under localIds of whoever the call was made for. Absent for a
    /// call nobody is signed in behind, such as a background pass.
    pub person: Option<String>,

    /// Who served the call. Free text: providers are added without the shape changing.
    pub provider: String,

    /// The work session the call belongs to, as the system that owns the session names it.
    /// Absent when it belongs to none.
    pub session: Option<String>,
}