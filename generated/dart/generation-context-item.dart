// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final generationContextItem = generationContextItemFromJson(jsonString);

import 'dart:convert';

GenerationContextItem generationContextItemFromJson(String str) => GenerationContextItem.fromJson(json.decode(str));

String generationContextItemToJson(GenerationContextItem data) => json.encode(data.toJson());


///One piece of material that was put in front of the model for a generation, and where it
///came from. Written down because the source can change afterwards: this says what was
///actually read, in the order it was read.
class GenerationContextItem {
    
    ///The material as it was handed to the model. A copy on purpose — the source may be edited
    ///or deleted later, and this is what was read.
    String content;
    
    ///The generation this was given to, by its id in the system that holds it.
    String generation;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///Its place in the order the items were assembled in, counting from the first. Position,
    ///not score.
    int rank;
    
    ///How close the retrieval judged it to the ask. Absent when the item was not chosen by
    ///similarity. The scale belongs to whichever retrieval produced it.
    double? similarityScore;
    
    ///The id of that thing, in the system that owns it. Paired with sourceType, which says what
    ///kind of id it is.
    String sourceId;
    
    ///What kind of thing the material came from. Free text: the kinds belong to whatever the
    ///retrieving system can reach.
    String sourceType;

    GenerationContextItem({
        required this.content,
        required this.generation,
        this.id,
        required this.rank,
        this.similarityScore,
        required this.sourceId,
        required this.sourceType,
    });

    factory GenerationContextItem.fromJson(Map<String, dynamic> json) => GenerationContextItem(
        content: json["content"],
        generation: json["generation"],
        id: json["id"],
        rank: json["rank"],
        similarityScore: json["similarityScore"]?.toDouble(),
        sourceId: json["sourceId"],
        sourceType: json["sourceType"],
    );

    Map<String, dynamic> toJson() => {
        "content": content,
        "generation": generation,
        "id": id,
        "rank": rank,
        "similarityScore": similarityScore,
        "sourceId": sourceId,
        "sourceType": sourceType,
    };
}