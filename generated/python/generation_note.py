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
class GenerationNote:
    """Something somebody wrote beside a generation — a remark about the text, not part of it.
    It stays its own record so the generation reads as the model left it.
    """
    body: str
    """What they wrote, in their words."""

    generation: str
    """The generation the note is about, by its id in the system that holds it."""

    session: str
    """The working session the note was written in, by that session's id in the system that
    holds it. The note is attributed to the session, not to a wallet: who was at the keyboard
    is the session's own business.
    """
    created_at: Optional[datetime] = None
    """When the note was written."""

    id: Optional[str] = None
    """The record's own id in the system that holds it."""

    updated_at: Optional[datetime] = None
    """When it was last rewritten. A note is editable, so this differs from createdAt once it
    has been.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'GenerationNote':
        assert isinstance(obj, dict)
        body = from_str(obj.get("body"))
        generation = from_str(obj.get("generation"))
        session = from_str(obj.get("session"))
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        id = from_union([from_str, from_none], obj.get("id"))
        updated_at = from_union([from_datetime, from_none], obj.get("updatedAt"))
        return GenerationNote(body, generation, session, created_at, id, updated_at)

    def to_dict(self) -> dict:
        result: dict = {}
        result["body"] = from_str(self.body)
        result["generation"] = from_str(self.generation)
        result["session"] = from_str(self.session)
        if self.created_at is not None:
            result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.updated_at is not None:
            result["updatedAt"] = from_union([lambda x: x.isoformat(), from_none], self.updated_at)
        return result


def generation_note_from_dict(s: Any) -> GenerationNote:
    return GenerationNote.from_dict(s)


def generation_note_to_dict(x: GenerationNote) -> Any:
    return to_class(GenerationNote, x)