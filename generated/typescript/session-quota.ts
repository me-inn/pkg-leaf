// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * How much a work session may spend in a day. Its own record rather than fields on the
 * session, because the limits are set by whoever runs the system and the session is written
 * by whoever uses it.
 */
export interface SessionQuota {
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * Generations allowed in a day.
     */
    maxGenerationsPerDay: number;
    /**
     * Repurposes allowed in a day.
     */
    maxRepurposePerDay: number;
    /**
     * The wallet, handle, or id under localIds of whoever owns the quota. Carried so the holder
     * of a session id is not by itself the person allowed to change the limits; absent for a
     * session nobody has signed in for.
     */
    person?: string;
    /**
     * The work session the limits apply to, as the system that owns the session names it. One
     * quota per session.
     */
    session: string;
}