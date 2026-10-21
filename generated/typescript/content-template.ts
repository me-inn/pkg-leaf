// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * A saved starting point for generating something: what kind of piece, for which channel
 * and objective, with the standing instructions to use. Settings somebody wants back, not a
 * piece of content — nothing generated is kept here.
 */
export interface ContentTemplate {
    /**
     * Where the piece is meant to run, in the words of whoever saved the template. Free text
     * everywhere it appears: the vocabulary belongs to whoever publishes.
     */
    channel?: string;
    /**
     * When the template was saved.
     */
    createdAt?: Date;
    /**
     * What kind of piece it produces. Free text: the names belong to the generation flow, which
     * adds to them.
     */
    generationType: string;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * The standing instructions to apply, in the person's own words. The template's substance:
     * everything else only files it.
     */
    instructions?: string;
    /**
     * What the person called it, so they recognise it in a list.
     */
    name: string;
    /**
     * What the piece is meant to do. Free text, for the same reason as channel.
     */
    objective?: string;
    /**
     * The session the template belongs to, as the system that owns the session names it.
     * Optional: scoping a template to a working session is how Creative Flow holds it, not part
     * of what it is, and a system without sessions must be able to carry the same shape.
     */
    session?: string;
}