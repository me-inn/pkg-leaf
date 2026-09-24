// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final request = requestFromJson(jsonString);

import 'dart:convert';

Request requestFromJson(String str) => Request.fromJson(json.decode(str));

String requestToJson(Request data) => json.encode(data.toJson());


///Somebody asking somebody else for a time. A request, not a booking: it records what was
///asked, never that a slot is taken.
class Request {
    DateTime? answeredAt;
    
    ///How to reach whoever asked, so an answer can get back to them.
    List<ContactPoint>? contacts;
    DateTime? createdAt;
    
    ///The wallet or local id of whoever is asking, when they have one. Absent for somebody with
    ///no account anywhere.
    String? from;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///Who is asking, as they gave it. Unverified, and read by a person.
    String? requester;
    
    ///An answer is final. A second answer does not change the first.
    State? state;
    
    ///The wallet, handle, or id under localIds of whoever is being asked.
    String to;
    
    ///When they want, in their own words. Not a timestamp: a parsed date is a claim about a
    ///timezone and a working hour, and a person reading the words cannot misread them.
    String wanted;

    Request({
        this.answeredAt,
        this.contacts,
        this.createdAt,
        this.from,
        this.id,
        this.requester,
        this.state,
        required this.to,
        required this.wanted,
    });

    factory Request.fromJson(Map<String, dynamic> json) => Request(
        answeredAt: json["answeredAt"] == null ? null : DateTime.parse(json["answeredAt"]),
        contacts: json["contacts"] == null ? [] : List<ContactPoint>.from(json["contacts"]!.map((x) => ContactPoint.fromJson(x))),
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        from: json["from"],
        id: json["id"],
        requester: json["requester"],
        state: stateValues.map[json["state"]],
        to: json["to"],
        wanted: json["wanted"],
    );

    Map<String, dynamic> toJson() => {
        "answeredAt": answeredAt?.toIso8601String(),
        "contacts": contacts == null ? [] : List<dynamic>.from(contacts!.map((x) => x.toJson())),
        "createdAt": createdAt?.toIso8601String(),
        "from": from,
        "id": id,
        "requester": requester,
        "state": stateValues.reverse[state],
        "to": to,
        "wanted": wanted,
    };
}


///One way to reach an actor.
class ContactPoint {
    
    ///The language to write to this point in.
    Locale? locale;
    
    ///Which channel the value is for.
    Type type;
    
    ///An address, or a number in E.164 digits including the country code.
    String value;
    bool? verified;
    DateTime? verifiedAt;

    ContactPoint({
        this.locale,
        required this.type,
        required this.value,
        this.verified,
        this.verifiedAt,
    });

    factory ContactPoint.fromJson(Map<String, dynamic> json) => ContactPoint(
        locale: localeValues.map[json["locale"]],
        type: typeValues.map[json["type"]]!,
        value: json["value"],
        verified: json["verified"],
        verifiedAt: json["verifiedAt"] == null ? null : DateTime.parse(json["verifiedAt"]),
    );

    Map<String, dynamic> toJson() => {
        "locale": localeValues.reverse[locale],
        "type": typeValues.reverse[type],
        "value": value,
        "verified": verified,
        "verifiedAt": verifiedAt?.toIso8601String(),
    };
}


///The language to write to this point in.
enum Locale {
    EN,
    ES,
    PT
}

final localeValues = EnumValues({
    "en": Locale.EN,
    "es": Locale.ES,
    "pt": Locale.PT
});


///Which channel the value is for.
enum Type {
    EMAIL,
    MOBILE,
    PHONE,
    WHATSAPP
}

final typeValues = EnumValues({
    "email": Type.EMAIL,
    "mobile": Type.MOBILE,
    "phone": Type.PHONE,
    "whatsapp": Type.WHATSAPP
});


///An answer is final. A second answer does not change the first.
enum State {
    CONFIRMED,
    DECLINED,
    PENDING
}

final stateValues = EnumValues({
    "confirmed": State.CONFIRMED,
    "declined": State.DECLINED,
    "pending": State.PENDING
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