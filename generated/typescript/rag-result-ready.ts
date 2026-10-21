// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * A question was answered, and the answer comes back with what it was built out of. The
 * sources travel so the asker can show its work without holding the chunks. Keys are
 * snake_case, not the camelCase the rest of leaf uses: this travels inside a Liquid
 * envelope, whose own fields (event_id, occurred_at, event_type, owner_unit_ref) are
 * snake_case and pinned byte-exact by signed golden vectors. The shape follows the wire.
 */
export interface RagResultReady {
    /**
     * The answer, grounded in the sources below.
     */
    answer: string;
    /**
     * The job the answer was worked under, when the question arrived as one.
     */
    job_id?: string;
    /**
     * The question as asked, repeated so the answer is readable on its own.
     */
    query: string;
    /**
     * The working session the question was asked in.
     */
    session_id: string;
    /**
     * The chunks the answer was built from, in order of relevance. Absent when the search found
     * nothing to stand on. A producer of this event always fills in score, chunkType and
     * excerpt, even though the shared shape only insists on the two pointers.
     */
    sources?: RagSource[];
}

/**
 * One chunk the answer stood on. The same shape as common.v1 ragSource, written out here in
 * the relay's snake_case rather than referenced.
 */
export interface RagSource {
    /**
     * The asset the chunk came from, as the system that owns the asset names it.
     */
    asset: string;
    /**
     * What the parent asset was called when the answer was written. Kept as a copy on purpose:
     * a citation should still read after the asset is retitled.
     */
    asset_title?: string;
    /**
     * The chunk itself, as the system that owns the chunk names it.
     */
    chunk: string;
    /**
     * Which part of the asset the chunk is — a summary, a transcript, a block of article text.
     * Free text: the vocabulary belongs to whoever chunks.
     */
    chunk_type?: string;
    /**
     * The opening of the chunk, carried so a person can see what was cited without fetching it.
     */
    excerpt?: string;
    /**
     * How close the chunk sat to the question, as the retrieval scored it. Comparable inside
     * one search, not across searches: the scale belongs to the model that searched.
     */
    score?: number;
    /**
     * A picture of the parent asset, when the system that serves it offers one. Derived, and
     * resolvable only against the deploy that built it.
     */
    thumbnail_url?: string;
}