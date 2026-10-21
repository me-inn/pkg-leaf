// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final performanceSignal = performanceSignalFromJson(jsonString);

import 'dart:convert';

PerformanceSignal performanceSignalFromJson(String str) => PerformanceSignal.fromJson(json.decode(str));

String performanceSignalToJson(PerformanceSignal data) => json.encode(data.toJson());


///One number a platform reported about one generated piece, at one moment. A reading and
///not a total: a second reading of the same metric is another record, so what a piece did
///over time is the series and never a field that gets overwritten.
class PerformanceSignal {
    
    ///The id of the generated piece the number is about, in the system that owns it.
    String generation;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///What was counted, in the platform's own word for it. Free text for the same reason, and
    ///never translated on the way in: a platform's reach is not another platform's reach.
    String metricName;
    
    ///The number, as reported. No unit travels with it — the unit is whatever the platform
    ///means by that metric name.
    double metricValue;
    
    ///Where the piece ran and who counted. Free text: the names belong to the platforms, and a
    ///list here would be out of date the week somebody publishes somewhere new.
    String platform;
    
    ///When the reading was taken, which is not when the piece was published and not when the
    ///platform computed it.
    DateTime? recordedAt;

    PerformanceSignal({
        required this.generation,
        this.id,
        required this.metricName,
        required this.metricValue,
        required this.platform,
        this.recordedAt,
    });

    factory PerformanceSignal.fromJson(Map<String, dynamic> json) => PerformanceSignal(
        generation: json["generation"],
        id: json["id"],
        metricName: json["metricName"],
        metricValue: json["metricValue"]?.toDouble(),
        platform: json["platform"],
        recordedAt: json["recordedAt"] == null ? null : DateTime.parse(json["recordedAt"]),
    );

    Map<String, dynamic> toJson() => {
        "generation": generation,
        "id": id,
        "metricName": metricName,
        "metricValue": metricValue,
        "platform": platform,
        "recordedAt": recordedAt?.toIso8601String(),
    };
}