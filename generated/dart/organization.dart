// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final organization = organizationFromJson(jsonString);

import 'dart:convert';

Organization organizationFromJson(String str) => Organization.fromJson(json.decode(str));

String organizationToJson(Organization data) => json.encode(data.toJson());


///An organisation.
class Organization {
    
    ///Ways to reach it.
    List<ContactPoint>? contacts;
    
    ///ISO 3166-1 alpha-2 country of registration.
    String? country;
    DateTime? createdAt;
    
    ///The name it is known by.
    String displayName;
    bool? isActive;
    
    ///The name it is registered under.
    String? legalName;
    
    ///The id this organisation has in each system that holds a record of it.
    Map<String, String>? localIds;
    
    ///URL-safe handle, lowercase.
    String? slug;
    
    ///Its tax or registry identifiers, one per scheme.
    List<TaxIdentifier>? taxIds;
    DateTime? updatedAt;
    
    ///ed25519 public key, hex. Identifies the organisation. Absent until it holds one.
    String? wallet;
    String? website;

    Organization({
        this.contacts,
        this.country,
        this.createdAt,
        required this.displayName,
        this.isActive,
        this.legalName,
        this.localIds,
        this.slug,
        this.taxIds,
        this.updatedAt,
        this.wallet,
        this.website,
    });

    factory Organization.fromJson(Map<String, dynamic> json) => Organization(
        contacts: json["contacts"] == null ? [] : List<ContactPoint>.from(json["contacts"]!.map((x) => ContactPoint.fromJson(x))),
        country: json["country"],
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        displayName: json["displayName"],
        isActive: json["isActive"],
        legalName: json["legalName"],
        localIds: Map.from(json["localIds"]!).map((k, v) => MapEntry<String, String>(k, v)),
        slug: json["slug"],
        taxIds: json["taxIds"] == null ? [] : List<TaxIdentifier>.from(json["taxIds"]!.map((x) => TaxIdentifier.fromJson(x))),
        updatedAt: json["updatedAt"] == null ? null : DateTime.parse(json["updatedAt"]),
        wallet: json["wallet"],
        website: json["website"],
    );

    Map<String, dynamic> toJson() => {
        "contacts": contacts == null ? [] : List<dynamic>.from(contacts!.map((x) => x.toJson())),
        "country": country,
        "createdAt": createdAt?.toIso8601String(),
        "displayName": displayName,
        "isActive": isActive,
        "legalName": legalName,
        "localIds": Map.from(localIds!).map((k, v) => MapEntry<String, dynamic>(k, v)),
        "slug": slug,
        "taxIds": taxIds == null ? [] : List<dynamic>.from(taxIds!.map((x) => x.toJson())),
        "updatedAt": updatedAt?.toIso8601String(),
        "wallet": wallet,
        "website": website,
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