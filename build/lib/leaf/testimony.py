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


class State(Enum):
    """Published only once the subject has agreed. Pending is written and not readable by anyone
    but its author.
    """
    HIDDEN = "hidden"
    PENDING = "pending"
    PUBLISHED = "published"


@dataclass
class Testimony:
    """Something one person wrote about another, published with the subject's consent and their
    author's name attached.
    """
    author: str
    """The wallet, or the id under localIds, of whoever wrote it."""

    subject: str
    """The wallet, or the id under localIds, of whoever it is about."""

    created_at: Optional[datetime] = None
    detail: Optional[str] = None
    """What was written, in the author's own words. A scene rather than an attribute: what the
    subject did, told by whoever was there.
    """
    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    published_at: Optional[datetime] = None
    sealed_until: Optional[datetime] = None
    """While set, the subject is told the record exists and not what it says. Opens when they
    write their own, or when this passes.
    """
    signature: Optional[str] = None
    """ed25519 over the record, hex. Signed by the author's wallet, so the words can be shown to
    have come from them.
    """
    state: Optional[State] = None
    """Published only once the subject has agreed. Pending is written and not readable by anyone
    but its author.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'Testimony':
        assert isinstance(obj, dict)
        author = from_str(obj.get("author"))
        subject = from_str(obj.get("subject"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        detail = from_union([from_str, from_none], obj.get("detail"))
        id = from_union([from_str, from_none], obj.get("id"))
        published_at = from_union([from_datetime, from_none], obj.get("publishedAt"))
        sealed_until = from_union([from_datetime, from_none], obj.get("sealedUntil"))
        signature = from_union([from_str, from_none], obj.get("signature"))
        state = from_union([State, from_none], obj.get("state"))
        return Testimony(author, subject, created_at, detail, id, published_at, sealed_until, signature, state)

    def to_dict(self) -> dict:
        result: dict = {}
        result["author"] = from_str(self.author)
        result["subject"] = from_str(self.subject)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.detail is not None:
            result["detail"] = from_union([from_str, from_none], self.detail)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.published_at is not None:
            result["publishedAt"] = from_union([lambda x: x.isoformat(), from_none], self.published_at)
        if self.sealed_until is not None:
            result["sealedUntil"] = from_union([lambda x: x.isoformat(), from_none], self.sealed_until)
        if self.signature is not None:
            result["signature"] = from_union([from_str, from_none], self.signature)
        if self.state is not None:
            result["state"] = from_union([lambda x: to_enum(State, x), from_none], self.state)
        return result


def testimony_from_dict(s: Any) -> Testimony:
    return Testimony.from_dict(s)


def testimony_to_dict(x: Testimony) -> Any:
    return to_class(Testimony, x)