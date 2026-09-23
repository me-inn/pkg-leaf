// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * A person belonging to an organisation.
 */
export interface Membership {
    /**
     * What they may do inside it. Free text: the verbs belong to the system that grants them.
     */
    capabilities?: string[];
    createdAt?:    Date;
    /**
     * The wallet or local id of whoever invited them.
     */
    invitedBy?: string;
    /**
     * The organisation's wallet, or its id under localIds.
     */
    organization: string;
    /**
     * The person's wallet, or their id under localIds.
     */
    person:     string;
    status?:    Status;
    updatedAt?: Date;
}

export type Status = "invited" | "active" | "suspended" | "left";