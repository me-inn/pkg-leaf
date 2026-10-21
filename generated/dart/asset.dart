// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final asset = assetFromJson(jsonString);

import 'dart:convert';

Asset assetFromJson(String str) => Asset.fromJson(json.decode(str));

String assetToJson(Asset data) => json.encode(data.toJson());


///Something somebody put in — a file uploaded or a page ingested from a URL — and
///everything a machine later said about it. The bytes never travel: what travels is where
///they are kept, what kind of thing they are, and the reading a pipeline made of them.
class Asset {
    
    ///What a machine said the asset is.
    String? aiDescription;
    
    ///The longer reading a machine made of it.
    String? aiSummary;
    
    ///Tags a machine put on it. Free text: the vocabulary belongs to whoever enriched the
    ///asset, not to this shape.
    List<String>? aiTags;
    
    ///A title a machine gave it, which is not the filename and not a title a person wrote.
    String? aiTitle;
    
    ///What kind of thing it is, which decides which pipeline reads it.
    AssetType assetType;
    
    ///The media type, as declared on arrival.
    String contentType;
    
    ///When the asset was recorded, which is not when the file was made.
    DateTime? createdAt;
    
    ///The semantic vector of the whole asset.
    List<double>? embedding;
    
    ///Size in bytes.
    int fileSize;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///Raw technical metadata as the extractor read it off the file — dimensions, duration,
    ///codec, whatever the format carries.
    Map<String, dynamic>? metadata;
    
    ///The name the file had when it arrived. Never the name it is stored under.
    String originalFilename;
    
    ///The wallet, handle, or id under localIds of whoever the asset belongs to. Absent for an
    ///asset that was put in before anybody claimed it.
    String? owner;
    
    ///Which step it was on. Read together with the status, it says where a run stopped: failed
    ///at ai_enrichment is a different repair from failed at embedding_indexing. Absent before
    ///the first step runs.
    ProcessingStage? processingStage;
    
    ///Where the pipeline stands on this asset.
    ProcessingStatus processingStatus;
    
    ///The id of the working session it was put in during, in the system that owns the session.
    ///Absent when it was not put in through one.
    String? session;
    
    ///How it arrived: handed over as a file, or fetched from an address.
    SourceType? sourceType;
    
    ///The address it was fetched from, when it was fetched. Kept even after ingestion, because
    ///the copy and the original drift apart.
    String? sourceUrl;
    
    ///Where the bytes sit in the store that holds them. Meaningful only to that store; a reader
    ///asks it, never resolves the key itself.
    String storageKey;
    
    ///A preview image made from the asset. A second file the asset owns, not the asset itself:
    ///it is derived, and absent until something made one.
    StoredFile? thumbnail;
    
    ///What was said in it, for an asset that is heard rather than read.
    String? transcriptText;
    DateTime? updatedAt;
    
    ///What is seen in it, for an asset that is looked at rather than read.
    String? visualSummary;

    Asset({
        this.aiDescription,
        this.aiSummary,
        this.aiTags,
        this.aiTitle,
        required this.assetType,
        required this.contentType,
        this.createdAt,
        this.embedding,
        required this.fileSize,
        this.id,
        this.metadata,
        required this.originalFilename,
        this.owner,
        this.processingStage,
        required this.processingStatus,
        this.session,
        this.sourceType,
        this.sourceUrl,
        required this.storageKey,
        this.thumbnail,
        this.transcriptText,
        this.updatedAt,
        this.visualSummary,
    });

    factory Asset.fromJson(Map<String, dynamic> json) => Asset(
        aiDescription: json["aiDescription"],
        aiSummary: json["aiSummary"],
        aiTags: json["aiTags"] == null ? [] : List<String>.from(json["aiTags"]!.map((x) => x)),
        aiTitle: json["aiTitle"],
        assetType: assetTypeValues.map[json["assetType"]]!,
        contentType: json["contentType"],
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        embedding: json["embedding"] == null ? [] : List<double>.from(json["embedding"]!.map((x) => x?.toDouble())),
        fileSize: json["fileSize"],
        id: json["id"],
        metadata: Map.from(json["metadata"]!).map((k, v) => MapEntry<String, dynamic>(k, v)),
        originalFilename: json["originalFilename"],
        owner: json["owner"],
        processingStage: processingStageValues.map[json["processingStage"]],
        processingStatus: processingStatusValues.map[json["processingStatus"]]!,
        session: json["session"],
        sourceType: sourceTypeValues.map[json["sourceType"]],
        sourceUrl: json["sourceUrl"],
        storageKey: json["storageKey"],
        thumbnail: json["thumbnail"] == null ? null : StoredFile.fromJson(json["thumbnail"]),
        transcriptText: json["transcriptText"],
        updatedAt: json["updatedAt"] == null ? null : DateTime.parse(json["updatedAt"]),
        visualSummary: json["visualSummary"],
    );

