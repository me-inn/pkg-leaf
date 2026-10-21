// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * A session holding on to a generation: kept near, so it is found again. An edge and not a
 * column, because being pinned is not a property of the generation — the same generation is
 * pinned in one session and not in another, and a column would make one session's opinion
 * look like the thing's own.
 */
export interface GenerationPin {
    /**
     * The generation being held on to, by its id in the system that holds it.
     */
    generation: string;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * When it was pinned.
     */
    pinnedAt?: Date;
    /**
     * The working session holding on to it, by that session's id in the system that holds it.
     * That a session pins a generation at most once is the pinning system's rule, not a
     * constraint of this shape.
     */
    session: string;
}