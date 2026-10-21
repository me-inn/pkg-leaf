// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * One rendering of a book into a file somebody can hand over — a pdf, an epub, a docx. A
 * pointer and a state, never the file: the bytes live in the store that rendered them, and
 * this says which store, under which key, and whether it finished.
 */
export interface BookExport {
    /**
     * The id of the book that was rendered, in the system that holds the book.
     */
    book: string;
    /**
     * When the rendering finished, whether it succeeded or failed.
     */
    completedAt?: Date;
    /**
     * When the export was asked for, which is not when the file was ready.
     */
    createdAt?: Date;
    /**
     * Why the rendering failed, in the words of whoever rendered it. Present only when it did.
     */
    errorMessage?: string;
    /**
     * The rendered file, where it is kept and how big it is. Absent until the rendering says
     * done.
     */
    file?: StoredFile;
    /**
     * What was rendered. A pdf for reading on a screen and a pdf for a printer are two formats,
     * not one: the page, the bleed and the margins differ.
     */
    format: Format;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * How the rendering went. The file is only there to fetch once this says done.
     */
    status?: Status;
}

/**
 * The rendered file, where it is kept and how big it is. Absent until the rendering says
 * done.
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
 * What was rendered. A pdf for reading on a screen and a pdf for a printer are two formats,
 * not one: the page, the bleed and the margins differ.
 */
export type Format = "pdf_ebook" | "pdf_print" | "epub" | "docx";

/**
 * How the rendering went. The file is only there to fetch once this says done.
 */
export type Status = "queued" | "processing" | "done" | "failed";