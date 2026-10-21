// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * A second take on a generation, asked for as its own piece of work. It says which
 * generation it came from and which job was run for it — the text it produced belongs to
 * that job's own record, not to this edge.
 */
export interface GenerationVariant {
    /**
     * When the variant was asked for, which is not when the job finished.
     */
    createdAt?: Date;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * The processing job run to produce it, by its id in the system that runs it. The variant
     * is the link between the two; neither side carries the other.
     */
    job: string;
    /**
     * The generation this is a variant of, by its id in the system that holds it.
     */
    parentGeneration: string;
}