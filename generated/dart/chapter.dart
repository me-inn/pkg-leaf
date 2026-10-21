// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final chapter = chapterFromJson(jsonString);

import 'dart:convert';

Chapter chapterFromJson(String str) => Chapter.fromJson(json.decode(str));

String chapterToJson(Chapter data) => json.encode(data.toJson());


///One chapter of a book: its place in the running order and the text as it stands now.
///Earlier states of that text are revisions, each its own record.
class Chapter {
    
    ///The id of the book this chapter belongs to, in the system that holds the book.
    String book;
    
    ///The text as it stands now. Empty while the chapter is only a heading.
    String? content;
    DateTime? createdAt;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///Where it falls in the running order. The number the chapters are sorted by, not the
    ///number printed on the page.
    int? order;
    
    ///How far along this chapter is, which moves on its own and not with the book's.
    Status? status;
    
    ///What happens in it, in a few lines. Written so the chapter can be reasoned about without
    ///reading it whole.
    String? summary;
    
    ///The chapter heading.
    String title;
    DateTime? updatedAt;
    
    ///Words in the current text, counted by whoever holds it.
    int? wordCount;

    Chapter({
        required this.book,
        this.content,
        this.createdAt,
        this.id,
        this.order,
        this.status,
        this.summary,
        required this.title,
        this.updatedAt,
        this.wordCount,
    });

    factory Chapter.fromJson(Map<String, dynamic> json) => Chapter(
        book: json["book"],
        content: json["content"],
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        id: json["id"],
        order: json["order"],
        status: statusValues.map[json["status"]],
        summary: json["summary"],
        title: json["title"],
        updatedAt: json["updatedAt"] == null ? null : DateTime.parse(json["updatedAt"]),
        wordCount: json["wordCount"],
    );

    Map<String, dynamic> toJson() => {
        "book": book,
        "content": content,
        "createdAt": createdAt?.toIso8601String(),
        "id": id,
        "order": order,
        "status": statusValues.reverse[status],
        "summary": summary,
        "title": title,
        "updatedAt": updatedAt?.toIso8601String(),
        "wordCount": wordCount,
    };
}


///How far along this chapter is, which moves on its own and not with the book's.
enum Status {
    APPROVED,
    DRAFT,
    REVIEW,
    WRITING
}

final statusValues = EnumValues({
    "approved": Status.APPROVED,
    "draft": Status.DRAFT,
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