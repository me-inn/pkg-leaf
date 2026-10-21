// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final assetRelation = assetRelationFromJson(jsonString);

import 'dart:convert';

AssetRelation assetRelationFromJson(String str) => AssetRelation.fromJson(json.decode(str));

String assetRelationToJson(AssetRelation data) => json.encode(data.toJson());


///One asset pointing at another, and what the pointing means. An edge rather than a column:
///an asset has no single related asset, and each kind of tie — one derived from another,
///one resembling another — would otherwise add a field to a thing it was never an attribute
///of.
class AssetRelation {
    DateTime? createdAt;
    
    ///The id of the asset the tie starts at, in the system that owns it. The direction carries
    ///the meaning: derived_from read the other way is false.
    String fromAsset;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///What the tie means, in the words of whoever drew it. Free text: the vocabulary belongs to
    ///the system that relates them.
    String relationType;
    
    ///The id of the asset the tie points at, in the system that owns it.
    String toAsset;

    AssetRelation({
        this.createdAt,
        required this.fromAsset,
        this.id,
        required this.relationType,
        required this.toAsset,
    });

    factory AssetRelation.fromJson(Map<String, dynamic> json) => AssetRelation(
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        fromAsset: json["fromAsset"],
        id: json["id"],
        relationType: json["relationType"],
        toAsset: json["toAsset"],
    );

    Map<String, dynamic> toJson() => {
        "createdAt": createdAt?.toIso8601String(),
        "fromAsset": fromAsset,
        "id": id,
        "relationType": relationType,
        "toAsset": toAsset,
    };
}