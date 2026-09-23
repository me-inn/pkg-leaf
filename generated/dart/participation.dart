// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final participation = participationFromJson(jsonString);

import 'dart:convert';

Participation participationFromJson(String str) => Participation.fromJson(json.decode(str));

String participationToJson(Participation data) => json.encode(data.toJson());


///An organisation's role in an event, a publication, a split or a programme.
class Participation {
    
    ///What kind of thing it participates in.
    Context context;
    
    ///The id of that thing, in the system that owns it.
    String contextId;
    DateTime? createdAt;
    
    ///The organisation's wallet, or its id under localIds.
    String organization;
    
    ///Its role there, in that context's own words. Free text: the vocabulary belongs to the
    ///context.
    String role;
    Status? status;

    Participation({
        required this.context,
        required this.contextId,
        this.createdAt,
        required this.organization,
        required this.role,
        this.status,
    });

    factory Participation.fromJson(Map<String, dynamic> json) => Participation(
        context: contextValues.map[json["context"]]!,
        contextId: json["contextId"],
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        organization: json["organization"],
        role: json["role"],
        status: statusValues.map[json["status"]],
    );

    Map<String, dynamic> toJson() => {
        "context": contextValues.reverse[context],
        "contextId": contextId,
        "createdAt": createdAt?.toIso8601String(),
        "organization": organization,
        "role": role,
        "status": statusValues.reverse[status],
    };
}


///What kind of thing it participates in.
enum Context {
    EVENT,
    PROGRAM,
    PUBLICATION,
    SPLIT
}

final contextValues = EnumValues({
    "event": Context.EVENT,
    "program": Context.PROGRAM,
    "publication": Context.PUBLICATION,
    "split": Context.SPLIT
});

enum Status {
    ACTIVE,
    ENDED,
    PROPOSED
}

final statusValues = EnumValues({
    "active": Status.ACTIVE,
    "ended": Status.ENDED,
    "proposed": Status.PROPOSED
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