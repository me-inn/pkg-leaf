# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Any, TypeVar, Type, cast
import dateutil.parser


T = TypeVar("T")


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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Authorization:
    """Somebody letting a piece of software act for them. What was granted, to whom, and until
    when — never the credential that proves it. The code and the token are secrets, they are
    held only as a hash by the system that issued them, and neither has a shape here.
    """
    client: str
    """The https URL that identifies the software. It is also where that software describes
    itself, so nothing about it has to be copied here.
    """
    subject: str
    """The wallet, or the id under localIds, of whoever is being acted for. The grant is theirs
    and so is taking it back.
    """
    expires_at: Optional[datetime] = None
    """When it stops working on its own, with nobody having to do anything."""

    granted_at: Optional[datetime] = None
    label: Optional[str] = None
    """What the software calls itself, as it said. Recorded so a person recognises it when
    deciding what to take back; never used to decide anything.
    """
    revoked_at: Optional[datetime] = None
    """When it was taken back. A grant that ended is kept rather than deleted: what was allowed,
    and until when, is a fact about the past.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'Authorization':
        assert isinstance(obj, dict)
        client = from_str(obj.get("client"))
        subject = from_str(obj.get("subject"))
        expires_at = from_union([from_datetime, from_none], obj.get("expiresAt"))
        granted_at = from_union([from_datetime, from_none], obj.get("grantedAt"))
        label = from_union([from_str, from_none], obj.get("label"))
        revoked_at = from_union([from_datetime, from_none], obj.get("revokedAt"))
        return Authorization(client, subject, expires_at, granted_at, label, revoked_at)

    def to_dict(self) -> dict:
        result: dict = {}
        result["client"] = from_str(self.client)
        result["subject"] = from_str(self.subject)
        if self.expires_at is not None:
            result["expiresAt"] = from_union([lambda x: x.isoformat(), from_none], self.expires_at)
        if self.granted_at is not None:
            result["grantedAt"] = from_union([lambda x: x.isoformat(), from_none], self.granted_at)
        if self.label is not None:
            result["label"] = from_union([from_str, from_none], self.label)
        if self.revoked_at is not None:
            result["revokedAt"] = from_union([lambda x: x.isoformat(), from_none], self.revoked_at)
        return result


def authorization_from_dict(s: Any) -> Authorization:
    return Authorization.from_dict(s)


def authorization_to_dict(x: Authorization) -> Any:
    return to_class(Authorization, x)