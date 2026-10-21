// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * The shorter pieces were written and are handed over in full, for the same reason a
 * generation is. Keys are snake_case, not the camelCase the rest of leaf uses: this travels
 * inside a Liquid envelope, whose own fields (event_id, occurred_at, event_type,
 * owner_unit_ref) are snake_case and pinned byte-exact by signed golden vectors. The shape
 * follows the wire.
 */
export interface RepurposeReady {
    /**
     * What came out, keyed by the format that was asked for — hooks, captions, and the rest. A
     * format that was asked for and produced nothing is simply not here.
     */
    formats: { [key: string]: string };
    /**
     * The job the work was done under, which is what the asker was waiting on.
     */
    job_id: string;
    /**
     * The working session it was done in.
     */
    session_id: string;
}