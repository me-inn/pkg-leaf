# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Any, TypeVar, Type, cast
import dateutil.parser


T = TypeVar("T")


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
class WorkSession:
    """A stretch of work somebody keeps coming back to, and the defaults everything made inside
    it starts from. Named work-session, not session, because it has nothing to do with being
    signed in: it outlives any login and carries no credential.
    """
    created_at: datetime
    """When the session was opened."""

    last_seen: datetime
    """When it was last touched. The reason the record is worth keeping: it says which sessions
    are still alive.
    """
    brand_name: Optional[str] = None
    """The brand the work is for, as typed. A name, not a reference: the session is written
    before anybody decides whether that brand is a record anywhere.
    """
    default_channel: Optional[str] = None
    """Where work made here is headed unless told otherwise. Free text: the channels belong to
    the system that publishes.
    """
    default_objective: Optional[str] = None
    """What work made here is for unless told otherwise. Free text, in the vocabulary of whoever
    set it.
    """
    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    name: Optional[str] = None
    """What the person called it. Absent until they bother to name it."""

    person: Optional[str] = None
    """The wallet, handle, or id under localIds of whoever is working. Absent while the work is
    anonymous — a session can exist before anybody has signed in for it.
    """
    workspace: Optional[str] = None
    """The id of the workspace the session sits in, in the system that owns workspaces."""

    @staticmethod
    def from_dict(obj: Any) -> 'WorkSession':
        assert isinstance(obj, dict)
        created_at = from_datetime(obj.get("createdAt"))
        last_seen = from_datetime(obj.get("lastSeen"))
        brand_name = from_union([from_str, from_none], obj.get("brandName"))
        default_channel = from_union([from_str, from_none], obj.get("defaultChannel"))
        default_objective = from_union([from_str, from_none], obj.get("defaultObjective"))
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        person = from_union([from_str, from_none], obj.get("person"))
        workspace = from_union([from_str, from_none], obj.get("workspace"))
        return WorkSession(created_at, last_seen, brand_name, default_channel, default_objective, id, name, person, workspace)

    def to_dict(self) -> dict:
        result: dict = {}
        result["createdAt"] = self.created_at.isoformat()
        result["lastSeen"] = self.last_seen.isoformat()
        if self.brand_name is not None:
            result["brandName"] = from_union([from_str, from_none], self.brand_name)
        if self.default_channel is not None:
            result["defaultChannel"] = from_union([from_str, from_none], self.default_channel)
        if self.default_objective is not None:
            result["defaultObjective"] = from_union([from_str, from_none], self.default_objective)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.person is not None:
            result["person"] = from_union([from_str, from_none], self.person)
        if self.workspace is not None:
            result["workspace"] = from_union([from_str, from_none], self.workspace)
        return result


def work_session_from_dict(s: Any) -> WorkSession:
    return WorkSession.from_dict(s)


def work_session_to_dict(x: WorkSession) -> Any:
    return to_class(WorkSession, x)