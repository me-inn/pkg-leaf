// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * Somebody letting a piece of software act for them. What was granted, to whom, and until
 * when — never the credential that proves it. The code and the token are secrets, they are
 * held only as a hash by the system that issued them, and neither has a shape here.
 */
export interface Authorization {
    /**
     * The https URL that identifies the software. It is also where that software describes
     * itself, so nothing about it has to be copied here.
     */
    client: string;
    /**
     * When it stops working on its own, with nobody having to do anything.
     */
    expiresAt?: Date;
    grantedAt?: Date;
    /**
     * What the software calls itself, as it said. Recorded so a person recognises it when
     * deciding what to take back; never used to decide anything.
     */
    label?: string;
    /**
     * When it was taken back. A grant that ended is kept rather than deleted: what was allowed,
     * and until when, is a fact about the past.
     */
    revokedAt?: Date;
    /**
     * The wallet, or the id under localIds, of whoever is being acted for. The grant is theirs
     * and so is taking it back.
     */
    subject: string;
}