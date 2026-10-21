// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * An address somebody wants fetched and read. The address is not here: the job already
 * names the asset and where it points, and the pipeline reads it from there. Keys are
 * snake_case, not the camelCase the rest of leaf uses: this travels inside a Liquid
 * envelope, whose own fields (event_id, occurred_at, event_type, owner_unit_ref) are
 * snake_case and pinned byte-exact by signed golden vectors. The shape follows the wire.
 */
export interface AssetURLIngestRequested {
    /**
     * The job that names the asset and the address to fetch.
     */
    job_id: string;
}