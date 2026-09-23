// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final membership = membershipFromJson(jsonString);

import 'dart:convert';

Membership membershipFromJson(String str) => Membership.fromJson(json.decode(str));

String membershipToJson(Membership data) => json.encode(data.toJson());


///A person belonging to an organisation.
class Membership {
    
    ///What they may do inside it. Free text: the verbs belong to the system that grants them.
    List<String>? capabilities;
    DateTime? createdAt;
    
    ///The wallet or local id of whoever invited them.
    String? invitedBy;
    
    ///The organisation's wallet, or its id under localIds.
    String organization;
    
    ///The person's wallet, or their id under localIds.
    String person;
    Status? status;
    DateTime? updatedAt;

    Membership({
        this.capabilities,
        this.createdAt,
        this.invitedBy,
        required this.organization,
        required this.person,
        this.status,
        this.updatedAt,
    });

    factory Membership.fromJson(Map<String, dynamic> json) => Membership(
        capabilities: json["capabilities"] == null ? [] : List<String>.from(json["capabilities"]!.map((x) => x)),
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        invitedBy: json["invitedBy"],
        organization: json["organization"],
        person: json["person"],
        status: statusValues.map[json["status"]],
        updatedAt: json["updatedAt"] == null ? null : DateTime.parse(json["updatedAt"]),
    );

    Map<String, dynamic> toJson() => {
        "capabilities": capabilities == null ? [] : List<dynamic>.from(capabilities!.map((x) => x)),
        "createdAt": createdAt?.toIso8601String(),
        "invitedBy": invitedBy,
        "organization": organization,
        "person": person,
        "status": statusValues.reverse[status],
        "updatedAt": updatedAt?.toIso8601String(),
    };
}

enum Status {
    ACTIVE,
    INVITED,
    LEFT,
    SUSPENDED
}

final statusValues = EnumValues({
    "active": Status.ACTIVE,
    "invited": Status.INVITED,
    "left": Status.LEFT,
    "suspended": Status.SUSPENDED
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