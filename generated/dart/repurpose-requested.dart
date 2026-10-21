// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final repurposeRequested = repurposeRequestedFromJson(jsonString);

import 'dart:convert';

RepurposeRequested repurposeRequestedFromJson(String str) => RepurposeRequested.fromJson(json.decode(str));

String repurposeRequestedToJson(RepurposeRequested data) => json.encode(data.toJson());


///One piece of text somebody wants turned into several shorter ones. Unlike the other
///commands, the whole instruction travels in the event: the asking system holds no job of
///its own to read it back from. Keys are snake_case, not the camelCase the rest of leaf
///uses: this travels inside a Liquid envelope, whose own fields (event_id, occurred_at,
///event_type, owner_unit_ref) are snake_case and pinned byte-exact by signed golden
///vectors. The shape follows the wire.
class RepurposeRequested {
    
    ///Where the result is headed, which changes how it is written. Free text: the channels
    ///belong to whoever publishes.
    String? channel;
    
    ///The text to work from, in full. Not a reference to an asset: a repurpose can be asked of
    ///words that were never put in.
    String? context;
    
    ///Which shapes to write. Anything outside the list is dropped rather than refused, and a
    ///request left with none is not worked.
    List<Format>? formats;
    
    ///Anything else the asker wants said, in their own words.
    String? instructions;
    
    ///The job to report the work against, created by the pipeline if it does not exist yet.
    String jobId;
    
    ///BCP-47 tag of the language to write in. Detected from the context when absent.
    String? language;
    
    ///What the result is for, in the vocabulary of whoever asked.
    String? objective;
    
    ///The working session the request belongs to, which is where the brand voice and the
    ///defaults come from.
    String sessionId;
    
    ///Whether to write in the brand voice held for the session. False writes neutrally.
    bool? useBrandVoice;

    RepurposeRequested({
        this.channel,
        this.context,
        this.formats,
        this.instructions,
        required this.jobId,
        this.language,
        this.objective,
        required this.sessionId,
        this.useBrandVoice,
    });

    factory RepurposeRequested.fromJson(Map<String, dynamic> json) => RepurposeRequested(
        channel: json["channel"],
        context: json["context"],
        formats: json["formats"] == null ? [] : List<Format>.from(json["formats"]!.map((x) => formatValues.map[x]!)),
        instructions: json["instructions"],
        jobId: json["job_id"],
        language: json["language"],
        objective: json["objective"],
        sessionId: json["session_id"],
        useBrandVoice: json["use_brand_voice"],
    );

    Map<String, dynamic> toJson() => {
        "channel": channel,
        "context": context,
        "formats": formats == null ? [] : List<dynamic>.from(formats!.map((x) => formatValues.reverse[x])),
        "instructions": instructions,
        "job_id": jobId,
        "language": language,
        "objective": objective,
        "session_id": sessionId,
        "use_brand_voice": useBrandVoice,
    };
}

enum Format {
    CAPTIONS,
    CAROUSEL_COPY,
    CTA_VARIANTS,
    HASHTAGS,
    HOOKS,
    SHORT_SCRIPTS
}

final formatValues = EnumValues({
    "captions": Format.CAPTIONS,
    "carousel_copy": Format.CAROUSEL_COPY,
    "cta_variants": Format.CTA_VARIANTS,
    "hashtags": Format.HASHTAGS,
    "hooks": Format.HOOKS,
    "short_scripts": Format.SHORT_SCRIPTS
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