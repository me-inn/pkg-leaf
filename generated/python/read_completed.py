# Generated from the schema in schemas/. Do not edit: CI regenerates this file and fails on any difference. Change the schema and run ./generate.sh.

from dataclasses import dataclass
from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class ReadCompleted:
    """An asset was read through: metadata out, a machine's reading of it written, and its
    chunks indexed. Says the asset is now worth searching, and nothing about what it says.
    Keys are snake_case, not the camelCase the rest of leaf uses: this travels inside a
    Liquid envelope, whose own fields (event_id, occurred_at, event_type, owner_unit_ref) are
    snake_case and pinned byte-exact by signed golden vectors. The shape follows the wire.
    """
    content_id: str
    """The asset that was read."""

    session_id: str
    """The working session it was read in. Empty when the asset belongs to none."""

    @staticmethod
    def from_dict(obj: Any) -> 'ReadCompleted':
        assert isinstance(obj, dict)
        content_id = from_str(obj.get("content_id"))
        session_id = from_str(obj.get("session_id"))
        return ReadCompleted(content_id, session_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["content_id"] = from_str(self.content_id)
        result["session_id"] = from_str(self.session_id)
        return result


def read_completed_from_dict(s: Any) -> ReadCompleted:
    return ReadCompleted.from_dict(s)


def read_completed_to_dict(x: ReadCompleted) -> Any:
    return to_class(ReadCompleted, x)