// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final signalError = signalErrorFromJson(jsonString);

import 'dart:convert';

SignalError signalErrorFromJson(String str) => SignalError.fromJson(json.decode(str));

String signalErrorToJson(SignalError data) => json.encode(data.toJson());


///Something in the pipeline broke, said in a way another system can route rather than only
///print. The only event not about one piece of content: it is about a step that failed and
///who answers for it. Keys are snake_case, not the camelCase the rest of leaf uses: this
///travels inside a Liquid envelope, whose own fields (event_id, occurred_at, event_type,
///owner_unit_ref) are snake_case and pinned byte-exact by signed golden vectors. The shape
///follows the wire.
class SignalError {
    
    ///A machine-readable code such as ENRICHMENT_TIMEOUT. Free text: the vocabulary belongs to
    ///whoever raised it, and a reader matches on it rather than on the summary.
    String code;
    
    ///The trace this failure belongs to, for tying it to others from the same run.
    String? correlationId;
    
    ///Whatever else the raising step knew — the asset, the stage it stopped at. Keys belong to
    ///that step, so none are fixed here.
    Map<String, dynamic>? metadata;
    
    ///When the failure happened. Carried inside the payload as well as on the event, because
    ///the signal outlives the event that delivered it.
    DateTime occurredAt;
    
    ///The session or unit the failure belongs to. Who answers for it, which is how an error
    ///finds somebody at all.
    String ownerUnitRef;
    
    ///How bad it is, as judged where it was raised.
    Severity severity;
    
    ///The signal's own id, written where it was raised, so the same failure reported twice can
    ///be recognised as one.
    String signalId;
    
    ///The module that raised it, such as creativeflow.worker.process_asset. Says where to look,
    ///not who is at fault.
    String source;
    
    ///Where the handling of it stands. Raised as reported; moved on by whoever picks it up, not
    ///by whoever raised it.
    Status status;
    
    ///The thing that was being worked on when it broke, when there is one.
    String? subjectRef;
    
    ///What went wrong, for a person. Never the whole trace.
    String summary;

    SignalError({
        required this.code,
        this.correlationId,
        this.metadata,
        required this.occurredAt,
        required this.ownerUnitRef,
        required this.severity,
        required this.signalId,
        required this.source,
        required this.status,
        this.subjectRef,
        required this.summary,
    });

    factory SignalError.fromJson(Map<String, dynamic> json) => SignalError(
        code: json["code"],
        correlationId: json["correlation_id"],
        metadata: Map.from(json["metadata"]!).map((k, v) => MapEntry<String, dynamic>(k, v)),
        occurredAt: DateTime.parse(json["occurred_at"]),
        ownerUnitRef: json["owner_unit_ref"],
        severity: severityValues.map[json["severity"]]!,
        signalId: json["signal_id"],
        source: json["source"],
        status: statusValues.map[json["status"]]!,
        subjectRef: json["subject_ref"],
        summary: json["summary"],
    );

    Map<String, dynamic> toJson() => {
        "code": code,
        "correlation_id": correlationId,
        "metadata": Map.from(metadata!).map((k, v) => MapEntry<String, dynamic>(k, v)),
        "occurred_at": occurredAt.toIso8601String(),
        "owner_unit_ref": ownerUnitRef,
        "severity": severityValues.reverse[severity],
        "signal_id": signalId,
        "source": source,
        "status": statusValues.reverse[status],
        "subject_ref": subjectRef,
        "summary": summary,
    };
}


///How bad it is, as judged where it was raised.
enum Severity {
    CRITICAL,
    ERROR,
    INFO,
    WARNING
}

final severityValues = EnumValues({
    "critical": Severity.CRITICAL,
    "error": Severity.ERROR,
    "info": Severity.INFO,
    "warning": Severity.WARNING
});


///Where the handling of it stands. Raised as reported; moved on by whoever picks it up, not
///by whoever raised it.
enum Status {
    ACKNOWLEDGED,
    REPORTED,
    RESOLVED
}

final statusValues = EnumValues({
    "acknowledged": Status.ACKNOWLEDGED,
    "reported": Status.REPORTED,
    "resolved": Status.RESOLVED
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