// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * Something in the pipeline broke, said in a way another system can route rather than only
 * print. The only event not about one piece of content: it is about a step that failed and
 * who answers for it. Keys are snake_case, not the camelCase the rest of leaf uses: this
 * travels inside a Liquid envelope, whose own fields (event_id, occurred_at, event_type,
 * owner_unit_ref) are snake_case and pinned byte-exact by signed golden vectors. The shape
 * follows the wire.
 */
export interface SignalError {
    /**
     * A machine-readable code such as ENRICHMENT_TIMEOUT. Free text: the vocabulary belongs to
     * whoever raised it, and a reader matches on it rather than on the summary.
     */
    code: string;
    /**
     * The trace this failure belongs to, for tying it to others from the same run.
     */
    correlation_id?: string;
    /**
     * Whatever else the raising step knew — the asset, the stage it stopped at. Keys belong to
     * that step, so none are fixed here.
     */
    metadata?: { [key: string]: any };
    /**
     * When the failure happened. Carried inside the payload as well as on the event, because
     * the signal outlives the event that delivered it.
     */
    occurred_at: Date;
    /**
     * The session or unit the failure belongs to. Who answers for it, which is how an error
     * finds somebody at all.
     */
    owner_unit_ref: string;
    /**
     * How bad it is, as judged where it was raised.
     */
    severity: Severity;
    /**
     * The signal's own id, written where it was raised, so the same failure reported twice can
     * be recognised as one.
     */
    signal_id: string;
    /**
     * The module that raised it, such as creativeflow.worker.process_asset. Says where to look,
     * not who is at fault.
     */
    source: string;
    /**
     * Where the handling of it stands. Raised as reported; moved on by whoever picks it up, not
     * by whoever raised it.
     */
    status: Status;
    /**
     * The thing that was being worked on when it broke, when there is one.
     */
    subject_ref?: string;
    /**
     * What went wrong, for a person. Never the whole trace.
     */
    summary: string;
}

/**
 * How bad it is, as judged where it was raised.
 */
export type Severity = "info" | "warning" | "error" | "critical";

/**
 * Where the handling of it stands. Raised as reported; moved on by whoever picks it up, not
 * by whoever raised it.
 */
export type Status = "reported" | "acknowledged" | "resolved";