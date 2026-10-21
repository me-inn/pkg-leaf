// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * A book put out on one store, and what that store calls it. An edge between a title and a
 * platform: the same book on three stores is three of these, each with its own listing, its
 * own state and its own rate.
 */
export interface Publication {
    /**
     * The id of the book being put out, in the system that holds the book.
     */
    book:       string;
    createdAt?: Date;
    /**
     * What this listing is expected to pay in a month, in the currency the store settles in. An
     * estimate carried for planning, never an amount owed.
     */
    estimatedMonthlyRoyalty?: number;
    /**
     * What the store calls this listing — its ASIN, its product id. The only handle the store
     * will answer to.
     */
    externalId?: string;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * The page a reader buys it on.
     */
    listingUrl?: string;
    /**
     * Anything about this listing worth writing down, in the words of whoever put it out.
     */
    notes?: string;
    /**
     * Where it is being put out. Manual is for a channel nobody here talks to, recorded so the
     * title's whereabouts stay complete.
     */
    platform: Platform;
    /**
     * When the listing went live on the store.
     */
    publishedAt?: Date;
    /**
     * The author's share, as a fraction: 0.7 is seventy per cent. A fraction and not a
     * percentage so nobody has to guess which was meant.
     */
    royaltyRate?: number;
    /**
     * Where the listing stands on that store. Read from the store, not decided here.
     */
    status?: Status;
    /**
     * When it was sent to the store, which is not when the store accepted it.
     */
    submittedAt?: Date;
    updatedAt?:   Date;
}

/**
 * Where it is being put out. Manual is for a channel nobody here talks to, recorded so the
 * title's whereabouts stay complete.
 */
export type Platform = "amazon_kdp" | "google_play" | "apple_books" | "kobo" | "manual";

/**
 * Where the listing stands on that store. Read from the store, not decided here.
 */
export type Status = "draft" | "submitted" | "live" | "rejected" | "unpublished";