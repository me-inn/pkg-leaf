// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final assetIngestRequested = assetIngestRequestedFromJson(jsonString);

import 'dart:convert';

AssetIngestRequested assetIngestRequestedFromJson(String str) => AssetIngestRequested.fromJson(json.decode(str));

String assetIngestRequestedToJson(AssetIngestRequested data) => json.encode(data.toJson());


///Somebody put a file in somewhere else and wants it read. The bytes are already in the
///store; only the two ids travel. Keys are snake_case, not the camelCase the rest of leaf
///uses: this travels inside a Liquid envelope, whose own fields (event_id, occurred_at,
///event_type, owner_unit_ref) are snake_case and pinned byte-exact by signed golden
///vectors. The shape follows the wire.
class AssetIngestRequested {
    
    ///The asset to read, in the system that holds it.
    String assetId;
    
    ///The job to report the reading against. Written by whoever asked, so the asker can follow
    ///the work without waiting for a reply.
    String jobId;

    AssetIngestRequested({
        required this.assetId,
        required this.jobId,
    });

    factory AssetIngestRequested.fromJson(Map<String, dynamic> json) => AssetIngestRequested(
        assetId: json["asset_id"],
        jobId: json["job_id"],
    );

    Map<String, dynamic> toJson() => {
        "asset_id": assetId,
        "job_id": jobId,
    };
}