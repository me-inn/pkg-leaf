// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * An asset was read through: metadata out, a machine's reading of it written, and its
 * chunks indexed. Says the asset is now worth searching, and nothing about what it says.
 * Keys are snake_case, not the camelCase the rest of leaf uses: this travels inside a
 * Liquid envelope, whose own fields (event_id, occurred_at, event_type, owner_unit_ref) are
 * snake_case and pinned byte-exact by signed golden vectors. The shape follows the wire.
 */
export interface ReadCompleted {
    /**
     * The asset that was read.
     */
    content_id: string;
    /**
     * The working session it was read in. Empty when the asset belongs to none.
     */
    session_id: string;
}