// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final job = jobFromJson(jsonString);

import 'dart:convert';

Job jobFromJson(String str) => Job.fromJson(json.decode(str));

String jobToJson(Job data) => json.encode(data.toJson());


///A piece of work the pipeline does to one asset: ingest it, read it, index it. The job is
///the record of the attempt — when it started, when it stopped, and what went wrong — never
///the work's output, which belongs to the asset it was done to.
class Job {
    
    ///The asset being worked on, as the system that owns the asset names it. A job without one
    ///is not a job: there is nothing to process.
    String asset;
    
    ///When the job was queued.
    DateTime? createdAt;
    
    ///What went wrong, as the worker reported it. Read by a person deciding whether to retry;
    ///never parsed.
    String? errorMessage;
    
    ///When it stopped, whether it succeeded or failed. Absent while it runs.
    DateTime? finishedAt;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///When a worker picked it up, which is not when it was queued. Absent while it waits.
    DateTime? startedAt;
    
    ///Where the attempt got to. A closed vocabulary because the pipeline branches on it, and
    ///the same one the asset carries.
    ProcessingStatus status;

    Job({
        required this.asset,
        this.createdAt,
        this.errorMessage,
        this.finishedAt,
        this.id,
        this.startedAt,
        required this.status,
    });

    factory Job.fromJson(Map<String, dynamic> json) => Job(
        asset: json["asset"],
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        errorMessage: json["errorMessage"],
        finishedAt: json["finishedAt"] == null ? null : DateTime.parse(json["finishedAt"]),
        id: json["id"],
        startedAt: json["startedAt"] == null ? null : DateTime.parse(json["startedAt"]),
        status: processingStatusValues.map[json["status"]]!,
    );

    Map<String, dynamic> toJson() => {
        "asset": asset,
        "createdAt": createdAt?.toIso8601String(),
        "errorMessage": errorMessage,
        "finishedAt": finishedAt?.toIso8601String(),
        "id": id,
        "startedAt": startedAt?.toIso8601String(),
        "status": processingStatusValues.reverse[status],
    };
}


///Where the attempt got to. A closed vocabulary because the pipeline branches on it, and
///the same one the asset carries.
///
///Where a pipeline stands on the thing it was given. Which move from which is a rule held
///beside the type, never in it.
enum ProcessingStatus {
    COMPLETED,
    FAILED,
    PENDING,
    PROCESSING
}

final processingStatusValues = EnumValues({
    "completed": ProcessingStatus.COMPLETED,
    "failed": ProcessingStatus.FAILED,
    "pending": ProcessingStatus.PENDING,
    "processing": ProcessingStatus.PROCESSING
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