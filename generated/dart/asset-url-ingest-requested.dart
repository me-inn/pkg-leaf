// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final assetUrlIngestRequested = assetUrlIngestRequestedFromJson(jsonString);

import 'dart:convert';

AssetUrlIngestRequested assetUrlIngestRequestedFromJson(String str) => AssetUrlIngestRequested.fromJson(json.decode(str));

String assetUrlIngestRequestedToJson(AssetUrlIngestRequested data) => json.encode(data.toJson());


///An address somebody wants fetched and read. The address is not here: the job already
///names the asset and where it points, and the pipeline reads it from there. Keys are
///snake_case, not the camelCase the rest of leaf uses: this travels inside a Liquid
///envelope, whose own fields (event_id, occurred_at, event_type, owner_unit_ref) are
///snake_case and pinned byte-exact by signed golden vectors. The shape follows the wire.
class AssetUrlIngestRequested {
    
    ///The job that names the asset and the address to fetch.
    String jobId;

    AssetUrlIngestRequested({
        required this.jobId,
    });

    factory AssetUrlIngestRequested.fromJson(Map<String, dynamic> json) => AssetUrlIngestRequested(
        jobId: json["job_id"],
    );

    Map<String, dynamic> toJson() => {
        "job_id": jobId,
    };
}