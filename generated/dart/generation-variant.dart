// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final generationVariant = generationVariantFromJson(jsonString);

import 'dart:convert';

GenerationVariant generationVariantFromJson(String str) => GenerationVariant.fromJson(json.decode(str));

String generationVariantToJson(GenerationVariant data) => json.encode(data.toJson());


///A second take on a generation, asked for as its own piece of work. It says which
///generation it came from and which job was run for it — the text it produced belongs to
///that job's own record, not to this edge.
class GenerationVariant {
    
    ///When the variant was asked for, which is not when the job finished.
    DateTime? createdAt;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///The processing job run to produce it, by its id in the system that runs it. The variant
    ///is the link between the two; neither side carries the other.
    String job;
    
    ///The generation this is a variant of, by its id in the system that holds it.
    String parentGeneration;

    GenerationVariant({
        this.createdAt,
        this.id,
        required this.job,
        required this.parentGeneration,
    });

    factory GenerationVariant.fromJson(Map<String, dynamic> json) => GenerationVariant(
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        id: json["id"],
        job: json["job"],
        parentGeneration: json["parentGeneration"],
    );

    Map<String, dynamic> toJson() => {
        "createdAt": createdAt?.toIso8601String(),
        "id": id,
        "job": job,
        "parentGeneration": parentGeneration,
    };
}