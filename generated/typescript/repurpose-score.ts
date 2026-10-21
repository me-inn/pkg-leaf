// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * The same reading as a creative score, but of work a job turned into one other format. It
 * is its own record and not a column on the job: one job produces several formats, and each
 * is read on its own.
 */
export interface RepurposeScore {
    /**
     * When the output was scored, which is not when the job ran.
     */
    createdAt?: Date;
    /**
     * Which of the job's outputs this score is for. One score per format, so the job's own id
     * does not identify a record.
     */
    format: Format;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * The id of the repurpose job that produced the work, in the system that ran it.
     */
    job: string;
    /**
     * What the scorer made of that one output. The same shape a creative score carries, read
     * against the channel the format is meant for.
     */
    reading: CreativeReading;
}

/**
 * Which of the job's outputs this score is for. One score per format, so the job's own id
 * does not identify a record.
 */
export type Format = "hooks" | "captions" | "short_scripts" | "carousel_copy" | "hashtags" | "cta_variants";

/**
 * What the scorer made of that one output. The same shape a creative score carries, read
 * against the channel the format is meant for.
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