// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::Person;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: Person = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};
use std::collections::HashMap;

/// A person. Holds no authentication secret: password hashes, reset tokens and auth
/// providers belong to the system that authenticates.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Person {
    /// Ways to reach them.
    pub contacts: Option<Vec<ContactPoint>>,

    /// ISO 3166-1 alpha-2, where they are registered.
    pub country: Option<String>,

    pub created_at: Option<String>,

    /// The name they are known by.
    pub display_name: String,

    /// Their public address, without the @.
    pub handle: Option<String>,

    pub locale: Option<Locale>,

    /// The id this person has in each system that holds a record of them.
    pub local_ids: Option<HashMap<String, String>>,

    /// Their tax or registry identifiers, one per scheme.
    pub tax_ids: Option<Vec<TaxIdentifier>>,

    /// ed25519 public key, hex. Identifies the person. Absent until they hold one.
    pub wallet: Option<String>,
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

/// A tax or registry identifier.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct TaxIdentifier {
    /// ISO 3166-1 alpha-2, when the scheme does not imply one.
    pub country: Option<String>,

    /// URL of the supporting document.
    pub document_url: Option<String>,

    /// The scheme, such as CNPJ, CPF, NIF, VAT or EIN. Free text, always stated, never inferred
    /// from the length of the value.
    #[serde(rename = "type")]
    pub tax_identifier_type: String,

    pub value: String,
}