// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * What one call to a model cost: who made it, which model answered, how many tokens each
 * way, and the money. Separate from the credit ledger — credits are what the customer is
 * charged, tokens are what the call actually consumed, and the two move for different
 * reasons.
 */
export interface TokenUsage {
    /**
     * What the call was for, in the words of the system that made it. Free text: the kinds of
     * call belong to that system.
     */
    callType: string;
    /**
     * What the call cost in US dollars, worked out when it was written from the prices in force
     * then. Recorded rather than recomputed: prices change, and what was spent does not.
     */
    costUsd: number;
    /**
     * When the call was recorded.
     */
    createdAt?: Date;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * Tokens sent.
     */
    inputTokens: number;
    /**
     * The id of the job that made the call, in the system that owns jobs.
     */
    job?: string;
    /**
     * The model name as the provider gives it, verbatim. Kept exactly because the price was
     * read against this string.
     */
    model: string;
    /**
     * Tokens returned.
     */
    outputTokens: number;
    /**
     * The wallet, handle, or id under localIds of whoever the call was made for. Absent for a
     * call nobody is signed in behind, such as a background pass.
     */
    person?: string;
    /**
     * Who served the call. Free text: providers are added without the shape changing.
     */
    provider: string;
    /**
     * The work session the call belongs to, as the system that owns the session names it.
     * Absent when it belongs to none.
     */
    session?: string;
}