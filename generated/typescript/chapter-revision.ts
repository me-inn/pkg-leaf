// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * A chapter's text as it stood at one moment, kept whole rather than as a difference, so an
 * old version reads without replaying the ones after it.
 */
export interface ChapterRevision {
    /**
     * The wallet, handle, or id under localIds of whoever made the change. Absent when it was
     * made by software rather than a person.
     */
    changedBy?: string;
    /**
     * One line on what changed, so a list of revisions can be read without opening each.
     */
    changeSummary?: string;
    /**
     * What kind of change it was. Free text: the vocabulary belongs to the system that writes
     * the revision.
     */
    changeType?: string;
    /**
     * The id of the chapter this is a revision of, in the system that holds the chapter.
     */
    chapter: string;
    /**
     * The whole text as it stood, not a difference against the one before.
     */
    content: string;
    /**
     * When the revision was written down.
     */
    createdAt?: Date;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * Which revision of that chapter this is, counting up. Ordering comes from this and not
     * from the clock, because two writes can land in the same second.
     */
    version: number;
    /**
     * Words in this revision's text.
     */
    wordCount?: number;
}