# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


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
class SessionQuota:
    """How much a work session may spend in a day. Its own record rather than fields on the
    session, because the limits are set by whoever runs the system and the session is written
    by whoever uses it.
    """
    max_generations_per_day: int
    """Generations allowed in a day."""

    max_repurpose_per_day: int
    """Repurposes allowed in a day."""

    session: str
    """The work session the limits apply to, as the system that owns the session names it. One
    quota per session.
    """
    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    person: Optional[str] = None
    """The wallet, handle, or id under localIds of whoever owns the quota. Carried so the holder
    of a session id is not by itself the person allowed to change the limits; absent for a
    session nobody has signed in for.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'SessionQuota':
        assert isinstance(obj, dict)
        max_generations_per_day = from_int(obj.get("maxGenerationsPerDay"))
        max_repurpose_per_day = from_int(obj.get("maxRepurposePerDay"))
        session = from_str(obj.get("session"))
        id = from_union([from_str, from_none], obj.get("id"))
        person = from_union([from_str, from_none], obj.get("person"))
        return SessionQuota(max_generations_per_day, max_repurpose_per_day, session, id, person)

    def to_dict(self) -> dict:
        result: dict = {}
        result["maxGenerationsPerDay"] = from_int(self.max_generations_per_day)
        result["maxRepurposePerDay"] = from_int(self.max_repurpose_per_day)
        result["session"] = from_str(self.session)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.person is not None:
            result["person"] = from_union([from_str, from_none], self.person)
        return result


def session_quota_from_dict(s: Any) -> SessionQuota:
    return SessionQuota.from_dict(s)


def session_quota_to_dict(x: SessionQuota) -> Any:
    return to_class(SessionQuota, x)