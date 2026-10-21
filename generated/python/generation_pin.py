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
class GenerationPin:
    """A session holding on to a generation: kept near, so it is found again. An edge and not a
    column, because being pinned is not a property of the generation — the same generation is
    pinned in one session and not in another, and a column would make one session's opinion
    look like the thing's own.
    """
    generation: str
    """The generation being held on to, by its id in the system that holds it."""

    session: str
    """The working session holding on to it, by that session's id in the system that holds it.
    That a session pins a generation at most once is the pinning system's rule, not a
    constraint of this shape.
    """
    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    pinned_at: Optional[datetime] = None
    """When it was pinned."""

    @staticmethod
    def from_dict(obj: Any) -> 'GenerationPin':
        assert isinstance(obj, dict)
        generation = from_str(obj.get("generation"))
        session = from_str(obj.get("session"))
        id = from_union([from_str, from_none], obj.get("id"))
        pinned_at = from_union([from_datetime, from_none], obj.get("pinnedAt"))
        return GenerationPin(generation, session, id, pinned_at)

    def to_dict(self) -> dict:
        result: dict = {}
        result["generation"] = from_str(self.generation)
        result["session"] = from_str(self.session)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.pinned_at is not None:
            result["pinnedAt"] = from_union([lambda x: x.isoformat(), from_none], self.pinned_at)
        return result


def generation_pin_from_dict(s: Any) -> GenerationPin:
    return GenerationPin.from_dict(s)


def generation_pin_to_dict(x: GenerationPin) -> Any:
    return to_class(GenerationPin, x)