// Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

// To parse this JSON data, do
//
//     final creditTransaction = creditTransactionFromJson(jsonString);

import 'dart:convert';

CreditTransaction creditTransactionFromJson(String str) => CreditTransaction.fromJson(json.decode(str));

String creditTransactionToJson(CreditTransaction data) => json.encode(data.toJson());


///One movement of credit on an account, written once and never changed. The balance on the
///account is the sum of these; a row kept after the fact is what makes it possible to say
///why.
class CreditTransaction {
    
    ///The id of the account the credit moved on, in the system that holds it.
    String account;
    
    ///Signed: negative spends, positive tops up or refills. One field rather than a direction
    ///and a magnitude, so adding them up needs no rules.
    int amount;
    
    ///The balance the moment after this movement was applied. Copied here on purpose: reading a
    ///balance as of some past row should not mean replaying the whole ledger.
    int balanceAfter;
    
    ///When the movement was recorded.
    DateTime? createdAt;
    
    ///A line a person can read on a receipt or in support. Written by whoever charged; empty
    ///when nobody wrote one.
    String description;
    
    ///The record's own id in the system that holds it.
    String? id;
    
    ///What caused the movement, in the words of the system that charged for it. Free text: the
    ///list of billable operations belongs to that system.
    String operation;
    
    ///The id of the job or generation that caused it, in the system that owns that thing.
    ///Absent for a refill or a top-up, which answer to nothing.
    String? reference;

    CreditTransaction({
        required this.account,
        required this.amount,
        required this.balanceAfter,
        this.createdAt,
        required this.description,
        this.id,
        required this.operation,
        this.reference,
    });

    factory CreditTransaction.fromJson(Map<String, dynamic> json) => CreditTransaction(
        account: json["account"],
        amount: json["amount"],
        balanceAfter: json["balanceAfter"],
        createdAt: json["createdAt"] == null ? null : DateTime.parse(json["createdAt"]),
        description: json["description"],
        id: json["id"],
        operation: json["operation"],
        reference: json["reference"],
    );

    Map<String, dynamic> toJson() => {
        "account": account,
        "amount": amount,
        "balanceAfter": balanceAfter,
        "createdAt": createdAt?.toIso8601String(),
        "description": description,
        "id": id,
        "operation": operation,
        "reference": reference,
    };
}