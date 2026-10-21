// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final chatMessage = chatMessageFromJson(jsonString);

import 'dart:convert';

ChatMessage chatMessageFromJson(String str) => ChatMessage.fromJson(json.decode(str));

String chatMessageToJson(ChatMessage data) => json.encode(data.toJson());


///One turn of a conversation held against a library: what was asked, or what was answered,
///and for an answer the chunks it was grounded on. The sources are pointers with enough of
///the text to recognise them — never the chunk itself, which stays with the asset it came
///from.
class ChatMessage {
    
    ///What was said. The question as typed, or the answer as generated.
    String content;
    
    ///When the turn was recorded. The only ordering the conversation has.
    DateTime? createdAt;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///Who spoke. Two values: a person asks and the model answers, and nothing else writes a
    ///turn.
    Role role;
    
    ///The session the turn belongs to, as the system that owns the session names it. Absent on
    ///rows written before turns were scoped.
    String? session;
    
    ///The chunks the answer was grounded on, in relevance order. Absent on a question, and
    ///empty on an answer that was grounded on nothing.
    List<RagSource>? sources;

    ChatMessage({
        required this.content,
        this.createdAt,
        this.id,
        required this.role,
        this.session,
        this.sources,
    });

    factory ChatMessage.fromJson(Map<String, dynamic> json) => ChatMessage(
        content: json["content"],
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        id: json["id"],
        role: roleValues.map[json["role"]]!,
        session: json["session"],
        sources: json["sources"] == null ? [] : List<RagSource>.from(json["sources"]!.map((x) => RagSource.fromJson(x))),
    );

    Map<String, dynamic> toJson() => {
        "content": content,
        "createdAt": createdAt?.toIso8601String(),
        "id": id,
        "role": roleValues.reverse[role],
        "session": session,
        "sources": sources == null ? [] : List<dynamic>.from(sources!.map((x) => x.toJson())),
    };
}


///Who spoke. Two values: a person asks and the model answers, and nothing else writes a
///turn.
enum Role {
    ASSISTANT,
    USER
}

final roleValues = EnumValues({
    "assistant": Role.ASSISTANT,
    "user": Role.USER
});


///One retrieved chunk an answer leaned on, as it was at the time of the answer. A pointer
///plus what a person needs to judge it — never the chunk, which stays with the asset it
///came from — so the citation still reads once the chunk has changed.
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
        assetTitle: json["assetTitle"],
        chunk: json["chunk"],
        chunkType: json["chunkType"],
        excerpt: json["excerpt"],
        score: json["score"]?.toDouble(),
        thumbnailUrl: json["thumbnailUrl"],
    );

    Map<String, dynamic> toJson() => {
        "asset": asset,
        "assetTitle": assetTitle,
        "chunk": chunk,
        "chunkType": chunkType,
        "excerpt": excerpt,
        "score": score,
        "thumbnailUrl": thumbnailUrl,
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