// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final generationNote = generationNoteFromJson(jsonString);

import 'dart:convert';

GenerationNote generationNoteFromJson(String str) => GenerationNote.fromJson(json.decode(str));

String generationNoteToJson(GenerationNote data) => json.encode(data.toJson());


///Something somebody wrote beside a generation — a remark about the text, not part of it.
///It stays its own record so the generation reads as the model left it.
class GenerationNote {
    
    ///What they wrote, in their words.
    String body;
    
    ///When the note was written.
    DateTime? createdAt;
    
    ///The generation the note is about, by its id in the system that holds it.
    String generation;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///The working session the note was written in, by that session's id in the system that
    ///holds it. The note is attributed to the session, not to a wallet: who was at the keyboard
    ///is the session's own business.
    String session;
    
    ///When it was last rewritten. A note is editable, so this differs from createdAt once it
    ///has been.
    DateTime? updatedAt;

    GenerationNote({
        required this.body,
        this.createdAt,
        required this.generation,
        this.id,
        required this.session,
        this.updatedAt,
    });

    factory GenerationNote.fromJson(Map<String, dynamic> json) => GenerationNote(
        body: json["body"],
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        generation: json["generation"],
        id: json["id"],
        session: json["session"],
        updatedAt: json["updatedAt"] == null ? null : DateTime.parse(json["updatedAt"]),
    );

    Map<String, dynamic> toJson() => {
        "body": body,
        "createdAt": createdAt?.toIso8601String(),
        "generation": generation,
        "id": id,
        "session": session,
        "updatedAt": updatedAt?.toIso8601String(),
    };
}