// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * Something somebody put in — a file uploaded or a page ingested from a URL — and
 * everything a machine later said about it. The bytes never travel: what travels is where
 * they are kept, what kind of thing they are, and the reading a pipeline made of them.
 */
export interface Asset {
    /**
     * What a machine said the asset is.
     */
    aiDescription?: string;
    /**
     * The longer reading a machine made of it.
     */
    aiSummary?: string;
    /**
     * Tags a machine put on it. Free text: the vocabulary belongs to whoever enriched the
     * asset, not to this shape.
     */
    aiTags?: string[];
    /**
     * A title a machine gave it, which is not the filename and not a title a person wrote.
     */
    aiTitle?: string;
    /**
     * What kind of thing it is, which decides which pipeline reads it.
     */
    assetType: AssetType;
    /**
     * The media type, as declared on arrival.
     */
    contentType: string;
    /**
     * When the asset was recorded, which is not when the file was made.
     */
    createdAt?: Date;
    /**
     * The semantic vector of the whole asset.
     */
    embedding?: number[];
    /**
     * Size in bytes.
     */
    fileSize: number;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * Raw technical metadata as the extractor read it off the file — dimensions, duration,
     * codec, whatever the format carries.
     */
    metadata?: { [key: string]: any };
    /**
     * The name the file had when it arrived. Never the name it is stored under.
     */
    originalFilename: string;
    /**
     * The wallet, handle, or id under localIds of whoever the asset belongs to. Absent for an
     * asset that was put in before anybody claimed it.
     */
    owner?: string;
    /**
     * Which step it was on. Read together with the status, it says where a run stopped: failed
     * at ai_enrichment is a different repair from failed at embedding_indexing. Absent before
     * the first step runs.
     */
    processingStage?: ProcessingStage;
    /**
     * Where the pipeline stands on this asset.
     */
    processingStatus: ProcessingStatus;
    /**
     * The id of the working session it was put in during, in the system that owns the session.
     * Absent when it was not put in through one.
     */
    session?: string;
    /**
     * How it arrived: handed over as a file, or fetched from an address.
     */
    sourceType?: SourceType;
    /**
     * The address it was fetched from, when it was fetched. Kept even after ingestion, because
     * the copy and the original drift apart.
     */
    sourceUrl?: string;
    /**
     * Where the bytes sit in the store that holds them. Meaningful only to that store; a reader
     * asks it, never resolves the key itself.
     */
    storageKey: string;
    /**
     * A preview image made from the asset. A second file the asset owns, not the asset itself:
     * it is derived, and absent until something made one.
     */
    thumbnail?: StoredFile;
    /**
     * What was said in it, for an asset that is heard rather than read.
     */
    transcriptText?: string;
    updatedAt?:      Date;
    /**
     * What is seen in it, for an asset that is looked at rather than read.
     */
    visualSummary?: string;
}

/**
 * What kind of thing it is, which decides which pipeline reads it.
 *
 * What kind of thing an asset is, which decides which pipeline reads it. A document covers
 * an article, a PDF, or raw text.
 */
export type AssetType = "image" | "video" | "document";

/**
 * Which step it was on. Read together with the status, it says where a run stopped: failed
 * at ai_enrichment is a different repair from failed at embedding_indexing. Absent before
 * the first step runs.
 */
export type ProcessingStage = "metadata_extraction" | "ai_enrichment" | "embedding_indexing" | "completed";

/**
 * Where the pipeline stands on this asset.
 *
 * Where a pipeline stands on the thing it was given. Which move from which is a rule held
 * beside the type, never in it.
 */
export type ProcessingStatus = "pending" | "processing" | "completed" | "failed";

/**
 * How it arrived: handed over as a file, or fetched from an address.
 */
export type SourceType = "upload" | "url";

/**
 * A preview image made from the asset. A second file the asset owns, not the asset itself:
 * it is derived, and absent until something made one.
 *
 * Bytes somebody is keeping, pointed at rather than carried. Never the file itself: the
 * store that holds it holds it, and this says which key to ask under and, while it lasts,
 * where it can be fetched. Nothing is required, because a file can be known by its key
 * before any address has been issued for it, and served by an address before anybody
 * recorded a key.
 */
export interface StoredFile {
    /**
     * How big it is, so whoever is about to fetch it knows what they are asking for.
     */
    sizeBytes?: number;
    /**
     * Where the bytes sit in the store that holds them. The lasting handle, meaningful only to
     * that store: a reader asks the store, never resolves the key itself.
     */
    storageKey?: string;
    /**
     * Where the file can be fetched right now. Often signed and short-lived, so it is read at
     * the moment of use and never kept as the address of the file.
     */
    url?: string;
}