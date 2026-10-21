// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::Job;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: Job = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

/// A piece of work the pipeline does to one asset: ingest it, read it, index it. The job is
/// the record of the attempt — when it started, when it stopped, and what went wrong — never
/// the work's output, which belongs to the asset it was done to.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Job {
    /// The asset being worked on, as the system that owns the asset names it. A job without one
    /// is not a job: there is nothing to process.
    pub asset: String,

    /// When the job was queued.
    pub created_at: Option<String>,

    /// What went wrong, as the worker reported it. Read by a person deciding whether to retry;
    /// never parsed.
    pub error_message: Option<String>,

    /// When it stopped, whether it succeeded or failed. Absent while it runs.
    pub finished_at: Option<String>,

    /// The record's own id in the system that holds it.
    pub id: Option<String>,

    /// When a worker picked it up, which is not when it was queued. Absent while it waits.
    pub started_at: Option<String>,

    /// Where the attempt got to. A closed vocabulary because the pipeline branches on it, and
    /// the same one the asset carries.
    pub status: ProcessingStatus,
}

/// Where the attempt got to. A closed vocabulary because the pipeline branches on it, and
/// the same one the asset carries.
///
/// Where a pipeline stands on the thing it was given. Which move from which is a rule held
/// beside the type, never in it.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum ProcessingStatus {
    Completed,

    Failed,

    Pending,

    Processing,
}