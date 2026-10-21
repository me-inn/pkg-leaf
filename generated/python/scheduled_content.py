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
class ScheduledContent:
    """An intention to publish something that was already generated, at a time somebody picked.
    A plan, not a publication: nothing here says it went out, and the generation itself stays
    where it was made.
    """
    generation: str
    """What is to be published, as the system that holds the generation names it. A pointer: the
    text lives there and is not copied here, so editing it does not leave two versions.
    """
    publish_at: datetime
    """When it is meant to go out. A moment, not a window, and the only field anything schedules
    on.
    """
    created_at: Optional[datetime] = None
    """When the plan was made, which is not when it publishes."""

    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    notes: Optional[str] = None
    """Anything the person wanted to remember about this one. Read by a person, never acted on."""

    platform: Optional[str] = None
    """Where it is meant to go, in the words of whoever scheduled it. Free text: the vocabulary
    belongs to whoever publishes, and nothing here posts anything.
    """
    session: Optional[str] = None
    """The session the plan belongs to, as the system that owns the session names it. Optional:
    scoping a scheduled item to a working session is how Creative Flow holds it, not part of
    what it is, and a system without sessions must be able to carry the same shape.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'ScheduledContent':
        assert isinstance(obj, dict)
        generation = from_str(obj.get("generation"))
        publish_at = from_datetime(obj.get("publishAt"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        id = from_union([from_str, from_none], obj.get("id"))
        notes = from_union([from_str, from_none], obj.get("notes"))
        platform = from_union([from_str, from_none], obj.get("platform"))
        session = from_union([from_str, from_none], obj.get("session"))
        return ScheduledContent(generation, publish_at, created_at, id, notes, platform, session)

    def to_dict(self) -> dict:
        result: dict = {}
        result["generation"] = from_str(self.generation)
        result["publishAt"] = self.publish_at.isoformat()
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.notes is not None:
            result["notes"] = from_union([from_str, from_none], self.notes)
        if self.platform is not None:
            result["platform"] = from_union([from_str, from_none], self.platform)
        if self.session is not None:
            result["session"] = from_union([from_str, from_none], self.session)
        return result


def scheduled_content_from_dict(s: Any) -> ScheduledContent:
    return ScheduledContent.from_dict(s)


def scheduled_content_to_dict(x: ScheduledContent) -> Any:
    return to_class(ScheduledContent, x)