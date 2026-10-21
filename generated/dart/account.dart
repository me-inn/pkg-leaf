// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final account = accountFromJson(jsonString);

import 'dart:convert';

Account accountFromJson(String str) => Account.fromJson(json.decode(str));

String accountToJson(Account data) => json.encode(data.toJson());


///What somebody is owed by the system that bills them: a plan, a credit balance, and the
///day the cycle turns over. Not an actor and not an organisation — the actor is the person
///who owns it, named here by key. One person can be billed by more than one system, and
///each one keeps its own account.
class Account {
    DateTime? createdAt;
    
    ///Credits left to spend. Whole credits, never fractions, because a half-spent credit is not
    ///a thing anybody can sell.
    int creditsBalance;
    
    ///When the next cycle starts and the balance is refilled. Stated rather than computed from
    ///the plan, so a cycle moved by hand stays moved.
    DateTime cycleRenewsAt;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///The wallet, handle, or id under localIds of the person billed. One account per person per
    ///system.
    String owner;
    
    ///Which plan is in force, in the words of the system that sells it. Free text: the
    ///catalogue of plans belongs to the seller and changes without the shape changing.
    String plan;
    DateTime? updatedAt;

    Account({
        this.createdAt,
        required this.creditsBalance,
        required this.cycleRenewsAt,
        this.id,
        required this.owner,
        required this.plan,
        this.updatedAt,
    });

    factory Account.fromJson(Map<String, dynamic> json) => Account(
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        creditsBalance: json["creditsBalance"],
        cycleRenewsAt: DateTime.parse(json["cycleRenewsAt"]),
        id: json["id"],
        owner: json["owner"],
        plan: json["plan"],
        updatedAt: json["updatedAt"] == null ? null : DateTime.parse(json["updatedAt"]),
    );

    Map<String, dynamic> toJson() => {
        "createdAt": createdAt?.toIso8601String(),
        "creditsBalance": creditsBalance,
        "cycleRenewsAt": cycleRenewsAt.toIso8601String(),
        "id": id,
        "owner": owner,
        "plan": plan,
        "updatedAt": updatedAt?.toIso8601String(),
    };
}