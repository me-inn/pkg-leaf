// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * Something one person wrote about another, published with the subject's consent and their
 * author's name attached.
 */
export interface Testimony {
    /**
     * The wallet, or the id under localIds, of whoever wrote it.
     */
    author:     string;
    createdAt?: Date;
    /**
     * What was written, in the author's own words. A scene rather than an attribute: what the
     * subject did, told by whoever was there.
     */
    detail?: string;
    /**
     * The record's own id in the system that holds it.
     */
    id?:          string;
    publishedAt?: Date;
    /**
     * While set, the subject is told the record exists and not what it says. Opens when they
     * write their own, or when this passes.
     */
    sealedUntil?: Date;
    /**
     * ed25519 over the record, hex. Signed by the author's wallet, so the words can be shown to
     * have come from them.
     */
    signature?: string;
    /**
     * Published only once the subject has agreed. Pending is written and not readable by anyone
     * but its author.
     */
    state?: State;
    /**
     * The wallet, or the id under localIds, of whoever it is about.
     */
    subject: string;
}

/**
 * Published only once the subject has agreed. Pending is written and not readable by anyone
 * but its author.
 */
export type State = "pending" | "published" | "hidden";