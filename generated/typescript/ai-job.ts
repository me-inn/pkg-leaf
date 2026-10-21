// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * A short-lived record of an asynchronous model call — a generation, a retrieval answer, an
 * edit, a repurpose. Separate from job: a job is work done to one asset and reports timing,
 * this is work asked for inside a session and reports an answer. The two are kept apart
 * rather than merged behind a discriminator because they do not agree on what is required
 * or on what is kept.
 */
export interface AIJob {
    /**
     * When the call was queued.
     */
    createdAt?: Date;
    /**
     * What went wrong, as the worker reported it. Read by a person; never parsed.
     */
    errorMessage?: string;
    /**
     * The record's own id in the system that holds it. It is what the caller polls with.
     */
    id?: string;
    /**
     * Which kind of call was asked for. Free text: the vocabulary belongs to whoever queues the
     * job, and it grows every time a new flow is added.
     */
    jobType: string;
    /**
     * What came back, in the shape the job type produces. Left open on purpose: a repurpose
     * result and a retrieval answer have nothing in common, and declaring one shape for both
     * would describe neither.
     */
    result?: { [key: string]: any };
    /**
     * The session the job was asked for, as the system that owns the session names it. It is
     * what keeps one session from reading another's answer. Absent on rows written before jobs
     * were scoped.
     */
    session?: string;
    /**
     * Where the call got to. Free text here, unlike job: the column carries no enum and each
     * flow writes its own words.
     */
    status: string;
}