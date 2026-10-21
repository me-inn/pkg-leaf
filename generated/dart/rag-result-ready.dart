// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final ragResultReady = ragResultReadyFromJson(jsonString);

import 'dart:convert';

RagResultReady ragResultReadyFromJson(String str) => RagResultReady.fromJson(json.decode(str));

String ragResultReadyToJson(RagResultReady data) => json.encode(data.toJson());


///A question was answered, and the answer comes back with what it was built out of. The
///sources travel so the asker can show its work without holding the chunks. Keys are
///snake_case, not the camelCase the rest of leaf uses: this travels inside a Liquid
///envelope, whose own fields (event_id, occurred_at, event_type, owner_unit_ref) are
///snake_case and pinned byte-exact by signed golden vectors. The shape follows the wire.
class RagResultReady {
    
    ///The answer, grounded in the sources below.
    String answer;
    
    ///The job the answer was worked under, when the question arrived as one.
    String? jobId;
    
    ///The question as asked, repeated so the answer is readable on its own.
    String query;
    
    ///The working session the question was asked in.
    String sessionId;
    
    ///The chunks the answer was built from, in order of relevance. Absent when the search found
    ///nothing to stand on. A producer of this event always fills in score, chunkType and
    ///excerpt, even though the shared shape only insists on the two pointers.
    List<RagSource>? sources;

    RagResultReady({
        required this.answer,
        this.jobId,
        required this.query,
        required this.sessionId,
        this.sources,
    });

    factory RagResultReady.fromJson(Map<String, dynamic> json) => RagResultReady(
        answer: json["answer"],
        jobId: json["job_id"],
        query: json["query"],
        sessionId: json["session_id"],
        sources: json["sources"] == null ? [] : List<RagSource>.from(json["sources"]!.map((x) => RagSource.fromJson(x))),
    );

    Map<String, dynamic> toJson() => {
        "answer": answer,
        "job_id": jobId,
        "query": query,
        "session_id": sessionId,
        "sources": sources == null ? [] : List<dynamic>.from(sources!.map((x) => x.toJson())),
    };
}


///One chunk the answer stood on. The same shape as common.v1 ragSource, written out here in
///the relay's snake_case rather than referenced.
class RagSource {
    
    ///The asset the chunk came from, as the system that owns the asset names it.
    String asset;
    
    ///What the parent asset was called when the answer was written. Kept as a copy on purpose:
    ///a citation should still read after the asset is retitled.
    String? assetTitle;
    
    ///The chunk itself, as the system that owns the chunk names it.
    String chunk;
    
    ///Which part of the asset the chunk is — a summary, a transcript, a block of article text.
    ///Free text: the vocabulary belongs to whoever chunks.
    String? chunkType;
    
    ///The opening of the chunk, carried so a person can see what was cited without fetching it.
    String? excerpt;
    
    ///How close the chunk sat to the question, as the retrieval scored it. Comparable inside
    ///one search, not across searches: the scale belongs to the model that searched.
    double? score;
    
    ///A picture of the parent asset, when the system that serves it offers one. Derived, and
    ///resolvable only against the deploy that built it.
    String? thumbnailUrl;

    RagSource({
        required this.asset,
        this.assetTitle,
        required this.chunk,
        this.chunkType,
        this.excerpt,
        this.score,
        this.thumbnailUrl,
    });

    factory RagSource.fromJson(Map<String, dynamic> json) => RagSource(
        asset: json["asset"],
        assetTitle: json["asset_title"],
        chunk: json["chunk"],
        chunkType: json["chunk_type"],
        excerpt: json["excerpt"],
        score: json["score"]?.toDouble(),
        thumbnailUrl: json["thumbnail_url"],
    );

    Map<String, dynamic> toJson() => {
        "asset": asset,
        "asset_title": assetTitle,
        "chunk": chunk,
        "chunk_type": chunkType,
        "excerpt": excerpt,
        "score": score,
        "thumbnail_url": thumbnailUrl,
    };
}