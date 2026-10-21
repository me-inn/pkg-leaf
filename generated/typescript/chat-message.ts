// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * One turn of a conversation held against a library: what was asked, or what was answered,
 * and for an answer the chunks it was grounded on. The sources are pointers with enough of
 * the text to recognise them — never the chunk itself, which stays with the asset it came
 * from.
 */
export interface ChatMessage {
    /**
     * What was said. The question as typed, or the answer as generated.
     */
    content: string;
    /**
     * When the turn was recorded. The only ordering the conversation has.
     */
    createdAt?: Date;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * Who spoke. Two values: a person asks and the model answers, and nothing else writes a
     * turn.
     */
    role: Role;
    /**
     * The session the turn belongs to, as the system that owns the session names it. Absent on
     * rows written before turns were scoped.
     */
    session?: string;
    /**
     * The chunks the answer was grounded on, in relevance order. Absent on a question, and
     * empty on an answer that was grounded on nothing.
     */
    sources?: RagSource[];
}

/**
 * Who spoke. Two values: a person asks and the model answers, and nothing else writes a
 * turn.
 */
export type Role = "user" | "assistant";

/**
 * One retrieved chunk an answer leaned on, as it was at the time of the answer. A pointer
 * plus what a person needs to judge it — never the chunk, which stays with the asset it
 * came from — so the citation still reads once the chunk has changed.
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
    assetTitle?: string;
    /**
     * The chunk itself, as the system that owns the chunk names it.
     */
    chunk: string;
    /**
     * Which part of the asset the chunk is — a summary, a transcript, a block of article text.
     * Free text: the vocabulary belongs to whoever chunks.
     */
    chunkType?: string;
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
    thumbnailUrl?: string;
}