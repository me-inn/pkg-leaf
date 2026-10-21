// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

/**
 * A cut, a resize or a filter somebody wants applied. The original is never changed: the
 * result is a new asset. Keys are snake_case, not the camelCase the rest of leaf uses: this
 * travels inside a Liquid envelope, whose own fields (event_id, occurred_at, event_type,
 * owner_unit_ref) are snake_case and pinned byte-exact by signed golden vectors. The shape
 * follows the wire.
 */
export interface AssetEditRequested {
    /**
     * The asset to edit, which stays as it is.
     */
    asset_id: string;
    /**
     * What to do to it. Every step is optional and they apply together; an empty one copies the
     * asset.
     */
    edit_params?: EditParams;
    /**
     * The job to report the edit against.
     */
    job_id: string;
}

/**
 * What to do to it. Every step is optional and they apply together; an empty one copies the
 * asset.
 */
export interface EditParams {
    /**
     * The rectangle to keep, in pixels from the top left of the original.
     */
    crop?: CropParams;
    /**
     * How to treat the image. The four multipliers leave it alone at 1.
     */
    filters?: FilterParams;
    /**
     * The size to come out at, said either by naming a channel's preset or by giving both sides.
     */
    resize?: ResizeParams;
    /**
     * The stretch to keep, in seconds from the start. Video only.
     */
    trim?: TrimParams;
}

/**
 * The rectangle to keep, in pixels from the top left of the original.
 */
export interface CropParams {
    /**
     * How tall the kept rectangle is, in pixels.
     */
    height: number;
    /**
     * How wide the kept rectangle is, in pixels.
     */
    width: number;
    /**
     * Pixels from the left edge of the original to the left edge of the rectangle.
     */
    x: number;
    /**
     * Pixels from the top edge of the original to the top edge of the rectangle.
     */
    y: number;
}

/**
 * How to treat the image. The four multipliers leave it alone at 1.
 */
export interface FilterParams {
    /**
     * Gaussian sigma. 0 is no blur.
     */
    blur?: number;
    /**
     * Multiplier on how light it is. Below 1 darkens, above 1 lightens.
     */
    brightness?: number;
    /**
     * Multiplier on the distance between light and dark. Below 1 flattens, above 1 deepens.
     */
    contrast?: number;
    /**
     * 0 is grey.
     */
    saturation?: number;
    /**
     * Multiplier on edge definition. Below 1 softens, above 1 sharpens.
     */
    sharpness?: number;
    /**
     * Whether to darken the corners. On or off: how much is the editor's to decide.
     */
    vignette?: boolean;
}

/**
 * The size to come out at, said either by naming a channel's preset or by giving both sides.
 */
export interface ResizeParams {
    /**
     * How tall to come out, in pixels. Given together with width, instead of a preset.
     */
    height?: number;
    /**
     * A named size belonging to a channel. What each one resolves to is the editor's to know,
     * not this shape's.
     */
    preset?: Preset;
    /**
     * How wide to come out, in pixels. Given together with height, instead of a preset.
     */
    width?: number;
}

/**
 * A named size belonging to a channel. What each one resolves to is the editor's to know,
 * not this shape's.
 */
export type Preset = "ig_feed" | "ig_reels" | "ig_story" | "ig_landscape" | "tiktok";

/**
 * The stretch to keep, in seconds from the start. Video only.
 */
export interface TrimParams {
    /**
     * Where the kept stretch ends, in seconds from the start of the original.
     */
    end_seconds: number;
    /**
     * Where the kept stretch begins, in seconds from the start of the original.
     */
    start_seconds: number;
}