// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::Publication;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: Publication = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// A book put out on one store, and what that store calls it. An edge between a title and a
/// platform: the same book on three stores is three of these, each with its own listing, its
/// own state and its own rate.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Publication {
    /// The id of the book being put out, in the system that holds the book.
    pub book: String,

    pub created_at: Option<String>,

    /// What this listing is expected to pay in a month, in the currency the store settles in. An
    /// estimate carried for planning, never an amount owed.
    pub estimated_monthly_royalty: Option<f64>,

    /// What the store calls this listing — its ASIN, its product id. The only handle the store
    /// will answer to.
    pub external_id: Option<String>,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// The page a reader buys it on.
    pub listing_url: Option<String>,

    /// Anything about this listing worth writing down, in the words of whoever put it out.
    pub notes: Option<String>,

    /// Where it is being put out. Manual is for a channel nobody here talks to, recorded so the
    /// title's whereabouts stay complete.
    pub platform: Platform,

    /// When the listing went live on the store.
    pub published_at: Option<String>,

    /// The author's share, as a fraction: 0.7 is seventy per cent. A fraction and not a
    /// percentage so nobody has to guess which was meant.
    pub royalty_rate: Option<f64>,

    /// Where the listing stands on that store. Read from the store, not decided here.
    pub status: Option<Status>,

    /// When it was sent to the store, which is not when the store accepted it.
    pub submitted_at: Option<String>,

    pub updated_at: Option<String>,
}

/// Where it is being put out. Manual is for a channel nobody here talks to, recorded so the
/// title's whereabouts stay complete.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum Platform {
    #[serde(rename = "amazon_kdp")]
    AmazonKdp,

    #[serde(rename = "apple_books")]
    AppleBooks,

    #[serde(rename = "google_play")]
    GooglePlay,

    Kobo,

    Manual,
}

/// Where the listing stands on that store. Read from the store, not decided here.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum Status {
    Draft,

    Live,

    Rejected,

    Submitted,

    Unpublished,
}