// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * One piece of text somebody wants turned into several shorter ones. Unlike the other
 * commands, the whole instruction travels in the event: the asking system holds no job of
 * its own to read it back from. Keys are snake_case, not the camelCase the rest of leaf
 * uses: this travels inside a Liquid envelope, whose own fields (event_id, occurred_at,
 * event_type, owner_unit_ref) are snake_case and pinned byte-exact by signed golden
 * vectors. The shape follows the wire.
 */
export interface RepurposeRequested {
    /**
     * Where the result is headed, which changes how it is written. Free text: the channels
     * belong to whoever publishes.
     */
    channel?: string;
    /**
     * The text to work from, in full. Not a reference to an asset: a repurpose can be asked of
     * words that were never put in.
     */
    context?: string;
    /**
     * Which shapes to write. Anything outside the list is dropped rather than refused, and a
     * request left with none is not worked.
     */
    formats?: Format[];
    /**
     * Anything else the asker wants said, in their own words.
     */
    instructions?: string;
    /**
     * The job to report the work against, created by the pipeline if it does not exist yet.
     */
    job_id: string;
    /**
     * BCP-47 tag of the language to write in. Detected from the context when absent.
     */
    language?: string;
    /**
     * What the result is for, in the vocabulary of whoever asked.
     */
    objective?: string;
    /**
     * The working session the request belongs to, which is where the brand voice and the
     * defaults come from.
     */
    session_id: string;
    /**
     * Whether to write in the brand voice held for the session. False writes neutrally.
     */
    use_brand_voice?: boolean;
}

export type Format = "hooks" | "captions" | "short_scripts" | "carousel_copy" | "hashtags" | "cta_variants";