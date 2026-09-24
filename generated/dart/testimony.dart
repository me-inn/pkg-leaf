// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final testimony = testimonyFromJson(jsonString);

import 'dart:convert';

Testimony testimonyFromJson(String str) => Testimony.fromJson(json.decode(str));

String testimonyToJson(Testimony data) => json.encode(data.toJson());


///Something one person wrote about another, published with the subject's consent and their
///author's name attached.
class Testimony {
    
    ///The wallet, or the id under localIds, of whoever wrote it.
    String author;
    DateTime? createdAt;
    
    ///What was written, in the author's own words. A scene rather than an attribute: what the
    ///subject did, told by whoever was there.
    String? detail;
    
    ///The record's own id in the system that holds it.
    String? id;
    DateTime? publishedAt;
    
    ///While set, the subject is told the record exists and not what it says. Opens when they
    ///write their own, or when this passes.
    DateTime? sealedUntil;
    
    ///ed25519 over the record, hex. Signed by the author's wallet, so the words can be shown to
    ///have come from them.
    String? signature;
    
    ///Published only once the subject has agreed. Pending is written and not readable by anyone
    ///but its author.
    State? state;
    
    ///The wallet, or the id under localIds, of whoever it is about.
    String subject;

    Testimony({
        required this.author,
        this.createdAt,
        this.detail,
        this.id,
        this.publishedAt,
        this.sealedUntil,
        this.signature,
        this.state,
        required this.subject,
    });

    factory Testimony.fromJson(Map<String, dynamic> json) => Testimony(
        author: json["author"],
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        detail: json["detail"],
        id: json["id"],
        publishedAt: json["publishedAt"] == null ? null : DateTime.parse(json["publishedAt"]),
        sealedUntil: json["sealedUntil"] == null ? null : DateTime.parse(json["sealedUntil"]),
        signature: json["signature"],
        state: stateValues.map[json["state"]],
        subject: json["subject"],
    );

    Map<String, dynamic> toJson() => {
        "author": author,
        "createdAt": createdAt?.toIso8601String(),
        "detail": detail,
        "id": id,
        "publishedAt": publishedAt?.toIso8601String(),
        "sealedUntil": sealedUntil?.toIso8601String(),
        "signature": signature,
        "state": stateValues.reverse[state],
        "subject": subject,
    };
}


///Published only once the subject has agreed. Pending is written and not readable by anyone
///but its author.
enum State {
    HIDDEN,
    PENDING,
    PUBLISHED
}

final stateValues = EnumValues({
    "hidden": State.HIDDEN,
    "pending": State.PENDING,
    "published": State.PUBLISHED
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