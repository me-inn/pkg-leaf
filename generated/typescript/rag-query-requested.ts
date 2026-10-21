// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * A question somebody wants answered out of what was put in. Carries the whole question,
 * for the same reason repurpose does. Keys are snake_case, not the camelCase the rest of
 * leaf uses: this travels inside a Liquid envelope, whose own fields (event_id,
 * occurred_at, event_type, owner_unit_ref) are snake_case and pinned byte-exact by signed
 * golden vectors. The shape follows the wire.
 */
export interface RagQueryRequested {
    /**
     * Search only this kind of asset. Absent searches all of them.
     */
    asset_type?: AssetType;
    /**
     * The job to report the answer against, created by the pipeline if it does not exist yet.
     */
    job_id: string;
    /**
     * BCP-47 tag of the language to answer in. Detected from the question when absent.
     */
    language?: string;
    /**
     * The question, in natural language. A blank one is not worked.
     */
    query?: string;
    /**
     * What to return: an answer grounded in the sources, or only the rewritten text, with
     * nothing around it, for an editor that drops it straight into a document.
     */
    response_mode?: ResponseMode;
    /**
     * The working session to search in. The question is answered out of that session's
     * material, not out of everything.
     */
    session_id: string;
    /**
     * How many chunks to retrieve before answering. Absent leaves it to whoever searches.
     */
    top_k?: number;
}

/**
 * Search only this kind of asset. Absent searches all of them.
 *
 * What kind of thing an asset is, which decides which pipeline reads it. A document covers
 * an article, a PDF, or raw text.
 */
export type AssetType = "image" | "video" | "document";

/**
 * What to return: an answer grounded in the sources, or only the rewritten text, with
 * nothing around it, for an editor that drops it straight into a document.
 */
export type ResponseMode = "answer" | "rewrite";