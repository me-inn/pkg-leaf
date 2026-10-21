// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * The text a generation held at one point in its life. Kept as its own record so editing a
 * generation never loses what it said before — the generation carries the current text, the
 * versions carry the ones it had.
 */
export interface GenerationVersion {
    /**
     * When this version was written.
     */
    createdAt?: Date;
    /**
     * The generation this is a version of, by its id in the system that holds it.
     */
    generation: string;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * The text as it stood in this version.
     */
    output: string;
    /**
     * Which version this is, counting up within the generation. Ordering is the number's job;
     * whether it may skip or repeat is the writing system's rule.
     */
    version: number;
}