// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final assetChunk = assetChunkFromJson(jsonString);

import 'dart:convert';

AssetChunk assetChunkFromJson(String str) => AssetChunk.fromJson(json.decode(str));

String assetChunkToJson(AssetChunk data) => json.encode(data.toJson());


///One piece of an asset held separately so it can be searched on its own. The text is kept
///beside the vector so whoever answers from a chunk can show the excerpt it answered from,
///without opening the asset.
class AssetChunk {
    
    ///The id of the asset this piece was cut from, in the system that owns it.
    String asset;
    
    ///Position among the pieces of the same type on the same asset. Zero while a type yields
    ///one piece; it exists so splitting a long text later does not change the shape.
    int chunkOrder;
    
    ///The text that was embedded, verbatim.
    String chunkText;
    
    ///Which reading of the asset this piece is. They are indexed together but recall
    ///differently: title_tags catches a keyword, summary catches a meaning.
    ChunkType chunkType;
    DateTime? createdAt;
    
    ///The semantic vector of this piece. A reader holding another model recomputes it from
    ///chunkText.
    List<double>? embedding;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///Whatever the splitter recorded about the cut — offsets into the source, token counts.
    Map<String, dynamic>? metadata;

    AssetChunk({
        required this.asset,
        required this.chunkOrder,
        required this.chunkText,
        required this.chunkType,
        this.createdAt,
        this.embedding,
        this.id,
        this.metadata,
    });

    factory AssetChunk.fromJson(Map<String, dynamic> json) => AssetChunk(
        asset: json["asset"],
        chunkOrder: json["chunkOrder"],
        chunkText: json["chunkText"],
        chunkType: chunkTypeValues.map[json["chunkType"]]!,
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        embedding: json["embedding"] == null ? [] : List<double>.from(json["embedding"]!.map((x) => x?.toDouble())),
        id: json["id"],
        metadata: Map.from(json["metadata"]!).map((k, v) => MapEntry<String, dynamic>(k, v)),
    );

    Map<String, dynamic> toJson() => {
        "asset": asset,
        "chunkOrder": chunkOrder,
        "chunkText": chunkText,
        "chunkType": chunkTypeValues.reverse[chunkType],
        "createdAt": createdAt?.toIso8601String(),
        "embedding": embedding == null ? [] : List<dynamic>.from(embedding!.map((x) => x)),
        "id": id,
        "metadata": Map.from(metadata!).map((k, v) => MapEntry<String, dynamic>(k, v)),
    };
}


///Which reading of the asset this piece is. They are indexed together but recall
///differently: title_tags catches a keyword, summary catches a meaning.
enum ChunkType {
    ARTICLE_TEXT,
    DESCRIPTION,
    METADATA,
    SUMMARY,
    TITLE_TAGS,
    TRANSCRIPT,
    VISUAL_SUMMARY
}

final chunkTypeValues = EnumValues({
    "article_text": ChunkType.ARTICLE_TEXT,
    "description": ChunkType.DESCRIPTION,
    "metadata": ChunkType.METADATA,
    "summary": ChunkType.SUMMARY,
    "title_tags": ChunkType.TITLE_TAGS,
    "transcript": ChunkType.TRANSCRIPT,
    "visual_summary": ChunkType.VISUAL_SUMMARY
});

class EnumValues<T> {
    Map<String, T> map;
    late Map<T, String> reverseMap;

    EnumValues(this.map);

    Map<T, String> get reverse {
            reverseMap = map.map((k, v) => MapEntry(v, k));
            return reverseMap;
    }
}