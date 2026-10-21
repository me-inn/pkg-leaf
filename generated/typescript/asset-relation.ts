// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * One asset pointing at another, and what the pointing means. An edge rather than a column:
 * an asset has no single related asset, and each kind of tie — one derived from another,
 * one resembling another — would otherwise add a field to a thing it was never an attribute
 * of.
 */
export interface AssetRelation {
    createdAt?: Date;
    /**
     * The id of the asset the tie starts at, in the system that owns it. The direction carries
     * the meaning: derived_from read the other way is false.
     */
    fromAsset: string;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * What the tie means, in the words of whoever drew it. Free text: the vocabulary belongs to
     * the system that relates them.
     */
    relationType: string;
    /**
     * The id of the asset the tie points at, in the system that owns it.
     */
    toAsset: string;
}