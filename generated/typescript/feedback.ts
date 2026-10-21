// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * A rating somebody gave a thing the software produced, with a line about it if they wrote
 * one. About an output and not about a person: it carries no subject, no consent and no
 * signature, which is what separates it from a testimony.
 */
export interface Feedback {
    /**
     * What they wrote alongside the rating, in their own words.
     */
    comment?: string;
    /**
     * When it was given.
     */
    createdAt?: Date;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * The rating as given, 1 to 5. Collected both ways: as a thumb, where only 1 and 5 are ever
     * written, and as the whole scale. Which of the two it was is not recorded, so a mean over
     * mixed records is a number about nothing.
     */
    rating: number;
    /**
     * The id of the working session it came from, in the system that holds it. Not a person.
     */
    session?: string;
    /**
     * The id of that thing, in the system that owns it. It is read together with targetType and
     * alone means nothing — two kinds of target do not share an id space.
     */
    target: string;
    /**
     * What kind of thing was rated. Free text with the two the system records so far: a target
     * type is added whenever something new becomes ratable, and a closed list here would have
     * to be versioned for each one.
     */
    targetType: string;
}