// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final notice = noticeFromJson(jsonString);

import 'dart:convert';

Notice noticeFromJson(String str) => Notice.fromJson(json.decode(str));

String noticeToJson(Notice data) => json.encode(data.toJson());


///A link somebody put out — a video, a magazine, a product — and one line about it. A
///pointer, never content: the system that holds the link holds what it says, and whoever
///carries the notice only says that the link exists and when.
class Notice {
    
    ///The wallet, handle, or id under localIds of whoever put the link out.
    String by;
    
    ///When the notice was recorded, which is not when the link was published.
    DateTime? createdAt;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///One line about it, in the words of whoever put it out. Read by a person; never fetched
    ///from the link.
    String? line;
    
    ///Where the link goes. https, so a page vouching for it can hand it to a machine.
    String url;

    Notice({
        required this.by,
        this.createdAt,
        this.id,
        this.line,
        required this.url,
    });

    factory Notice.fromJson(Map<String, dynamic> json) => Notice(
        by: json["by"],
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        id: json["id"],
        line: json["line"],
        url: json["url"],
    );

    Map<String, dynamic> toJson() => {
        "by": by,
        "createdAt": createdAt?.toIso8601String(),
        "id": id,
        "line": line,
        "url": url,
    };
}