# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, Any, TypeVar, Callable, Type, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


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


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Status(Enum):
    ACTIVE = "active"
    INVITED = "invited"
    LEFT = "left"
    SUSPENDED = "suspended"


@dataclass
class Membership:
    """A person belonging to an organisation."""

    organization: str
    """The organisation's wallet, or its id under localIds."""

    person: str
    """The person's wallet, or their id under localIds."""

    capabilities: Optional[List[str]] = None
    """What they may do inside it. Free text: the verbs belong to the system that grants them."""

    created_at: Optional[datetime] = None
    invited_by: Optional[str] = None
    """The wallet or local id of whoever invited them."""

    status: Optional[Status] = None
    updated_at: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Membership':
        assert isinstance(obj, dict)
        organization = from_str(obj.get("organization"))
        person = from_str(obj.get("person"))
        capabilities = from_union([lambda x: from_list(from_str, x), from_none], obj.get("capabilities"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        invited_by = from_union([from_str, from_none], obj.get("invitedBy"))
        status = from_union([Status, from_none], obj.get("status"))
        updated_at = from_union([from_datetime, from_none], obj.get("updatedAt"))
        return Membership(organization, person, capabilities, created_at, invited_by, status, updated_at)

    def to_dict(self) -> dict:
        result: dict = {}
        result["organization"] = from_str(self.organization)
        result["person"] = from_str(self.person)
        if self.capabilities is not None:
            result["capabilities"] = from_union([lambda x: from_list(from_str, x), from_none], self.capabilities)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.invited_by is not None:
            result["invitedBy"] = from_union([from_str, from_none], self.invited_by)
        if self.status is not None:
            result["status"] = from_union([lambda x: to_enum(Status, x), from_none], self.status)
        if self.updated_at is not None:
            result["updatedAt"] = from_union([lambda x: x.isoformat(), from_none], self.updated_at)
        return result


def membership_from_dict(s: Any) -> Membership:
    return Membership.from_dict(s)


def membership_to_dict(x: Membership) -> Any:
    return to_class(Membership, x)