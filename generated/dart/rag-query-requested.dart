// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final ragQueryRequested = ragQueryRequestedFromJson(jsonString);

import 'dart:convert';

RagQueryRequested ragQueryRequestedFromJson(String str) => RagQueryRequested.fromJson(json.decode(str));

String ragQueryRequestedToJson(RagQueryRequested data) => json.encode(data.toJson());


///A question somebody wants answered out of what was put in. Carries the whole question,
///for the same reason repurpose does. Keys are snake_case, not the camelCase the rest of
///leaf uses: this travels inside a Liquid envelope, whose own fields (event_id,
///occurred_at, event_type, owner_unit_ref) are snake_case and pinned byte-exact by signed
///golden vectors. The shape follows the wire.
class RagQueryRequested {
    
    ///Search only this kind of asset. Absent searches all of them.
    AssetType? assetType;
    
    ///The job to report the answer against, created by the pipeline if it does not exist yet.
    String jobId;
    
    ///BCP-47 tag of the language to answer in. Detected from the question when absent.
    String? language;
    
    ///The question, in natural language. A blank one is not worked.
    String? query;
    
    ///What to return: an answer grounded in the sources, or only the rewritten text, with
    ///nothing around it, for an editor that drops it straight into a document.
    ResponseMode? responseMode;
    
    ///The working session to search in. The question is answered out of that session's
    ///material, not out of everything.
    String sessionId;
    
    ///How many chunks to retrieve before answering. Absent leaves it to whoever searches.
    int? topK;

    RagQueryRequested({
        this.assetType,
        required this.jobId,
        this.language,
        this.query,
        this.responseMode,
        required this.sessionId,
        this.topK,
    });

    factory RagQueryRequested.fromJson(Map<String, dynamic> json) => RagQueryRequested(
        assetType: assetTypeValues.map[json["asset_type"]],
        jobId: json["job_id"],
        language: json["language"],
        query: json["query"],
        responseMode: responseModeValues.map[json["response_mode"]],
        sessionId: json["session_id"],
        topK: json["top_k"],
    );

    Map<String, dynamic> toJson() => {
        "asset_type": assetTypeValues.reverse[assetType],
        "job_id": jobId,
        "language": language,
        "query": query,
        "response_mode": responseModeValues.reverse[responseMode],
        "session_id": sessionId,
        "top_k": topK,
    };
}


///Search only this kind of asset. Absent searches all of them.
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


///What to return: an answer grounded in the sources, or only the rewritten text, with
///nothing around it, for an editor that drops it straight into a document.
enum ResponseMode {
    ANSWER,
    REWRITE
}

final responseModeValues = EnumValues({
    "answer": ResponseMode.ANSWER,
    "rewrite": ResponseMode.REWRITE
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