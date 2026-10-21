// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final generationPin = generationPinFromJson(jsonString);

import 'dart:convert';

GenerationPin generationPinFromJson(String str) => GenerationPin.fromJson(json.decode(str));

String generationPinToJson(GenerationPin data) => json.encode(data.toJson());


///A session holding on to a generation: kept near, so it is found again. An edge and not a
///column, because being pinned is not a property of the generation — the same generation is
///pinned in one session and not in another, and a column would make one session's opinion
///look like the thing's own.
class GenerationPin {
    
    ///The generation being held on to, by its id in the system that holds it.
    String generation;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///When it was pinned.
    DateTime? pinnedAt;
    
    ///The working session holding on to it, by that session's id in the system that holds it.
    ///That a session pins a generation at most once is the pinning system's rule, not a
    ///constraint of this shape.
    String session;

    GenerationPin({
        required this.generation,
        this.id,
        this.pinnedAt,
        required this.session,
    });

    factory GenerationPin.fromJson(Map<String, dynamic> json) => GenerationPin(
        generation: json["generation"],
        id: json["id"],
        pinnedAt: json["pinnedAt"] == null ? null : DateTime.parse(json["pinnedAt"]),
        session: json["session"],
    );

    Map<String, dynamic> toJson() => {
        "generation": generation,
        "id": id,
        "pinnedAt": pinnedAt?.toIso8601String(),
        "session": session,
    };
}