// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final repurposeReady = repurposeReadyFromJson(jsonString);

import 'dart:convert';

RepurposeReady repurposeReadyFromJson(String str) => RepurposeReady.fromJson(json.decode(str));

String repurposeReadyToJson(RepurposeReady data) => json.encode(data.toJson());


///The shorter pieces were written and are handed over in full, for the same reason a
///generation is. Keys are snake_case, not the camelCase the rest of leaf uses: this travels
///inside a Liquid envelope, whose own fields (event_id, occurred_at, event_type,
///owner_unit_ref) are snake_case and pinned byte-exact by signed golden vectors. The shape
///follows the wire.
class RepurposeReady {
    
    ///What came out, keyed by the format that was asked for — hooks, captions, and the rest. A
    ///format that was asked for and produced nothing is simply not here.
    Map<String, String> formats;
    
    ///The job the work was done under, which is what the asker was waiting on.
    String jobId;
    
    ///The working session it was done in.
    String sessionId;

    RepurposeReady({
        required this.formats,
        required this.jobId,
        required this.sessionId,
    });

    factory RepurposeReady.fromJson(Map<String, dynamic> json) => RepurposeReady(
        formats: Map.from(json["formats"]).map((k, v) => MapEntry<String, String>(k, v)),
        jobId: json["job_id"],
        sessionId: json["session_id"],
    );

    Map<String, dynamic> toJson() => {
        "formats": Map.from(formats).map((k, v) => MapEntry<String, dynamic>(k, v)),
        "job_id": jobId,
        "session_id": sessionId,
    };
}