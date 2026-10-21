// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * What somebody did with a generated piece when it was handed to them: took it, threw it
 * away, or rewrote it. An act rather than an opinion — the rewrite is the feedback, and it
 * is the one signal that says what good would have looked like.
 */
export interface GenerationFeedback {
    /**
     * What they did with it.
     */
    action: Action;
    /**
     * When they did it.
     */
    createdAt?: Date;
    /**
     * The piece as they rewrote it. Present when the action was edited; that it must be is a
     * rule the writing system keeps, not a shape.
     */
    editedOutput?: string;
    /**
     * The id of the generated piece this was done to, in the system that owns it.
     */
    generation: string;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * The id of the working session it happened in, in the system that holds it. Not a person:
     * a session says the acts came from one sitting, and whether anybody is named is the
     * holding system's business.
     */
    session?: string;
}

/**
 * What they did with it.
 */
export type Action = "approved" | "rejected" | "edited";