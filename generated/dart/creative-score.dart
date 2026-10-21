// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final creativeScore = creativeScoreFromJson(jsonString);

import 'dart:convert';

CreativeScore creativeScoreFromJson(String str) => CreativeScore.fromJson(json.decode(str));

String creativeScoreToJson(CreativeScore data) => json.encode(data.toJson());


///A reading of one generated piece: how it sat against the voice it was written for, how it
///fitted the channel it was written into, and why. About a piece of work, never about the
///person who asked for it — nothing here is said about an actor.
class CreativeScore {
    
    ///When the piece was scored, which is not when it was written.
    DateTime? createdAt;
    
    ///The id of the generated piece this reads, in the system that owns it. A piece of work,
    ///not an actor: it has no wallet.
    String generation;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///The model that read the piece, as it was named at the time. Recorded so two scores can be
    ///told apart when the scorer changed underneath them.
    String? modelUsed;
    
    ///What the scorer made of the piece: the two scores, the one carried alongside them, and
    ///why.
    CreativeReading reading;

    CreativeScore({
        this.createdAt,
        required this.generation,
        this.id,
        this.modelUsed,
        required this.reading,
    });

    factory CreativeScore.fromJson(Map<String, dynamic> json) => CreativeScore(
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        generation: json["generation"],
        id: json["id"],
        modelUsed: json["modelUsed"],
        reading: CreativeReading.fromJson(json["reading"]),
    );

    Map<String, dynamic> toJson() => {
        "createdAt": createdAt?.toIso8601String(),
        "generation": generation,
        "id": id,
        "modelUsed": modelUsed,
        "reading": reading.toJson(),
    };
}


///What the scorer made of the piece: the two scores, the one carried alongside them, and
///why.
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