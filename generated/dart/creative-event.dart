// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final creativeEvent = creativeEventFromJson(jsonString);

import 'dart:convert';

CreativeEvent creativeEventFromJson(String str) => CreativeEvent.fromJson(json.decode(str));

String creativeEventToJson(CreativeEvent data) => json.encode(data.toJson());


///One thing the creative pipeline was asked to do, or one thing it finished — as it travels
///between the system that asks and the system that works. Commands go one way and results
///come back the other way over the same relay, so they are one shape with one type field
///rather than two. The event carries no content: what it carries is an id of something a
///system already holds, and enough words to act on it. Keys are snake_case, not the
///camelCase the rest of leaf uses: this travels inside a Liquid envelope, whose own fields
///(event_id, occurred_at, event_type, owner_unit_ref) are snake_case and pinned byte-exact
///by signed golden vectors. The shape follows the wire.
class CreativeEvent {
    
    ///ed25519 public key, hex, of whoever signed the event. The only thing that says who asked:
    ///a reader admits an event by this key, never by the name below.
    String? author;
    
    ///What the signing system calls itself, such as creativeflow. A label for reading a log; it
    ///proves nothing, and two systems may well claim the same one.
    String? authorName;
    
    ///The asset, generation or job the event is about, repeated outside the payload so a reader
    ///can file the event without opening it. Absent for events about no single thing, such as
    ///an error.
    String? contentId;
    
    ///The device the event was written on, when more than one writes for the same author.
    String? deviceId;
    
    ///What happened, written as <domain>.<action>. The requested forms are commands addressed
    ///to the pipeline; the rest are results it emits. It alone decides which payload shape
    ///applies — two different commands can carry the same single id and are told apart by
    ///nothing else.
    EventType eventType;
    
    ///The record's own id in the system that holds it. Also what makes the event replayable
    ///without doing the work twice: a reader that has seen this id has already acted.
    String? id;
    
    ///A counter for ordering events from one author when wall clocks disagree. Comparable only
    ///against events from the same author.
    int? lamport;
    
    ///When the author says it happened, which is not when a reader received it.
    DateTime? occurredAt;
    
    ///The session or unit the event belongs to, which is who answers for it. Set on errors
    ///above all, where it is the only thing saying whose work broke.
    String? ownerUnitRef;
    
    ///What the event is about. Open on purpose: eventType decides which schema the payload is,
    ///and a reader picks that type rather than matching on the shape. The union used to live
    ///here as anyOf and the generator kept only its first branch, so the other fourteen
    ///payloads had no type at all; each is now its own schema. asset.ingest_requested ->
    ///AssetIngestRequested; asset.url_ingest_requested -> AssetUrlIngestRequested;
    ///generation.requested -> GenerationRequested; repurpose.requested -> RepurposeRequested;
    ///rag.query_requested -> RagQueryRequested; asset.edit_requested -> AssetEditRequested;
    ///read.completed -> ReadCompleted; derivative.created -> DerivativeCreated;
    ///citation.created -> CitationCreated; value.snapshot -> ValueSnapshot; signal.error ->
    ///SignalError; generation.ready -> GenerationReady; rag.result_ready -> RagResultReady;
    ///repurpose.ready -> RepurposeReady; asset.edit_ready -> AssetEditReady.
    Map<String, dynamic> payload;

    CreativeEvent({
        this.author,
        this.authorName,
        this.contentId,
        this.deviceId,
        required this.eventType,
        this.id,
        this.lamport,
        this.occurredAt,
        this.ownerUnitRef,
        required this.payload,
    });

    factory CreativeEvent.fromJson(Map<String, dynamic> json) => CreativeEvent(
        author: json["author"],
        authorName: json["author_name"],
        contentId: json["content_id"],
        deviceId: json["device_id"],
        eventType: eventTypeValues.map[json["event_type"]]!,
        id: json["id"],
        lamport: json["lamport"],
        occurredAt: json["occurred_at"] == null ? null : DateTime.parse(json["occurred_at"]),
        ownerUnitRef: json["owner_unit_ref"],
        payload: Map.from(json["payload"]).map((k, v) => MapEntry<String, dynamic>(k, v)),
    );

    Map<String, dynamic> toJson() => {
        "author": author,
        "author_name": authorName,
        "content_id": contentId,
        "device_id": deviceId,
        "event_type": eventTypeValues.reverse[eventType],
        "id": id,
        "lamport": lamport,
        "occurred_at": occurredAt?.toIso8601String(),
        "owner_unit_ref": ownerUnitRef,
        "payload": Map.from(payload).map((k, v) => MapEntry<String, dynamic>(k, v)),
    };
}


///What happened, written as <domain>.<action>. The requested forms are commands addressed
///to the pipeline; the rest are results it emits. It alone decides which payload shape
///applies — two different commands can carry the same single id and are told apart by
///nothing else.
enum EventType {
    ASSET_EDIT_READY,
    ASSET_EDIT_REQUESTED,
    ASSET_INGEST_REQUESTED,
    ASSET_URL_INGEST_REQUESTED,
    CITATION_CREATED,
    DERIVATIVE_CREATED,
    GENERATION_READY,
    GENERATION_REQUESTED,
    RAG_QUERY_REQUESTED,
    RAG_RESULT_READY,
    READ_COMPLETED,
    REPURPOSE_READY,
    REPURPOSE_REQUESTED,
    SIGNAL_ERROR,
    VALUE_SNAPSHOT
}

final eventTypeValues = EnumValues({
    "asset.edit_ready": EventType.ASSET_EDIT_READY,
    "asset.edit_requested": EventType.ASSET_EDIT_REQUESTED,
    "asset.ingest_requested": EventType.ASSET_INGEST_REQUESTED,
    "asset.url_ingest_requested": EventType.ASSET_URL_INGEST_REQUESTED,
    "citation.created": EventType.CITATION_CREATED,
    "derivative.created": EventType.DERIVATIVE_CREATED,
    "generation.ready": EventType.GENERATION_READY,
    "generation.requested": EventType.GENERATION_REQUESTED,
    "rag.query_requested": EventType.RAG_QUERY_REQUESTED,
    "rag.result_ready": EventType.RAG_RESULT_READY,
    "read.completed": EventType.READ_COMPLETED,
    "repurpose.ready": EventType.REPURPOSE_READY,
    "repurpose.requested": EventType.REPURPOSE_REQUESTED,
    "signal.error": EventType.SIGNAL_ERROR,
    "value.snapshot": EventType.VALUE_SNAPSHOT
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