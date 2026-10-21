// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::AssetEditRequested;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: AssetEditRequested = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// A cut, a resize or a filter somebody wants applied. The original is never changed: the
/// result is a new asset. Keys are snake_case, not the camelCase the rest of leaf uses: this
/// travels inside a Liquid envelope, whose own fields (event_id, occurred_at, event_type,
/// owner_unit_ref) are snake_case and pinned byte-exact by signed golden vectors. The shape
/// follows the wire.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AssetEditRequested {
    /// The asset to edit, which stays as it is.
    pub asset_id: String,

    /// What to do to it. Every step is optional and they apply together; an empty one copies the
    /// asset.
    pub edit_params: Option<EditParams>,

    /// The job to report the edit against.
    pub job_id: String,
}

/// What to do to it. Every step is optional and they apply together; an empty one copies the
/// asset.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct EditParams {
    /// The rectangle to keep, in pixels from the top left of the original.
    pub crop: Option<CropParams>,

    /// How to treat the image. The four multipliers leave it alone at 1.
    pub filters: Option<FilterParams>,

    /// The size to come out at, said either by naming a channel's preset or by giving both sides.
    pub resize: Option<ResizeParams>,

    /// The stretch to keep, in seconds from the start. Video only.
    pub trim: Option<TrimParams>,
}

/// The rectangle to keep, in pixels from the top left of the original.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CropParams {
    /// How tall the kept rectangle is, in pixels.
    pub height: i64,

    /// How wide the kept rectangle is, in pixels.
    pub width: i64,

    /// Pixels from the left edge of the original to the left edge of the rectangle.
    pub x: i64,

    /// Pixels from the top edge of the original to the top edge of the rectangle.
    pub y: i64,
}

/// How to treat the image. The four multipliers leave it alone at 1.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FilterParams {
    /// Gaussian sigma. 0 is no blur.
    pub blur: Option<f64>,

    /// Multiplier on how light it is. Below 1 darkens, above 1 lightens.
    pub brightness: Option<f64>,

    /// Multiplier on the distance between light and dark. Below 1 flattens, above 1 deepens.
    pub contrast: Option<f64>,

    /// 0 is grey.
    pub saturation: Option<f64>,

    /// Multiplier on edge definition. Below 1 softens, above 1 sharpens.
    pub sharpness: Option<f64>,

    /// Whether to darken the corners. On or off: how much is the editor's to decide.
    pub vignette: Option<bool>,
}

/// The size to come out at, said either by naming a channel's preset or by giving both sides.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ResizeParams {
    /// How tall to come out, in pixels. Given together with width, instead of a preset.
    pub height: Option<i64>,

    /// A named size belonging to a channel. What each one resolves to is the editor's to know,
    /// not this shape's.
    pub preset: Option<Preset>,

    /// How wide to come out, in pixels. Given together with height, instead of a preset.
    pub width: Option<i64>,
}

/// A named size belonging to a channel. What each one resolves to is the editor's to know,
/// not this shape's.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum Preset {
    #[serde(rename = "ig_feed")]
    IgFeed,

    #[serde(rename = "ig_landscape")]
    IgLandscape,

    #[serde(rename = "ig_reels")]
    IgReels,

    #[serde(rename = "ig_story")]
    IgStory,

    Tiktok,
}

/// The stretch to keep, in seconds from the start. Video only.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TrimParams {
    /// Where the kept stretch ends, in seconds from the start of the original.
    pub end_seconds: f64,

    /// Where the kept stretch begins, in seconds from the start of the original.
    pub start_seconds: f64,
}