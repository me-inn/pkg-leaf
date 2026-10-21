// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final generationVersion = generationVersionFromJson(jsonString);

import 'dart:convert';

GenerationVersion generationVersionFromJson(String str) => GenerationVersion.fromJson(json.decode(str));

String generationVersionToJson(GenerationVersion data) => json.encode(data.toJson());


///The text a generation held at one point in its life. Kept as its own record so editing a
///generation never loses what it said before — the generation carries the current text, the
///versions carry the ones it had.
class GenerationVersion {
    
    ///When this version was written.
    DateTime? createdAt;
    
    ///The generation this is a version of, by its id in the system that holds it.
    String generation;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///The text as it stood in this version.
    String output;
    
    ///Which version this is, counting up within the generation. Ordering is the number's job;
    ///whether it may skip or repeat is the writing system's rule.
    int version;

    GenerationVersion({
        this.createdAt,
        required this.generation,
        this.id,
        required this.output,
        required this.version,
    });

    factory GenerationVersion.fromJson(Map<String, dynamic> json) => GenerationVersion(
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        generation: json["generation"],
        id: json["id"],
        output: json["output"],
        version: json["version"],
    );

    Map<String, dynamic> toJson() => {
        "createdAt": createdAt?.toIso8601String(),
        "generation": generation,
        "id": id,
        "output": output,
        "version": version,
    };
}