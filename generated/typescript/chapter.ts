// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * One chapter of a book: its place in the running order and the text as it stands now.
 * Earlier states of that text are revisions, each its own record.
 */
export interface Chapter {
    /**
     * The id of the book this chapter belongs to, in the system that holds the book.
     */
    book: string;
    /**
     * The text as it stands now. Empty while the chapter is only a heading.
     */
    content?:   string;
    createdAt?: Date;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * Where it falls in the running order. The number the chapters are sorted by, not the
     * number printed on the page.
     */
    order?: number;
    /**
     * How far along this chapter is, which moves on its own and not with the book's.
     */
    status?: Status;
    /**
     * What happens in it, in a few lines. Written so the chapter can be reasoned about without
     * reading it whole.
     */
    summary?: string;
    /**
     * The chapter heading.
     */
    title:      string;
    updatedAt?: Date;
    /**
     * Words in the current text, counted by whoever holds it.
     */
    wordCount?: number;
}

/**
 * How far along this chapter is, which moves on its own and not with the book's.
 */
export type Status = "draft" | "writing" | "review" | "approved";