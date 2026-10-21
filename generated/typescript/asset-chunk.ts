// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * One piece of an asset held separately so it can be searched on its own. The text is kept
 * beside the vector so whoever answers from a chunk can show the excerpt it answered from,
 * without opening the asset.
 */
export interface AssetChunk {
    /**
     * The id of the asset this piece was cut from, in the system that owns it.
     */
    asset: string;
    /**
     * Position among the pieces of the same type on the same asset. Zero while a type yields
     * one piece; it exists so splitting a long text later does not change the shape.
     */
    chunkOrder: number;
    /**
     * The text that was embedded, verbatim.
     */
    chunkText: string;
    /**
     * Which reading of the asset this piece is. They are indexed together but recall
     * differently: title_tags catches a keyword, summary catches a meaning.
     */
    chunkType:  ChunkType;
    createdAt?: Date;
    /**
     * The semantic vector of this piece. A reader holding another model recomputes it from
     * chunkText.
     */
    embedding?: number[];
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * Whatever the splitter recorded about the cut — offsets into the source, token counts.
     */
    metadata?: { [key: string]: any };
}

/**
 * Which reading of the asset this piece is. They are indexed together but recall
 * differently: title_tags catches a keyword, summary catches a meaning.
 */
export type ChunkType = "title_tags" | "description" | "summary" | "metadata" | "transcript" | "visual_summary" | "article_text";