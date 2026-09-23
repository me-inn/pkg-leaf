// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * An organisation's role in an event, a publication, a split or a programme.
 */
export interface Participation {
    /**
     * What kind of thing it participates in.
     */
    context: Context;
    /**
     * The id of that thing, in the system that owns it.
     */
    contextId:  string;
    createdAt?: Date;
    /**
     * The organisation's wallet, or its id under localIds.
     */
    organization: string;
    /**
     * Its role there, in that context's own words. Free text: the vocabulary belongs to the
     * context.
     */
    role:    string;
    status?: Status;
}

/**
 * What kind of thing it participates in.
 */
export type Context = "event" | "publication" | "split" | "program";

export type Status = "proposed" | "active" | "ended";