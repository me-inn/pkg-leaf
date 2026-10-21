// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * A named gathering of assets, made by a person because they belong together for a reason
 * no pipeline would find. It holds no assets: it holds the edges that say which ones are in
 * it, and when each was put there.
 */
export interface Collection {
    /**
     * The assets in it, each as its own edge: being in a collection is not an attribute of an
     * asset, and the moment it was added belongs to the putting-in, not to either side.
     */
    assets?:    Asset[];
    createdAt?: Date;
    /**
     * Why these belong together. Written by a person; never derived from what is inside.
     */
    description?: string;
    /**
     * The record's own id in the system that holds it.
     */
    id?: string;
    /**
     * What it is called, in the words of whoever gathered it.
     */
    name: string;
    /**
     * The id of the working session it was made in, in the system that owns the session. Absent
     * when it was not made through one.
     */
    session?:   string;
    updatedAt?: Date;
}

export interface Asset {
    /**
     * When it was put in, which is not when the asset was recorded.
     */
    addedAt?: Date;
    /**
     * The id of the asset, in the system that owns it.
     */
    asset: string;
    /**
     * The edge's own id in the system that holds it.
     */
    id?: string;
}