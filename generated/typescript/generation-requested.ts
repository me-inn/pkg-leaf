// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * A piece of content somebody wants written. What to write is in the job, not in the event.
 * Keys are snake_case, not the camelCase the rest of leaf uses: this travels inside a
 * Liquid envelope, whose own fields (event_id, occurred_at, event_type, owner_unit_ref) are
 * snake_case and pinned byte-exact by signed golden vectors. The shape follows the wire.
 */
export interface GenerationRequested {
    /**
     * The job holding the template, the sources and everything else the generation needs.
     */
    job_id: string;
}