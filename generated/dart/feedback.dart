// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final feedback = feedbackFromJson(jsonString);

import 'dart:convert';

Feedback feedbackFromJson(String str) => Feedback.fromJson(json.decode(str));

String feedbackToJson(Feedback data) => json.encode(data.toJson());


///A rating somebody gave a thing the software produced, with a line about it if they wrote
///one. About an output and not about a person: it carries no subject, no consent and no
///signature, which is what separates it from a testimony.
class Feedback {
    
    ///What they wrote alongside the rating, in their own words.
    String? comment;
    
    ///When it was given.
    DateTime? createdAt;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///The rating as given, 1 to 5. Collected both ways: as a thumb, where only 1 and 5 are ever
    ///written, and as the whole scale. Which of the two it was is not recorded, so a mean over
    ///mixed records is a number about nothing.
    int rating;
    
    ///The id of the working session it came from, in the system that holds it. Not a person.
    String? session;
    
    ///The id of that thing, in the system that owns it. It is read together with targetType and
    ///alone means nothing — two kinds of target do not share an id space.
    String target;
    
    ///What kind of thing was rated. Free text with the two the system records so far: a target
    ///type is added whenever something new becomes ratable, and a closed list here would have
    ///to be versioned for each one.
    String targetType;

    Feedback({
        this.comment,
        this.createdAt,
        this.id,
        required this.rating,
        this.session,
        required this.target,
        required this.targetType,
    });

    factory Feedback.fromJson(Map<String, dynamic> json) => Feedback(
        comment: json["comment"],
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        id: json["id"],
        rating: json["rating"],
        session: json["session"],
        target: json["target"],
        targetType: json["targetType"],
    );

    Map<String, dynamic> toJson() => {
        "comment": comment,
        "createdAt": createdAt?.toIso8601String(),
        "id": id,
        "rating": rating,
        "session": session,
        "target": target,
        "targetType": targetType,
    };
}