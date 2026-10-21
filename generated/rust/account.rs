// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::Account;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: Account = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// What somebody is owed by the system that bills them: a plan, a credit balance, and the
/// day the cycle turns over. Not an actor and not an organisation — the actor is the person
/// who owns it, named here by key. One person can be billed by more than one system, and
/// each one keeps its own account.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Account {
    pub created_at: Option<String>,

    /// Credits left to spend. Whole credits, never fractions, because a half-spent credit is not
    /// a thing anybody can sell.
    pub credits_balance: i64,

    /// When the next cycle starts and the balance is refilled. Stated rather than computed from
    /// the plan, so a cycle moved by hand stays moved.
    pub cycle_renews_at: String,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// The wallet, handle, or id under localIds of the person billed. One account per person per
    /// system.
    pub owner: String,

    /// Which plan is in force, in the words of the system that sells it. Free text: the
    /// catalogue of plans belongs to the seller and changes without the shape changing.
    pub plan: String,

    pub updated_at: Option<String>,
}