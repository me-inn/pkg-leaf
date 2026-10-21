// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final tokenUsage = tokenUsageFromJson(jsonString);

import 'dart:convert';

TokenUsage tokenUsageFromJson(String str) => TokenUsage.fromJson(json.decode(str));

String tokenUsageToJson(TokenUsage data) => json.encode(data.toJson());


///What one call to a model cost: who made it, which model answered, how many tokens each
///way, and the money. Separate from the credit ledger — credits are what the customer is
///charged, tokens are what the call actually consumed, and the two move for different
///reasons.
class TokenUsage {
    
    ///What the call was for, in the words of the system that made it. Free text: the kinds of
    ///call belong to that system.
    String callType;
    
    ///What the call cost in US dollars, worked out when it was written from the prices in force
    ///then. Recorded rather than recomputed: prices change, and what was spent does not.
    double costUsd;
    
    ///When the call was recorded.
    DateTime? createdAt;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///Tokens sent.
    int inputTokens;
    
    ///The id of the job that made the call, in the system that owns jobs.
    String? job;
    
    ///The model name as the provider gives it, verbatim. Kept exactly because the price was
    ///read against this string.
    String model;
    
    ///Tokens returned.
    int outputTokens;
    
    ///The wallet, handle, or id under localIds of whoever the call was made for. Absent for a
    ///call nobody is signed in behind, such as a background pass.
    String? person;
    
    ///Who served the call. Free text: providers are added without the shape changing.
    String provider;
    
    ///The work session the call belongs to, as the system that owns the session names it.
    ///Absent when it belongs to none.
    String? session;

    TokenUsage({
        required this.callType,
        required this.costUsd,
        this.createdAt,
        this.id,
        required this.inputTokens,
        this.job,
        required this.model,
        required this.outputTokens,
        this.person,
        required this.provider,
        this.session,
    });

    factory TokenUsage.fromJson(Map<String, dynamic> json) => TokenUsage(
        callType: json["callType"],
        costUsd: json["costUsd"]?.toDouble(),
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        id: json["id"],
        inputTokens: json["inputTokens"],
        job: json["job"],
        model: json["model"],
        outputTokens: json["outputTokens"],
        person: json["person"],
        provider: json["provider"],
        session: json["session"],
    );

    Map<String, dynamic> toJson() => {
        "callType": callType,
        "costUsd": costUsd,
        "createdAt": createdAt?.toIso8601String(),
        "id": id,
        "inputTokens": inputTokens,
        "job": job,
        "model": model,
        "outputTokens": outputTokens,
        "person": person,
        "provider": provider,
        "session": session,
    };
}