// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final generationFeedback = generationFeedbackFromJson(jsonString);

import 'dart:convert';

GenerationFeedback generationFeedbackFromJson(String str) => GenerationFeedback.fromJson(json.decode(str));

String generationFeedbackToJson(GenerationFeedback data) => json.encode(data.toJson());


///What somebody did with a generated piece when it was handed to them: took it, threw it
///away, or rewrote it. An act rather than an opinion — the rewrite is the feedback, and it
///is the one signal that says what good would have looked like.
class GenerationFeedback {
    
    ///What they did with it.
    Action action;
    
    ///When they did it.
    DateTime? createdAt;
    
    ///The piece as they rewrote it. Present when the action was edited; that it must be is a
    ///rule the writing system keeps, not a shape.
    String? editedOutput;
    
    ///The id of the generated piece this was done to, in the system that owns it.
    String generation;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///The id of the working session it happened in, in the system that holds it. Not a person:
    ///a session says the acts came from one sitting, and whether anybody is named is the
    ///holding system's business.
    String? session;

    GenerationFeedback({
        required this.action,
        this.createdAt,
        this.editedOutput,
        required this.generation,
        this.id,
        this.session,
    });

    factory GenerationFeedback.fromJson(Map<String, dynamic> json) => GenerationFeedback(
        action: actionValues.map[json["action"]]!,
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        editedOutput: json["editedOutput"],
        generation: json["generation"],
        id: json["id"],
        session: json["session"],
    );

    Map<String, dynamic> toJson() => {
        "action": actionValues.reverse[action],
        "createdAt": createdAt?.toIso8601String(),
        "editedOutput": editedOutput,
        "generation": generation,
        "id": id,
        "session": session,
    };
}


///What they did with it.
enum Action {
    APPROVED,
    EDITED,
    REJECTED
}

final actionValues = EnumValues({
    "approved": Action.APPROVED,
    "edited": Action.EDITED,
    "rejected": Action.REJECTED
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