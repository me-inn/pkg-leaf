# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Any, TypeVar, Type, cast
import dateutil.parser


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class CreditTransaction:
    """One movement of credit on an account, written once and never changed. The balance on the
    account is the sum of these; a row kept after the fact is what makes it possible to say
    why.
    """
    account: str
    """The id of the account the credit moved on, in the system that holds it."""

    amount: int
    """Signed: negative spends, positive tops up or refills. One field rather than a direction
    and a magnitude, so adding them up needs no rules.
    """
    balance_after: int
    """The balance the moment after this movement was applied. Copied here on purpose: reading a
    balance as of some past row should not mean replaying the whole ledger.
    """
    description: str
    """A line a person can read on a receipt or in support. Written by whoever charged; empty
    when nobody wrote one.
    """
    operation: str
    """What caused the movement, in the words of the system that charged for it. Free text: the
    list of billable operations belongs to that system.
    """
    created_at: Optional[datetime] = None
    """When the movement was recorded."""

    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    reference: Optional[str] = None
    """The id of the job or generation that caused it, in the system that owns that thing.
    Absent for a refill or a top-up, which answer to nothing.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'CreditTransaction':
        assert isinstance(obj, dict)
        account = from_str(obj.get("account"))
        amount = from_int(obj.get("amount"))
        balance_after = from_int(obj.get("balanceAfter"))
        description = from_str(obj.get("description"))
        operation = from_str(obj.get("operation"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        id = from_union([from_str, from_none], obj.get("id"))
        reference = from_union([from_str, from_none], obj.get("reference"))
        return CreditTransaction(account, amount, balance_after, description, operation, created_at, id, reference)

    def to_dict(self) -> dict:
        result: dict = {}
        result["account"] = from_str(self.account)
        result["amount"] = from_int(self.amount)
        result["balanceAfter"] = from_int(self.balance_after)
        result["description"] = from_str(self.description)
        result["operation"] = from_str(self.operation)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.reference is not None:
            result["reference"] = from_union([from_str, from_none], self.reference)
        return result


def credit_transaction_from_dict(s: Any) -> CreditTransaction:
    return CreditTransaction.from_dict(s)


def credit_transaction_to_dict(x: CreditTransaction) -> Any:
    return to_class(CreditTransaction, x)