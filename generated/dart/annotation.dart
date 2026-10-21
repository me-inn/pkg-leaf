// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final annotation = annotationFromJson(jsonString);

import 'dart:convert';

Annotation annotationFromJson(String str) => Annotation.fromJson(json.decode(str));

String annotationToJson(Annotation data) => json.encode(data.toJson());


///A note somebody left on a book, and where in the text they left it. The note is the
///record; the passage it points at stays in the chapter, quoted here only so the note still
///reads once the text around it has moved.
class Annotation {
    
    ///Where the passage ends, counted the same way.
    int? anchorEnd;
    
    ///Where the passage starts in the chapter text, counted in characters from the beginning.
    ///Valid against the revision that was open at the time.
    int? anchorStart;
    
    ///What kind of remark it is, which decides who it is addressed to: a todo waits on the
    ///author, a beta_feedback came from a reader, an ai_suggestion was not written by a person
    ///at all.
    AnnotationType annotationType;
    
    ///The id of the book it was left on, in the system that owns it.
    String book;
    
    ///The id of the chapter it was left on, in the system that owns it. Absent for a note about
    ///the book as a whole.
    String? chapter;
    DateTime? createdAt;
    
    ///The wallet, handle, or id under localIds of whoever left it. Absent for a note no person
    ///wrote.
    String? createdBy;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///What they wrote.
    String note;
    
    ///Whether the note has been dealt with. It stays on the record once resolved; nothing here
    ///is removed by being answered.
    bool resolved;
    
    ///The passage as it read when the note was made. Kept verbatim because the anchors drift
    ///once the chapter is edited, and the quote is what survives that.
    String? textSelection;

    Annotation({
        this.anchorEnd,
        this.anchorStart,
        required this.annotationType,
        required this.book,
        this.chapter,
        this.createdAt,
        this.createdBy,
        this.id,
        required this.note,
        required this.resolved,
        this.textSelection,
    });

    factory Annotation.fromJson(Map<String, dynamic> json) => Annotation(
        anchorEnd: json["anchorEnd"],
        anchorStart: json["anchorStart"],
        annotationType: annotationTypeValues.map[json["annotationType"]]!,
        book: json["book"],
        chapter: json["chapter"],
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        createdBy: json["createdBy"],
        id: json["id"],
        note: json["note"],
        resolved: json["resolved"],
        textSelection: json["textSelection"],
    );

    Map<String, dynamic> toJson() => {
        "anchorEnd": anchorEnd,
        "anchorStart": anchorStart,
        "annotationType": annotationTypeValues.reverse[annotationType],
        "book": book,
        "chapter": chapter,
        "createdAt": createdAt?.toIso8601String(),
        "createdBy": createdBy,
        "id": id,
        "note": note,
        "resolved": resolved,
        "textSelection": textSelection,
    };
}


///What kind of remark it is, which decides who it is addressed to: a todo waits on the
///author, a beta_feedback came from a reader, an ai_suggestion was not written by a person
///at all.
enum AnnotationType {
    AI_SUGGESTION,
    BETA_FEEDBACK,
    NOTE,
    QUESTION,
    TODO
}

final annotationTypeValues = EnumValues({
    "ai_suggestion": AnnotationType.AI_SUGGESTION,
    "beta_feedback": AnnotationType.BETA_FEEDBACK,
    "note": AnnotationType.NOTE,
    "question": AnnotationType.QUESTION,
    "todo": AnnotationType.TODO
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