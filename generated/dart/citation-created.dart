// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final citationCreated = citationCreatedFromJson(jsonString);

import 'dart:convert';

CitationCreated citationCreatedFromJson(String str) => CitationCreated.fromJson(json.decode(str));

String citationCreatedToJson(CitationCreated data) => json.encode(data.toJson());


///An address was fetched and kept as an asset. The address stays in the event because the
///copy and the page drift apart from that moment. Keys are snake_case, not the camelCase
///the rest of leaf uses: this travels inside a Liquid envelope, whose own fields (event_id,
///occurred_at, event_type, owner_unit_ref) are snake_case and pinned byte-exact by signed
///golden vectors. The shape follows the wire.
class CitationCreated {
    
    ///The asset the fetched page became.
    String contentId;
    
    ///The working session it was fetched into.
    String sessionId;
    
    ///The address it was fetched from.
    String sourceUrl;

    CitationCreated({
        required this.contentId,
        required this.sessionId,
        required this.sourceUrl,
    });

    factory CitationCreated.fromJson(Map<String, dynamic> json) => CitationCreated(
        contentId: json["content_id"],
        sessionId: json["session_id"],
        sourceUrl: json["source_url"],
    );

    Map<String, dynamic> toJson() => {
        "content_id": contentId,
        "session_id": sessionId,
        "source_url": sourceUrl,
    };
}