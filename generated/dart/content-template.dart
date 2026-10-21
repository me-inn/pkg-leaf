// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final contentTemplate = contentTemplateFromJson(jsonString);

import 'dart:convert';

ContentTemplate contentTemplateFromJson(String str) => ContentTemplate.fromJson(json.decode(str));

String contentTemplateToJson(ContentTemplate data) => json.encode(data.toJson());


///A saved starting point for generating something: what kind of piece, for which channel
///and objective, with the standing instructions to use. Settings somebody wants back, not a
///piece of content — nothing generated is kept here.
class ContentTemplate {
    
    ///Where the piece is meant to run, in the words of whoever saved the template. Free text
    ///everywhere it appears: the vocabulary belongs to whoever publishes.
    String? channel;
    
    ///When the template was saved.
    DateTime? createdAt;
    
    ///What kind of piece it produces. Free text: the names belong to the generation flow, which
    ///adds to them.
    String generationType;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///The standing instructions to apply, in the person's own words. The template's substance:
    ///everything else only files it.
    String? instructions;
    
    ///What the person called it, so they recognise it in a list.
    String name;
    
    ///What the piece is meant to do. Free text, for the same reason as channel.
    String? objective;
    
    ///The session the template belongs to, as the system that owns the session names it.
    ///Optional: scoping a template to a working session is how Creative Flow holds it, not part
    ///of what it is, and a system without sessions must be able to carry the same shape.
    String? session;

    ContentTemplate({
        this.channel,
        this.createdAt,
        required this.generationType,
        this.id,
        this.instructions,
        required this.name,
        this.objective,
        this.session,
    });

    factory ContentTemplate.fromJson(Map<String, dynamic> json) => ContentTemplate(
        channel: json["channel"],
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        generationType: json["generationType"],
        id: json["id"],
        instructions: json["instructions"],
        name: json["name"],
        objective: json["objective"],
        session: json["session"],
    );

    Map<String, dynamic> toJson() => {
        "channel": channel,
        "createdAt": createdAt?.toIso8601String(),
        "generationType": generationType,
        "id": id,
        "instructions": instructions,
        "name": name,
        "objective": objective,
        "session": session,
    };
}