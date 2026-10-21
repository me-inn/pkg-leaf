// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * Content was written from assets already put in. The relay understands this type natively,
 * which is why it exists beside generation.ready: this one says a derivative was made, that
 * one hands over what it says. Keys are snake_case, not the camelCase the rest of leaf
 * uses: this travels inside a Liquid envelope, whose own fields (event_id, occurred_at,
 * event_type, owner_unit_ref) are snake_case and pinned byte-exact by signed golden
 * vectors. The shape follows the wire.
 */
export interface DerivativeCreated {
    /**
     * The generation that was made.
     */
    content_id: string;
    /**
     * The working session it was made in.
     */
    session_id: string;
    /**
     * The assets it was written from, by id. Absent when nothing was drawn on.
     */
    source_assets?: string[];
    /**
     * Which template it was written from. Free text: the templates belong to whoever generates.
     */
    template: string;
}