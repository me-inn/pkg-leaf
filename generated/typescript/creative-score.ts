// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * A reading of one generated piece: how it sat against the voice it was written for, how it
 * fitted the channel it was written into, and why. About a piece of work, never about the
 * person who asked for it — nothing here is said about an actor.
 */
export interface CreativeScore {
    /**
     * When the piece was scored, which is not when it was written.
     */
    createdAt?: Date;
    /**
     * The id of the generated piece this reads, in the system that owns it. A piece of work,
     * not an actor: it has no wallet.
     */
    generation: string;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * The model that read the piece, as it was named at the time. Recorded so two scores can be
     * told apart when the scorer changed underneath them.
     */
    modelUsed?: string;
    /**
     * What the scorer made of the piece: the two scores, the one carried alongside them, and
     * why.
     */
    reading: CreativeReading;
}

/**
 * What the scorer made of the piece: the two scores, the one carried alongside them, and
 * why.
 *
 * What a model made of a piece of work: how it sat against the voice it was written for,
 * how it fitted the channel it was written into, and why. About the work, never about
 * whoever asked for it — nothing here is said about an actor, so none of it is testimony.
 */
export interface CreativeReading {
    /**
     * How close the work came to the voice it was written for, from 0 to 1. The range is what
     * the scorer produces, and keeping a number inside it is the job of the code that writes
     * the record.
     */
    brandVoiceScore: number;
    /**
     * How well the work fitted the channel it was written into, from 0 to 1, on the same scale.
     */
    channelFitScore: number;
    /**
     * The single number carried alongside the two others, from 0 to 1. Stated rather than
     * derived here: how the scorer weighed voice against fit is its own, and recomputing it
     * elsewhere would invent a weighting nobody agreed to.
     */
    overallScore: number;
    /**
     * Why those numbers, in the scorer's own words. Kept because a number with no account of
     * itself cannot be argued with.
     */
    reasoning: string;
}