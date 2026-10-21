// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final bookExport = bookExportFromJson(jsonString);

import 'dart:convert';

BookExport bookExportFromJson(String str) => BookExport.fromJson(json.decode(str));

String bookExportToJson(BookExport data) => json.encode(data.toJson());


///One rendering of a book into a file somebody can hand over — a pdf, an epub, a docx. A
///pointer and a state, never the file: the bytes live in the store that rendered them, and
///this says which store, under which key, and whether it finished.
class BookExport {
    
    ///The id of the book that was rendered, in the system that holds the book.
    String book;
    
    ///When the rendering finished, whether it succeeded or failed.
    DateTime? completedAt;
    
    ///When the export was asked for, which is not when the file was ready.
    DateTime? createdAt;
    
    ///Why the rendering failed, in the words of whoever rendered it. Present only when it did.
    String? errorMessage;
    
    ///The rendered file, where it is kept and how big it is. Absent until the rendering says
    ///done.
    StoredFile? file;
    
    ///What was rendered. A pdf for reading on a screen and a pdf for a printer are two formats,
    ///not one: the page, the bleed and the margins differ.
    Format format;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///How the rendering went. The file is only there to fetch once this says done.
    Status? status;

    BookExport({
        required this.book,
        this.completedAt,
        this.createdAt,
        this.errorMessage,
        this.file,
        required this.format,
        this.id,
        this.status,
    });

    factory BookExport.fromJson(Map<String, dynamic> json) => BookExport(
        book: json["book"],
        completedAt: json["completedAt"] == null ? null : DateTime.parse(json["completedAt"]),
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        errorMessage: json["errorMessage"],
        file: json["file"] == null ? null : StoredFile.fromJson(json["file"]),
        format: formatValues.map[json["format"]]!,
        id: json["id"],
        status: statusValues.map[json["status"]],
    );

    Map<String, dynamic> toJson() => {
        "book": book,
        "completedAt": completedAt?.toIso8601String(),
        "createdAt": createdAt?.toIso8601String(),
        "errorMessage": errorMessage,
        "file": file?.toJson(),
        "format": formatValues.reverse[format],
        "id": id,
        "status": statusValues.reverse[status],
    };
}


///The rendered file, where it is kept and how big it is. Absent until the rendering says
///done.
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


///What was rendered. A pdf for reading on a screen and a pdf for a printer are two formats,
///not one: the page, the bleed and the margins differ.
enum Format {
    DOCX,
    EPUB,
    PDF_EBOOK,
    PDF_PRINT
}

final formatValues = EnumValues({
    "docx": Format.DOCX,
    "epub": Format.EPUB,
    "pdf_ebook": Format.PDF_EBOOK,
    "pdf_print": Format.PDF_PRINT
});


///How the rendering went. The file is only there to fetch once this says done.
enum Status {
    DONE,
    FAILED,
    PROCESSING,
    QUEUED
}

final statusValues = EnumValues({
    "done": Status.DONE,
    "failed": Status.FAILED,
    "processing": Status.PROCESSING,
    "queued": Status.QUEUED
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