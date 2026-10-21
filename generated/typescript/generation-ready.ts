// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * Content was written and is handed over in full. The one result that carries the work
 * itself rather than a reference to it: the asking system has no database of generations to
 * read it back from. Keys are snake_case, not the camelCase the rest of leaf uses: this
 * travels inside a Liquid envelope, whose own fields (event_id, occurred_at, event_type,
 * owner_unit_ref) are snake_case and pinned byte-exact by signed golden vectors. The shape
 * follows the wire.
 */
export interface GenerationReady {
    /**
     * The generation that was made.
     */
    content_id: string;
    /**
     * The text, as written.
     */
    output: string;
    /**
     * What the pipeline thought of its own output. Absent when nothing scored it, which is not
     * the same as a score of zero.
     */
    overall_score?: number;
    /**
     * The working session it was made in.
     */
    session_id: string;
    /**
     * The assets it was written from, by id.
     */
    source_assets?: string[];
    /**
     * Which template it was written from.
     */
    template: string;
}