// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * Something somebody wrote beside a generation — a remark about the text, not part of it.
 * It stays its own record so the generation reads as the model left it.
 */
export interface GenerationNote {
    /**
     * What they wrote, in their words.
     */
    body: string;
    /**
     * When the note was written.
     */
    createdAt?: Date;
    /**
     * The generation the note is about, by its id in the system that holds it.
     */
    generation: string;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * The working session the note was written in, by that session's id in the system that
     * holds it. The note is attributed to the session, not to a wallet: who was at the keyboard
     * is the session's own business.
     */
    session: string;
    /**
     * When it was last rewritten. A note is editable, so this differs from createdAt once it
     * has been.
     */
    updatedAt?: Date;
}