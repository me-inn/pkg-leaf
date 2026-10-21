// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * One thing the creative pipeline was asked to do, or one thing it finished — as it travels
 * between the system that asks and the system that works. Commands go one way and results
 * come back the other way over the same relay, so they are one shape with one type field
 * rather than two. The event carries no content: what it carries is an id of something a
 * system already holds, and enough words to act on it. Keys are snake_case, not the
 * camelCase the rest of leaf uses: this travels inside a Liquid envelope, whose own fields
 * (event_id, occurred_at, event_type, owner_unit_ref) are snake_case and pinned byte-exact
 * by signed golden vectors. The shape follows the wire.
 */
export interface CreativeEvent {
    /**
     * ed25519 public key, hex, of whoever signed the event. The only thing that says who asked:
     * a reader admits an event by this key, never by the name below.
     */
    author?: string;
    /**
     * What the signing system calls itself, such as creativeflow. A label for reading a log; it
     * proves nothing, and two systems may well claim the same one.
     */
    author_name?: string;
    /**
     * The asset, generation or job the event is about, repeated outside the payload so a reader
     * can file the event without opening it. Absent for events about no single thing, such as
     * an error.
     */
    content_id?: string;
    /**
     * The device the event was written on, when more than one writes for the same author.
     */
    device_id?: string;
    /**
     * What happened, written as <domain>.<action>. The requested forms are commands addressed
     * to the pipeline; the rest are results it emits. It alone decides which payload shape
     * applies — two different commands can carry the same single id and are told apart by
     * nothing else.
     */
    event_type: EventType;
    /**
     * The record's own id in the system that holds it. Also what makes the event replayable
     * without doing the work twice: a reader that has seen this id has already acted.
     */
    id?: string;
    /**
     * A counter for ordering events from one author when wall clocks disagree. Comparable only
     * against events from the same author.
     */
    lamport?: number;
    /**
     * When the author says it happened, which is not when a reader received it.
     */
    occurred_at?: Date;
    /**
     * The session or unit the event belongs to, which is who answers for it. Set on errors
     * above all, where it is the only thing saying whose work broke.
     */
    owner_unit_ref?: string;
    /**
     * What the event is about. Open on purpose: eventType decides which schema the payload is,
     * and a reader picks that type rather than matching on the shape. The union used to live
     * here as anyOf and the generator kept only its first branch, so the other fourteen
     * payloads had no type at all; each is now its own schema. asset.ingest_requested ->
     * AssetIngestRequested; asset.url_ingest_requested -> AssetUrlIngestRequested;
     * generation.requested -> GenerationRequested; repurpose.requested -> RepurposeRequested;
     * rag.query_requested -> RagQueryRequested; asset.edit_requested -> AssetEditRequested;
     * read.completed -> ReadCompleted; derivative.created -> DerivativeCreated;
     * citation.created -> CitationCreated; value.snapshot -> ValueSnapshot; signal.error ->
     * SignalError; generation.ready -> GenerationReady; rag.result_ready -> RagResultReady;
     * repurpose.ready -> RepurposeReady; asset.edit_ready -> AssetEditReady.
     */
    payload: { [key: string]: any };
}

/**
 * What happened, written as <domain>.<action>. The requested forms are commands addressed
 * to the pipeline; the rest are results it emits. It alone decides which payload shape
 * applies — two different commands can carry the same single id and are told apart by
 * nothing else.
 */
export type EventType = "asset.ingest_requested" | "asset.url_ingest_requested" | "generation.requested" | "repurpose.requested" | "rag.query_requested" | "asset.edit_requested" | "read.completed" | "derivative.created" | "citation.created" | "value.snapshot" | "signal.error" | "generation.ready" | "rag.result_ready" | "repurpose.ready" | "asset.edit_ready";