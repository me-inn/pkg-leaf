// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * A note hanging off a point in a chapter's text — a footnote, an endnote, a citation, an
 * entry in the bibliography. Its own record, because where it prints depends on the format
 * the book is exported to and not on the sentence it came from.
 */
export interface Footnote {
    /**
     * The offset into the chapter's text where the marker sits. Counted in characters from the
     * start, so editing the text ahead of it moves the note.
     */
    anchorPosition?: number;
    /**
     * The id of the chapter the note belongs to, in the system that holds the chapter.
     */
    chapter: string;
    /**
     * What the note says.
     */
    content:    string;
    createdAt?: Date;
    /**
     * What kind of note it is, which decides where it prints: at the foot of the page, at the
     * back, inline, or in the list at the end.
     */
    footnoteType?: FootnoteType;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * Where it falls among that chapter's notes. What the printed marker is numbered from.
     */
    order?: number;
}

/**
 * What kind of note it is, which decides where it prints: at the foot of the page, at the
 * back, inline, or in the list at the end.
 */
export type FootnoteType = "footnote" | "endnote" | "citation" | "bibliography";