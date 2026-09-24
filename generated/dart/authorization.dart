// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final authorization = authorizationFromJson(jsonString);

import 'dart:convert';

Authorization authorizationFromJson(String str) => Authorization.fromJson(json.decode(str));

String authorizationToJson(Authorization data) => json.encode(data.toJson());


///Somebody letting a piece of software act for them. What was granted, to whom, and until
///when — never the credential that proves it. The code and the token are secrets, they are
///held only as a hash by the system that issued them, and neither has a shape here.
class Authorization {
    
    ///The https URL that identifies the software. It is also where that software describes
    ///itself, so nothing about it has to be copied here.
    String client;
    
    ///When it stops working on its own, with nobody having to do anything.
    DateTime? expiresAt;
    DateTime? grantedAt;
    
    ///What the software calls itself, as it said. Recorded so a person recognises it when
    ///deciding what to take back; never used to decide anything.
    String? label;
    
    ///When it was taken back. A grant that ended is kept rather than deleted: what was allowed,
    ///and until when, is a fact about the past.
    DateTime? revokedAt;
    
    ///The wallet, or the id under localIds, of whoever is being acted for. The grant is theirs
    ///and so is taking it back.
    String subject;

    Authorization({
        required this.client,
        this.expiresAt,
        this.grantedAt,
        this.label,
        this.revokedAt,
        required this.subject,
    });

    factory Authorization.fromJson(Map<String, dynamic> json) => Authorization(
        client: json["client"],
        expiresAt: json["expiresAt"] == null ? null : DateTime.parse(json["expiresAt"]),
        grantedAt: json["grantedAt"] == null ? null : DateTime.parse(json["grantedAt"]),
        label: json["label"],
        revokedAt: json["revokedAt"] == null ? null : DateTime.parse(json["revokedAt"]),
        subject: json["subject"],
    );

    Map<String, dynamic> toJson() => {
        "client": client,
        "expiresAt": expiresAt?.toIso8601String(),
        "grantedAt": grantedAt?.toIso8601String(),
        "label": label,
        "revokedAt": revokedAt?.toIso8601String(),
        "subject": subject,
    };
}