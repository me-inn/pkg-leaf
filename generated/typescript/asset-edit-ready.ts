// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * An edit was applied and saved as a new asset. Both ids travel, because the point of the
 * event is the pair: the original still stands and this one came from it. Keys are
 * snake_case, not the camelCase the rest of leaf uses: this travels inside a Liquid
 * envelope, whose own fields (event_id, occurred_at, event_type, owner_unit_ref) are
 * snake_case and pinned byte-exact by signed golden vectors. The shape follows the wire.
 */
export interface AssetEditReady {
    /**
     * The new asset the edit became. Named contentId and not assetId so every result event
     * points at its subject under one name.
     */
    content_id: string;
    /**
     * The asset that was edited, unchanged.
     */
    original_asset_id: string;
    /**
     * The working session the edit was made in.
     */
    session_id: string;
    /**
     * Where the edited bytes sit in the store that holds them. Meaningful only to that store.
     */
    storage_key: string;
}