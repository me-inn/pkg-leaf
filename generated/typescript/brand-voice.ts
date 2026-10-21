// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * A snapshot of what a session has been approving: how much, how well it scored, and which
 * channels and objectives it kept coming back to. Counted once and written down, so the
 * figures a person saw on a day can be shown again on another day without recounting them.
 */
export interface BrandVoice {
    /**
     * How many pieces had been approved when the snapshot was taken.
     */
    approvedCount: number;
    /**
     * The mean of the latest score of each scored generation. Absent when nothing had been
     * scored yet, which is not the same as zero.
     */
    avgOverallScore?: number;
    /**
     * When the snapshot was taken. It is what makes the figures readable later: they are true
     * of that moment and of no other.
     */
    createdAt?: Date;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * The session this was counted over, as the system that owns the session names it.
     * Optional: scoping a profile to a working session is how Creative Flow holds it, not part
     * of what it is, and a system without sessions must be able to carry the same shape.
     */
    session?: string;
    /**
     * The channels that came up most, most frequent first. A list, whatever a given store
     * serialises it into.
     */
    topChannels?: string[];
    /**
     * The objectives that came up most, most frequent first.
     */
    topObjectives?: string[];
}