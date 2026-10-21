// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * One attempt to call a webhook: what was sent, what came back, and how many tries it took.
 * A record of its own rather than a column on the subscription, because one subscription
 * has many deliveries and each outlives the state of the next. No signature travels here,
 * for the same reason none travels on the subscription.
 */
export interface WebhookDelivery {
    /**
     * How many times this delivery has been tried.
     */
    attempts?: number;
    /**
     * When the attempt was recorded, which is not when the event happened.
     */
    createdAt?: Date;
    /**
     * Which event triggered the call. Free text, matching one of the names on the subscription.
     */
    event: string;
    /**
     * The status code the endpoint answered with. Absent when the call never got an answer — a
     * timeout and a 500 are different failures.
     */
    httpStatus?: number;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * The body that was posted. Open on purpose: its keys belong to whoever emits the event,
     * and the delivery only records what went out.
     */
    payload?: { [key: string]: any };
    /**
     * What the endpoint wrote back, kept as given. Read when a delivery has to be explained,
     * never parsed.
     */
    responseBody?: string;
    /**
     * Where the attempt stands. Free text rather than an enum: the source has no declared set,
     * only a default of pending.
     */
    status?: string;
    /**
     * The subscription this attempt was made for, as the system that holds it names it.
     */
    webhook: string;
}