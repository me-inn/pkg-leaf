// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final valueSnapshot = valueSnapshotFromJson(jsonString);

import 'dart:convert';

ValueSnapshot valueSnapshotFromJson(String str) => ValueSnapshot.fromJson(json.decode(str));

String valueSnapshotToJson(ValueSnapshot data) => json.encode(data.toJson());


///What something was worth over a stretch of time — a score, or a person saying yes or no
///to a generation. A reading taken, never a running total: two snapshots of the same thing
///are both true of their own window. Keys are snake_case, not the camelCase the rest of
///leaf uses: this travels inside a Liquid envelope, whose own fields (event_id,
///occurred_at, event_type, owner_unit_ref) are snake_case and pinned byte-exact by signed
///golden vectors. The shape follows the wire.
class ValueSnapshot {
    
    ///What was scored.
    String contentId;
    
    ///The working session it was taken in.
    String sessionId;
    
    ///The reading, normalised. A thumb up is 1 and a thumb down is 0; what any other number
    ///means belongs to whoever took it.
    double value;
    
    ///End of the stretch the reading covers.
    DateTime windowEnd;
    
    ///Start of the stretch the reading covers. Equal to the end for a reading of one moment,
    ///such as a thumb.
    DateTime windowStart;

    ValueSnapshot({
        required this.contentId,
        required this.sessionId,
        required this.value,
        required this.windowEnd,
        required this.windowStart,
    });

    factory ValueSnapshot.fromJson(Map<String, dynamic> json) => ValueSnapshot(
        contentId: json["content_id"],
        sessionId: json["session_id"],
        value: json["value"]?.toDouble(),
        windowEnd: DateTime.parse(json["window_end"]),
        windowStart: DateTime.parse(json["window_start"]),
    );

    Map<String, dynamic> toJson() => {
        "content_id": contentId,
        "session_id": sessionId,
        "value": value,
        "window_end": windowEnd.toIso8601String(),
        "window_start": windowStart.toIso8601String(),
    };
}