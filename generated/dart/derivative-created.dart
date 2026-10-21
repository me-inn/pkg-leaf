// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final derivativeCreated = derivativeCreatedFromJson(jsonString);

import 'dart:convert';

DerivativeCreated derivativeCreatedFromJson(String str) => DerivativeCreated.fromJson(json.decode(str));

String derivativeCreatedToJson(DerivativeCreated data) => json.encode(data.toJson());


///Content was written from assets already put in. The relay understands this type natively,
///which is why it exists beside generation.ready: this one says a derivative was made, that
///one hands over what it says. Keys are snake_case, not the camelCase the rest of leaf
///uses: this travels inside a Liquid envelope, whose own fields (event_id, occurred_at,
///event_type, owner_unit_ref) are snake_case and pinned byte-exact by signed golden
///vectors. The shape follows the wire.
class DerivativeCreated {
    
    ///The generation that was made.
    String contentId;
    
    ///The working session it was made in.
    String sessionId;
    
    ///The assets it was written from, by id. Absent when nothing was drawn on.
    List<String>? sourceAssets;
    
    ///Which template it was written from. Free text: the templates belong to whoever generates.
    String template;

    DerivativeCreated({
        required this.contentId,
        required this.sessionId,
        this.sourceAssets,
        required this.template,
    });

    factory DerivativeCreated.fromJson(Map<String, dynamic> json) => DerivativeCreated(
        contentId: json["content_id"],
        sessionId: json["session_id"],
        sourceAssets: json["source_assets"] == null ? [] : List<String>.from(json["source_assets"]!.map((x) => x)),
        template: json["template"],
    );

    Map<String, dynamic> toJson() => {
        "content_id": contentId,
        "session_id": sessionId,
        "source_assets": sourceAssets == null ? [] : List<dynamic>.from(sourceAssets!.map((x) => x)),
        "template": template,
    };
}