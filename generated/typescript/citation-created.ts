// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * An address was fetched and kept as an asset. The address stays in the event because the
 * copy and the page drift apart from that moment. Keys are snake_case, not the camelCase
 * the rest of leaf uses: this travels inside a Liquid envelope, whose own fields (event_id,
 * occurred_at, event_type, owner_unit_ref) are snake_case and pinned byte-exact by signed
 * golden vectors. The shape follows the wire.
 */
export interface CitationCreated {
    /**
     * The asset the fetched page became.
     */
    content_id: string;
    /**
     * The working session it was fetched into.
     */
    session_id: string;
    /**
     * The address it was fetched from.
     */
    source_url: string;
}