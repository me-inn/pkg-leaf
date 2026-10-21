// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final brandVoice = brandVoiceFromJson(jsonString);

import 'dart:convert';

BrandVoice brandVoiceFromJson(String str) => BrandVoice.fromJson(json.decode(str));

String brandVoiceToJson(BrandVoice data) => json.encode(data.toJson());


///A snapshot of what a session has been approving: how much, how well it scored, and which
///channels and objectives it kept coming back to. Counted once and written down, so the
///figures a person saw on a day can be shown again on another day without recounting them.
class BrandVoice {
    
    ///How many pieces had been approved when the snapshot was taken.
    int approvedCount;
    
    ///The mean of the latest score of each scored generation. Absent when nothing had been
    ///scored yet, which is not the same as zero.
    double? avgOverallScore;
    
    ///When the snapshot was taken. It is what makes the figures readable later: they are true
    ///of that moment and of no other.
    DateTime? createdAt;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///The session this was counted over, as the system that owns the session names it.
    ///Optional: scoping a profile to a working session is how Creative Flow holds it, not part
    ///of what it is, and a system without sessions must be able to carry the same shape.
    String? session;
    
    ///The channels that came up most, most frequent first. A list, whatever a given store
    ///serialises it into.
    List<String>? topChannels;
    
    ///The objectives that came up most, most frequent first.
    List<String>? topObjectives;

    BrandVoice({
        required this.approvedCount,
        this.avgOverallScore,
        this.createdAt,
        this.id,
        this.session,
        this.topChannels,
        this.topObjectives,
    });

    factory BrandVoice.fromJson(Map<String, dynamic> json) => BrandVoice(
        approvedCount: json["approvedCount"],
        avgOverallScore: json["avgOverallScore"]?.toDouble(),
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        id: json["id"],
        session: json["session"],
        topChannels: json["topChannels"] == null ? [] : List<String>.from(json["topChannels"]!.map((x) => x)),
        topObjectives: json["topObjectives"] == null ? [] : List<String>.from(json["topObjectives"]!.map((x) => x)),
    );

    Map<String, dynamic> toJson() => {
        "approvedCount": approvedCount,
        "avgOverallScore": avgOverallScore,
        "createdAt": createdAt?.toIso8601String(),
        "id": id,
        "session": session,
        "topChannels": topChannels == null ? [] : List<dynamic>.from(topChannels!.map((x) => x)),
        "topObjectives": topObjectives == null ? [] : List<dynamic>.from(topObjectives!.map((x) => x)),
    };
}