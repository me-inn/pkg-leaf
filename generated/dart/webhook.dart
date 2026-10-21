// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final webhook = webhookFromJson(jsonString);

import 'dart:convert';

Webhook webhookFromJson(String str) => Webhook.fromJson(json.decode(str));

String webhookToJson(Webhook data) => json.encode(data.toJson());


///A standing instruction to call a URL when something happens. The subscription only: what
///is to be called and for which events. No signing secret travels here — whoever signs a
///delivery holds the key for it, and a shared shape carrying it would be a secret in every
///system that read the shape.
class Webhook {
    
    ///Whether it is still being called. Turned off rather than deleted, so the deliveries
    ///already made keep pointing at something.
    bool? active;
    
    ///When the subscription was registered.
    DateTime? createdAt;
    
    ///Which events to post. Free text: the names belong to whoever emits them, and a shape that
    ///fixed them would go stale the first time one is added.
    List<String> events;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///The session the subscription belongs to, as the system that owns the session names it.
    ///Deliveries are scoped by it, and so is who may read the subscription back. Optional:
    ///scoping a subscription to a working session is how Creative Flow holds it, not part of
    ///what it is, and a system without sessions must be able to carry the same shape.
    String? session;
    
    ///Where to post. http or https, as given: a subscription to a URL that no longer answers is
    ///still a fact about what was asked for.
    String url;

    Webhook({
        this.active,
        this.createdAt,
        required this.events,
        this.id,
        this.session,
        required this.url,
    });

    factory Webhook.fromJson(Map<String, dynamic> json) => Webhook(
        active: json["active"],
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        events: List<String>.from(json["events"].map((x) => x)),
        id: json["id"],
        session: json["session"],
        url: json["url"],
    );

    Map<String, dynamic> toJson() => {
        "active": active,
        "createdAt": createdAt?.toIso8601String(),
        "events": List<dynamic>.from(events.map((x) => x)),
        "id": id,
        "session": session,
        "url": url,
    };
}