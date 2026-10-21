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


class Action(Enum):
    """What they did with it."""

    APPROVED = "approved"
    EDITED = "edited"
    REJECTED = "rejected"


@dataclass
class GenerationFeedback:
    """What somebody did with a generated piece when it was handed to them: took it, threw it
    away, or rewrote it. An act rather than an opinion — the rewrite is the feedback, and it
    is the one signal that says what good would have looked like.
    """
    action: Action
    """What they did with it."""

    generation: str
    """The id of the generated piece this was done to, in the system that owns it."""

    created_at: Optional[datetime] = None
    """When they did it."""

    edited_output: Optional[str] = None
    """The piece as they rewrote it. Present when the action was edited; that it must be is a
    rule the writing system keeps, not a shape.
    """
    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    session: Optional[str] = None
    """The id of the working session it happened in, in the system that holds it. Not a person:
    a session says the acts came from one sitting, and whether anybody is named is the
    holding system's business.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'GenerationFeedback':
        assert isinstance(obj, dict)
        action = Action(obj.get("action"))
        generation = from_str(obj.get("generation"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        edited_output = from_union([from_str, from_none], obj.get("editedOutput"))
        id = from_union([from_str, from_none], obj.get("id"))
        session = from_union([from_str, from_none], obj.get("session"))
        return GenerationFeedback(action, generation, created_at, edited_output, id, session)

    def to_dict(self) -> dict:
        result: dict = {}
        result["action"] = to_enum(Action, self.action)
        result["generation"] = from_str(self.generation)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.edited_output is not None:
            result["editedOutput"] = from_union([from_str, from_none], self.edited_output)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.session is not None:
            result["session"] = from_union([from_str, from_none], self.session)
        return result


def generation_feedback_from_dict(s: Any) -> GenerationFeedback:
    return GenerationFeedback.from_dict(s)


def generation_feedback_to_dict(x: GenerationFeedback) -> Any:
    return to_class(GenerationFeedback, x)