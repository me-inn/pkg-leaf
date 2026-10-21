// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * A piece of work the pipeline does to one asset: ingest it, read it, index it. The job is
 * the record of the attempt — when it started, when it stopped, and what went wrong — never
 * the work's output, which belongs to the asset it was done to.
 */
export interface Job {
    /**
     * The asset being worked on, as the system that owns the asset names it. A job without one
     * is not a job: there is nothing to process.
     */
    asset: string;
    /**
     * When the job was queued.
     */
    createdAt?: Date;
    /**
     * What went wrong, as the worker reported it. Read by a person deciding whether to retry;
     * never parsed.
     */
    errorMessage?: string;
    /**
     * When it stopped, whether it succeeded or failed. Absent while it runs.
     */
    finishedAt?: Date;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * When a worker picked it up, which is not when it was queued. Absent while it waits.
     */
    startedAt?: Date;
    /**
     * Where the attempt got to. A closed vocabulary because the pipeline branches on it, and
     * the same one the asset carries.
     */
    status: ProcessingStatus;
}

/**
 * Where the attempt got to. A closed vocabulary because the pipeline branches on it, and
 * the same one the asset carries.
 *
 * Where a pipeline stands on the thing it was given. Which move from which is a rule held
 * beside the type, never in it.
 */
export type ProcessingStatus = "pending" | "processing" | "completed" | "failed";