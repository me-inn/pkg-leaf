// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final webhookDelivery = webhookDeliveryFromJson(jsonString);

import 'dart:convert';

WebhookDelivery webhookDeliveryFromJson(String str) => WebhookDelivery.fromJson(json.decode(str));

String webhookDeliveryToJson(WebhookDelivery data) => json.encode(data.toJson());


///One attempt to call a webhook: what was sent, what came back, and how many tries it took.
///A record of its own rather than a column on the subscription, because one subscription
///has many deliveries and each outlives the state of the next. No signature travels here,
///for the same reason none travels on the subscription.
class WebhookDelivery {
    
    ///How many times this delivery has been tried.
    int? attempts;
    
    ///When the attempt was recorded, which is not when the event happened.
    DateTime? createdAt;
    
    ///Which event triggered the call. Free text, matching one of the names on the subscription.
    String event;
    
    ///The status code the endpoint answered with. Absent when the call never got an answer — a
    ///timeout and a 500 are different failures.
    int? httpStatus;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///The body that was posted. Open on purpose: its keys belong to whoever emits the event,
    ///and the delivery only records what went out.
    Map<String, dynamic>? payload;
    
    ///What the endpoint wrote back, kept as given. Read when a delivery has to be explained,
    ///never parsed.
    String? responseBody;
    
    ///Where the attempt stands. Free text rather than an enum: the source has no declared set,
    ///only a default of pending.
    String? status;
    
    ///The subscription this attempt was made for, as the system that holds it names it.
    String webhook;

    WebhookDelivery({
        this.attempts,
        this.createdAt,
        required this.event,
        this.httpStatus,
        this.id,
        this.payload,
        this.responseBody,
        this.status,
        required this.webhook,
    });

    factory WebhookDelivery.fromJson(Map<String, dynamic> json) => WebhookDelivery(
        attempts: json["attempts"],
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        event: json["event"],
        httpStatus: json["httpStatus"],
        id: json["id"],
        payload: Map.from(json["payload"]!).map((k, v) => MapEntry<String, dynamic>(k, v)),
        responseBody: json["responseBody"],
        status: json["status"],
        webhook: json["webhook"],
    );

    Map<String, dynamic> toJson() => {
        "attempts": attempts,
        "createdAt": createdAt?.toIso8601String(),
        "event": event,
        "httpStatus": httpStatus,
        "id": id,
        "payload": Map.from(payload!).map((k, v) => MapEntry<String, dynamic>(k, v)),
        "responseBody": responseBody,
        "status": status,
        "webhook": webhook,
    };
}