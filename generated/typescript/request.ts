// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * Somebody asking somebody else for a time. A request, not a booking: it records what was
 * asked, never that a slot is taken.
 */
export interface Request {
    answeredAt?: Date;
    /**
     * How to reach whoever asked, so an answer can get back to them.
     */
    contacts?:  ContactPoint[];
    createdAt?: Date;
    /**
     * The wallet or local id of whoever is asking, when they have one. Absent for somebody with
     * no account anywhere.
     */
    from?: string;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * Who is asking, as they gave it. Unverified, and read by a person.
     */
    requester?: string;
    /**
     * An answer is final. A second answer does not change the first.
     */
    state?: State;
    /**
     * The wallet, handle, or id under localIds of whoever is being asked.
     */
    to: string;
    /**
     * When they want, in their own words. Not a timestamp: a parsed date is a claim about a
     * timezone and a working hour, and a person reading the words cannot misread them.
     */
    wanted: string;
}

/**
 * One way to reach an actor.
 */
export interface ContactPoint {
    /**
     * The language to write to this point in.
     */
    locale?: Locale;
    /**
     * Which channel the value is for.
     */
    type: Type;
    /**
     * An address, or a number in E.164 digits including the country code.
     */
    value:       string;
    verified?:   boolean;
    verifiedAt?: Date;
}

/**
 * The language to write to this point in.
 */
export type Locale = "pt" | "en" | "es";

/**
 * Which channel the value is for.
 */
export type Type = "email" | "whatsapp" | "mobile" | "phone";

/**
 * An answer is final. A second answer does not change the first.
 */
export type State = "pending" | "confirmed" | "declined";