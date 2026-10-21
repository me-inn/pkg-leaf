// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final repurposeScore = repurposeScoreFromJson(jsonString);

import 'dart:convert';

RepurposeScore repurposeScoreFromJson(String str) => RepurposeScore.fromJson(json.decode(str));

String repurposeScoreToJson(RepurposeScore data) => json.encode(data.toJson());


///The same reading as a creative score, but of work a job turned into one other format. It
///is its own record and not a column on the job: one job produces several formats, and each
///is read on its own.
class RepurposeScore {
    
    ///When the output was scored, which is not when the job ran.
    DateTime? createdAt;
    
    ///Which of the job's outputs this score is for. One score per format, so the job's own id
    ///does not identify a record.
    Format format;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///The id of the repurpose job that produced the work, in the system that ran it.
    String job;
    
    ///What the scorer made of that one output. The same shape a creative score carries, read
    ///against the channel the format is meant for.
    CreativeReading reading;

    RepurposeScore({
        this.createdAt,
        required this.format,
        this.id,
        required this.job,
        required this.reading,
    });

    factory RepurposeScore.fromJson(Map<String, dynamic> json) => RepurposeScore(
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        format: formatValues.map[json["format"]]!,
        id: json["id"],
        job: json["job"],
        reading: CreativeReading.fromJson(json["reading"]),
    );

    Map<String, dynamic> toJson() => {
        "createdAt": createdAt?.toIso8601String(),
        "format": formatValues.reverse[format],
        "id": id,
        "job": job,
        "reading": reading.toJson(),
    };
}


///Which of the job's outputs this score is for. One score per format, so the job's own id
///does not identify a record.
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


///What the scorer made of that one output. The same shape a creative score carries, read
///against the channel the format is meant for.
///
///What a model made of a piece of work: how it sat against the voice it was written for,
///how it fitted the channel it was written into, and why. About the work, never about
///whoever asked for it — nothing here is said about an actor, so none of it is testimony.
class CreativeReading {
    
    ///How close the work came to the voice it was written for, from 0 to 1. The range is what
    ///the scorer produces, and keeping a number inside it is the job of the code that writes
    ///the record.
    double brandVoiceScore;
    
    ///How well the work fitted the channel it was written into, from 0 to 1, on the same scale.
    double channelFitScore;
    
    ///The single number carried alongside the two others, from 0 to 1. Stated rather than
    ///derived here: how the scorer weighed voice against fit is its own, and recomputing it
    ///elsewhere would invent a weighting nobody agreed to.
    double overallScore;
    
    ///Why those numbers, in the scorer's own words. Kept because a number with no account of
    ///itself cannot be argued with.
    String reasoning;

    CreativeReading({
        required this.brandVoiceScore,
        required this.channelFitScore,
        required this.overallScore,
        required this.reasoning,
    });

    factory CreativeReading.fromJson(Map<String, dynamic> json) => CreativeReading(
        brandVoiceScore: json["brandVoiceScore"]?.toDouble(),
        channelFitScore: json["channelFitScore"]?.toDouble(),
        overallScore: json["overallScore"]?.toDouble(),
        reasoning: json["reasoning"],
    );

    Map<String, dynamic> toJson() => {
        "brandVoiceScore": brandVoiceScore,
        "channelFitScore": channelFitScore,
        "overallScore": overallScore,
        "reasoning": reasoning,
    };
}

class EnumValues<T> {
    Map<String, T> map;
    late Map<T, String> reverseMap;

    EnumValues(this.map);

    Map<T, String> get reverse {
            reverseMap = map.map((k, v) => MapEntry(v, k));
            return reverseMap;
    }
}