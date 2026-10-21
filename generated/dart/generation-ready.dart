// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final generationReady = generationReadyFromJson(jsonString);

import 'dart:convert';

GenerationReady generationReadyFromJson(String str) => GenerationReady.fromJson(json.decode(str));

String generationReadyToJson(GenerationReady data) => json.encode(data.toJson());


///Content was written and is handed over in full. The one result that carries the work
///itself rather than a reference to it: the asking system has no database of generations to
///read it back from. Keys are snake_case, not the camelCase the rest of leaf uses: this
///travels inside a Liquid envelope, whose own fields (event_id, occurred_at, event_type,
///owner_unit_ref) are snake_case and pinned byte-exact by signed golden vectors. The shape
///follows the wire.
class GenerationReady {
    
    ///The generation that was made.
    String contentId;
    
    ///The text, as written.
    String output;
    
    ///What the pipeline thought of its own output. Absent when nothing scored it, which is not
    ///the same as a score of zero.
    double? overallScore;
    
    ///The working session it was made in.
    String sessionId;
    
    ///The assets it was written from, by id.
    List<String>? sourceAssets;
    
    ///Which template it was written from.
    String template;

    GenerationReady({
        required this.contentId,
        required this.output,
        this.overallScore,
        required this.sessionId,
        this.sourceAssets,
        required this.template,
    });

    factory GenerationReady.fromJson(Map<String, dynamic> json) => GenerationReady(
        contentId: json["content_id"],
        output: json["output"],
        overallScore: json["overall_score"]?.toDouble(),
        sessionId: json["session_id"],
        sourceAssets: json["source_assets"] == null ? [] : List<String>.from(json["source_assets"]!.map((x) => x)),
        template: json["template"],
    );

    Map<String, dynamic> toJson() => {
        "content_id": contentId,
        "output": output,
        "overall_score": overallScore,
        "session_id": sessionId,
        "source_assets": sourceAssets == null ? [] : List<dynamic>.from(sourceAssets!.map((x) => x)),
        "template": template,
    };
}