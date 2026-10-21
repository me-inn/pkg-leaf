// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final book = bookFromJson(jsonString);

import 'dart:convert';

Book bookFromJson(String str) => Book.fromJson(json.decode(str));

String bookToJson(Book data) => json.encode(data.toJson());


///A long-form title somebody is writing: what it is about, how far along it is, and where
///its cover sits. The chapters are not inside it — each is its own record pointing back, so
///a book can be read without carrying its whole text.
class Book {
    
    ///The model that helped write it, named as the system that called it names it. Absent when
    ///nothing was asked of one.
    String? aiModel;
    
    ///The wallet, handle, or id under localIds of whoever is writing it. Absent while the title
    ///belongs to nobody yet.
    String? author;
    
    ///The cover image, where it is kept. Absent while the title has none.
    StoredFile? cover;
    
    ///The brief the cover image was asked for with. Kept because the image can be asked for
    ///again.
    String? coverPrompt;
    DateTime? createdAt;
    
    ///Words written so far across the chapters. Counted by whoever holds the text, carried here
    ///so a reader of the book alone can say how far along it is.
    int? currentWordCount;
    
    ///What the book is about, in the words of whoever is writing it. Written for a reader
    ///deciding, not for a catalogue.
    String? description;
    
    ///The shelf it belongs on. A closed list because it decides how the title is filed, not how
    ///it reads.
    Genre genre;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///The BISAC subject code given to the store, such as FIC000000. Separate from genre: one is
    ///ours, this one is the trade's.
    String? kdpBisac;
    
    ///The keywords the title is listed under on the store. Free text, in the words of whoever
    ///sells it.
    List<String>? kdpKeywords;
    
    ///The language the book is written in, as a BCP 47 tag such as pt, en or pt-BR.
    String? language;
    
    ///The id of the working session the book was started from, in the system that holds that
    ///session. Absent when it was not started from one.
    String? session;
    
    ///How far along it is. Which move from which is a rule held beside the type, never in it.
    Status? status;
    
    ///The line under the title, when there is one.
    String? subtitle;
    
    ///The length being aimed at, set by whoever is writing. Zero while no target was chosen.
    int? targetWordCount;
    
    ///The title on the cover.
    String title;
    DateTime? updatedAt;

    Book({
        this.aiModel,
        this.author,
        this.cover,
        this.coverPrompt,
        this.createdAt,
        this.currentWordCount,
        this.description,
        required this.genre,
        this.id,
        this.kdpBisac,
        this.kdpKeywords,
        this.language,
        this.session,
        this.status,
        this.subtitle,
        this.targetWordCount,
        required this.title,
        this.updatedAt,
    });

    factory Book.fromJson(Map<String, dynamic> json) => Book(
        aiModel: json["aiModel"],
        author: json["author"],
        cover: json["cover"] == null ? null : StoredFile.fromJson(json["cover"]),
        coverPrompt: json["coverPrompt"],
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        currentWordCount: json["currentWordCount"],
        description: json["description"],
        genre: genreValues.map[json["genre"]]!,
        id: json["id"],
        kdpBisac: json["kdpBisac"],
        kdpKeywords: json["kdpKeywords"] == null ? [] : List<String>.from(json["kdpKeywords"]!.map((x) => x)),
        language: json["language"],
        session: json["session"],
        status: statusValues.map[json["status"]],
        subtitle: json["subtitle"],
        targetWordCount: json["targetWordCount"],
        title: json["title"],
        updatedAt: json["updatedAt"] == null ? null : DateTime.parse(json["updatedAt"]),
    );

    Map<String, dynamic> toJson() => {
        "aiModel": aiModel,
        "author": author,
        "cover": cover?.toJson(),
        "coverPrompt": coverPrompt,
        "createdAt": createdAt?.toIso8601String(),
        "currentWordCount": currentWordCount,
        "description": description,
        "genre": genreValues.reverse[genre],
        "id": id,
        "kdpBisac": kdpBisac,
        "kdpKeywords": kdpKeywords == null ? [] : List<dynamic>.from(kdpKeywords!.map((x) => x)),
        "language": language,
        "session": session,
        "status": statusValues.reverse[status],
        "subtitle": subtitle,
        "targetWordCount": targetWordCount,
        "title": title,
        "updatedAt": updatedAt?.toIso8601String(),
    };
}


///The cover image, where it is kept. Absent while the title has none.
///
///Bytes somebody is keeping, pointed at rather than carried. Never the file itself: the
///store that holds it holds it, and this says which key to ask under and, while it lasts,
///where it can be fetched. Nothing is required, because a file can be known by its key
///before any address has been issued for it, and served by an address before anybody
///recorded a key.
class StoredFile {
    
    ///How big it is, so whoever is about to fetch it knows what they are asking for.
    int? sizeBytes;
    
    ///Where the bytes sit in the store that holds them. The lasting handle, meaningful only to
    ///that store: a reader asks the store, never resolves the key itself.
    String? storageKey;
    
    ///Where the file can be fetched right now. Often signed and short-lived, so it is read at
    ///the moment of use and never kept as the address of the file.
    String? url;

    StoredFile({
        this.sizeBytes,
        this.storageKey,
        this.url,
    });

    factory StoredFile.fromJson(Map<String, dynamic> json) => StoredFile(
        sizeBytes: json["sizeBytes"],
        storageKey: json["storageKey"],
        url: json["url"],
    );

    Map<String, dynamic> toJson() => {
        "sizeBytes": sizeBytes,
        "storageKey": storageKey,
        "url": url,
    };
}


///The shelf it belongs on. A closed list because it decides how the title is filed, not how
///it reads.
enum Genre {
    ACADEMIC,
    BIOGRAPHY,
    BUSINESS,
    CHILDREN,
    FANTASY,
    FICTION,
    HISTORICAL,
    HORROR,
    NON_FICTION,
    OTHER,
    POETRY,
    ROMANCE,
    SCIENCE_FICTION,
    SELF_HELP,
    THRILLER,
    YOUNG_ADULT
}

final genreValues = EnumValues({
    "academic": Genre.ACADEMIC,
    "biography": Genre.BIOGRAPHY,
    "business": Genre.BUSINESS,
    "children": Genre.CHILDREN,
    "fantasy": Genre.FANTASY,
    "fiction": Genre.FICTION,
    "historical": Genre.HISTORICAL,
    "horror": Genre.HORROR,
    "non_fiction": Genre.NON_FICTION,
    "other": Genre.OTHER,
    "poetry": Genre.POETRY,
    "romance": Genre.ROMANCE,
    "science_fiction": Genre.SCIENCE_FICTION,
    "self_help": Genre.SELF_HELP,
    "thriller": Genre.THRILLER,
    "young_adult": Genre.YOUNG_ADULT
});


///How far along it is. Which move from which is a rule held beside the type, never in it.
enum Status {
    APPROVED,
    DRAFT,
    PUBLISHED,
    REVIEW,
    WRITING
}

final statusValues = EnumValues({
    "approved": Status.APPROVED,
    "draft": Status.DRAFT,
    "published": Status.PUBLISHED,
    "review": Status.REVIEW,
    "writing": Status.WRITING
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