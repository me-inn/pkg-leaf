// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final chapterRevision = chapterRevisionFromJson(jsonString);

import 'dart:convert';

ChapterRevision chapterRevisionFromJson(String str) => ChapterRevision.fromJson(json.decode(str));

String chapterRevisionToJson(ChapterRevision data) => json.encode(data.toJson());


///A chapter's text as it stood at one moment, kept whole rather than as a difference, so an
///old version reads without replaying the ones after it.
class ChapterRevision {
    
    ///The wallet, handle, or id under localIds of whoever made the change. Absent when it was
    ///made by software rather than a person.
    String? changedBy;
    
    ///One line on what changed, so a list of revisions can be read without opening each.
    String? changeSummary;
    
    ///What kind of change it was. Free text: the vocabulary belongs to the system that writes
    ///the revision.
    String? changeType;
    
    ///The id of the chapter this is a revision of, in the system that holds the chapter.
    String chapter;
    
    ///The whole text as it stood, not a difference against the one before.
    String content;
    
    ///When the revision was written down.
    DateTime? createdAt;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///Which revision of that chapter this is, counting up. Ordering comes from this and not
    ///from the clock, because two writes can land in the same second.
    int version;
    
    ///Words in this revision's text.
    int? wordCount;

    ChapterRevision({
        this.changedBy,
        this.changeSummary,
        this.changeType,
        required this.chapter,
        required this.content,
        this.createdAt,
        this.id,
        required this.version,
        this.wordCount,
    });

    factory ChapterRevision.fromJson(Map<String, dynamic> json) => ChapterRevision(
        changedBy: json["changedBy"],
        changeSummary: json["changeSummary"],
        changeType: json["changeType"],
        chapter: json["chapter"],
        content: json["content"],
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        id: json["id"],
        version: json["version"],
        wordCount: json["wordCount"],
    );

    Map<String, dynamic> toJson() => {
        "changedBy": changedBy,
        "changeSummary": changeSummary,
        "changeType": changeType,
        "chapter": chapter,
        "content": content,
        "createdAt": createdAt?.toIso8601String(),
        "id": id,
        "version": version,
        "wordCount": wordCount,
    };
}