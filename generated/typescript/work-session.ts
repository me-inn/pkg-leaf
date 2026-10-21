// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * A stretch of work somebody keeps coming back to, and the defaults everything made inside
 * it starts from. Named work-session, not session, because it has nothing to do with being
 * signed in: it outlives any login and carries no credential.
 */
export interface WorkSession {
    /**
     * The brand the work is for, as typed. A name, not a reference: the session is written
     * before anybody decides whether that brand is a record anywhere.
     */
    brandName?: string;
    /**
     * When the session was opened.
     */
    createdAt: Date;
    /**
     * Where work made here is headed unless told otherwise. Free text: the channels belong to
     * the system that publishes.
     */
    defaultChannel?: string;
    /**
     * What work made here is for unless told otherwise. Free text, in the vocabulary of whoever
     * set it.
     */
    defaultObjective?: string;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * When it was last touched. The reason the record is worth keeping: it says which sessions
     * are still alive.
     */
    lastSeen: Date;
    /**
     * What the person called it. Absent until they bother to name it.
     */
    name?: string;
    /**
     * The wallet, handle, or id under localIds of whoever is working. Absent while the work is
     * anonymous — a session can exist before anybody has signed in for it.
     */
    person?: string;
    /**
     * The id of the workspace the session sits in, in the system that owns workspaces.
     */
    workspace?: string;
}