    Map<String, dynamic> toJson() => {
        "aiDescription": aiDescription,
        "aiSummary": aiSummary,
        "aiTags": aiTags == null ? [] : List<dynamic>.from(aiTags!.map((x) => x)),
        "aiTitle": aiTitle,
        "assetType": assetTypeValues.reverse[assetType],
        "contentType": contentType,
        "createdAt": createdAt?.toIso8601String(),
        "embedding": embedding == null ? [] : List<dynamic>.from(embedding!.map((x) => x)),
        "fileSize": fileSize,
        "id": id,
        "metadata": Map.from(metadata!).map((k, v) => MapEntry<String, dynamic>(k, v)),
        "originalFilename": originalFilename,
        "owner": owner,
        "processingStage": processingStageValues.reverse[processingStage],
        "processingStatus": processingStatusValues.reverse[processingStatus],
        "session": session,
        "sourceType": sourceTypeValues.reverse[sourceType],
        "sourceUrl": sourceUrl,
        "storageKey": storageKey,
        "thumbnail": thumbnail?.toJson(),
        "transcriptText": transcriptText,
        "updatedAt": updatedAt?.toIso8601String(),
        "visualSummary": visualSummary,
    };
}


///What kind of thing it is, which decides which pipeline reads it.
///
///What kind of thing an asset is, which decides which pipeline reads it. A document covers
///an article, a PDF, or raw text.
enum AssetType {
    DOCUMENT,
    IMAGE,
    VIDEO
}

final assetTypeValues = EnumValues({
    "document": AssetType.DOCUMENT,
    "image": AssetType.IMAGE,
    "video": AssetType.VIDEO
});


///Which step it was on. Read together with the status, it says where a run stopped: failed
///at ai_enrichment is a different repair from failed at embedding_indexing. Absent before
///the first step runs.
enum ProcessingStage {
    AI_ENRICHMENT,
    COMPLETED,
    EMBEDDING_INDEXING,
    METADATA_EXTRACTION
}

final processingStageValues = EnumValues({
    "ai_enrichment": ProcessingStage.AI_ENRICHMENT,
    "completed": ProcessingStage.COMPLETED,
    "embedding_indexing": ProcessingStage.EMBEDDING_INDEXING,
    "metadata_extraction": ProcessingStage.METADATA_EXTRACTION
});


///Where the pipeline stands on this asset.
///
///Where a pipeline stands on the thing it was given. Which move from which is a rule held
///beside the type, never in it.
enum ProcessingStatus {
    COMPLETED,
    FAILED,
    PENDING,
    PROCESSING
}

final processingStatusValues = EnumValues({
    "completed": ProcessingStatus.COMPLETED,
    "failed": ProcessingStatus.FAILED,
    "pending": ProcessingStatus.PENDING,
    "processing": ProcessingStatus.PROCESSING
});


///How it arrived: handed over as a file, or fetched from an address.
enum SourceType {
    UPLOAD,
    URL
}

final sourceTypeValues = EnumValues({
    "upload": SourceType.UPLOAD,
    "url": SourceType.URL
});


///A preview image made from the asset. A second file the asset owns, not the asset itself:
///it is derived, and absent until something made one.
///
///Bytes somebody is keeping, pointed at rather than carried. Never the file itself: the
///store that holds it holds it, and this says which key to ask under and, while it lasts,
///where it can be fetched. Nothing is required, because a file can be known by its key
///before any address has been issued for it, and served by an address before anybody
///recorded a key.
class StoredFile {
    
    ///How big it is, so whoever is about to fetch it knows what they are asking for.
    int? sizeBytes;
    
    ///Where the bytes sit in the store that holds them. The lasting handle, meaningful only to
    ///that store: a reader asks the store, never resolves the key itself.
    String? storageKey;
    
    ///Where the file can be fetched right now. Often signed and short-lived, so it is read at
    ///the moment of use and never kept as the address of the file.
    String? url;

    StoredFile({
        this.sizeBytes,
        this.storageKey,
        this.url,
    });

    factory StoredFile.fromJson(Map<String, dynamic> json) => StoredFile(
        sizeBytes: json["sizeBytes"],
        storageKey: json["storageKey"],
        url: json["url"],
    );

    Map<String, dynamic> toJson() => {
        "sizeBytes": sizeBytes,
        "storageKey": storageKey,
        "url": url,
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