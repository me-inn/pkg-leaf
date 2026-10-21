// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final assetEditReady = assetEditReadyFromJson(jsonString);

import 'dart:convert';

AssetEditReady assetEditReadyFromJson(String str) => AssetEditReady.fromJson(json.decode(str));

String assetEditReadyToJson(AssetEditReady data) => json.encode(data.toJson());


///An edit was applied and saved as a new asset. Both ids travel, because the point of the
///event is the pair: the original still stands and this one came from it. Keys are
///snake_case, not the camelCase the rest of leaf uses: this travels inside a Liquid
///envelope, whose own fields (event_id, occurred_at, event_type, owner_unit_ref) are
///snake_case and pinned byte-exact by signed golden vectors. The shape follows the wire.
class AssetEditReady {
    
    ///The new asset the edit became. Named contentId and not assetId so every result event
    ///points at its subject under one name.
    String contentId;
    
    ///The asset that was edited, unchanged.
    String originalAssetId;
    
    ///The working session the edit was made in.
    String sessionId;
    
    ///Where the edited bytes sit in the store that holds them. Meaningful only to that store.
    String storageKey;

    AssetEditReady({
        required this.contentId,
        required this.originalAssetId,
        required this.sessionId,
        required this.storageKey,
    });

    factory AssetEditReady.fromJson(Map<String, dynamic> json) => AssetEditReady(
        contentId: json["content_id"],
        originalAssetId: json["original_asset_id"],
        sessionId: json["session_id"],
        storageKey: json["storage_key"],
    );

    Map<String, dynamic> toJson() => {
        "content_id": contentId,
        "original_asset_id": originalAssetId,
        "session_id": sessionId,
        "storage_key": storageKey,
    };
}