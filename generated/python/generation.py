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


class ContentStatus(Enum):
    """Where the text stands. Which status may follow which is a rule held by the system that
    moves it, not a constraint of this shape.
    """
    APPROVED = "approved"
    ARCHIVED = "archived"
    DRAFT = "draft"
    PUBLISHED = "published"


@dataclass
class Generation:
    """One thing a model wrote when somebody asked for it: what was asked, what it was given to
    read, and the text that came out. The assets it read are named by id and stay where they
    are — this record is the asking, not a copy of the material.
    """
    generation_type: str
    """What kind of thing was asked for. Free text: the vocabulary grows with every surface that
    asks, so it is not closed here.
    """
    asset_ids: Optional[List[str]] = None
    """The assets the model was given to read, by their ids in the system that holds them. Ids,
    never the material: the asset is somebody else's record.
    """
    channel: Optional[str] = None
    """Where the text was meant to go. Free text: the channels belong to whoever publishes, not
    to this shape.
    """
    content_status: Optional[ContentStatus] = None
    """Where the text stands. Which status may follow which is a rule held by the system that
    moves it, not a constraint of this shape.
    """
    created_at: Optional[datetime] = None
    """When the generation was recorded."""

    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    instructions: Optional[str] = None
    """What the person asked for, in their own words, before anything was assembled around it."""

    model_used: Optional[str] = None
    """Which model wrote it, under the name its provider gives it. Recorded so a later reading
    knows what produced the text — never a key, never a provider credential.
    """
    objective: Optional[str] = None
    """What the text was meant to achieve. Free text, for the same reason as channel."""

    output: Optional[str] = None
    """The text the model produced. Empty while the generation exists and has produced nothing
    yet.
    """
    prompt_used: Optional[str] = None
    """The prompt actually sent, after the instructions and the context were assembled into one.
    Kept because the instructions alone do not reproduce it.
    """
    session: Optional[str] = None
    """The working session it was generated in, by that session's id in the system that holds
    it. A session, not a person: who was at the keyboard is the session's own business.
    Absent when it was generated outside one.
    """
    tags: Optional[List[str]] = None
    """Labels somebody put on it. Free text, theirs."""

    @staticmethod
    def from_dict(obj: Any) -> 'Generation':
        assert isinstance(obj, dict)
        generation_type = from_str(obj.get("generationType"))
        asset_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("assetIds"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        content_status = from_union([ContentStatus, from_none], obj.get("contentStatus"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        id = from_union([from_str, from_none], obj.get("id"))
        instructions = from_union([from_str, from_none], obj.get("instructions"))
        model_used = from_union([from_str, from_none], obj.get("modelUsed"))
        objective = from_union([from_str, from_none], obj.get("objective"))
        output = from_union([from_str, from_none], obj.get("output"))
        prompt_used = from_union([from_str, from_none], obj.get("promptUsed"))
        session = from_union([from_str, from_none], obj.get("session"))
        tags = from_union([lambda x: from_list(from_str, x), from_none], obj.get("tags"))
        return Generation(generation_type, asset_ids, channel, content_status, created_at, id, instructions, model_used, objective, output, prompt_used, session, tags)

    def to_dict(self) -> dict:
        result: dict = {}
        result["generationType"] = from_str(self.generation_type)
        if self.asset_ids is not None:
            result["assetIds"] = from_union([lambda x: from_list(from_str, x), from_none], self.asset_ids)
        if self.channel is not None:
            result["channel"] = from_union([from_str, from_none], self.channel)
        if self.content_status is not None:
            result["contentStatus"] = from_union([lambda x: to_enum(ContentStatus, x), from_none], self.content_status)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.instructions is not None:
            result["instructions"] = from_union([from_str, from_none], self.instructions)
        if self.model_used is not None:
            result["modelUsed"] = from_union([from_str, from_none], self.model_used)
        if self.objective is not None:
            result["objective"] = from_union([from_str, from_none], self.objective)
        if self.output is not None:
            result["output"] = from_union([from_str, from_none], self.output)
        if self.prompt_used is not None:
            result["promptUsed"] = from_union([from_str, from_none], self.prompt_used)
        if self.session is not None:
            result["session"] = from_union([from_str, from_none], self.session)
        if self.tags is not None:
            result["tags"] = from_union([lambda x: from_list(from_str, x), from_none], self.tags)
        return result


def generation_from_dict(s: Any) -> Generation:
    return Generation.from_dict(s)


def generation_to_dict(x: Generation) -> Any:
    return to_class(Generation, x)