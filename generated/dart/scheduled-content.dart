// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final scheduledContent = scheduledContentFromJson(jsonString);

import 'dart:convert';

ScheduledContent scheduledContentFromJson(String str) => ScheduledContent.fromJson(json.decode(str));

String scheduledContentToJson(ScheduledContent data) => json.encode(data.toJson());


///An intention to publish something that was already generated, at a time somebody picked.
///A plan, not a publication: nothing here says it went out, and the generation itself stays
///where it was made.
class ScheduledContent {
    
    ///When the plan was made, which is not when it publishes.
    DateTime? createdAt;
    
    ///What is to be published, as the system that holds the generation names it. A pointer: the
    ///text lives there and is not copied here, so editing it does not leave two versions.
    String generation;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///Anything the person wanted to remember about this one. Read by a person, never acted on.
    String? notes;
    
    ///Where it is meant to go, in the words of whoever scheduled it. Free text: the vocabulary
    ///belongs to whoever publishes, and nothing here posts anything.
    String? platform;
    
    ///When it is meant to go out. A moment, not a window, and the only field anything schedules
    ///on.
    DateTime publishAt;
    
    ///The session the plan belongs to, as the system that owns the session names it. Optional:
    ///scoping a scheduled item to a working session is how Creative Flow holds it, not part of
    ///what it is, and a system without sessions must be able to carry the same shape.
    String? session;

    ScheduledContent({
        this.createdAt,
        required this.generation,
        this.id,
        this.notes,
        this.platform,
        required this.publishAt,
        this.session,
    });

    factory ScheduledContent.fromJson(Map<String, dynamic> json) => ScheduledContent(
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        generation: json["generation"],
        id: json["id"],
        notes: json["notes"],
        platform: json["platform"],
        publishAt: DateTime.parse(json["publishAt"]),
        session: json["session"],
    );

    Map<String, dynamic> toJson() => {
        "createdAt": createdAt?.toIso8601String(),
        "generation": generation,
        "id": id,
        "notes": notes,
        "platform": platform,
        "publishAt": publishAt.toIso8601String(),
        "session": session,
    };
}