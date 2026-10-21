// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::Feedback;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: Feedback = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// A rating somebody gave a thing the software produced, with a line about it if they wrote
/// one. About an output and not about a person: it carries no subject, no consent and no
/// signature, which is what separates it from a testimony.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Feedback {
    /// What they wrote alongside the rating, in their own words.
    pub comment: Option<String>,

    /// When it was given.
    pub created_at: Option<String>,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// The rating as given, 1 to 5. Collected both ways: as a thumb, where only 1 and 5 are ever
    /// written, and as the whole scale. Which of the two it was is not recorded, so a mean over
    /// mixed records is a number about nothing.
    pub rating: i64,

    /// The id of the working session it came from, in the system that holds it. Not a person.
    pub session: Option<String>,

    /// The id of that thing, in the system that owns it. It is read together with targetType and
    /// alone means nothing — two kinds of target do not share an id space.
    pub target: String,

    /// What kind of thing was rated. Free text with the two the system records so far: a target
    /// type is added whenever something new becomes ratable, and a closed list here would have
    /// to be versioned for each one.
    pub target_type: String,
}