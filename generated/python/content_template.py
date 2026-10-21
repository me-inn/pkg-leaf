# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")


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


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class ContentTemplate:
    """A saved starting point for generating something: what kind of piece, for which channel
    and objective, with the standing instructions to use. Settings somebody wants back, not a
    piece of content — nothing generated is kept here.
    """
    generation_type: str
    """What kind of piece it produces. Free text: the names belong to the generation flow, which
    adds to them.
    """
    name: str
    """What the person called it, so they recognise it in a list."""

    channel: Optional[str] = None
    """Where the piece is meant to run, in the words of whoever saved the template. Free text
    everywhere it appears: the vocabulary belongs to whoever publishes.
    """
    created_at: Optional[datetime] = None
    """When the template was saved."""

    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    instructions: Optional[str] = None
    """The standing instructions to apply, in the person's own words. The template's substance:
    everything else only files it.
    """
    objective: Optional[str] = None
    """What the piece is meant to do. Free text, for the same reason as channel."""

    session: Optional[str] = None
    """The session the template belongs to, as the system that owns the session names it.
    Optional: scoping a template to a working session is how Creative Flow holds it, not part
    of what it is, and a system without sessions must be able to carry the same shape.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'ContentTemplate':
        assert isinstance(obj, dict)
        generation_type = from_str(obj.get("generationType"))
        name = from_str(obj.get("name"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        id = from_union([from_str, from_none], obj.get("id"))
        instructions = from_union([from_str, from_none], obj.get("instructions"))
        objective = from_union([from_str, from_none], obj.get("objective"))
        session = from_union([from_str, from_none], obj.get("session"))
        return ContentTemplate(generation_type, name, channel, created_at, id, instructions, objective, session)

    def to_dict(self) -> dict:
        result: dict = {}
        result["generationType"] = from_str(self.generation_type)
        result["name"] = from_str(self.name)
        if self.channel is not None:
            result["channel"] = from_union([from_str, from_none], self.channel)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.instructions is not None:
            result["instructions"] = from_union([from_str, from_none], self.instructions)
        if self.objective is not None:
            result["objective"] = from_union([from_str, from_none], self.objective)
        if self.session is not None:
            result["session"] = from_union([from_str, from_none], self.session)
        return result


def content_template_from_dict(s: Any) -> ContentTemplate:
    return ContentTemplate.from_dict(s)


def content_template_to_dict(x: ContentTemplate) -> Any:
    return to_class(ContentTemplate, x)