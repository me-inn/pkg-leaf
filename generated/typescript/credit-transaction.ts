// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * One movement of credit on an account, written once and never changed. The balance on the
 * account is the sum of these; a row kept after the fact is what makes it possible to say
 * why.
 */
export interface CreditTransaction {
    /**
     * The id of the account the credit moved on, in the system that holds it.
     */
    account: string;
    /**
     * Signed: negative spends, positive tops up or refills. One field rather than a direction
     * and a magnitude, so adding them up needs no rules.
     */
    amount: number;
    /**
     * The balance the moment after this movement was applied. Copied here on purpose: reading a
     * balance as of some past row should not mean replaying the whole ledger.
     */
    balanceAfter: number;
    /**
     * When the movement was recorded.
     */
    createdAt?: Date;
    /**
     * A line a person can read on a receipt or in support. Written by whoever charged; empty
     * when nobody wrote one.
     */
    description: string;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * What caused the movement, in the words of the system that charged for it. Free text: the
     * list of billable operations belongs to that system.
     */
    operation: string;
    /**
     * The id of the job or generation that caused it, in the system that owns that thing.
     * Absent for a refill or a top-up, which answer to nothing.
     */
    reference?: string;
}