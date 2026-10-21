// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final workSession = workSessionFromJson(jsonString);

import 'dart:convert';

WorkSession workSessionFromJson(String str) => WorkSession.fromJson(json.decode(str));

String workSessionToJson(WorkSession data) => json.encode(data.toJson());


///A stretch of work somebody keeps coming back to, and the defaults everything made inside
///it starts from. Named work-session, not session, because it has nothing to do with being
///signed in: it outlives any login and carries no credential.
class WorkSession {
    
    ///The brand the work is for, as typed. A name, not a reference: the session is written
    ///before anybody decides whether that brand is a record anywhere.
    String? brandName;
    
    ///When the session was opened.
    DateTime createdAt;
    
    ///Where work made here is headed unless told otherwise. Free text: the channels belong to
    ///the system that publishes.
    String? defaultChannel;
    
    ///What work made here is for unless told otherwise. Free text, in the vocabulary of whoever
    ///set it.
    String? defaultObjective;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///When it was last touched. The reason the record is worth keeping: it says which sessions
    ///are still alive.
    DateTime lastSeen;
    
    ///What the person called it. Absent until they bother to name it.
    String? name;
    
    ///The wallet, handle, or id under localIds of whoever is working. Absent while the work is
    ///anonymous — a session can exist before anybody has signed in for it.
    String? person;
    
    ///The id of the workspace the session sits in, in the system that owns workspaces.
    String? workspace;

    WorkSession({
        this.brandName,
        required this.createdAt,
        this.defaultChannel,
        this.defaultObjective,
        this.id,
        required this.lastSeen,
        this.name,
        this.person,
        this.workspace,
    });

    factory WorkSession.fromJson(Map<String, dynamic> json) => WorkSession(
        brandName: json["brandName"],
        createdAt: DateTime.parse(json["createdAt"]),
        defaultChannel: json["defaultChannel"],
        defaultObjective: json["defaultObjective"],
        id: json["id"],
        lastSeen: DateTime.parse(json["lastSeen"]),
        name: json["name"],
        person: json["person"],
        workspace: json["workspace"],
    );

    Map<String, dynamic> toJson() => {
        "brandName": brandName,
        "createdAt": createdAt.toIso8601String(),
        "defaultChannel": defaultChannel,
        "defaultObjective": defaultObjective,
        "id": id,
        "lastSeen": lastSeen.toIso8601String(),
        "name": name,
        "person": person,
        "workspace": workspace,
    };
}