// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * What somebody is owed by the system that bills them: a plan, a credit balance, and the
 * day the cycle turns over. Not an actor and not an organisation — the actor is the person
 * who owns it, named here by key. One person can be billed by more than one system, and
 * each one keeps its own account.
 */
export interface Account {
    createdAt?: Date;
    /**
     * Credits left to spend. Whole credits, never fractions, because a half-spent credit is not
     * a thing anybody can sell.
     */
    creditsBalance: number;
    /**
     * When the next cycle starts and the balance is refilled. Stated rather than computed from
     * the plan, so a cycle moved by hand stays moved.
     */
    cycleRenewsAt: Date;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * The wallet, handle, or id under localIds of the person billed. One account per person per
     * system.
     */
    owner: string;
    /**
     * Which plan is in force, in the words of the system that sells it. Free text: the
     * catalogue of plans belongs to the seller and changes without the shape changing.
     */
    plan:       string;
    updatedAt?: Date;
}