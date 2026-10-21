// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * One thing a model wrote when somebody asked for it: what was asked, what it was given to
 * read, and the text that came out. The assets it read are named by id and stay where they
 * are — this record is the asking, not a copy of the material.
 */
export interface Generation {
    /**
     * The assets the model was given to read, by their ids in the system that holds them. Ids,
     * never the material: the asset is somebody else's record.
     */
    assetIds?: string[];
    /**
     * Where the text was meant to go. Free text: the channels belong to whoever publishes, not
     * to this shape.
     */
    channel?: string;
    /**
     * Where the text stands. Which status may follow which is a rule held by the system that
     * moves it, not a constraint of this shape.
     */
    contentStatus?: ContentStatus;
    /**
     * When the generation was recorded.
     */
    createdAt?: Date;
    /**
     * What kind of thing was asked for. Free text: the vocabulary grows with every surface that
     * asks, so it is not closed here.
     */
    generationType: string;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * What the person asked for, in their own words, before anything was assembled around it.
     */
    instructions?: string;
    /**
     * Which model wrote it, under the name its provider gives it. Recorded so a later reading
     * knows what produced the text — never a key, never a provider credential.
     */
    modelUsed?: string;
    /**
     * What the text was meant to achieve. Free text, for the same reason as channel.
     */
    objective?: string;
    /**
     * The text the model produced. Empty while the generation exists and has produced nothing
     * yet.
     */
    output?: string;
    /**
     * The prompt actually sent, after the instructions and the context were assembled into one.
     * Kept because the instructions alone do not reproduce it.
     */
    promptUsed?: string;
    /**
     * The working session it was generated in, by that session's id in the system that holds
     * it. A session, not a person: who was at the keyboard is the session's own business.
     * Absent when it was generated outside one.
     */
    session?: string;
    /**
     * Labels somebody put on it. Free text, theirs.
     */
    tags?: string[];
}

/**
 * Where the text stands. Which status may follow which is a rule held by the system that
 * moves it, not a constraint of this shape.
 */
export type ContentStatus = "draft" | "approved" | "published" | "archived";