// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final publication = publicationFromJson(jsonString);

import 'dart:convert';

Publication publicationFromJson(String str) => Publication.fromJson(json.decode(str));

String publicationToJson(Publication data) => json.encode(data.toJson());


///A book put out on one store, and what that store calls it. An edge between a title and a
///platform: the same book on three stores is three of these, each with its own listing, its
///own state and its own rate.
class Publication {
    
    ///The id of the book being put out, in the system that holds the book.
    String book;
    DateTime? createdAt;
    
    ///What this listing is expected to pay in a month, in the currency the store settles in. An
    ///estimate carried for planning, never an amount owed.
    double? estimatedMonthlyRoyalty;
    
    ///What the store calls this listing — its ASIN, its product id. The only handle the store
    ///will answer to.
    String? externalId;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///The page a reader buys it on.
    String? listingUrl;
    
    ///Anything about this listing worth writing down, in the words of whoever put it out.
    String? notes;
    
    ///Where it is being put out. Manual is for a channel nobody here talks to, recorded so the
    ///title's whereabouts stay complete.
    Platform platform;
    
    ///When the listing went live on the store.
    DateTime? publishedAt;
    
    ///The author's share, as a fraction: 0.7 is seventy per cent. A fraction and not a
    ///percentage so nobody has to guess which was meant.
    double? royaltyRate;
    
    ///Where the listing stands on that store. Read from the store, not decided here.
    Status? status;
    
    ///When it was sent to the store, which is not when the store accepted it.
    DateTime? submittedAt;
    DateTime? updatedAt;

    Publication({
        required this.book,
        this.createdAt,
        this.estimatedMonthlyRoyalty,
        this.externalId,
        this.id,
        this.listingUrl,
        this.notes,
        required this.platform,
        this.publishedAt,
        this.royaltyRate,
        this.status,
        this.submittedAt,
        this.updatedAt,
    });

    factory Publication.fromJson(Map<String, dynamic> json) => Publication(
        book: json["book"],
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        estimatedMonthlyRoyalty: json["estimatedMonthlyRoyalty"]?.toDouble(),
        externalId: json["externalId"],
        id: json["id"],
        listingUrl: json["listingUrl"],
        notes: json["notes"],
        platform: platformValues.map[json["platform"]]!,
        publishedAt: json["publishedAt"] == null ? null : DateTime.parse(json["publishedAt"]),
        royaltyRate: json["royaltyRate"]?.toDouble(),
        status: statusValues.map[json["status"]],
        submittedAt: json["submittedAt"] == null ? null : DateTime.parse(json["submittedAt"]),
        updatedAt: json["updatedAt"] == null ? null : DateTime.parse(json["updatedAt"]),
    );

    Map<String, dynamic> toJson() => {
        "book": book,
        "createdAt": createdAt?.toIso8601String(),
        "estimatedMonthlyRoyalty": estimatedMonthlyRoyalty,
        "externalId": externalId,
        "id": id,
        "listingUrl": listingUrl,
        "notes": notes,
        "platform": platformValues.reverse[platform],
        "publishedAt": publishedAt?.toIso8601String(),
        "royaltyRate": royaltyRate,
        "status": statusValues.reverse[status],
        "submittedAt": submittedAt?.toIso8601String(),
        "updatedAt": updatedAt?.toIso8601String(),
    };
}


///Where it is being put out. Manual is for a channel nobody here talks to, recorded so the
///title's whereabouts stay complete.
enum Platform {
    AMAZON_KDP,
    APPLE_BOOKS,
    GOOGLE_PLAY,
    KOBO,
    MANUAL
}

final platformValues = EnumValues({
    "amazon_kdp": Platform.AMAZON_KDP,
    "apple_books": Platform.APPLE_BOOKS,
    "google_play": Platform.GOOGLE_PLAY,
    "kobo": Platform.KOBO,
    "manual": Platform.MANUAL
});


///Where the listing stands on that store. Read from the store, not decided here.
enum Status {
    DRAFT,
    LIVE,
    REJECTED,
    SUBMITTED,
    UNPUBLISHED
}

final statusValues = EnumValues({
    "draft": Status.DRAFT,
    "live": Status.LIVE,
    "rejected": Status.REJECTED,
    "submitted": Status.SUBMITTED,
    "unpublished": Status.UNPUBLISHED
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