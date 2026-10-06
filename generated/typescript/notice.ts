// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * A link somebody put out — a video, a magazine, a product — and one line about it. A
 * pointer, never content: the system that holds the link holds what it says, and whoever
 * carries the notice only says that the link exists and when.
 */
export interface Notice {
    /**
     * The wallet, handle, or id under localIds of whoever put the link out.
     */
    by: string;
    /**
     * When the notice was recorded, which is not when the link was published.
     */
    createdAt?: Date;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * One line about it, in the words of whoever put it out. Read by a person; never fetched
     * from the link.
     */
    line?: string;
    /**
     * Where the link goes. https, so a page vouching for it can hand it to a machine.
     */
    url: string;
}