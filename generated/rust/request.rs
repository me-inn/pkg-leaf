// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::Request;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: Request = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// Somebody asking somebody else for a time. A request, not a booking: it records what was
/// asked, never that a slot is taken.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Request {
    pub answered_at: Option<String>,

    /// How to reach whoever asked, so an answer can get back to them.
    pub contacts: Option<Vec<ContactPoint>>,

    pub created_at: Option<String>,

    /// The wallet or local id of whoever is asking, when they have one. Absent for somebody with
    /// no account anywhere.
    pub from: Option<String>,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// Who is asking, as they gave it. Unverified, and read by a person.
    pub requester: Option<String>,

    /// An answer is final. A second answer does not change the first.
    pub state: Option<State>,

    /// The wallet, handle, or id under localIds of whoever is being asked.
    pub to: String,

    /// When they want, in their own words. Not a timestamp: a parsed date is a claim about a
    /// timezone and a working hour, and a person reading the words cannot misread them.
    pub wanted: String,
}

/// One way to reach an actor.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct ContactPoint {
    /// The language to write to this point in.
    pub locale: Option<Locale>,

    /// Which channel the value is for.
    #[serde(rename = "type")]
    pub contact_point_type: Type,

    /// An address, or a number in E.164 digits including the country code.
    pub value: String,

    pub verified: Option<bool>,

    pub verified_at: Option<String>,
}

/// Which channel the value is for.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum Type {
    Email,

    Mobile,

    Phone,

    Whatsapp,
}

/// The language to write to this point in.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum Locale {
    En,

    Es,

    Pt,
}

/// An answer is final. A second answer does not change the first.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum State {
    Confirmed,

    Declined,

    Pending,
}