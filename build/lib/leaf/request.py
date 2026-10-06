# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from enum import Enum
from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, Callable, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Locale(Enum):
    """The language to write to this point in."""

    EN = "en"
    ES = "es"
    PT = "pt"


class TypeEnum(Enum):
    """Which channel the value is for."""

    EMAIL = "email"
    MOBILE = "mobile"
    PHONE = "phone"
    WHATSAPP = "whatsapp"


@dataclass
class ContactPoint:
    """One way to reach an actor."""

    type: TypeEnum
    """Which channel the value is for."""

    value: str
    """An address, or a number in E.164 digits including the country code."""

    locale: Optional[Locale] = None
    """The language to write to this point in."""

    verified: Optional[bool] = None
    verified_at: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ContactPoint':
        assert isinstance(obj, dict)
        type = TypeEnum(obj.get("type"))
        value = from_str(obj.get("value"))
        locale = from_union([Locale, from_none], obj.get("locale"))
        verified = from_union([from_bool, from_none], obj.get("verified"))
        verified_at = from_union([from_datetime, from_none], obj.get("verifiedAt"))
        return ContactPoint(type, value, locale, verified, verified_at)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(TypeEnum, self.type)
        result["value"] = from_str(self.value)
        if self.locale is not None:
            result["locale"] = from_union([lambda x: to_enum(Locale, x), from_none], self.locale)
        if self.verified is not None:
            result["verified"] = from_union([from_bool, from_none], self.verified)
        if self.verified_at is not None:
            result["verifiedAt"] = from_union([lambda x: x.isoformat(), from_none], self.verified_at)
        return result


class State(Enum):
    """An answer is final. A second answer does not change the first."""

    CONFIRMED = "confirmed"
    DECLINED = "declined"
    PENDING = "pending"


@dataclass
class Request:
    """Somebody asking somebody else for a time. A request, not a booking: it records what was
    asked, never that a slot is taken.
    """
    to: str
    """The wallet, handle, or id under localIds of whoever is being asked."""

    wanted: str
    """When they want, in their own words. Not a timestamp: a parsed date is a claim about a
    timezone and a working hour, and a person reading the words cannot misread them.
    """
    answered_at: Optional[datetime] = None
    contacts: Optional[List[ContactPoint]] = None
    """How to reach whoever asked, so an answer can get back to them."""

    created_at: Optional[datetime] = None
    request_from: Optional[str] = None
    """The wallet or local id of whoever is asking, when they have one. Absent for somebody with
    no account anywhere.
    """
    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    requester: Optional[str] = None
    """Who is asking, as they gave it. Unverified, and read by a person."""

    state: Optional[State] = None
    """An answer is final. A second answer does not change the first."""

    @staticmethod
    def from_dict(obj: Any) -> 'Request':
        assert isinstance(obj, dict)
        to = from_str(obj.get("to"))
        wanted = from_str(obj.get("wanted"))
        answered_at = from_union([from_datetime, from_none], obj.get("answeredAt"))
        contacts = from_union([lambda x: from_list(ContactPoint.from_dict, x), from_none], obj.get("contacts"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        request_from = from_union([from_str, from_none], obj.get("from"))
        id = from_union([from_str, from_none], obj.get("id"))
        requester = from_union([from_str, from_none], obj.get("requester"))
        state = from_union([State, from_none], obj.get("state"))
        return Request(to, wanted, answered_at, contacts, created_at, request_from, id, requester, state)

    def to_dict(self) -> dict:
        result: dict = {}
        result["to"] = from_str(self.to)
        result["wanted"] = from_str(self.wanted)
        if self.answered_at is not None:
            result["answeredAt"] = from_union([lambda x: x.isoformat(), from_none], self.answered_at)
        if self.contacts is not None:
            result["contacts"] = from_union([lambda x: from_list(lambda x: to_class(ContactPoint, x), x), from_none], self.contacts)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.request_from is not None:
            result["from"] = from_union([from_str, from_none], self.request_from)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.requester is not None:
            result["requester"] = from_union([from_str, from_none], self.requester)
        if self.state is not None:
            result["state"] = from_union([lambda x: to_enum(State, x), from_none], self.state)
        return result


def request_from_dict(s: Any) -> Request:
    return Request.from_dict(s)


def request_to_dict(x: Request) -> Any:
    return to_class(Request, x)