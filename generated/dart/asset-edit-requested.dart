// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final assetEditRequested = assetEditRequestedFromJson(jsonString);

import 'dart:convert';

AssetEditRequested assetEditRequestedFromJson(String str) => AssetEditRequested.fromJson(json.decode(str));

String assetEditRequestedToJson(AssetEditRequested data) => json.encode(data.toJson());


///A cut, a resize or a filter somebody wants applied. The original is never changed: the
///result is a new asset. Keys are snake_case, not the camelCase the rest of leaf uses: this
///travels inside a Liquid envelope, whose own fields (event_id, occurred_at, event_type,
///owner_unit_ref) are snake_case and pinned byte-exact by signed golden vectors. The shape
///follows the wire.
class AssetEditRequested {
    
    ///The asset to edit, which stays as it is.
    String assetId;
    
    ///What to do to it. Every step is optional and they apply together; an empty one copies the
    ///asset.
    EditParams? editParams;
    
    ///The job to report the edit against.
    String jobId;

    AssetEditRequested({
        required this.assetId,
        this.editParams,
        required this.jobId,
    });

    factory AssetEditRequested.fromJson(Map<String, dynamic> json) => AssetEditRequested(
        assetId: json["asset_id"],
        editParams: json["edit_params"] == null ? null : EditParams.fromJson(json["edit_params"]),
        jobId: json["job_id"],
    );

    Map<String, dynamic> toJson() => {
        "asset_id": assetId,
        "edit_params": editParams?.toJson(),
        "job_id": jobId,
    };
}


///What to do to it. Every step is optional and they apply together; an empty one copies the
///asset.
class EditParams {
    
    ///The rectangle to keep, in pixels from the top left of the original.
    CropParams? crop;
    
    ///How to treat the image. The four multipliers leave it alone at 1.
    FilterParams? filters;
    
    ///The size to come out at, said either by naming a channel's preset or by giving both sides.
    ResizeParams? resize;
    
    ///The stretch to keep, in seconds from the start. Video only.
    TrimParams? trim;

    EditParams({
        this.crop,
        this.filters,
        this.resize,
        this.trim,
    });

    factory EditParams.fromJson(Map<String, dynamic> json) => EditParams(
        crop: json["crop"] == null ? null : CropParams.fromJson(json["crop"]),
        filters: json["filters"] == null ? null : FilterParams.fromJson(json["filters"]),
        resize: json["resize"] == null ? null : ResizeParams.fromJson(json["resize"]),
        trim: json["trim"] == null ? null : TrimParams.fromJson(json["trim"]),
    );

    Map<String, dynamic> toJson() => {
        "crop": crop?.toJson(),
        "filters": filters?.toJson(),
        "resize": resize?.toJson(),
        "trim": trim?.toJson(),
    };
}


///The rectangle to keep, in pixels from the top left of the original.
class CropParams {
    
    ///How tall the kept rectangle is, in pixels.
    int height;
    
    ///How wide the kept rectangle is, in pixels.
    int width;
    
    ///Pixels from the left edge of the original to the left edge of the rectangle.
    int x;
    
    ///Pixels from the top edge of the original to the top edge of the rectangle.
    int y;

    CropParams({
        required this.height,
        required this.width,
        required this.x,
        required this.y,
    });

    factory CropParams.fromJson(Map<String, dynamic> json) => CropParams(
        height: json["height"],
        width: json["width"],
        x: json["x"],
        y: json["y"],
    );

    Map<String, dynamic> toJson() => {
        "height": height,
        "width": width,
        "x": x,
        "y": y,
    };
}


///How to treat the image. The four multipliers leave it alone at 1.
class FilterParams {
    
    ///Gaussian sigma. 0 is no blur.
    double? blur;
    
    ///Multiplier on how light it is. Below 1 darkens, above 1 lightens.
    double? brightness;
    
    ///Multiplier on the distance between light and dark. Below 1 flattens, above 1 deepens.
    double? contrast;
    
    ///0 is grey.
    double? saturation;
    
    ///Multiplier on edge definition. Below 1 softens, above 1 sharpens.
    double? sharpness;
    
    ///Whether to darken the corners. On or off: how much is the editor's to decide.
    bool? vignette;

    FilterParams({
        this.blur,
        this.brightness,
        this.contrast,
        this.saturation,
        this.sharpness,
        this.vignette,
    });

    factory FilterParams.fromJson(Map<String, dynamic> json) => FilterParams(
        blur: json["blur"]?.toDouble(),
        brightness: json["brightness"]?.toDouble(),
        contrast: json["contrast"]?.toDouble(),
        saturation: json["saturation"]?.toDouble(),
        sharpness: json["sharpness"]?.toDouble(),
        vignette: json["vignette"],
    );

    Map<String, dynamic> toJson() => {
        "blur": blur,
        "brightness": brightness,
        "contrast": contrast,
        "saturation": saturation,
        "sharpness": sharpness,
        "vignette": vignette,
    };
}


///The size to come out at, said either by naming a channel's preset or by giving both sides.
class ResizeParams {
    
    ///How tall to come out, in pixels. Given together with width, instead of a preset.
    int? height;
    
    ///A named size belonging to a channel. What each one resolves to is the editor's to know,
    ///not this shape's.
    Preset? preset;
    
    ///How wide to come out, in pixels. Given together with height, instead of a preset.
    int? width;

    ResizeParams({
        this.height,
        this.preset,
        this.width,
    });

    factory ResizeParams.fromJson(Map<String, dynamic> json) => ResizeParams(
        height: json["height"],
        preset: presetValues.map[json["preset"]],
        width: json["width"],
    );

    Map<String, dynamic> toJson() => {
        "height": height,
        "preset": presetValues.reverse[preset],
        "width": width,
    };
}


///A named size belonging to a channel. What each one resolves to is the editor's to know,
///not this shape's.
enum Preset {
    IG_FEED,
    IG_LANDSCAPE,
    IG_REELS,
    IG_STORY,
    TIKTOK
}

final presetValues = EnumValues({
    "ig_feed": Preset.IG_FEED,
    "ig_landscape": Preset.IG_LANDSCAPE,
    "ig_reels": Preset.IG_REELS,
    "ig_story": Preset.IG_STORY,
    "tiktok": Preset.TIKTOK
});


///The stretch to keep, in seconds from the start. Video only.
class TrimParams {
    
    ///Where the kept stretch ends, in seconds from the start of the original.
    double endSeconds;
    
    ///Where the kept stretch begins, in seconds from the start of the original.
    double startSeconds;

    TrimParams({
        required this.endSeconds,
        required this.startSeconds,
    });

    factory TrimParams.fromJson(Map<String, dynamic> json) => TrimParams(
        endSeconds: json["end_seconds"]?.toDouble(),
        startSeconds: json["start_seconds"]?.toDouble(),
    );

    Map<String, dynamic> toJson() => {
        "end_seconds": endSeconds,
        "start_seconds": startSeconds,
    };
}

class EnumValues<T> {
    Map<String, T> map;
    late Map<T, String> reverseMap;

    EnumValues(this.map);

    Map<T, String> get reverse {
            reverseMap = map.map((k, v) => MapEntry(v, k));
            return reverseMap;
    }
}