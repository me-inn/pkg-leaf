// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final generation = generationFromJson(jsonString);

import 'dart:convert';

Generation generationFromJson(String str) => Generation.fromJson(json.decode(str));

String generationToJson(Generation data) => json.encode(data.toJson());


///One thing a model wrote when somebody asked for it: what was asked, what it was given to
///read, and the text that came out. The assets it read are named by id and stay where they
///are — this record is the asking, not a copy of the material.
class Generation {
    
    ///The assets the model was given to read, by their ids in the system that holds them. Ids,
    ///never the material: the asset is somebody else's record.
    List<String>? assetIds;
    
    ///Where the text was meant to go. Free text: the channels belong to whoever publishes, not
    ///to this shape.
    String? channel;
    
    ///Where the text stands. Which status may follow which is a rule held by the system that
    ///moves it, not a constraint of this shape.
    ContentStatus? contentStatus;
    
    ///When the generation was recorded.
    DateTime? createdAt;
    
    ///What kind of thing was asked for. Free text: the vocabulary grows with every surface that
    ///asks, so it is not closed here.
    String generationType;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///What the person asked for, in their own words, before anything was assembled around it.
    String? instructions;
    
    ///Which model wrote it, under the name its provider gives it. Recorded so a later reading
    ///knows what produced the text — never a key, never a provider credential.
    String? modelUsed;
    
    ///What the text was meant to achieve. Free text, for the same reason as channel.
    String? objective;
    
    ///The text the model produced. Empty while the generation exists and has produced nothing
    ///yet.
    String? output;
    
    ///The prompt actually sent, after the instructions and the context were assembled into one.
    ///Kept because the instructions alone do not reproduce it.
    String? promptUsed;
    
    ///The working session it was generated in, by that session's id in the system that holds
    ///it. A session, not a person: who was at the keyboard is the session's own business.
    ///Absent when it was generated outside one.
    String? session;
    
    ///Labels somebody put on it. Free text, theirs.
    List<String>? tags;

    Generation({
        this.assetIds,
        this.channel,
        this.contentStatus,
        this.createdAt,
        required this.generationType,
        this.id,
        this.instructions,
        this.modelUsed,
        this.objective,
        this.output,
        this.promptUsed,
        this.session,
        this.tags,
    });

    factory Generation.fromJson(Map<String, dynamic> json) => Generation(
        assetIds: json["assetIds"] == null ? [] : List<String>.from(json["assetIds"]!.map((x) => x)),
        channel: json["channel"],
        contentStatus: contentStatusValues.map[json["contentStatus"]],
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        generationType: json["generationType"],
        id: json["id"],
        instructions: json["instructions"],
        modelUsed: json["modelUsed"],
        objective: json["objective"],
        output: json["output"],
        promptUsed: json["promptUsed"],
        session: json["session"],
        tags: json["tags"] == null ? [] : List<String>.from(json["tags"]!.map((x) => x)),
    );

    Map<String, dynamic> toJson() => {
        "assetIds": assetIds == null ? [] : List<dynamic>.from(assetIds!.map((x) => x)),
        "channel": channel,
        "contentStatus": contentStatusValues.reverse[contentStatus],
        "createdAt": createdAt?.toIso8601String(),
        "generationType": generationType,
        "id": id,
        "instructions": instructions,
        "modelUsed": modelUsed,
        "objective": objective,
        "output": output,
        "promptUsed": promptUsed,
        "session": session,
        "tags": tags == null ? [] : List<dynamic>.from(tags!.map((x) => x)),
    };
}


///Where the text stands. Which status may follow which is a rule held by the system that
///moves it, not a constraint of this shape.
enum ContentStatus {
    APPROVED,
    ARCHIVED,
    DRAFT,
    PUBLISHED
}

final contentStatusValues = EnumValues({
    "approved": ContentStatus.APPROVED,
    "archived": ContentStatus.ARCHIVED,
    "draft": ContentStatus.DRAFT,
    "published": ContentStatus.PUBLISHED
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