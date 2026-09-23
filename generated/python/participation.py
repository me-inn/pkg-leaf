# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Any, TypeVar, Type, cast
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
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


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Context(Enum):
    """What kind of thing it participates in."""

    EVENT = "event"
    PROGRAM = "program"
    PUBLICATION = "publication"
    SPLIT = "split"


class Status(Enum):
    ACTIVE = "active"
    ENDED = "ended"
    PROPOSED = "proposed"


@dataclass
class Participation:
    """An organisation's role in an event, a publication, a split or a programme."""

    context: Context
    """What kind of thing it participates in."""

    context_id: str
    """The id of that thing, in the system that owns it."""

    organization: str
    """The organisation's wallet, or its id under localIds."""

    role: str
    """Its role there, in that context's own words. Free text: the vocabulary belongs to the
    context.
    """
    created_at: Optional[datetime] = None
    status: Optional[Status] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Participation':
        assert isinstance(obj, dict)
        context = Context(obj.get("context"))
        context_id = from_str(obj.get("contextId"))
        organization = from_str(obj.get("organization"))
        role = from_str(obj.get("role"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        status = from_union([Status, from_none], obj.get("status"))
        return Participation(context, context_id, organization, role, created_at, status)

    def to_dict(self) -> dict:
        result: dict = {}
        result["context"] = to_enum(Context, self.context)
        result["contextId"] = from_str(self.context_id)
        result["organization"] = from_str(self.organization)
        result["role"] = from_str(self.role)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.status is not None:
            result["status"] = from_union([lambda x: to_enum(Status, x), from_none], self.status)
        return result


def participation_from_dict(s: Any) -> Participation:
    return Participation.from_dict(s)


def participation_to_dict(x: Participation) -> Any:
    return to_class(Participation, x)