// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * One piece of material that was put in front of the model for a generation, and where it
 * came from. Written down because the source can change afterwards: this says what was
 * actually read, in the order it was read.
 */
export interface GenerationContextItem {
    /**
     * The material as it was handed to the model. A copy on purpose — the source may be edited
     * or deleted later, and this is what was read.
     */
    content: string;
    /**
     * The generation this was given to, by its id in the system that holds it.
     */
    generation: string;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * Its place in the order the items were assembled in, counting from the first. Position,
     * not score.
     */
    rank: number;
    /**
     * How close the retrieval judged it to the ask. Absent when the item was not chosen by
     * similarity. The scale belongs to whichever retrieval produced it.
     */
    similarityScore?: number;
    /**
     * The id of that thing, in the system that owns it. Paired with sourceType, which says what
     * kind of id it is.
     */
    sourceId: string;
    /**
     * What kind of thing the material came from. Free text: the kinds belong to whatever the
     * retrieving system can reach.
     */
    sourceType: string;
}