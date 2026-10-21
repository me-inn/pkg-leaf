// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * A note somebody left on a book, and where in the text they left it. The note is the
 * record; the passage it points at stays in the chapter, quoted here only so the note still
 * reads once the text around it has moved.
 */
export interface Annotation {
    /**
     * Where the passage ends, counted the same way.
     */
    anchorEnd?: number;
    /**
     * Where the passage starts in the chapter text, counted in characters from the beginning.
     * Valid against the revision that was open at the time.
     */
    anchorStart?: number;
    /**
     * What kind of remark it is, which decides who it is addressed to: a todo waits on the
     * author, a beta_feedback came from a reader, an ai_suggestion was not written by a person
     * at all.
     */
    annotationType: AnnotationType;
    /**
     * The id of the book it was left on, in the system that owns it.
     */
    book: string;
    /**
     * The id of the chapter it was left on, in the system that owns it. Absent for a note about
     * the book as a whole.
     */
    chapter?:   string;
    createdAt?: Date;
    /**
     * The wallet, handle, or id under localIds of whoever left it. Absent for a note no person
     * wrote.
     */
    createdBy?: string;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * What they wrote.
     */
    note: string;
    /**
     * Whether the note has been dealt with. It stays on the record once resolved; nothing here
     * is removed by being answered.
     */
    resolved: boolean;
    /**
     * The passage as it read when the note was made. Kept verbatim because the anchors drift
     * once the chapter is edited, and the quote is what survives that.
     */
    textSelection?: string;
}

/**
 * What kind of remark it is, which decides who it is addressed to: a todo waits on the
 * author, a beta_feedback came from a reader, an ai_suggestion was not written by a person
 * at all.
 */
export type AnnotationType = "note" | "question" | "todo" | "ai_suggestion" | "beta_feedback";