// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * One number a platform reported about one generated piece, at one moment. A reading and
 * not a total: a second reading of the same metric is another record, so what a piece did
 * over time is the series and never a field that gets overwritten.
 */
export interface PerformanceSignal {
    /**
     * The id of the generated piece the number is about, in the system that owns it.
     */
    generation: string;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * What was counted, in the platform's own word for it. Free text for the same reason, and
     * never translated on the way in: a platform's reach is not another platform's reach.
     */
    metricName: string;
    /**
     * The number, as reported. No unit travels with it — the unit is whatever the platform
     * means by that metric name.
     */
    metricValue: number;
    /**
     * Where the piece ran and who counted. Free text: the names belong to the platforms, and a
     * list here would be out of date the week somebody publishes somewhere new.
     */
    platform: string;
    /**
     * When the reading was taken, which is not when the piece was published and not when the
     * platform computed it.
     */
    recordedAt?: Date;
}