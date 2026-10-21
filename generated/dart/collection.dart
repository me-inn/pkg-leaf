// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final collection = collectionFromJson(jsonString);

import 'dart:convert';

Collection collectionFromJson(String str) => Collection.fromJson(json.decode(str));

String collectionToJson(Collection data) => json.encode(data.toJson());


///A named gathering of assets, made by a person because they belong together for a reason
///no pipeline would find. It holds no assets: it holds the edges that say which ones are in
///it, and when each was put there.
class Collection {
    
    ///The assets in it, each as its own edge: being in a collection is not an attribute of an
    ///asset, and the moment it was added belongs to the putting-in, not to either side.
    List<Asset>? assets;
    DateTime? createdAt;
    
    ///Why these belong together. Written by a person; never derived from what is inside.
    String? description;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///What it is called, in the words of whoever gathered it.
    String name;
    
    ///The id of the working session it was made in, in the system that owns the session. Absent
    ///when it was not made through one.
    String? session;
    DateTime? updatedAt;

    Collection({
        this.assets,
        this.createdAt,
        this.description,
        this.id,
        required this.name,
        this.session,
        this.updatedAt,
    });

    factory Collection.fromJson(Map<String, dynamic> json) => Collection(
        assets: json["assets"] == null ? [] : List<Asset>.from(json["assets"]!.map((x) => Asset.fromJson(x))),
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        description: json["description"],
        id: json["id"],
        name: json["name"],
        session: json["session"],
        updatedAt: json["updatedAt"] == null ? null : DateTime.parse(json["updatedAt"]),
    );

    Map<String, dynamic> toJson() => {
        "assets": assets == null ? [] : List<dynamic>.from(assets!.map((x) => x.toJson())),
        "createdAt": createdAt?.toIso8601String(),
        "description": description,
        "id": id,
        "name": name,
        "session": session,
        "updatedAt": updatedAt?.toIso8601String(),
    };
}

class Asset {
    
    ///When it was put in, which is not when the asset was recorded.
    DateTime? addedAt;
    
    ///The id of the asset, in the system that owns it.
    String asset;
    
    ///The edge's own id in the system that holds it.
    String? id;

    Asset({
        this.addedAt,
        required this.asset,
        this.id,
    });

    factory Asset.fromJson(Map<String, dynamic> json) => Asset(
        addedAt: json["addedAt"] == null ? null : DateTime.parse(json["addedAt"]),
        asset: json["asset"],
        id: json["id"],
    );

    Map<String, dynamic> toJson() => {
        "addedAt": addedAt?.toIso8601String(),
        "asset": asset,
        "id": id,
    };
}