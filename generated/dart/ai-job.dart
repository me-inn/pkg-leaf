// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final aiJob = aiJobFromJson(jsonString);

import 'dart:convert';

AiJob aiJobFromJson(String str) => AiJob.fromJson(json.decode(str));

String aiJobToJson(AiJob data) => json.encode(data.toJson());


///A short-lived record of an asynchronous model call — a generation, a retrieval answer, an
///edit, a repurpose. Separate from job: a job is work done to one asset and reports timing,
///this is work asked for inside a session and reports an answer. The two are kept apart
///rather than merged behind a discriminator because they do not agree on what is required
///or on what is kept.
class AiJob {
    
    ///When the call was queued.
    DateTime? createdAt;
    
    ///What went wrong, as the worker reported it. Read by a person; never parsed.
    String? errorMessage;
    
    ///The record's own id in the system that holds it. It is what the caller polls with.
    String? id;
    
    ///Which kind of call was asked for. Free text: the vocabulary belongs to whoever queues the
    ///job, and it grows every time a new flow is added.
    String jobType;
    
    ///What came back, in the shape the job type produces. Left open on purpose: a repurpose
    ///result and a retrieval answer have nothing in common, and declaring one shape for both
    ///would describe neither.
    Map<String, dynamic>? result;
    
    ///The session the job was asked for, as the system that owns the session names it. It is
    ///what keeps one session from reading another's answer. Absent on rows written before jobs
    ///were scoped.
    String? session;
    
    ///Where the call got to. Free text here, unlike job: the column carries no enum and each
    ///flow writes its own words.
    String status;

    AiJob({
        this.createdAt,
        this.errorMessage,
        this.id,
        required this.jobType,
        this.result,
        this.session,
        required this.status,
    });

    factory AiJob.fromJson(Map<String, dynamic> json) => AiJob(
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        errorMessage: json["errorMessage"],
        id: json["id"],
        jobType: json["jobType"],
        result: Map.from(json["result"]!).map((k, v) => MapEntry<String, dynamic>(k, v)),
        session: json["session"],
        status: json["status"],
    );

    Map<String, dynamic> toJson() => {
        "createdAt": createdAt?.toIso8601String(),
        "errorMessage": errorMessage,
        "id": id,
        "jobType": jobType,
        "result": Map.from(result!).map((k, v) => MapEntry<String, dynamic>(k, v)),
        "session": session,
        "status": status,
    };
}