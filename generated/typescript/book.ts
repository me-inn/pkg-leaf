// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * A long-form title somebody is writing: what it is about, how far along it is, and where
 * its cover sits. The chapters are not inside it — each is its own record pointing back, so
 * a book can be read without carrying its whole text.
 */
export interface Book {
    /**
     * The model that helped write it, named as the system that called it names it. Absent when
     * nothing was asked of one.
     */
    aiModel?: string;
    /**
     * The wallet, handle, or id under localIds of whoever is writing it. Absent while the title
     * belongs to nobody yet.
     */
    author?: string;
    /**
     * The cover image, where it is kept. Absent while the title has none.
     */
    cover?: StoredFile;
    /**
     * The brief the cover image was asked for with. Kept because the image can be asked for
     * again.
     */
    coverPrompt?: string;
    createdAt?:   Date;
    /**
     * Words written so far across the chapters. Counted by whoever holds the text, carried here
     * so a reader of the book alone can say how far along it is.
     */
    currentWordCount?: number;
    /**
     * What the book is about, in the words of whoever is writing it. Written for a reader
     * deciding, not for a catalogue.
     */
    description?: string;
    /**
     * The shelf it belongs on. A closed list because it decides how the title is filed, not how
     * it reads.
     */
    genre: Genre;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * The BISAC subject code given to the store, such as FIC000000. Separate from genre: one is
     * ours, this one is the trade's.
     */
    kdpBisac?: string;
    /**
     * The keywords the title is listed under on the store. Free text, in the words of whoever
     * sells it.
     */
    kdpKeywords?: string[];
    /**
     * The language the book is written in, as a BCP 47 tag such as pt, en or pt-BR.
     */
    language?: string;
    /**
     * The id of the working session the book was started from, in the system that holds that
     * session. Absent when it was not started from one.
     */
    session?: string;
    /**
     * How far along it is. Which move from which is a rule held beside the type, never in it.
     */
    status?: Status;
    /**
     * The line under the title, when there is one.
     */
    subtitle?: string;
    /**
     * The length being aimed at, set by whoever is writing. Zero while no target was chosen.
     */
    targetWordCount?: number;
    /**
     * The title on the cover.
     */
    title:      string;
    updatedAt?: Date;
}

/**
 * The cover image, where it is kept. Absent while the title has none.
 *
 * Bytes somebody is keeping, pointed at rather than carried. Never the file itself: the
 * store that holds it holds it, and this says which key to ask under and, while it lasts,
 * where it can be fetched. Nothing is required, because a file can be known by its key
 * before any address has been issued for it, and served by an address before anybody
 * recorded a key.
 */
export interface StoredFile {
    /**
     * How big it is, so whoever is about to fetch it knows what they are asking for.
     */
    sizeBytes?: number;
    /**
     * Where the bytes sit in the store that holds them. The lasting handle, meaningful only to
     * that store: a reader asks the store, never resolves the key itself.
     */
    storageKey?: string;
    /**
     * Where the file can be fetched right now. Often signed and short-lived, so it is read at
     * the moment of use and never kept as the address of the file.
     */
    url?: string;
}

/**
 * The shelf it belongs on. A closed list because it decides how the title is filed, not how
 * it reads.
 */
export type Genre = "fiction" | "non_fiction" | "self_help" | "business" | "biography" | "children" | "young_adult" | "romance" | "thriller" | "science_fiction" | "fantasy" | "horror" | "historical" | "poetry" | "academic" | "other";

/**
 * How far along it is. Which move from which is a rule held beside the type, never in it.
 */
export type Status = "draft" | "writing" | "review" | "approved" | "published";