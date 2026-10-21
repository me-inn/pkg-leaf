// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final generationRequested = generationRequestedFromJson(jsonString);

import 'dart:convert';

GenerationRequested generationRequestedFromJson(String str) => GenerationRequested.fromJson(json.decode(str));

String generationRequestedToJson(GenerationRequested data) => json.encode(data.toJson());


///A piece of content somebody wants written. What to write is in the job, not in the event.
///Keys are snake_case, not the camelCase the rest of leaf uses: this travels inside a
///Liquid envelope, whose own fields (event_id, occurred_at, event_type, owner_unit_ref) are
///snake_case and pinned byte-exact by signed golden vectors. The shape follows the wire.
class GenerationRequested {
    
    ///The job holding the template, the sources and everything else the generation needs.
    String jobId;

    GenerationRequested({
        required this.jobId,
    });

    factory GenerationRequested.fromJson(Map<String, dynamic> json) => GenerationRequested(
        jobId: json["job_id"],
    );

    Map<String, dynamic> toJson() => {
        "job_id": jobId,
    };
}