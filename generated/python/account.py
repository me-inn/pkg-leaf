# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Any, TypeVar, Type, cast
import dateutil.parser


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


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
class Account:
    """What somebody is owed by the system that bills them: a plan, a credit balance, and the
    day the cycle turns over. Not an actor and not an organisation — the actor is the person
    who owns it, named here by key. One person can be billed by more than one system, and
    each one keeps its own account.
    """
    credits_balance: int
    """Credits left to spend. Whole credits, never fractions, because a half-spent credit is not
    a thing anybody can sell.
    """
    cycle_renews_at: datetime
    """When the next cycle starts and the balance is refilled. Stated rather than computed from
    the plan, so a cycle moved by hand stays moved.
    """
    owner: str
    """The wallet, handle, or id under localIds of the person billed. One account per person per
    system.
    """
    plan: str
    """Which plan is in force, in the words of the system that sells it. Free text: the
    catalogue of plans belongs to the seller and changes without the shape changing.
    """
    created_at: Optional[datetime] = None
    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    updated_at: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Account':
        assert isinstance(obj, dict)
        credits_balance = from_int(obj.get("creditsBalance"))
        cycle_renews_at = from_datetime(obj.get("cycleRenewsAt"))
        owner = from_str(obj.get("owner"))
        plan = from_str(obj.get("plan"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        id = from_union([from_str, from_none], obj.get("id"))
        updated_at = from_union([from_datetime, from_none], obj.get("updatedAt"))
        return Account(credits_balance, cycle_renews_at, owner, plan, created_at, id, updated_at)

    def to_dict(self) -> dict:
        result: dict = {}
        result["creditsBalance"] = from_int(self.credits_balance)
        result["cycleRenewsAt"] = self.cycle_renews_at.isoformat()
        result["owner"] = from_str(self.owner)
        result["plan"] = from_str(self.plan)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.updated_at is not None:
            result["updatedAt"] = from_union([lambda x: x.isoformat(), from_none], self.updated_at)
        return result


def account_from_dict(s: Any) -> Account:
    return Account.from_dict(s)


def account_to_dict(x: Account) -> Any:
    return to_class(Account, x)