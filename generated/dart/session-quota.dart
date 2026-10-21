// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final sessionQuota = sessionQuotaFromJson(jsonString);

import 'dart:convert';

SessionQuota sessionQuotaFromJson(String str) => SessionQuota.fromJson(json.decode(str));

String sessionQuotaToJson(SessionQuota data) => json.encode(data.toJson());


///How much a work session may spend in a day. Its own record rather than fields on the
///session, because the limits are set by whoever runs the system and the session is written
///by whoever uses it.
class SessionQuota {
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///Generations allowed in a day.
    int maxGenerationsPerDay;
    
    ///Repurposes allowed in a day.
    int maxRepurposePerDay;
    
    ///The wallet, handle, or id under localIds of whoever owns the quota. Carried so the holder
    ///of a session id is not by itself the person allowed to change the limits; absent for a
    ///session nobody has signed in for.
    String? person;
    
    ///The work session the limits apply to, as the system that owns the session names it. One
    ///quota per session.
    String session;

    SessionQuota({
        this.id,
        required this.maxGenerationsPerDay,
        required this.maxRepurposePerDay,
        this.person,
        required this.session,
    });

    factory SessionQuota.fromJson(Map<String, dynamic> json) => SessionQuota(
        id: json["id"],
        maxGenerationsPerDay: json["maxGenerationsPerDay"],
        maxRepurposePerDay: json["maxRepurposePerDay"],
        person: json["person"],
        session: json["session"],
    );

    Map<String, dynamic> toJson() => {
        "id": id,
        "maxGenerationsPerDay": maxGenerationsPerDay,
        "maxRepurposePerDay": maxRepurposePerDay,
        "person": person,
        "session": session,
    };
}