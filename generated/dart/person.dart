// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final person = personFromJson(jsonString);

import 'dart:convert';

Person personFromJson(String str) => Person.fromJson(json.decode(str));

String personToJson(Person data) => json.encode(data.toJson());


///A person. Holds no authentication secret: password hashes, reset tokens and auth
///providers belong to the system that authenticates.
class Person {
    
    ///Ways to reach them.
    List<ContactPoint>? contacts;
    
    ///ISO 3166-1 alpha-2, where they are registered.
    String? country;
    DateTime? createdAt;
    
    ///The name they are known by.
    String displayName;
    
    ///Their public address, without the @.
    String? handle;
    Locale? locale;
    
    ///The id this person has in each system that holds a record of them.
    Map<String, String>? localIds;
    
    ///Their tax or registry identifiers, one per scheme.
    List<TaxIdentifier>? taxIds;
    
    ///ed25519 public key, hex. Identifies the person. Absent until they hold one.
    String? wallet;

    Person({
        this.contacts,
        this.country,
        this.createdAt,
        required this.displayName,
        this.handle,
        this.locale,
        this.localIds,
        this.taxIds,
        this.wallet,
    });

    factory Person.fromJson(Map<String, dynamic> json) => Person(
        contacts: json["contacts"] == null ? [] : List<ContactPoint>.from(json["contacts"]!.map((x) => ContactPoint.fromJson(x))),
        country: json["country"],
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        displayName: json["displayName"],
        handle: json["handle"],
        locale: localeValues.map[json["locale"]],
        localIds: Map.from(json["localIds"]!).map((k, v) => MapEntry<String, String>(k, v)),
        taxIds: json["taxIds"] == null ? [] : List<TaxIdentifier>.from(json["taxIds"]!.map((x) => TaxIdentifier.fromJson(x))),
        wallet: json["wallet"],
    );

    Map<String, dynamic> toJson() => {
        "contacts": contacts == null ? [] : List<dynamic>.from(contacts!.map((x) => x.toJson())),
        "country": country,
        "createdAt": createdAt?.toIso8601String(),
        "displayName": displayName,
        "handle": handle,
        "locale": localeValues.reverse[locale],
        "localIds": Map.from(localIds!).map((k, v) => MapEntry<String, dynamic>(k, v)),
        "taxIds": taxIds == null ? [] : List<dynamic>.from(taxIds!.map((x) => x.toJson())),
        "wallet": wallet,
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


///A tax or registry identifier.
class TaxIdentifier {
    
    ///ISO 3166-1 alpha-2, when the scheme does not imply one.
    String? country;
    
    ///URL of the supporting document.
    String? documentUrl;
    
    ///The scheme, such as CNPJ, CPF, NIF, VAT or EIN. Free text, always stated, never inferred
    ///from the length of the value.
    String type;
    String value;

    TaxIdentifier({
        this.country,
        this.documentUrl,
        required this.type,
        required this.value,
    });

    factory TaxIdentifier.fromJson(Map<String, dynamic> json) => TaxIdentifier(
        country: json["country"],
        documentUrl: json["documentUrl"],
        type: json["type"],
        value: json["value"],
    );

    Map<String, dynamic> toJson() => {
        "country": country,
        "documentUrl": documentUrl,
        "type": type,
        "value": value,
    };
}

class EnumValues<T> {
    Map<String, T> map;
    late Map<T, String> reverseMap;

    EnumValues(this.map);

    Map<T, String> get reverse {
            reverseMap = map.map((k, v) => MapEntry(v, k));
            return reverseMap;
    }
}