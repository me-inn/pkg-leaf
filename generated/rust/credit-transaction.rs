// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::CreditTransaction;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: CreditTransaction = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// One movement of credit on an account, written once and never changed. The balance on the
/// account is the sum of these; a row kept after the fact is what makes it possible to say
/// why.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct CreditTransaction {
    /// The id of the account the credit moved on, in the system that holds it.
    pub account: String,

    /// Signed: negative spends, positive tops up or refills. One field rather than a direction
    /// and a magnitude, so adding them up needs no rules.
    pub amount: i64,

    /// The balance the moment after this movement was applied. Copied here on purpose: reading a
    /// balance as of some past row should not mean replaying the whole ledger.
    pub balance_after: i64,

    /// When the movement was recorded.
    pub created_at: Option<String>,

    /// A line a person can read on a receipt or in support. Written by whoever charged; empty
    /// when nobody wrote one.
    pub description: String,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// What caused the movement, in the words of the system that charged for it. Free text: the
    /// list of billable operations belongs to that system.
    pub operation: String,

    /// The id of the job or generation that caused it, in the system that owns that thing.
    /// Absent for a refill or a top-up, which answer to nothing.
    pub reference: Option<String>,
}